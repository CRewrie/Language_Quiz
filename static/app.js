"use strict";

const app = document.getElementById("app");
const LETTERS = ["A", "B", "C", "D", "E", "F"];
let session = null; // { quizId, title, questions, pos, results, answered, restart }

// ---------- helpers ----------

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

// Inline markup: {漢字|かんじ} for furigana, **bold**.
function render(text) {
  return escapeHtml(text || "")
    .replace(/\{([^|{}]+)\|([^{}]+)\}/g, "<ruby>$1<rt>$2</rt></ruby>")
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/\n/g, "<br>");
}

// Block markup for guides: blank line = new paragraph, "- " lines = bullet list.
function renderBlocks(text) {
  return (text || "").split(/\n{2,}/).map(par => {
    let html = "", items = [], lines = [];
    const flushLines = () => { if (lines.length) html += `<p>${lines.map(render).join("<br>")}</p>`; lines = []; };
    const flushItems = () => { if (items.length) html += `<ul>${items.map(i => `<li>${render(i)}</li>`).join("")}</ul>`; items = []; };
    for (const line of par.split("\n")) {
      if (line.startsWith("- ")) { flushLines(); items.push(line.slice(2)); }
      else { flushItems(); lines.push(line); }
    }
    flushLines(); flushItems();
    return html;
  }).join("");
}

function guideHtml(point, open = false) {
  const examples = (point.examples || []).map(([jp, en]) =>
    `<li><span class="ex-jp">${render(jp)}</span><span class="ex-en">${render(en)}</span></li>`).join("");
  return `
    <details class="guide"${open ? " open" : ""}>
      <summary><span class="guide-title">📖 ${render(point.title)}</span><span class="guide-summary">${render(point.summary)}</span></summary>
      <div class="guide-body">
        ${renderBlocks(point.body)}
        ${examples ? `<span class="label">Examples</span><ul class="examples">${examples}</ul>` : ""}
      </div>
    </details>`;
}

function shuffled(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

const store = {
  get(key, fallback) {
    try { const v = localStorage.getItem(key); return v === null ? fallback : JSON.parse(v); } catch { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* storage unavailable */ }
  },
};

// ---------- saved progress (survives reloads; one slot per browser) ----------

const PROGRESS_KEY = "progress";
const PROGRESS_TTL = 14 * 24 * 3600 * 1000; // forget unfinished quizzes after two weeks

// Session keys: "quiz:<id>" or "mix:<category>"; a mistakes retry is "retry|" + its base key.
const baseKey = key => key.replace(/^retry\|/, "");

function hrefFor(key) {
  const k = baseKey(key);
  if (k.startsWith("quiz:")) return `#/quiz/${encodeURIComponent(k.slice(5))}/start`;
  const cat = k.slice(4);
  return cat ? `#/mix/${encodeURIComponent(cat)}` : "#/mix";
}

function saveProgress() {
  if (!session) return;
  const { key, quizId, title, questions, pos, results } = session;
  store.set(PROGRESS_KEY, { key, quizId, title, questions, pos, results, savedAt: Date.now() });
}

// The saved session, optionally only if it belongs to one of the given keys.
function loadProgress(...keys) {
  const p = store.get(PROGRESS_KEY, null);
  if (!p || !Array.isArray(p.questions) || Date.now() - p.savedAt > PROGRESS_TTL) return null;
  if (keys.length && !keys.includes(p.key)) return null;
  return p;
}

function clearProgress() {
  try { localStorage.removeItem(PROGRESS_KEY); } catch { /* storage unavailable */ }
}

function progressLabel(p) {
  return `question ${Math.min(p.results.length + 1, p.questions.length)} of ${p.questions.length}`;
}

// Chinese script (simplified / traditional); the server ignores it for Japanese quizzes.
let script = store.get("script", "simp") === "trad" ? "trad" : "simp";

async function api(path, body) {
  if (body) body = { ...body, script };
  else path += (path.includes("?") ? "&" : "?") + "script=" + script;
  if (STATIC) return staticApi(path, body);
  const res = await fetch(path, body ? {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body),
  } : undefined);
  if (!res.ok) throw new Error(await res.text());
  return res.json();
}

// ---------- static mode (GitHub Pages) ----------
// The exported site has no server: the same API is answered here from the JSON files
// under data/ (written by `japanese_quiz export`). Mirrors the server in src/main.rs.

const STATIC = window.QUIZ_STATIC === true;
const staticCache = new Map();

function fetchJSON(path) {
  if (!staticCache.has(path)) {
    staticCache.set(path, fetch(path).then(r => {
      if (!r.ok) { staticCache.delete(path); throw new Error(`${path}: ${r.status}`); }
      return r.json();
    }));
  }
  return staticCache.get(path);
}

const staticList = sc => fetchJSON(sc === "trad" ? "data/quizzes.trad.json" : "data/quizzes.json");

async function staticQuiz(id, sc) {
  const entry = (await staticList("simp")).find(q => q.id === id);
  if (!entry) throw new Error("quiz not found");
  const trad = sc === "trad" && entry.language === "zh";
  return fetchJSON(`data/quiz/${encodeURIComponent(id)}${trad ? ".trad" : ""}.json`);
}

function publicQuestions(quiz) {
  return quiz.questions.map((q, index) => ({
    quiz_id: quiz.id, index, prompt: q.prompt, options: q.options,
    ...(q.fixed_order ? { fixed_order: true } : {}),
    answerText: q.options[q.answer], point: q.point || null,
  }));
}

// Same ordering rule as the server: never the same correct answer twice in a row
// (when the pool allows it) and rarely the same grammar point.
function spreadQuestions(items) {
  const cost = qs => qs.slice(1).reduce((sum, q, i) =>
    sum + (qs[i].answerText === q.answerText ? 100 : 0) + (qs[i].point && qs[i].point === q.point ? 1 : 0), 0);
  let best = null;
  for (let attempt = 0; attempt < 200; attempt++) {
    const order = greedyOrder(items);
    const c = cost(order);
    if (!best || c < best.c) best = { c, order };
    if (c === 0) break;
  }
  return best ? best.order : items;
}

function greedyOrder(items) {
  const pool = shuffled(items), out = [];
  while (pool.length) {
    const prev = out[out.length - 1];
    const counts = new Map();
    for (const q of pool) counts.set(q.answerText, (counts.get(q.answerText) || 0) + 1);
    const [top, topCount] = [...counts].reduce((a, b) => (b[1] > a[1] ? b : a));
    const forced = topCount * 2 > pool.length && (!prev || prev.answerText !== top);
    const fits = (q, checkPoint) =>
      (!prev || prev.answerText !== q.answerText) &&
      (!checkPoint || !prev || !prev.point || prev.point !== q.point) &&
      (!forced || q.answerText === top);
    let i = pool.findIndex(q => fits(q, true));
    if (i < 0) i = pool.findIndex(q => fits(q, false));
    out.push(pool.splice(Math.max(i, 0), 1)[0]);
  }
  return out;
}

const stripPrivate = qs => qs.map(({ answerText, point, ...q }) => q);

async function staticApi(path, body) {
  if (body) {
    const quiz = await staticQuiz(body.quiz_id, body.script);
    const q = quiz.questions[body.index];
    if (!q) throw new Error("question not found");
    const correct = body.choice === q.answer;
    const note = !correct && body.choice !== null ? (q.notes?.[body.choice] || null) : null;
    return {
      correct, answer: q.answer, explanation: q.explanation, note, notes: q.notes || [],
      translation: q.translation || "", point: quiz.points?.find(p => p.id === q.point) || null,
    };
  }
  const url = new URL(path, location.href);
  const sc = url.searchParams.get("script") || "simp";
  if (url.pathname.endsWith("/api/quizzes")) return staticList(sc);
  const m = url.pathname.match(/\/api\/quizzes\/([^/]+)$/);
  if (m) {
    const quiz = await staticQuiz(decodeURIComponent(m[1]), sc);
    const { id, language, title, description, level, points } = quiz;
    return { id, language, title, description, level, points, questions: stripPrivate(spreadQuestions(publicQuestions(quiz))) };
  }
  if (url.pathname.endsWith("/api/mix")) {
    const category = url.searchParams.get("category");
    const count = Math.min(Math.max(Number(url.searchParams.get("count")) || 20, 1), 200);
    const list = (await staticList("simp")).filter(q => !category || q.category === category);
    const quizzes = await Promise.all(list.map(q => staticQuiz(q.id, sc)));
    const all = shuffled(quizzes.flatMap(publicQuestions)).slice(0, count);
    return {
      id: "mix", language: list[0]?.language || "", title: "Random mix",
      description: "Questions drawn from several quizzes.", level: "", points: [],
      questions: stripPrivate(spreadQuestions(all)),
    };
  }
  throw new Error("not found: " + url.pathname);
}

// ---------- language & reading-aid toggle ----------

const LANGS = {
  ja: { label: "日本語", html: "ja", ruby: "Furigana", brand: "文法", dunno: "わかりません", correct: "正解！" },
  zh: { label: "中文", html: "zh-CN", ruby: "Pinyin", brand: "语法", dunno: "不知道", correct: "对了！" },
};
let lang = LANGS[store.get("lang", "ja")] ? store.get("lang", "ja") : "ja";

function setLang(l) {
  if (!LANGS[l]) return;
  lang = l;
  store.set("lang", l);
  const trad = l === "zh" && script === "trad";
  document.documentElement.lang = trad ? "zh-TW" : LANGS[l].html;
  document.getElementById("ruby-label").textContent = LANGS[l].ruby;
  document.getElementById("brand-word").textContent = trad ? "語法" : LANGS[l].brand;
  document.getElementById("script-switch").hidden = l !== "zh";
  document.querySelectorAll("[data-script]").forEach(b => b.classList.toggle("active", b.dataset.script === script));
}

// Switching script mid-quiz reloads the texts of the questions in the running session.
async function setScript(sc) {
  if (sc === script) return;
  script = sc;
  store.set("script", sc);
  setLang(lang);
  const s = session;
  if (!s || !document.querySelector(".question")) return route();
  const ids = [...new Set(s.questions.map(q => q.quiz_id))];
  const quizzes = new Map(await Promise.all(ids.map(async id => [id, await api(`/api/quizzes/${encodeURIComponent(id)}`)])));
  const update = q => {
    const fresh = quizzes.get(q.quiz_id).questions.find(x => x.index === q.index);
    if (fresh) { q.prompt = fresh.prompt; q.options = fresh.options; }
  };
  s.questions.forEach(update);
  s.results.forEach(r => update(r.q));
  if (s.key.startsWith("quiz:") || s.key.startsWith("retry|quiz:")) {
    const quiz = quizzes.get(ids[0]);
    s.title = s.key.startsWith("retry|") ? `${shortTitle(quiz.title)} (mistakes)` : quiz.title;
  }
  const answered = s.results.length > s.pos;
  if (answered) {
    const r = s.results[s.pos];
    Object.assign(r, await api("/api/check", { quiz_id: r.q.quiz_id, index: r.q.index, choice: r.choice }), { q: s.questions[s.pos] });
  }
  saveProgress();
  showQuestion();
  if (answered) { s.answered = true; renderAnswer(s.results[s.pos]); }
}
document.querySelectorAll("[data-script]").forEach(b => b.addEventListener("click", () => setScript(b.dataset.script)));
setLang(lang);

const toggle = document.getElementById("furigana-toggle");
toggle.checked = store.get("furigana", true);
document.body.classList.toggle("no-furigana", !toggle.checked);
toggle.addEventListener("change", () => {
  store.set("furigana", toggle.checked);
  document.body.classList.toggle("no-furigana", !toggle.checked);
});

// ---------- sounds ----------

// Short tones synthesised with Web Audio, so there are no sound files to load.
const sound = {
  ctx: null,
  on: store.get("sound", true),
  tone(freq, start, dur, { type = "sine", gain = 0.18, slideTo = null } = {}) {
    const ctx = this.ctx, t = ctx.currentTime + start;
    const osc = ctx.createOscillator(), amp = ctx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, t);
    if (slideTo) osc.frequency.exponentialRampToValueAtTime(slideTo, t + dur);
    amp.gain.setValueAtTime(0.0001, t);
    amp.gain.exponentialRampToValueAtTime(gain, t + 0.012);
    amp.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    osc.connect(amp).connect(ctx.destination);
    osc.start(t);
    osc.stop(t + dur + 0.02);
  },
  play(name) {
    if (!this.on) return;
    try {
      this.ctx ??= new (window.AudioContext || window.webkitAudioContext)();
      if (this.ctx.state === "suspended") this.ctx.resume();
      const T = this.tone.bind(this);
      if (name === "click") T(1250, 0, 0.045, { type: "triangle", gain: 0.07 });
      else if (name === "correct") { T(880, 0, 0.13); T(1318.5, 0.09, 0.24); }
      else if (name === "wrong") T(220, 0, 0.32, { type: "triangle", gain: 0.16, slideTo: 150 });
      else if (name === "finish") [523.3, 659.3, 784, 1046.5].forEach((f, i) => T(f, i * 0.11, 0.28, { gain: 0.14 }));
    } catch { /* audio unavailable: stay silent */ }
  },
};

const soundToggle = document.getElementById("sound-toggle");
function updateSoundToggle() {
  soundToggle.textContent = sound.on ? "🔊" : "🔇";
  soundToggle.setAttribute("aria-label", sound.on ? "Sound on" : "Sound off");
}
updateSoundToggle();
soundToggle.addEventListener("click", () => {
  sound.on = !sound.on;
  store.set("sound", sound.on);
  updateSoundToggle();
  sound.play("click");
});

// A soft click for buttons and links that act like buttons (answer options have their own sounds).
document.addEventListener("click", e => {
  if (e.target.closest(".btn, .segmented button, .quiz-card, .list-title")) sound.play("click");
});

// ---------- home ----------

function groupByCategory(quizzes) {
  const groups = new Map();
  for (const q of quizzes) {
    if (!groups.has(q.category)) groups.set(q.category, []);
    groups.get(q.category).push(q);
  }
  return groups;
}

// Quiz kinds, recognised from the id, so the quiz files don't need an extra field.
const KINDS = [
  ["grammar", "📚", "Grammar topics"],
  ["contrast", "⚖️", "Which one? (contrast)"],
  ["order", "★", "Sentence building"],
  ["reading", "📖", "Reading & exam practice"],
];
function quizKind(q) {
  if (/contrast/.test(q.id)) return "contrast";
  if (/sentence-order|word-order|hsk-order/.test(q.id)) return "order";
  if (/bunsho|hsk/.test(q.id)) return "reading";
  return "grammar";
}

const plainText = t => String(t || "").replace(/\{([^|{}]+)\|[^{}]+\}/g, "$1").replace(/\*\*/g, "");
const levelLabel = category => /mix/i.test(category) ? "Mix" : (category.match(/\b([NABC][1-5])\b/) || [])[1] || category;
// "Particles: が, に, で" → "Particles", "Which One? A/B, …" → "Which One?"; the points are listed separately.
const shortTitle = title => {
  const m = title.match(/^(.+?)(: |\? )/);
  return m ? m[1] + (m[2] === "? " ? "?" : "") : title;
};

function quizStatus(q, best, saved) {
  if (saved && (saved.key === `quiz:${q.id}` || saved.key === `retry|quiz:${q.id}`)) return "progress";
  if (best[q.id] == null) return "new";
  return best[q.id] >= 80 ? "done" : "weak";
}
const STATUS_LABEL = { new: "Not started", progress: "In progress", weak: "Below 80% — worth repeating", done: "80% or more" };

function bestBadge(best, id) {
  return best[id] != null ? `<span class="best">${best[id]}%</span>` : "";
}

function pointsLine(q) {
  return q.points.length ? q.points.map(p => render(shortTitle(p))).join(" · ") : render(q.description);
}

function quizItemHtml(q, best, saved, view, showLevel = false) {
  const st = quizStatus(q, best, saved);
  const href = `#/quiz/${encodeURIComponent(q.id)}`;
  const level = showLevel ? `<span class="pill">${escapeHtml(levelLabel(q.category))}</span>` : "";
  if (view === "list") {
    return `
    <div class="list-row">
      <span class="dot ${st}" title="${STATUS_LABEL[st]}"></span>
      <div class="list-main">
        <a class="list-title" href="${href}">${level}${render(shortTitle(q.title))}</a>
        <div class="list-points">${pointsLine(q)}</div>
      </div>
      <div class="list-side">
        <span class="muted">${q.count} Q</span>
        ${bestBadge(best, q.id)}
        <a class="btn small" href="${href}/start">Start</a>
      </div>
    </div>`;
  }
  return `
    <a class="quiz-card" href="${href}">
      <div class="qc-head"><span class="dot ${st}" title="${STATUS_LABEL[st]}"></span><h3>${level}${render(shortTitle(q.title))}</h3></div>
      <p>${pointsLine(q)}</p>
      <div class="meta"><span>${q.count} questions</span>${bestBadge(best, q.id)}</div>
    </a>`;
}

function itemsHtml(list, best, saved, view, showLevel) {
  const inner = list.map(q => quizItemHtml(q, best, saved, view, showLevel)).join("");
  return view === "list" ? `<div class="list">${inner}</div>` : `<div class="grid">${inner}</div>`;
}

function levelStats(list, best) {
  const done = list.filter(q => (best[q.id] ?? -1) >= 80).length;
  const started = list.filter(q => best[q.id] != null).length;
  return { done, started, total: list.length, pct: list.length ? Math.round((done / list.length) * 100) : 0 };
}

const FILTERS = { all: "All", open: "Open", weak: "Below 70%" };
function passesFilter(q, best, filter) {
  if (filter === "open") return (best[q.id] ?? -1) < 80;
  if (filter === "weak") return best[q.id] != null && best[q.id] < 70;
  return true;
}

function levelBodyHtml(category, list, best, saved, view, filter) {
  const stats = levelStats(list, best);
  const total = list.reduce((n, q) => n + q.count, 0);
  const shown = list.filter(q => passesFilter(q, best, filter));
  const collapsed = store.get("collapsed", {});
  const groups = KINDS.map(([kind, icon, label]) => {
    const items = shown.filter(q => quizKind(q) === kind);
    if (!items.length) return "";
    return `
      <details class="qgroup" data-kind="${kind}"${collapsed[kind] ? "" : " open"}>
        <summary><span>${icon} ${label}</span><span class="muted">${items.length}</span></summary>
        ${itemsHtml(items, best, saved, view)}
      </details>`;
  }).join("");
  return `
    <div class="level-head">
      <div>
        <h2>${escapeHtml(category)}</h2>
        <div class="muted">${stats.done} of ${stats.total} quizzes at 80%+ · ${stats.started} started</div>
        <div class="bar"><span style="width:${stats.pct}%"></span></div>
      </div>
      <div class="segmented mini filters" role="group" aria-label="Filter">
        ${Object.entries(FILTERS).map(([k, v]) => `<button data-filter="${k}" class="${k === filter ? "active" : ""}">${v}</button>`).join("")}
      </div>
    </div>
    <a class="mix-banner" href="#/mix/${encodeURIComponent(category)}">
      <span>🎲 <strong>Random mix</strong> — 20 questions from all ${total} in ${escapeHtml(levelLabel(category))}</span>
      <span class="btn small">Start</span>
    </a>
    ${groups || `<p class="muted empty">Nothing here with this filter — well done, or try “All”.</p>`}`;
}

function searchHtml(query, quizzes, best, saved, view) {
  const words = query.toLowerCase().split(/\s+/).filter(Boolean);
  const hits = quizzes.filter(q => {
    const hay = plainText([q.title, q.description, ...q.points].join(" ")).toLowerCase();
    return words.every(w => hay.includes(w));
  });
  if (!hits.length) return `<p class="muted empty">No quiz matches “${escapeHtml(query)}”.</p>`;
  return `<div class="level-head"><div><h2>Search</h2><div class="muted">${hits.length} quiz${hits.length === 1 ? "" : "zes"} for “${escapeHtml(query)}”</div></div></div>
    ${itemsHtml(hits, best, saved, view, true)}`;
}

async function showHome() {
  session = null;
  document.body.classList.add("home");
  const quizzes = (await api("/api/quizzes")).filter(q => (q.language || "ja") === lang);
  const best = store.get("best", {});
  const view = store.get("view", "cards");
  const filter = FILTERS[store.get("filter", "all")] ? store.get("filter", "all") : "all";
  const saved = loadProgress();
  const groups = [...groupByCategory(quizzes)];
  let level = store.get(`level:${lang}`, null);
  if (!groups.some(([c]) => c === level)) level = groups[0]?.[0];

  const levelNav = groups.map(([category, list]) => {
    const st = levelStats(list, best);
    return `<button class="level${category === level ? " active" : ""}" data-level="${escapeHtml(category)}">
      <span class="lv">${escapeHtml(levelLabel(category))}</span>
      <span class="lv-count">${st.done}/${st.total}</span>
      <span class="bar"><span style="width:${st.pct}%"></span></span>
    </button>`;
  }).join("");

  const resume = saved ? `
    <div class="resume-banner">
      <div><strong>Continue where you left off</strong><span class="muted">${render(saved.title)} · ${progressLabel(saved)}</span></div>
      <div class="resume-actions">
        <a class="btn small" href="${hrefFor(saved.key)}">Continue</a>
        <button class="btn small secondary" id="discard">Discard</button>
      </div>
    </div>` : "";

  app.innerHTML = `
    ${resume}
    <div class="home-head">
      <div>
        <h1>Choose a quiz</h1>
        <p class="sub">Pick a level, open a quiz to read its guide, or jump straight in.</p>
      </div>
      <div class="home-controls">
        <div class="segmented" role="group" aria-label="Language">
          ${Object.entries(LANGS).map(([k, v]) => `<button data-lang="${k}" class="${k === lang ? "active" : ""}">${v.label}</button>`).join("")}
        </div>
        <div class="segmented" role="group" aria-label="View">
          <button data-view="cards" class="${view === "cards" ? "active" : ""}">Cards</button>
          <button data-view="list" class="${view === "list" ? "active" : ""}">List</button>
        </div>
      </div>
    </div>
    <div class="home-layout">
      <nav class="levels" aria-label="Levels">${levelNav}</nav>
      <div class="level-main">
        <div class="search"><input id="search" type="search" placeholder="Search grammar — e.g. ${lang === "zh" ? "把, 了, even" : "ものの, ように, even if"}" autocomplete="off"></div>
        <div id="level-body"></div>
      </div>
    </div>`;

  const body = document.getElementById("level-body");
  const levelList = new Map(groups);
  const renderBody = () => {
    const query = document.getElementById("search").value.trim();
    body.innerHTML = query ? searchHtml(query, quizzes, best, saved, view)
      : levelBodyHtml(level, levelList.get(level) || [], best, saved, view, filter);
    body.querySelectorAll("[data-filter]").forEach(b => b.addEventListener("click", () => {
      store.set("filter", b.dataset.filter);
      showHome();
    }));
    body.querySelectorAll("details.qgroup").forEach(d => d.addEventListener("toggle", () => {
      const collapsed = store.get("collapsed", {});
      collapsed[d.dataset.kind] = !d.open;
      store.set("collapsed", collapsed);
    }));
  };
  renderBody();
  document.getElementById("search").addEventListener("input", renderBody);

  const discard = document.getElementById("discard");
  if (discard) discard.addEventListener("click", () => { clearProgress(); showHome(); });
  app.querySelectorAll("[data-level]").forEach(b => b.addEventListener("click", () => {
    store.set(`level:${lang}`, b.dataset.level);
    showHome();
  }));
  app.querySelector(".level.active")?.scrollIntoView({ block: "nearest", inline: "center" });
  app.querySelectorAll("[data-view]").forEach(b => b.addEventListener("click", () => {
    store.set("view", b.dataset.view);
    showHome();
  }));
  app.querySelectorAll("[data-lang]").forEach(b => b.addEventListener("click", () => {
    setLang(b.dataset.lang);
    showHome();
  }));
}

// ---------- quiz intro / study page ----------

async function showIntro(id) {
  session = null;
  const quiz = await api(`/api/quizzes/${encodeURIComponent(id)}`);
  setLang(quiz.language);
  const best = store.get("best", {});
  const saved = loadProgress(`quiz:${quiz.id}`, `retry|quiz:${quiz.id}`);
  const startHref = `#/quiz/${encodeURIComponent(quiz.id)}/start`;
  const startButtons = saved
    ? `<a class="btn" href="${startHref}">Continue (${progressLabel(saved)})</a>
       <button class="btn secondary" id="start-over">Start over</button>`
    : `<a class="btn" href="${startHref}">Start quiz (${quiz.questions.length} questions)</a>`;
  app.innerHTML = `
    <p class="crumb"><a href="#/">← All quizzes</a></p>
    <h1>${render(quiz.title)}</h1>
    <p class="sub">${render(quiz.description)}</p>
    <div class="actions" style="justify-content:flex-start">
      ${startButtons}
      ${quiz.points.length ? `<button class="btn secondary" id="expand">Expand all guides</button>` : ""}
      ${best[quiz.id] != null ? `<span class="muted" style="align-self:center">Best: ${best[quiz.id]}%</span>` : ""}
    </div>
    ${quiz.points.length ? `<h2 class="section-title">Grammar points</h2>${quiz.points.map(p => guideHtml(p)).join("")}` : ""}`;
  const startOver = document.getElementById("start-over");
  if (startOver) startOver.addEventListener("click", () => { clearProgress(); location.hash = startHref; });
  const expand = document.getElementById("expand");
  if (expand) expand.addEventListener("click", () => {
    const all = app.querySelectorAll("details.guide");
    const open = [...all].some(d => !d.open);
    all.forEach(d => { d.open = open; });
    expand.textContent = open ? "Collapse all guides" : "Expand all guides";
  });
}

// ---------- quiz ----------

function startSession(quiz, questions, key) {
  session = {
    key,
    quizId: quiz.id,
    title: quiz.title,
    questions: questions.map(q => ({ ...q, order: q.fixed_order ? q.options.map((_, i) => i) : shuffled(q.options.map((_, i) => i)) })),
    pos: 0,
    results: [],
    answered: false,
  };
  saveProgress();
  showQuestion();
}

// Picks up a saved session exactly where it was, including an answered-but-not-yet-advanced question.
function resumeSession(saved) {
  session = { ...saved, answered: false };
  delete session.savedAt;
  showQuestion();
  if (session.results.length > session.pos) {
    session.answered = true;
    renderAnswer(session.results[session.pos]);
  }
}

function showQuestion() {
  const s = session;
  const q = s.questions[s.pos];
  s.answered = false;
  const correctSoFar = s.results.filter(r => r.correct).length;
  const options = q.order.map((orig, i) => `
    <button class="option" data-choice="${orig}">
      <span class="key">${LETTERS[i]}</span><span>${render(q.options[orig])}</span>
    </button>`).join("");
  app.innerHTML = `
    <h1>${render(shortTitle(s.title))}</h1>
    <div class="progress-label"><span>Question ${s.pos + 1} / ${s.questions.length}</span><span>${correctSoFar} correct</span></div>
    <div class="progress"><div style="width:${(s.pos / s.questions.length) * 100}%"></div></div>
    <div class="question">
      <p class="prompt">${render(q.prompt)}</p>
      <div class="options">
        ${options}
        <button class="option dunno" data-choice="none"><span class="key">?</span><span>${LANGS[lang].dunno} (I don't know)</span></button>
      </div>
      <div id="feedback"></div>
    </div>
    <p class="hint">Keys: A–D or 1–4 to answer (afterwards: show why) · 0 for ${LANGS[lang].dunno} · Enter for next</p>`;
  app.querySelectorAll(".option").forEach(btn =>
    btn.addEventListener("click", () => answer(btn.dataset.choice === "none" ? null : Number(btn.dataset.choice))));
  window.scrollTo(0, 0);
}

async function answer(choice) {
  const s = session;
  if (!s) return;
  if (s.answered) return inspect(choice);
  s.answered = true;
  sound.play("click");
  const q = s.questions[s.pos];
  let resp;
  try {
    resp = await api("/api/check", { quiz_id: q.quiz_id, index: q.index, choice });
  } catch (e) {
    s.answered = false;
    alert("Could not reach the server: " + e.message);
    return;
  }
  s.results.push({ q, choice, ...resp });
  sound.play(resp.correct ? "correct" : "wrong");
  saveProgress();
  renderAnswer(s.results[s.results.length - 1]);
}

// Shows the marked options and feedback for an answered question (also used when resuming).
function renderAnswer(r) {
  const s = session;
  app.querySelector(".options").classList.add("answered");
  app.querySelectorAll(".option").forEach(btn => {
    const c = btn.dataset.choice === "none" ? null : Number(btn.dataset.choice);
    if (c === null) btn.disabled = true;
    if (c === r.answer) btn.classList.add("correct");
    else if (c === r.choice) btn.classList.add("wrong");
    else btn.classList.add("faded");
  });

  const last = s.pos === s.questions.length - 1;
  const fb = document.getElementById("feedback");
  fb.innerHTML = feedbackHtml(r.q, r.choice, r) + `
    <div class="actions"><button class="btn" id="next">${last ? "See results" : "Next →"}</button></div>`;
  const next = document.getElementById("next");
  next.addEventListener("click", advance);
  next.focus({ preventScroll: true });
  if (r.choice !== null) markInspected(r.choice);
}

// After answering, clicking an option (or pressing its key) shows the explanation for that option.
function whyHtml(q, orig, resp) {
  if (orig === resp.answer) return `<strong>「${render(q.options[orig])}」 is the answer.</strong> See the grammar point below.`;
  const note = resp.notes?.[orig] || (orig === resp.choice ? resp.note : "");
  return `<strong>Why not 「${render(q.options[orig])}」?</strong> ${
    note ? render(note) : "It doesn't fit the grammar of this sentence; see the explanation below."}`;
}

function markInspected(orig) {
  app.querySelectorAll(".option").forEach(b => b.classList.toggle("inspected", Number(b.dataset.choice) === orig && b.dataset.choice !== "none"));
}

function inspect(orig) {
  const s = session;
  const r = s.results[s.pos];
  if (!r || orig === null) return;
  const box = document.getElementById("why");
  if (!box) return;
  box.innerHTML = whyHtml(r.q, orig, r);
  box.hidden = false;
  markInspected(orig);
  sound.play("click");
}

function feedbackHtml(q, choice, resp) {
  const correctText = render(q.options[resp.answer]);
  let html;
  if (resp.correct) {
    html = `<div class="feedback good"><h4>${LANGS[lang].correct} Correct</h4>`;
  } else if (choice === null) {
    html = `<div class="feedback bad"><h4>The answer is 「${correctText}」</h4>`;
  } else {
    html = `<div class="feedback bad"><h4>Not quite. The answer is 「${correctText}」</h4>`;
  }
  html += `<div class="why-wrong" id="why"${resp.correct || choice === null ? " hidden" : ""}>${
    choice === null || resp.correct ? "" : whyHtml(q, choice, resp)}</div>`;
  html += `<p class="inspect-hint">Tap any option above to see why it is (or isn't) right.</p>`;
  html += `<span class="label">Grammar point</span><p>${render(resp.explanation)}</p>`;
  if (resp.translation) html += `<p class="translation">“${render(resp.translation)}”</p>`;
  html += `</div>`;
  if (resp.point) html += guideHtml(resp.point);
  return html;
}

function advance() {
  const s = session;
  if (!s || !s.answered) return;
  if (s.pos < s.questions.length - 1) { s.pos++; saveProgress(); showQuestion(); }
  else showResults();
}

// ---------- results ----------

function showResults() {
  const s = session;
  clearProgress();
  const correct = s.results.filter(r => r.correct).length;
  const pct = Math.round((correct / s.results.length) * 100);
  if (pct >= 70) sound.play("finish");
  if (s.quizId !== "mix" && s.quizId !== "retry") {
    const best = store.get("best", {});
    best[s.quizId] = Math.max(best[s.quizId] || 0, pct);
    store.set("best", best);
  }
  const mistakes = s.results.filter(r => !r.correct);
  const review = mistakes.map(r => `
    <div class="review-item">
      <p class="prompt">${render(r.q.prompt)}</p>
      <p class="ans yours">✗ Your answer: ${r.choice === null ? LANGS[lang].dunno : render(r.q.options[r.choice])}</p>
      <p class="ans right">✓ Correct: ${render(r.q.options[r.answer])}</p>
      ${r.note ? `<div class="why-wrong"><strong>Why yours is wrong:</strong> ${render(r.note)}</div>` : ""}
      <p>${render(r.explanation)}</p>
      ${r.translation ? `<p class="translation">“${render(r.translation)}”</p>` : ""}
      ${r.point ? guideHtml(r.point) : ""}
    </div>`).join("");
  app.innerHTML = `
    <h1>${render(shortTitle(s.title))}: results</h1>
    <p class="score-big">${correct} / ${s.results.length}</p>
    <p class="sub">${pct}% · ${pct === 100 ? "完璧！ Perfect score." : pct >= 80 ? "よくできました！ Well done." : pct >= 50 ? "もう少し！ Getting there." : "がんばって！ Review the points below and try again."}</p>
    <div class="actions" style="justify-content:flex-start">
      ${mistakes.length ? `<button class="btn" id="retry">Retry my ${mistakes.length} mistake${mistakes.length > 1 ? "s" : ""}</button>` : ""}
      <button class="btn secondary" id="again">Restart</button>
      <a class="btn secondary" href="#/">All quizzes</a>
    </div>
    ${mistakes.length ? `<h2 class="section-title">Review</h2>${review}` : ""}`;
  const retry = document.getElementById("retry");
  if (retry) retry.addEventListener("click", () =>
    startSession({ id: "retry", title: `${shortTitle(s.title)} (mistakes)` }, shuffled(mistakes.map(r => r.q)), `retry|${baseKey(s.key)}`));
  document.getElementById("again").addEventListener("click", () => restart(baseKey(s.key)));
  window.scrollTo(0, 0);
}

// ---------- routing & keys ----------

async function startQuiz(id, fresh = false) {
  const key = `quiz:${id}`;
  const saved = !fresh && loadProgress(key, `retry|${key}`);
  if (saved) return resumeSession(saved);
  const quiz = await api(`/api/quizzes/${encodeURIComponent(id)}`);
  setLang(quiz.language);
  startSession(quiz, quiz.questions, key);
}

async function startMix(category, fresh = false) {
  const key = `mix:${category}`;
  const saved = !fresh && loadProgress(key, `retry|${key}`);
  if (saved) return resumeSession(saved);
  const query = category ? `&category=${encodeURIComponent(category)}` : "";
  const quiz = await api(`/api/mix?count=20${query}`);
  quiz.title = category ? `Random mix: ${category}` : "Random mix";
  setLang(quiz.language);
  startSession(quiz, quiz.questions, key);
}

function restart(key) {
  clearProgress();
  if (key.startsWith("quiz:")) startQuiz(key.slice(5), true);
  else startMix(key.slice(4), true);
}

async function route() {
  const hash = location.hash;
  document.body.classList.remove("home");
  let m;
  try {
    if ((m = hash.match(/^#\/quiz\/([^/]+)\/start$/))) await startQuiz(decodeURIComponent(m[1]));
    else if ((m = hash.match(/^#\/quiz\/([^/]+)$/))) await showIntro(decodeURIComponent(m[1]));
    else if ((m = hash.match(/^#\/mix(?:\/(.+))?$/))) await startMix(m[1] ? decodeURIComponent(m[1]) : "");
    else await showHome();
  } catch (e) {
    app.innerHTML = `<p>Something went wrong: ${escapeHtml(e.message)}</p><p><a href="#/">Back to quizzes</a></p>`;
  }
  window.scrollTo(0, 0);
}

document.getElementById("home-link").addEventListener("click", e => { e.preventDefault(); location.hash = "#/"; });
window.addEventListener("hashchange", route);

document.addEventListener("keydown", e => {
  if (!session || e.metaKey || e.ctrlKey || e.altKey) return;
  const s = session;
  if (!document.querySelector(".question")) return;
  const order = s.questions[s.pos].order;
  if (s.answered) {
    if (e.key === "Enter" || e.key === "ArrowRight") { e.preventDefault(); advance(); return; }
    const k = e.key.toUpperCase();
    let i = LETTERS.indexOf(k);
    if (i < 0 && /^[1-9]$/.test(k)) i = Number(k) - 1;
    if (i >= 0 && i < order.length) inspect(order[i]);
    return;
  }
  const k = e.key.toUpperCase();
  let i = LETTERS.indexOf(k);
  if (i < 0 && /^[1-9]$/.test(k)) i = Number(k) - 1;
  if (i >= 0 && i < order.length) answer(order[i]);
  else if (k === "0" || k === "?") answer(null);
});

route();
