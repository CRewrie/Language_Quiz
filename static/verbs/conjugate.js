// Conjugation engine for the verb lookup. Works on kana (the reading); toKanji() puts the verb's kanji back.
// Verb: { k: kanji, r: reading, c: class } — class: ru, u, iku, aru, suru, kuru, honor (いらっしゃる …), tou (問う).
// tools/gen_verb_dict.py checks it against the Verb Lab's engine (tools/gen_ja_verbs.py).
const Conj = (() => {
  const ROW = { "う": "わいうえお", "く": "かきくけこ", "ぐ": "がぎぐげご", "す": "さしすせそ", "つ": "たちつてと",
    "ぬ": "なにぬねの", "ぶ": "ばびぶべぼ", "む": "まみむめも", "る": "らりるれろ" };
  const A = 0, I = 1, E = 3, O = 4;
  const GODAN = new Set(["u", "iku", "aru", "honor", "tou"]);
  // Verbs that already mean "can …", so they have no potential form of their own.
  const NO_POTENTIAL = new Set(["できる", "分かる", "見える", "聞こえる", "要る", "ある"]);
  // Verbs that are keigo themselves, or have no keigo form in use.
  const NO_KEIGO = new Set(["いらっしゃる", "おっしゃる", "くださる", "なさる", "召し上がる", "参る", "申す", "致す", "いただく",
    "差し上げる", "おる", "拝見する", "申し上げる", "うかがう", "ある", "できる", "分かる", "見える", "聞こえる", "要る"]);

  // 愛する, 接する …: the noun is a single kanji, so 愛できる / ご愛になる don't exist
  const oneKanjiSuru = v => v.c === "suru" && v.k !== v.r && [...v.k].length === 3;
  const shift = (r, col) => r.slice(0, -1) + ROW[r.at(-1)][col];
  const drop = (s, n = 1) => s.slice(0, -n);

  function masuStem(r, c) {
    if (c === "ru") return drop(r);
    if (c === "suru") return drop(r, 2) + "し";
    if (c === "kuru") return "き";
    if (c === "honor") return drop(r) + "い";
    return shift(r, I);
  }

  function nai(r, c) {
    if (c === "aru") return "ない";
    if (c === "ru") return drop(r) + "ない";
    if (c === "suru") return drop(r, 2) + "しない";
    if (c === "kuru") return "こない";
    return shift(r, A) + "ない";
  }

  function te(r, c, ta = false) {
    const [t, d] = ta ? ["た", "だ"] : ["て", "で"];
    if (c === "ru") return drop(r) + t;
    if (c === "suru") return drop(r, 2) + "し" + t;
    if (c === "kuru") return "き" + t;
    if (c === "iku") return drop(r) + "っ" + t;
    if (c === "tou") return r + t;
    const last = r.at(-1), s = drop(r);
    if ("うつる".includes(last)) return s + "っ" + t;
    if ("ぬぶむ".includes(last)) return s + "ん" + d;
    if (last === "く") return s + "い" + t;
    if (last === "ぐ") return s + "い" + d;
    if (last === "す") return s + "し" + t;
    throw new Error("cannot conjugate " + r);
  }

  // Keigo with its own verb: [kanji, kana] in the polite present.
  const HONORIFIC = {
    "来る": [["いらっしゃいます", "いらっしゃいます"], ["お見えになります", "おみえになります"]],
    "行く": [["いらっしゃいます", "いらっしゃいます"], ["おいでになります", "おいでになります"]],
    "いる": [["いらっしゃいます", "いらっしゃいます"]],
    "食べる": [["召し上がります", "めしあがります"]], "飲む": [["召し上がります", "めしあがります"]],
    "言う": [["おっしゃいます", "おっしゃいます"]], "見る": [["ご覧になります", "ごらんになります"]],
    "する": [["なさいます", "なさいます"]], "寝る": [["お休みになります", "おやすみになります"]],
    "着る": [["お召しになります", "おめしになります"]], "知る": [["ご存じです", "ごぞんじです"]],
    "くれる": [["くださいます", "くださいます"]],
  };
  const HUMBLE = {
    "行く": [["参ります", "まいります"], ["伺います", "うかがいます"]], "来る": [["参ります", "まいります"]],
    "言う": [["申します", "もうします"], ["申し上げます", "もうしあげます"]], "見る": [["拝見します", "はいけんします"]],
    "する": [["いたします", "いたします"]], "会う": [["お目にかかります", "おめにかかります"]],
    "食べる": [["いただきます", "いただきます"]], "飲む": [["いただきます", "いただきます"]], "もらう": [["いただきます", "いただきます"]],
    "いる": [["おります", "おります"]], "あげる": [["差し上げます", "さしあげます"]], "知る": [["存じております", "ぞんじております"]],
    "思う": [["存じます", "ぞんじます"]], "聞く": [["伺います", "うかがいます"]], "訪ねる": [["伺います", "うかがいます"]],
    "見せる": [["お目にかけます", "おめにかけます"]], "借りる": [["拝借します", "はいしゃくします"]], "読む": [["拝読します", "はいどくします"]],
  };
  // Noun + する that take お (not ご) in keigo.
  const O_NOUNS = new Set(["電話", "返事", "約束", "世話", "掃除", "洗濯", "料理", "買い物", "散歩", "化粧"]);

  /** Every form as a list of kana spellings (first = main), or null when the verb has no such form. */
  function conjugate(v) {
    const { r, c } = v;
    const ms = masuStem(r, c), n = nai(r, c), t = te(r, c), ta = te(r, c, true);
    const p = drop(r, 2); // the noun of noun + する ("" for する itself)
    const pick = (ru, suru, kuru, godan) => c === "ru" ? ru : c === "suru" ? suru : c === "kuru" ? kuru : godan;
    const f = {
      dict: [r], nai: [n], ta: [ta], nakatta: [drop(n) + "かった"],
      masu: [ms + "ます"], masen: [ms + "ません"], mashita: [ms + "ました"], masendeshita: [ms + "ませんでした"],
      mashou: [ms + "ましょう"], stem: [ms],
      te: [t], naide: [n + "で"], nakute: [drop(n) + "くて"], teiru: [t + "いる"], tekudasai: [t + "ください"],
      naidekudasai: [n + "でください"], temoii: [t + "もいい"], tewaikenai: [t + "はいけない"], tari: [ta + "り"],
      ba: [pick(drop(r) + "れば", p + "すれば", "くれば", shift(r, E) + "ば")],
      nakereba: [drop(n) + "ければならない", drop(n) + "ければいけない", drop(n) + "きゃ"],
      tara: [ta + "ら"], nakattara: [drop(n) + "かったら"],
      volitional: [pick(drop(r) + "よう", p + "しよう", "こよう", shift(r, O) + "う")],
      tai: [ms + "たい"], takunai: [ms + "たくない"], nasai: [ms + "なさい"],
      prohibitive: [r + "な"],
    };
    const imp = c === "aru" ? null : pick([r === "くれる" ? "くれ" : drop(r) + "ろ"], [p + "しろ", p + "せよ"], ["こい"],
      [c === "honor" ? drop(r) + "い" : shift(r, E)]);
    f.imperative = imp;
    if (!NO_POTENTIAL.has(v.k) && c !== "aru" && !oneKanjiSuru(v)) {
      const pot = pick(drop(r) + "られる", p + "できる", "こられる", shift(r, E) + "る");
      f.potential = [pot];
      f.potential_nai = [drop(pot) + "ない"];
      f.potential_masu = [drop(pot) + "ます"];
    }
    if (c !== "aru") {
      const pas = pick(drop(r) + "られる", p + "される", "こられる", shift(r, A) + "れる");
      const cau = pick(drop(r) + "させる", p + "させる", "こさせる", shift(r, A) + "せる");
      const long = drop(cau) + "られる";
      // godan: the short causative-passive (飲まされる) is the usual one, except after す (話させられる)
      const cp = GODAN.has(c) && r.at(-1) !== "す" ? [shift(r, A) + "される", long] : [long];
      Object.assign(f, {
        passive: [pas], passive_ta: [drop(pas) + "た"],
        causative: [cau], causative_ta: [drop(cau) + "た"],
        caus_pass: cp, caus_pass_ta: cp.map(x => drop(x) + "た"),
      });
    }
    if (c === "aru") { // ある is about things: no requests, wishes or ongoing ている
      for (const id of ["teiru", "tekudasai", "naidekudasai", "temoii", "tewaikenai", "mashou", "tai", "takunai", "nasai",
        "prohibitive", "volitional"]) delete f[id];
    }
    if (c === "honor") { // keigo verbs are used for others' actions: no "I want to", "can", passive or causative
      for (const id of Object.keys(f)) if (/^(potential|passive|causative|caus_pass|tai|takunai|nasai|volitional)/.test(id)) delete f[id];
    }
    return f;
  }

  // Shared kana ending of kanji and reading: 食べる / たべる → 2
  function okuri(k, r) {
    let n = 0;
    while (n < Math.min(k.length, r.length) && k.at(-1 - n) === r.at(-1 - n)) n++;
    return n;
  }

  /** Kana form → the same form written with the verb's kanji (たべました → 食べました). */
  function toKanji(kana, v) {
    const { k, r, c } = v;
    if (k === r) return kana;
    if (c === "kuru") return "きくこ".includes(kana[0]) ? "来" + kana.slice(1) : kana;
    const n = okuri(k, r), kp = k.slice(0, k.length - n), rp = r.slice(0, r.length - n);
    return kana.startsWith(rp) ? kp + kana.slice(rp.length) : kana;
  }

  /** Honorific and humble (polite present): list of [kanji, kana], or null. */
  function keigo(v, humble) {
    if (NO_KEIGO.has(v.k) || v.c === "honor" || oneKanjiSuru(v) || (humble && v.k === "くれる")) return null;
    const own = (humble ? HUMBLE : HONORIFIC)[v.k];
    if (own) return Object.assign([...own], { own: true });
    if (v.c === "suru") {
      if (v.k === v.r && v.r !== "する") { // katakana noun: コピーなさいます / コピーいたします
        const s = drop(v.k, 2) + (humble ? "いたします" : "なさいます");
        return [[s, s]];
      }
      const nk = drop(v.k, 2), nr = drop(v.r, 2), pre = O_NOUNS.has(nk) ? "お" : "ご";
      return humble
        ? [[nk + "いたします", nr + "いたします"], [pre + nk + "します", pre + nr + "します"], [pre + nk + "いたします", pre + nr + "いたします"]]
        : [[nk + "なさいます", nr + "なさいます"], [pre + nk + "になります", pre + nr + "になります"]];
    }
    if (v.c === "kuru") return null;
    const sr = masuStem(v.r, v.c);
    if (sr.length < 2) return null; // 寝る, 出る …: no お〜になる form (お出になる is wrong)
    const sk = toKanji(sr + "ます", v).slice(0, -2);
    return humble
      ? [["お" + sk + "します", "お" + sr + "します"], ["お" + sk + "いたします", "お" + sr + "いたします"]]
      : [["お" + sk + "になります", "お" + sr + "になります"]];
  }

  // How a form is built, per verb class. {E} etc. are filled in by how().
  function how(id, v) {
    const { r, c } = v;
    const last = r.at(-1);
    const row = col => `${last} → ${shift(r, col).at(-1)}`;
    const irregular = c === "suru" ? "する is irregular" : c === "kuru" ? "来る is irregular" : "";
    const stemRule = c === "ru" ? "drop る" : c === "honor" ? "る → い (special)" : irregular || row(I);
    const naiRule = c === "ru" ? "drop る" : c === "aru" ? "ある → ない (irregular)" : irregular ||
      `${row(A)}${last === "う" ? " (う becomes わ)" : ""}`;
    const tete = (t, d) => c === "ru" ? `drop る + ${t}` : c === "iku" ? `行く → 行っ${t} (exception)` :
      c === "tou" ? `問う → 問う${t} (exception)` : irregular || {
        "う": `う・つ・る → っ${t}`, "つ": `う・つ・る → っ${t}`, "る": `う・つ・る → っ${t}`, "ぬ": `ぬ・ぶ・む → ん${d}`,
        "ぶ": `ぬ・ぶ・む → ん${d}`, "む": `ぬ・ぶ・む → ん${d}`, "く": `く → い${t}`, "ぐ": `ぐ → い${d}`, "す": `す → し${t}` }[last];
    const teRule = tete("て", "で"), taRule = tete("た", "だ");
    const g = (ru, other) => c === "ru" ? ru : irregular || other;
    const R = {
      dict: "the dictionary form",
      masu: `ます-stem (${stemRule}) + ます`, masen: `ます-stem (${stemRule}) + ません`, mashita: `ます-stem (${stemRule}) + ました`,
      masendeshita: `ます-stem (${stemRule}) + ませんでした`, mashou: `ます-stem (${stemRule}) + ましょう`, stem: stemRule,
      nai: `${naiRule} + ない`, nakatta: `ない → なかった`, naide: "ない-form + で", nakute: "ない → なくて",
      ta: taRule, te: teRule, teiru: "て-form + いる", tekudasai: "て-form + ください", naidekudasai: "ない-form + でください",
      temoii: "て-form + もいい", tewaikenai: "て-form + はいけない", tari: "た-form + り",
      ba: g("drop る + れば", `${row(E)} + ば`), nakereba: "ない → なければ + ならない / いけない (casual: なきゃ)",
      tara: "た-form + ら", nakattara: "なかった + ら",
      volitional: g("drop る + よう", `${row(O)} + う`),
      tai: `ます-stem + たい (conjugates like an い-adjective)`, takunai: "ます-stem + たくない", nasai: "ます-stem + なさい",
      imperative: g("drop る + ろ", c === "honor" ? "る → い (special)" : `${row(E)}`), prohibitive: "dictionary form + な",
      potential: g("drop る + られる", `${row(E)} + る`), potential_nai: "potential is a る-verb: drop る + ない",
      potential_masu: "potential is a る-verb: drop る + ます",
      passive: g("drop る + られる", `${row(A)} + れる`), passive_ta: "passive is a る-verb: drop る + た",
      causative: g("drop る + させる", `${row(A)} + せる`), causative_ta: "causative is a る-verb: drop る + た",
      caus_pass: g("drop る + させられる", `${row(A)} + される (long form: せられる)`),
      caus_pass_ta: "causative-passive is a る-verb: drop る + た",
      hon: "お + ます-stem + になる (verbs with their own keigo word use that)",
      hum: "お + ます-stem + する (verbs with their own keigo word use that)",
    };
    return R[id] || "";
  }

  // Groups of forms. ex: example sentence — {F} is the form, {名|な} is furigana; en: {V} base, {Vd} past,
  // {Vn} past participle, {Vg} -ing of the verb's English meaning.
  const GROUPS = [
    { title: "Polite (です・ます)", forms: [
      { id: "masu", label: "present / future", jp: "ます形", ex: "{明日|あした}{F}。", en: "I'll {V} tomorrow." },
      { id: "masen", label: "negative", jp: "ません", ex: "{今日|きょう}は{F}。", en: "I won't {V} today." },
      { id: "mashita", label: "past", jp: "ました", ex: "{昨日|きのう}{F}。", en: "I {Vd} yesterday." },
      { id: "masendeshita", label: "past negative", jp: "ませんでした", ex: "{昨日|きのう}は{F}。", en: "I didn't {V} yesterday." },
      { id: "mashou", label: "let's …", jp: "ましょう", ex: "{一緒|いっしょ}に{F}。", en: "Let's {V} together." },
    ] },
    { title: "Plain (casual)", forms: [
      { id: "dict", label: "present / future", jp: "辞書形", ex: "{明日|あした}{F}よ。", en: "I'll {V} tomorrow." },
      { id: "nai", label: "negative", jp: "ない形", ex: "{今日|きょう}は{F}。", en: "I won't {V} today." },
      { id: "ta", label: "past", jp: "た形", ex: "{昨日|きのう}{F}。", en: "I {Vd} yesterday." },
      { id: "nakatta", label: "past negative", jp: "なかった", ex: "{昨日|きのう}は{F}。", en: "I didn't {V} yesterday." },
      { id: "stem", label: "ます-stem", jp: "連用形", ex: "{F}に{行|い}きます。", en: "I'm going (out) to {V}." },
    ] },
    { title: "て-form and friends", forms: [
      { id: "te", label: "て-form (… and …)", jp: "て形", ex: "{F}から、{帰|かえ}ります。", en: "I'll {V}, and then go home." },
      { id: "teiru", label: "ongoing / resulting state", jp: "ている", ex: "{今|いま}、{F}。", en: "I'm {Vg} right now." },
      { id: "tekudasai", label: "please …", jp: "てください", ex: "どうぞ、{F}。", en: "Please {V}." },
      { id: "naidekudasai", label: "please don't …", jp: "ないでください", ex: "ここでは{F}。", en: "Please don't {V} here." },
      { id: "temoii", label: "may …", jp: "てもいい", ex: "{F}ですか。", en: "May I {V}?" },
      { id: "tewaikenai", label: "must not …", jp: "てはいけない", ex: "ここで{F}。", en: "You must not {V} here." },
      { id: "nakute", label: "not having to …", jp: "なくてもいい", ex: "{F}もいいです。", en: "You don't have to {V}." },
      { id: "tari", label: "things like …", jp: "たり", ex: "{週末|しゅうまつ}は{F}、{休|やす}んだりします。", en: "On weekends I do things like {Vg} and resting." },
    ] },
    { title: "If and when", forms: [
      { id: "ba", label: "if … (ば)", jp: "ば形", ex: "{F}、{分|わ}かりますよ。", en: "If you {V}, you'll understand." },
      { id: "tara", label: "if / when … (たら)", jp: "たら", ex: "{F}、{連絡|れんらく}してください。", en: "When you {V}, let me know." },
      { id: "nakattara", label: "if … not", jp: "なかったら", ex: "{F}、{困|こま}ります。", en: "If you don't {V}, I'll be in trouble." },
      { id: "nakereba", label: "must …", jp: "なければならない", ex: "{明日|あした}までに{F}。", en: "I have to {V} by tomorrow." },
    ] },
    { title: "Wanting, intending, ordering", forms: [
      { id: "tai", label: "want to …", jp: "たい", ex: "{私|わたし}も{F}です。", en: "I want to {V} too." },
      { id: "takunai", label: "don't want to …", jp: "たくない", ex: "{今日|きょう}は{F}です。", en: "I don't want to {V} today." },
      { id: "volitional", label: "let's / I'll … (plain)", jp: "意向形", ex: "{F}と{思|おも}います。", en: "I think I'll {V}." },
      { id: "nasai", label: "do … (firm request)", jp: "なさい", ex: "{早|はや}く{F}。", en: "{V}, quickly. (parent to child)" },
      { id: "imperative", label: "command (blunt)", jp: "命令形", ex: "{早|はや}く{F}！", en: "{V}, quickly! (blunt — shouted, signs, manga)" },
      { id: "prohibitive", label: "don't! (blunt)", jp: "禁止形", ex: "{F}！", en: "Don't {V}! (blunt)" },
    ] },
    { title: "Can (potential)", forms: [
      { id: "potential", label: "can …", jp: "可能形", ex: "{私|わたし}も{F}よ。", en: "I can {V} too." },
      { id: "potential_masu", label: "can … (polite)", jp: "可能形・ます", ex: "{私|わたし}も{F}。", en: "I can {V} too." },
      { id: "potential_nai", label: "can't …", jp: "可能形・ない", ex: "まだ{F}。", en: "I can't {V} yet." },
    ] },
    { title: "Passive and causative", forms: [
      { id: "passive", label: "passive", jp: "受身形", ex: "よく{F}。", en: "It's often {Vn}. (people often {V} it)" },
      { id: "passive_ta", label: "passive, past", jp: "受身形・た", ex: "{友|とも}だちに{F}。", en: "It was {Vn} by my friend. (with verbs that take no object: my friend {Vd}, and it bothered me)" },
      { id: "causative", label: "make / let …", jp: "使役形", ex: "{子供|こども}に{F}。", en: "I make (or let) the child {V}." },
      { id: "causative_ta", label: "made / let …, past", jp: "使役形・た", ex: "{子供|こども}に{F}。", en: "I made (or let) the child {V}." },
      { id: "caus_pass", label: "be made to …", jp: "使役受身形", ex: "いつも{母|はは}に{F}。", en: "My mother always makes me {V}." },
      { id: "caus_pass_ta", label: "was made to …", jp: "使役受身形・た", ex: "{母|はは}に{F}。", en: "I was made to {V} by my mother." },
    ] },
    { title: "Keigo (polite speech)", forms: [
      { id: "hon", label: "honorific (someone else does it)", jp: "尊敬語", ex: "{先生|せんせい}が{F}。", en: "The teacher will {V}. (respectful)" },
      { id: "hum", label: "humble (I do it)", jp: "謙譲語", ex: "{私|わたし}が{F}。", en: "I will {V}. (humble)" },
    ] },
  ];

  /** Every form of a verb: { id: { kanji: [...], kana: [...] } } (kanji = kana when the verb has no kanji). */
  function table(v) {
    const f = conjugate(v), out = {};
    for (const [id, kana] of Object.entries(f)) {
      if (kana) out[id] = { kana, kanji: kana.map(x => toKanji(x, v)) };
    }
    for (const [id, humble] of [["hon", false], ["hum", true]]) {
      const kg = keigo(v, humble);
      if (kg) out[id] = { kanji: kg.map(x => x[0]), kana: kg.map(x => x[1]), own: !!kg.own };
    }
    return out;
  }

  return { conjugate, toKanji, keigo, table, how, GROUPS, NO_POTENTIAL, oneKanjiSuru };
})();
if (typeof module !== "undefined") module.exports = Conj;
