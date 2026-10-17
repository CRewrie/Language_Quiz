//! Local Japanese grammar quiz server.
//!
//! Quizzes are JSON files under `quizzes/` (subfolders allowed; loaded at startup,
//! sorted by path). A quiz may carry grammar `points`: study guides that its
//! questions refer to by id.
//! The browser never receives the answers up front: each choice is POSTed to
//! `/api/check`, which returns whether it was right plus the explanations.
//!
//! `japanese_quiz export <dir>` instead writes a static copy of the site (for GitHub Pages):
//! the same pages plus every quiz as JSON, with the checking done in the browser.

use std::{
    collections::HashMap,
    env, fs,
    net::{IpAddr, SocketAddr},
    path::{Path, PathBuf},
    sync::{
        atomic::{AtomicU64, Ordering},
        Arc,
    },
    time::{SystemTime, UNIX_EPOCH},
};

use axum::{
    extract::{Path as UrlPath, Query, State},
    http::{header, StatusCode},
    response::{Html, IntoResponse, Response},
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};

#[derive(Deserialize, Serialize, Clone)]
struct Quiz {
    id: String,
    #[serde(default = "default_category")]
    category: String,
    /// "ja" (default) or "zh"; the home page shows one language at a time.
    #[serde(default = "default_language")]
    language: String,
    title: String,
    description: String,
    level: String,
    #[serde(default)]
    points: Vec<Point>,
    questions: Vec<Question>,
}

fn default_category() -> String {
    "Other".into()
}

fn default_language() -> String {
    "ja".into()
}

/// A grammar point with a fuller explanation than a single question's feedback.
#[derive(Deserialize, Serialize, Clone)]
struct Point {
    id: String,
    title: String,
    summary: String,
    /// Paragraphs separated by blank lines; lines starting with "- " are bullets.
    body: String,
    /// Pairs of [Japanese, English].
    #[serde(default)]
    examples: Vec<[String; 2]>,
}

#[derive(Deserialize, Serialize, Clone)]
struct Question {
    prompt: String,
    options: Vec<String>,
    answer: usize,
    /// The grammar point behind the correct answer.
    explanation: String,
    /// One note per option: why that option is wrong (empty for the correct one).
    #[serde(default)]
    notes: Vec<String>,
    #[serde(default)]
    translation: String,
    /// Id of the grammar point (in the same quiz) this question practises.
    #[serde(default)]
    point: Option<String>,
    /// Show the options in the given order (e.g. positions A–D in a sentence).
    #[serde(default, skip_serializing_if = "std::ops::Not::not")]
    fixed_order: bool,
}

impl Quiz {
    fn point(&self, id: Option<&str>) -> Option<&Point> {
        id.and_then(|id| self.points.iter().find(|p| p.id == id))
    }
}

struct AppState {
    quizzes: Vec<Quiz>,
    /// Traditional-character copies of the Mandarin quizzes, by the same index.
    traditional: Vec<Option<Quiz>>,
    by_id: HashMap<String, usize>,
}

impl AppState {
    fn quiz(&self, id: &str, script: Script) -> Option<&Quiz> {
        self.by_id.get(id).map(|&i| self.nth(i, script))
    }

    fn nth(&self, i: usize, script: Script) -> &Quiz {
        match (script, &self.traditional[i]) {
            (Script::Traditional, Some(trad)) => trad,
            _ => &self.quizzes[i],
        }
    }

    fn all(&self, script: Script) -> impl Iterator<Item = &Quiz> {
        (0..self.quizzes.len()).map(move |i| self.nth(i, script))
    }
}

/// Which Chinese script to serve; only affects quizzes with `language: "zh"`.
#[derive(Deserialize, Clone, Copy, Default, PartialEq)]
enum Script {
    #[default]
    #[serde(rename = "simp")]
    Simplified,
    #[serde(rename = "trad")]
    Traditional,
}

#[derive(Deserialize, Default)]
struct ScriptParam {
    #[serde(default)]
    script: Script,
}

/// Simplified characters with more than one traditional form, decided by the ruby reading
/// (`{只|zhī}` is the measure word 隻, `{只|zhǐ}` stays 只).
const BY_READING: &[(&str, &str)] = &[
    ("{只|zhī}", "{隻|zhī}"),
    ("{里|lǐ}", "{裡|lǐ}"),
    ("{发|fà}", "{髮|fà}"),
    ("{干|gàn}", "{幹|gàn}"),
    ("{干|gān}", "{乾|gān}"),
];

/// Simplified → traditional (Taiwan-style 著 and 裡, but no vocabulary swaps, so the pinyin still fits).
fn traditional(text: &str) -> String {
    let mut s = text.to_string();
    for (simp, trad) in BY_READING {
        s = s.replace(simp, trad);
    }
    let s = zhconv::zhconv(&s, zhconv::Variant::ZhHant).replace('着', "著");
    // Left-over 里 is the location word (包里, 屋里) → 裡; only the distance unit stays 里.
    const UNITS: &[&str] = &["公里", "英里", "千里", "里程"];
    let mut s = s;
    for (i, unit) in UNITS.iter().enumerate() {
        s = s.replace(unit, &format!("\u{1}{i}\u{1}"));
    }
    s = s.replace('里', "裡");
    for (i, unit) in UNITS.iter().enumerate() {
        s = s.replace(&format!("\u{1}{i}\u{1}"), unit);
    }
    s
}

/// Converts every Chinese text field of a quiz to traditional characters.
/// Pinyin and English pass through unchanged; the category stays as is so mixes still match.
fn to_traditional(quiz: &Quiz) -> Quiz {
    let t = traditional;
    let mut q = quiz.clone();
    q.title = t(&q.title);
    q.description = t(&q.description);
    for p in &mut q.points {
        p.title = t(&p.title);
        p.summary = t(&p.summary);
        p.body = t(&p.body);
        for ex in &mut p.examples {
            ex[0] = t(&ex[0]);
        }
    }
    for question in &mut q.questions {
        question.prompt = t(&question.prompt);
        question.options = question.options.iter().map(|o| t(o)).collect();
        question.explanation = t(&question.explanation);
        question.notes = question.notes.iter().map(|n| t(n)).collect();
    }
    q
}

type Shared = Arc<AppState>;

#[derive(Serialize)]
struct QuizSummary<'a> {
    id: &'a str,
    category: &'a str,
    language: &'a str,
    title: &'a str,
    description: &'a str,
    level: &'a str,
    count: usize,
    points: Vec<&'a str>,
}

#[derive(Serialize, Clone)]
struct PublicQuestion<'a> {
    quiz_id: &'a str,
    index: usize,
    prompt: &'a str,
    options: &'a [String],
    #[serde(skip_serializing_if = "std::ops::Not::not")]
    fixed_order: bool,
    /// Used only to order questions; never sent to the browser.
    #[serde(skip)]
    answer_text: &'a str,
    #[serde(skip)]
    point: Option<&'a str>,
}

#[derive(Serialize)]
struct PublicQuiz<'a> {
    id: &'a str,
    language: &'a str,
    title: &'a str,
    description: &'a str,
    level: &'a str,
    points: &'a [Point],
    questions: Vec<PublicQuestion<'a>>,
}

#[derive(Deserialize)]
struct CheckRequest {
    quiz_id: String,
    index: usize,
    /// `None` means "わかりません".
    choice: Option<usize>,
    #[serde(default)]
    script: Script,
}

#[derive(Serialize)]
struct CheckResponse<'a> {
    correct: bool,
    answer: usize,
    explanation: &'a str,
    /// Why the chosen option is wrong, if it was wrong and a note exists.
    note: Option<&'a str>,
    /// One note per option (empty for the correct one), so every option can be reviewed afterwards.
    notes: &'a [String],
    translation: &'a str,
    point: Option<&'a Point>,
}

#[derive(Deserialize)]
struct MixParams {
    count: Option<usize>,
    /// Restrict the mix to one category.
    category: Option<String>,
    #[serde(default)]
    script: Script,
}

fn public_questions(quiz: &Quiz) -> Vec<PublicQuestion<'_>> {
    quiz.questions
        .iter()
        .enumerate()
        .map(|(index, q)| PublicQuestion {
            quiz_id: &quiz.id,
            index,
            prompt: &q.prompt,
            options: &q.options,
            fixed_order: q.fixed_order,
            answer_text: &q.options[q.answer],
            point: q.point.as_deref(),
        })
        .collect()
}

/// Orders questions so that the same correct answer never appears twice in a row
/// (when the question pool allows it), and the same grammar point rarely does.
fn spread(items: &mut Vec<PublicQuestion>) {
    // Repeated answers count far more than repeated grammar points.
    let cost = |qs: &[PublicQuestion]| -> usize {
        qs.windows(2)
            .map(|w| {
                let answer = usize::from(w[0].answer_text == w[1].answer_text) * 100;
                let point = usize::from(w[0].point.is_some() && w[0].point == w[1].point);
                answer + point
            })
            .sum()
    };
    let mut rng = Rng::new();
    let mut best: Option<(usize, Vec<PublicQuestion>)> = None;
    for _ in 0..200 {
        let candidate = greedy_order(items, &mut rng);
        let c = cost(&candidate);
        if best.as_ref().is_none_or(|(b, _)| c < *b) {
            best = Some((c, candidate));
        }
        if c == 0 {
            break;
        }
    }
    if let Some((_, order)) = best {
        *items = order;
    }
}

/// Builds a random order one question at a time, never repeating the previous answer
/// unless forced, and placing the most frequent answer first when it would otherwise run out of room.
fn greedy_order<'a>(items: &[PublicQuestion<'a>], rng: &mut Rng) -> Vec<PublicQuestion<'a>> {
    let mut pool = items.to_vec();
    rng.shuffle(&mut pool);
    let mut out: Vec<PublicQuestion> = Vec::with_capacity(pool.len());
    while !pool.is_empty() {
        let prev = out.last();
        let mut counts: HashMap<&str, usize> = HashMap::new();
        for q in &pool {
            *counts.entry(q.answer_text).or_default() += 1;
        }
        let (top, top_count) = counts.iter().max_by_key(|(_, c)| **c).map(|(a, c)| (*a, *c)).unwrap();
        let forced = top_count * 2 > pool.len() && prev.is_none_or(|p| p.answer_text != top);
        let fits = |q: &PublicQuestion, check_point: bool| {
            let answer_ok = prev.is_none_or(|p| p.answer_text != q.answer_text);
            let point_ok = !check_point || prev.is_none_or(|p| p.point.is_none() || p.point != q.point);
            answer_ok && point_ok && (!forced || q.answer_text == top)
        };
        let idx = pool
            .iter()
            .position(|q| fits(q, true))
            .or_else(|| pool.iter().position(|q| fits(q, false)))
            .unwrap_or(0);
        out.push(pool.remove(idx));
    }
    out
}

/// Small xorshift generator seeded from the clock and a counter; good enough for shuffling.
struct Rng(u64);

impl Rng {
    fn new() -> Self {
        static COUNTER: AtomicU64 = AtomicU64::new(0);
        let nanos = SystemTime::now().duration_since(UNIX_EPOCH).map(|d| d.as_nanos() as u64).unwrap_or(0);
        // splitmix64, so nearby seeds give unrelated sequences.
        let mut z = nanos ^ COUNTER.fetch_add(1, Ordering::Relaxed).wrapping_mul(0x9E37_79B9_7F4A_7C15);
        z = (z ^ (z >> 30)).wrapping_mul(0xBF58_476D_1CE4_E5B9);
        z = (z ^ (z >> 27)).wrapping_mul(0x94D0_49BB_1331_11EB);
        Rng((z ^ (z >> 31)) | 1)
    }

    fn next(&mut self) -> u64 {
        self.0 ^= self.0 << 13;
        self.0 ^= self.0 >> 7;
        self.0 ^= self.0 << 17;
        self.0
    }

    /// Fisher–Yates.
    fn shuffle<T>(&mut self, items: &mut [T]) {
        for i in (1..items.len()).rev() {
            let j = (self.next() % (i as u64 + 1)) as usize;
            items.swap(i, j);
        }
    }
}

async fn list_quizzes(State(state): State<Shared>, Query(params): Query<ScriptParam>) -> Json<serde_json::Value> {
    let list: Vec<_> = state
        .all(params.script)
        .map(|q| QuizSummary {
            id: &q.id,
            category: &q.category,
            language: &q.language,
            title: &q.title,
            description: &q.description,
            level: &q.level,
            count: q.questions.len(),
            points: q.points.iter().map(|p| p.title.as_str()).collect(),
        })
        .collect();
    Json(serde_json::to_value(list).expect("summaries serialize"))
}

async fn get_quiz(
    State(state): State<Shared>,
    UrlPath(id): UrlPath<String>,
    Query(params): Query<ScriptParam>,
) -> Response {
    let Some(quiz) = state.quiz(&id, params.script) else {
        return (StatusCode::NOT_FOUND, "quiz not found").into_response();
    };
    let mut questions = public_questions(quiz);
    spread(&mut questions);
    Json(PublicQuiz {
        id: &quiz.id,
        language: &quiz.language,
        title: &quiz.title,
        description: &quiz.description,
        level: &quiz.level,
        points: &quiz.points,
        questions,
    })
    .into_response()
}

/// A random selection of questions across every quiz (or one category).
async fn random_mix(State(state): State<Shared>, Query(params): Query<MixParams>) -> Response {
    let mut all: Vec<PublicQuestion> = state
        .all(params.script)
        .filter(|q| params.category.as_ref().is_none_or(|c| *c == q.category))
        .flat_map(public_questions)
        .collect();
    let language = params
        .category
        .as_ref()
        .and_then(|c| state.quizzes.iter().find(|q| q.category == *c))
        .map(|q| q.language.as_str());
    Rng::new().shuffle(&mut all);
    all.truncate(params.count.unwrap_or(20).clamp(1, 200));
    spread(&mut all);
    Json(PublicQuiz {
        id: "mix",
        language: language.unwrap_or(""),
        title: "Random mix",
        description: "Questions drawn from several quizzes.",
        level: "",
        points: &[],
        questions: all,
    })
    .into_response()
}

async fn check(State(state): State<Shared>, Json(req): Json<CheckRequest>) -> Response {
    let Some(quiz) = state.quiz(&req.quiz_id, req.script) else {
        return (StatusCode::NOT_FOUND, "quiz not found").into_response();
    };
    let Some(q) = quiz.questions.get(req.index) else {
        return (StatusCode::NOT_FOUND, "question not found").into_response();
    };
    let correct = req.choice == Some(q.answer);
    let note = match req.choice {
        Some(c) if !correct => q.notes.get(c).map(String::as_str).filter(|n| !n.is_empty()),
        _ => None,
    };
    Json(CheckResponse {
        correct,
        answer: q.answer,
        explanation: &q.explanation,
        note,
        notes: &q.notes,
        translation: &q.translation,
        point: quiz.point(q.point.as_deref()),
    })
    .into_response()
}

fn quiz_dir() -> PathBuf {
    if let Ok(dir) = env::var("QUIZ_DIR") {
        return dir.into();
    }
    let local = PathBuf::from("quizzes");
    if local.is_dir() {
        local
    } else {
        Path::new(env!("CARGO_MANIFEST_DIR")).join("quizzes")
    }
}

/// All `.json` files below `dir`, recursively.
fn json_files(dir: &Path, out: &mut Vec<PathBuf>) -> Result<(), String> {
    for entry in fs::read_dir(dir).map_err(|e| format!("cannot read {}: {e}", dir.display()))? {
        let path = entry.map_err(|e| e.to_string())?.path();
        if path.is_dir() {
            json_files(&path, out)?;
        } else if path.extension().is_some_and(|ext| ext == "json") {
            out.push(path);
        }
    }
    Ok(())
}

fn load_quizzes(dir: &Path) -> Result<Vec<Quiz>, String> {
    let mut paths = Vec::new();
    json_files(dir, &mut paths)?;
    paths.sort();

    let mut quizzes = Vec::new();
    for path in paths {
        let text = fs::read_to_string(&path).map_err(|e| format!("{}: {e}", path.display()))?;
        let quiz: Quiz =
            serde_json::from_str(&text).map_err(|e| format!("{}: {e}", path.display()))?;
        for (i, q) in quiz.questions.iter().enumerate() {
            if q.answer >= q.options.len() {
                return Err(format!("{}: question {} has an out-of-range answer", path.display(), i + 1));
            }
            if !q.notes.is_empty() && q.notes.len() != q.options.len() {
                return Err(format!("{}: question {} needs one note per option", path.display(), i + 1));
            }
            if q.point.is_some() && quiz.point(q.point.as_deref()).is_none() {
                return Err(format!("{}: question {} refers to an unknown point", path.display(), i + 1));
            }
        }
        quizzes.push(quiz);
    }
    Ok(quizzes)
}

const INDEX_HTML: &str = include_str!("../static/index.html");
const APP_JS: &str = include_str!("../static/app.js");
const STYLE_CSS: &str = include_str!("../static/style.css");
const FAVICON_SVG: &str = include_str!("../static/favicon.svg");
const TOUCH_ICON_PNG: &[u8] = include_bytes!("../static/apple-touch-icon.png");

/// Writes a static copy of the site: the pages (with relative links, so it works under a
/// sub-path such as user.github.io/repo/) and every quiz as JSON under `data/`.
/// Mandarin quizzes get a second `.trad.json` file with traditional characters.
fn export(out: &Path, quizzes: &[Quiz], traditional: &[Option<Quiz>]) -> std::io::Result<()> {
    let quiz_dir = out.join("data").join("quiz");
    fs::create_dir_all(&quiz_dir)?;

    let index = INDEX_HTML
        .replace("href=\"/", "href=\"")
        .replace("src=\"/", "src=\"")
        .replace("<script src=\"app.js\">", "<script>window.QUIZ_STATIC = true;</script>\n  <script src=\"app.js\">");
    fs::write(out.join("index.html"), index)?;
    fs::write(out.join("app.js"), APP_JS)?;
    fs::write(out.join("style.css"), STYLE_CSS)?;
    fs::write(out.join("favicon.svg"), FAVICON_SVG)?;
    fs::write(out.join("apple-touch-icon.png"), TOUCH_ICON_PNG)?;
    // Serve files as they are (no Jekyll processing on GitHub Pages).
    fs::write(out.join(".nojekyll"), "")?;

    let summary = |q: &Quiz| {
        serde_json::to_value(QuizSummary {
            id: &q.id,
            category: &q.category,
            language: &q.language,
            title: &q.title,
            description: &q.description,
            level: &q.level,
            count: q.questions.len(),
            points: q.points.iter().map(|p| p.title.as_str()).collect(),
        })
        .expect("summary serializes")
    };
    let simp: Vec<_> = quizzes.iter().map(summary).collect();
    let trad: Vec<_> = quizzes.iter().zip(traditional).map(|(q, t)| summary(t.as_ref().unwrap_or(q))).collect();
    fs::write(out.join("data").join("quizzes.json"), json(&simp))?;
    fs::write(out.join("data").join("quizzes.trad.json"), json(&trad))?;

    for (quiz, trad) in quizzes.iter().zip(traditional) {
        fs::write(quiz_dir.join(format!("{}.json", quiz.id)), json(quiz))?;
        if let Some(t) = trad {
            fs::write(quiz_dir.join(format!("{}.trad.json", quiz.id)), json(t))?;
        }
    }
    Ok(())
}

fn json<T: Serialize + ?Sized>(value: &T) -> String {
    serde_json::to_string(value).expect("serializes")
}

fn static_file(content_type: &'static str, body: &'static str) -> impl IntoResponse {
    ([(header::CONTENT_TYPE, content_type)], body)
}

#[tokio::main]
async fn main() {
    let dir = quiz_dir();
    let quizzes = load_quizzes(&dir).unwrap_or_else(|e| {
        eprintln!("error loading quizzes: {e}");
        std::process::exit(1);
    });
    let mut by_id = HashMap::new();
    for (i, quiz) in quizzes.iter().enumerate() {
        if by_id.insert(quiz.id.clone(), i).is_some() || quiz.id == "mix" {
            eprintln!("error: duplicate or reserved quiz id '{}'", quiz.id);
            std::process::exit(1);
        }
    }
    let total: usize = quizzes.iter().map(|q| q.questions.len()).sum();
    println!("Loaded {} quizzes ({total} questions) from {}", quizzes.len(), dir.display());

    let traditional = quizzes
        .iter()
        .map(|q| (q.language == "zh").then(|| to_traditional(q)))
        .collect();
    let traditional: Vec<Option<Quiz>> = traditional;

    let args: Vec<String> = env::args().collect();
    if args.get(1).map(String::as_str) == Some("export") {
        let out = PathBuf::from(args.get(2).map(String::as_str).unwrap_or("site"));
        if let Err(e) = export(&out, &quizzes, &traditional) {
            eprintln!("error exporting to {}: {e}", out.display());
            std::process::exit(1);
        }
        println!("Exported the static site to {}", out.display());
        return;
    }

    let state = Arc::new(AppState { quizzes, traditional, by_id });
    let app = Router::new()
        .route("/", get(|| async { Html(INDEX_HTML) }))
        .route("/app.js", get(|| async { static_file("text/javascript; charset=utf-8", APP_JS) }))
        .route("/style.css", get(|| async { static_file("text/css; charset=utf-8", STYLE_CSS) }))
        .route("/favicon.svg", get(|| async { static_file("image/svg+xml", FAVICON_SVG) }))
        .route("/apple-touch-icon.png", get(|| async { ([(header::CONTENT_TYPE, "image/png")], TOUCH_ICON_PNG) }))
        .route("/api/quizzes", get(list_quizzes))
        .route("/api/quizzes/{id}", get(get_quiz))
        .route("/api/mix", get(random_mix))
        .route("/api/check", post(check))
        .with_state(state);

    let port: u16 = env::var("PORT").ok().and_then(|p| p.parse().ok()).unwrap_or(3000);
    // Local-only by default; HOST=:: listens on all IPv6 (and usually IPv4) interfaces.
    let host: IpAddr = env::var("HOST")
        .ok()
        .and_then(|h| h.parse().ok())
        .unwrap_or(IpAddr::from([127, 0, 0, 1]));
    let addr = SocketAddr::new(host, port);
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap_or_else(|e| {
        eprintln!("cannot bind {addr}: {e}");
        std::process::exit(1);
    });
    println!("Japanese quiz listening on http://{addr}");
    axum::serve(listener, app).await.expect("server error");
}
