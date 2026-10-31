"""Generates the Adjective Lab (quizzes/07_adjectives): い- and な-adjectives, and how they differ from verbs.

It reuses the conjugation engine of the Verb Lab (tools/gen_ja_verbs.py) for both verbs and adjectives, so the
accepted answers, hints and explanations always match. Step 1 tells the word classes apart, step 2 drills the
forms, step 3 uses them in context, and the "Verb or adjective?" lessons put verbs and adjectives side by side.
Run from the repo root.
"""
import collections, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
import gen_ja_verbs as V
from gen_ja_verbs import ADJ, VERBS, GLOSS, ruby, to_kanji

# ---------------------------------------------------------------- words
ADJ.update({k: (k, r, kind) for k, r, kind in [
    ("長い", "ながい", "i"), ("短い", "みじかい", "i"), ("広い", "ひろい", "i"), ("狭い", "せまい", "i"),
    ("重い", "おもい", "i"), ("軽い", "かるい", "i"), ("遠い", "とおい", "i"), ("近い", "ちかい", "i"),
    ("明るい", "あかるい", "i"), ("強い", "つよい", "i"), ("弱い", "よわい", "i"), ("若い", "わかい", "i"),
    ("多い", "おおい", "i"), ("少ない", "すくない", "i"), ("甘い", "あまい", "i"), ("辛い", "からい", "i"),
    ("冷たい", "つめたい", "i"), ("暖かい", "あたたかい", "i"), ("涼しい", "すずしい", "i"), ("汚い", "きたない", "i"),
    ("悪い", "わるい", "i"), ("怖い", "こわい", "i"), ("寂しい", "さびしい", "i"), ("嬉しい", "うれしい", "i"),
    ("悲しい", "かなしい", "i"), ("欲しい", "ほしい", "i"), ("珍しい", "めずらしい", "i"), ("危ない", "あぶない", "i"),
    ("遅い", "おそい", "i"), ("速い", "はやい", "i"), ("白い", "しろい", "i"), ("低い", "ひくい", "i"),
    ("易しい", "やさしい", "i"), ("うるさい", "うるさい", "i"), ("つまらない", "つまらない", "i"), ("厳しい", "きびしい", "i"),
    ("美しい", "うつくしい", "i"), ("恥ずかしい", "はずかしい", "i"), ("素晴らしい", "すばらしい", "i"),
    ("大丈夫", "だいじょうぶ", "na"), ("必要", "ひつよう", "na"), ("特別", "とくべつ", "na"), ("自由", "じゆう", "na"),
    ("複雑", "ふくざつ", "na"), ("安全", "あんぜん", "na"), ("危険", "きけん", "na"), ("残念", "ざんねん", "na"),
    ("得意", "とくい", "na"), ("苦手", "にがて", "na"), ("素敵", "すてき", "na"), ("賑やか", "にぎやか", "na"),
    ("幸せ", "しあわせ", "na"), ("不便", "ふべん", "na"), ("真面目", "まじめ", "na"), ("大事", "だいじ", "na"),
    ("楽", "らく", "na"), ("大好き", "だいすき", "na"), ("失礼", "しつれい", "na"), ("変", "へん", "na"),
]})
VERBS.update({k: (k, r, cls) for k, r, cls in [
    ("混む", "こむ", "u"), ("太る", "ふとる", "u"), ("痩せる", "やせる", "ru"), ("空く", "すく", "u"),
    ("晴れる", "はれる", "ru"), ("曇る", "くもる", "u"), ("似る", "にる", "ru"), ("違う", "ちがう", "u"),
    ("困る", "こまる", "u"), ("濡れる", "ぬれる", "ru"), ("汚れる", "よごれる", "ru"), ("泣く", "なく", "u"),
    ("欲しがる", "ほしがる", "u"), ("降る", "ふる", "u"), ("落ちる", "おちる", "ru"),
]})
GLOSS.update({"混む": "get crowded", "太る": "put on weight", "痩せる": "lose weight", "空く": "become empty",
              "晴れる": "clear up", "曇る": "cloud over", "似る": "resemble", "違う": "differ", "困る": "be in trouble",
              "濡れる": "get wet", "汚れる": "get dirty", "泣く": "cry", "欲しがる": "want (someone else)", "降る": "fall (rain)"})

ADJ_GLOSS = {
    "高い": "expensive, high", "安い": "cheap", "新しい": "new", "古い": "old (things)", "暑い": "hot (weather)",
    "寒い": "cold (weather)", "忙しい": "busy", "楽しい": "fun", "難しい": "difficult", "おいしい": "tasty",
    "大きい": "big", "小さい": "small", "面白い": "interesting", "暗い": "dark", "優しい": "kind, gentle",
    "眠い": "sleepy", "早い": "early", "痛い": "painful", "いい": "good", "かっこいい": "cool, good-looking",
    "静か": "quiet", "きれい": "pretty, clean", "有名": "famous", "便利": "convenient", "元気": "well, lively",
    "好き": "liked", "嫌い": "disliked", "大変": "tough", "簡単": "easy", "上手": "good at", "下手": "bad at",
    "暇": "free (time)", "親切": "kind", "丁寧": "polite, careful", "大切": "important", "長い": "long",
    "短い": "short", "広い": "spacious", "狭い": "cramped", "重い": "heavy", "軽い": "light", "遠い": "far",
    "近い": "near", "明るい": "bright", "強い": "strong", "弱い": "weak", "若い": "young", "多い": "many",
    "少ない": "few", "甘い": "sweet", "辛い": "spicy", "冷たい": "cold (to touch)", "暖かい": "warm",
    "涼しい": "cool", "汚い": "dirty", "悪い": "bad", "怖い": "scary", "寂しい": "lonely", "嬉しい": "glad",
    "悲しい": "sad", "欲しい": "wanted", "珍しい": "rare", "危ない": "dangerous", "遅い": "late, slow",
    "速い": "fast", "白い": "white", "低い": "low", "易しい": "easy", "うるさい": "noisy", "つまらない": "boring",
    "厳しい": "strict", "美しい": "beautiful", "恥ずかしい": "embarrassing", "素晴らしい": "wonderful",
    "大丈夫": "all right", "必要": "necessary", "特別": "special", "自由": "free", "複雑": "complicated",
    "安全": "safe", "危険": "dangerous", "残念": "a pity", "得意": "good at", "苦手": "bad at", "素敵": "lovely",
    "賑やか": "lively", "幸せ": "happy", "不便": "inconvenient", "真面目": "serious", "大事": "important",
    "楽": "easy, comfortable", "大好き": "loved", "失礼": "rude", "変": "strange",
}
V.NA_TRAPS.update({"失礼"})

# ---------------------------------------------------------------- extra forms
# Adjectives: "becomes …" (present) and "if / when … (たら)".
V.ADJ_LABEL.update({"a_naru": "becomes … (なる)", "a_tara": "if / when … (たら)"})
V.LABEL.update(V.ADJ_LABEL)
V.ADJ_ENDING_I.update({"a_naru": "くなる", "a_tara": "かったら"})
V.ADJ_ENDING_NA.update({"a_naru": "になる", "a_tara": "だったら"})
_adj_forms = V.adj_forms


def adj_forms(key):
    f = _adj_forms(key)
    kanji, r, kind = ADJ[key]
    if kind == "na":
        f.update({"a_naru": [r + "になる"], "a_tara": [r + "だったら"]})
    else:
        stem = r[:-2] + "よ" if kind == "ii" else r[:-1]
        f.update({"a_naru": [stem + "くなる"], "a_tara": [stem + "かったら"]})
    return f


V.adj_forms = adj_forms

# Verbs: ます-stem + ending (すぎる, そう, たい).
VERB_STEM = {"v_sugiru": ("too much (すぎる)", "すぎる"), "v_sugita": ("did too much (すぎた)", "すぎた"),
             "v_sou": ("looks like it's about to … (そう)", "そう"), "v_tai": ("want to … (たい)", "たい")}
V.LABEL.update({k: v[0] for k, v in VERB_STEM.items()})
_build, _wrong = V.build, V.wrong_forms


def build(key, form):
    if form not in VERB_STEM:
        return _build(key, form)
    kanji, r, cls = VERBS[key]
    stem = V.masu_stem(r, cls)
    tail = VERB_STEM[form][1]
    accept = list(dict.fromkeys([to_kanji(stem + tail, key), stem + tail]))
    stem_k = to_kanji(stem + "ます", key)[:-2]
    why = f"{ruby(key)} is a verb: ます-stem ({stem_k}) + {tail} → **{accept[0]}**."
    return accept, why, to_kanji(stem + tail[0], key) + "…"


def wrong_forms(key, form, accept):
    if form not in VERB_STEM:
        return _wrong(key, form, accept)
    kanji, r, cls = VERBS[key]
    tail = VERB_STEM[form][1]
    note = f"{tail} goes on the ます-stem, not the dictionary form: {accept[0]}."
    return {r + tail: note, kanji + tail: note}


V.build, V.wrong_forms = build, wrong_forms

# Classic mix-ups in the polite past.
def polite_traps(key, form):
    out = {}
    if key in ADJ:
        kanji, r, kind = ADJ[key]
        if kind != "na" and form == "a_past_p":
            note = f"い-adjectives carry the past themselves: {to_kanji(adj_forms(key)['a_past'][0], key)}です — '…いでした' is a very common mistake."
            out[r + "でした"] = out[kanji + "でした"] = note
        if kind != "na" and form == "a_pastneg_p":
            note = "the past goes into the adjective: …くなかったです (or …くありませんでした), not …くないでした."
            stem = r[:-2] + "よ" if kind == "ii" else r[:-1]
            out[stem + "くないでした"] = out[to_kanji(stem + "くないでした", key)] = note
        if kind == "na" and form in ("a_past_p", "a_desu"):
            note = f"な-adjectives use です / でした directly: {to_kanji(adj_forms(key)[form][0], key)}."
            out[r + "だったです"] = out[kanji + "だったです"] = note
    elif key in VERBS and form in ("masu", "mashita", "masen", "masendeshita"):
        kanji, r, _ = VERBS[key]
        note = "verbs don't take です / でした — the ます-form does the job."
        for tail in ("です", "でした"):
            out[r + tail] = out[kanji + tail] = note
    return out


def cls_of(key):
    if key in VERBS:
        return "v"
    return {"i": "i", "ii": "i", "na": "na"}[ADJ[key][2]]


def gloss(key):
    if key in VERBS:
        return f"{VERBS[key][0]} = to {GLOSS[key]}" if key in GLOSS else ""
    return f"{ADJ[key][0]} = {ADJ_GLOSS[key]}" if key in ADJ_GLOSS else ""


# ---------------------------------------------------------------- guides
QZ = {}
CAT, LEVEL = "Adjective Lab", "Adjectives"

ADJ_BODY = V.ADJ_BODY
VS_BODY = """**Verb, い-adjective, な-adjective, noun — side by side**

| | verb 書く | い-adj. 高い | な-adj. 静か | noun 学生 |
|---|---|---|---|---|
| present | 書く / 書きます | 高い / 高いです | 静かだ / 静かです | 学生だ / 学生です |
| not | 書かない | 高**くない** | 静か**じゃない** | 学生じゃない |
| past | 書いた | 高**かった** | 静か**だった** | 学生だった |
| polite past | 書きました | 高かったです | 静かでした | 学生でした |
| before a noun | 書く人 | 高い本 | 静か**な**部屋 | 学生**の**時 |
| … and … | 書いて | 高**くて** | 静か**で** | 学生で |
| become | 書けるようになる | 高**く**なる | 静か**に**なる | 学生になる |

- **い-adjectives behave like verbs:** the word itself changes (高い → 高くない → 高かった). です only adds politeness: 高かったです, never 高いでした.
- **な-adjectives behave like nouns:** the word stays, だ / です / じゃない / だった do the work. The only difference: な before a noun (静かな部屋) where a noun takes の (学生の時).
- **Verbs have their own endings** (ない, ます, た) and never take です directly.

**Watch out for words whose class differs from English or German**
- English/German verb → Japanese adjective: 好き (like), 嫌い (hate), 欲しい (want), 上手・得意 (be good at), 怖い (be scared), 痛い (hurt).
- English/German adjective → Japanese verb: 疲れている (tired), 混んでいる (crowded), 結婚している (married), 違う (different)."""

GUIDE = {
    "adj": ("Adjective forms", "い-adjectives change their ending; な-adjectives keep it and add だ / じゃない / な.", ADJ_BODY),
    "vs": ("Verb or adjective?", "Same idea, different word class — and so different endings.", VS_BODY),
    "mixed": ("Mixed review", "Every form, shuffled — work out the word class first, then the ending.", ADJ_BODY),
}


def point(pid, title, summary, guide, examples=()):
    return {"id": pid, "title": title, "summary": summary, "body": GUIDE[guide][2], "examples": list(examples)}


def save(fname, id, title, description, points, questions, keep_order=False):
    QZ[fname] = {"id": id, "category": CAT, "title": title, "description": description, "level": LEVEL,
                 "points": points, "questions": questions}
    if keep_order:
        QZ[fname]["keep_order"] = True


def typed_q(prompt, key, form, pid, translation, note=""):
    accept, why, hint = build(key, form)
    wf = wrong_forms(key, form, accept)
    wf.update({k: v for k, v in polite_traps(key, form).items() if k not in accept})
    return {"point": pid, "prompt": prompt, "options": [], "answer": 0, "accept": accept, "hint": hint,
            "explanation": why + (" " + note if note else ""), "notes": [], "translation": translation,
            "wrong_forms": wf}


def context_quiz(fname, id, title, description, guide, items, titles, pid_fn=None):
    """items: (sentence, key, form, English[, note[, point id]])."""
    questions = []
    for it in items:
        sentence, key, form, en = it[:4]
        note = it[4] if len(it) > 4 else ""
        pid = it[5] if len(it) > 5 and it[5] else pid_fn(key, form) if pid_fn else cls_of(key)
        cue = V.LABEL[form]
        questions.append(typed_q(f"{sentence}\n→ {ruby(key)} · {cue}", key, form, pid, en, note))
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = []
    for p in pids:
        ex = next(q for q in questions if q["point"] == p)
        filled = ex["prompt"].split("\n")[0].replace("（　）", ex["accept"][0])
        points.append(point(p, titles[p][0], titles[p][1], guide, [[filled, ex["translation"]]]))
    save(fname, id, title, description, points, questions)


def drill_quiz(fname, id, title, description, guide, items, titles, keep_order=False, rule_hints=False):
    """items: (key, form, point id)."""
    questions = []
    for key, form, pid in items:
        q = typed_q(f"{ruby(key)} → （　）\n→ {V.LABEL[form]}", key, form, pid, gloss(key))
        if rule_hints:
            q["hint"] = titles[pid][0]
        questions.append(q)
    pids = list(dict.fromkeys(q["point"] for q in questions))
    save(fname, id, title, description, [point(p, titles[p][0], titles[p][1], guide) for p in pids], questions, keep_order)


# ---------------------------------------------------------------- step 1: word classes
V.adj_types_quiz("01_types", "verbs-adj-types", "Adjective Types: い or な?",
                 "Tell the two adjective types apart — including the な-adjectives that end in い.",
                 ["高い", "静か", "きれい", "おいしい", "便利", "嫌い", "新しい", "有名", "いい", "元気", "楽しい", "丁寧",
                  "かっこいい", "簡単", "暗い", "好き", "優しい", "大変"])
QZ["01_types"] = V.QZ.pop("01_types")

NOUNS = {"病気": ("{病気|びょうき}", "病気じゃない", "病気の人", "being ill"),
         "休み": ("{休|やす}み", "休みじゃない", "休みの日", "a day off"),
         "学生": ("{学生|がくせい}", "学生じゃない", "学生の時", "a student")}
CLASS_OPTS = ["verb", "い-adjective", "な-adjective", "noun"]
CLASS_POINTS = {
    "cls-v": ("Verbs", "End in an う-sound and conjugate with ない / ます / た: 分かる → 分からない, 分かります."),
    "cls-i": ("い-adjectives", "End in い and change themselves: 眠い → 眠くない, 眠かった."),
    "cls-na": ("な-adjectives", "Stay the same and add だ / じゃない; な before a noun: 好きな人."),
    "cls-n": ("Nouns", "Like な-adjectives, but の before a noun: 病気の人, 休みの日."),
}


def class_q(key, note):
    """What is this word? Verb, い-adjective, な-adjective or noun — with its forms as evidence."""
    if key in NOUNS:
        shown, neg, before, en = NOUNS[key]
        ans, pid = 3, "cls-n"
        why = f"{shown} is a noun: {neg}, {before} (with の, not な)."
    elif key in VERBS:
        ans, pid, shown = 0, "cls-v", ruby(key)
        k = lambda f: to_kanji(V.forms(VERBS[key][1], VERBS[key][2])[f][0], key)
        why = f"{shown} is a verb: {k('nai')}, {k('masu')}, {k('ta')}."
    else:
        kind = ADJ[key][2]
        f = adj_forms(key)
        k = lambda form: to_kanji(f[form][0], key)
        shown = ruby(key)
        if kind == "na":
            ans, pid = 2, "cls-na"
            why = f"{shown} is a な-adjective: {k('a_neg')}, {k('a_past')}, {k('a_noun')} + noun."
        else:
            ans, pid = 1, "cls-i"
            why = f"{shown} is an い-adjective: {k('a_neg')}, {k('a_past')}."
    notes = ["A verb would have ない / ます / た forms of its own.",
             "An い-adjective would change its い (…くない, …かった).",
             "A な-adjective would add じゃない and take な before a noun.",
             "A noun takes の before another noun."]
    notes[ans] = ""
    tr = ADJ_GLOSS.get(key) or GLOSS.get(key) or (NOUNS[key][3] if key in NOUNS else "")
    return {"point": pid, "prompt": f"Which word class is **{shown}**?", "options": CLASS_OPTS, "answer": ans,
            "fixed_order": True, "explanation": why + (" " + note if note else ""), "notes": notes,
            "translation": f"{plain(shown)} = {'to ' if key in VERBS else ''}{tr}"}


def plain(s):
    return re.sub(r"\{([^|}]+)\|[^}]+\}", r"\1", s)


CLASS_ITEMS = [
    ("好き", "English 'like' is a verb, but 好き is a な-adjective: 猫**が**好きです."),
    ("分かる", "German can say 'das ist mir klar' (an adjective), but Japanese only has the verb 分かる; what you understand takes が."),
    ("欲しい", "'Want' is a verb in English, but 欲しい (want a thing) is an い-adjective; the thing takes が: 車が欲しい."),
    ("疲れる", "'tired' is an adjective in English, but Japanese uses this verb: 疲れた / 疲れている (I'm tired)."),
    ("眠い", "Here English and Japanese agree: 'sleepy' is an adjective. 'To sleep' is the verb 寝る / 眠る."),
    ("上手", "'be good at' — 上手 is a な-adjective: 料理**が**上手です."),
    ("元気", ""), ("病気", "元気 is a な-adjective, but 病気 is a noun: 元気な人 vs 病気の人."),
    ("静か", ""), ("寒い", ""), ("嫌い", "It ends in い, but the い is part of the word: 嫌いじゃない (not 嫌くない)."),
    ("違う", "'Different' and 'wrong' are adjectives in English, but 違う is a verb: 違います, 違わない."),
    ("きれい", "It ends in い, but the い is part of the word: きれいじゃない (not きれくない)."),
    ("困る", "'that's a problem / I'm in trouble' is a verb: 困ります, 困った."),
    ("怖い", "'be scared' is an い-adjective: 犬が怖い, 怖かった."),
    ("休み", "'off / free (today)' is a noun: 明日は休みです, 休みの日."),
    ("暇", "'free (have time)' is a な-adjective: 暇な日, 暇じゃない."),
    ("混む", "'crowded' is a verb: 混んでいる (has got crowded)."),
    ("有名", "It ends in an い sound, but it's a な-adjective: 有名な店."),
    ("痛い", "'hurt' is a verb in English (wehtun), but 痛い is an い-adjective: 頭が痛い."),
    ("学生", ""), ("大丈夫", "'all right' — a な-adjective: 大丈夫じゃない."),
]
questions = [class_q(k, n) for k, n in CLASS_ITEMS]
pids = list(dict.fromkeys(q["point"] for q in questions))
save("02_word_class", "adj-word-class", "Verb, い, な or Noun? Word Classes",
     "The root of most mix-ups: which word class is it? Many differ from English and German (好き, 疲れる, 違う).",
     [point(p, *CLASS_POINTS[p], "vs") for p in pids], questions)

# ---------------------------------------------------------------- step 2: form drills
BACK = {"i": ("く / かっ / けれ / そう / すぎる after the stem → put い back", "an い-adjective: the い dropped for the ending, so add it back"),
        "na": ("じゃ / だ / で / な / に after the word → the word itself", "a な-adjective: the word never changes, just drop what follows"),
        "ii": ("よ- forms come from いい", "よ- (よくない, よかった) is the irregular stem of いい")}


def back_q(key, form, pid):
    kanji, r, kind = ADJ[key]
    kana = adj_forms(key)[form][0]
    shown = to_kanji(kana, key)
    hint, rule = BACK["ii" if kind == "ii" else kind]
    trap = " ⚠ The い of きれい / 嫌い / 有名 / 丁寧 belongs to the word — they're な-adjectives." if key in V.NA_TRAPS else ""
    base = "かっこいい" if key == "かっこいい" else kanji
    return {"point": pid, "prompt": f"{furigana_form(kana, key)} → （　）\n→ dictionary form", "options": [], "answer": 0,
            "accept": list(dict.fromkeys([base, r])), "hint": hint,
            "explanation": f"{shown}: {rule} → **{base}**.{trap}", "notes": [], "translation": gloss(key)}


def furigana_form(kana, key):
    """高くなかった with furigana on the kanji: {高|たか}くなかった."""
    kanji, r, _ = ADJ[key]
    if kanji == r:
        return kana
    n = V.okuri(kanji, r)
    kp, rp = kanji[:len(kanji) - n], r[:len(r) - n]
    return "{" + kp + "|" + rp + "}" + kana[len(rp):] if kana.startswith(rp) else kana


BACK_ITEMS = [("高い", "a_pastneg"), ("静か", "a_neg"), ("いい", "a_past"), ("おいしい", "a_sou"), ("便利", "a_noun"),
              ("寒い", "a_te"), ("元気", "a_te"), ("早い", "a_adv"), ("上手", "a_adv"), ("楽しい", "a_past"),
              ("有名", "a_past"), ("かっこいい", "a_neg"), ("きれい", "a_pastneg"), ("難しい", "a_ba"),
              ("嫌い", "a_past"), ("大きい", "a_sugiru")]
qs = [back_q(k, f, "back-ii" if ADJ[k][2] == "ii" else "back-" + ADJ[k][2]) for k, f in BACK_ITEMS]
save("03_back", "adj-back", "Back to the Dictionary Form",
     "See an adjective form, find the word you'd look up: 高くなかった → 高い, 静かじゃない → 静か.",
     [point(p, t, s, "adj") for p, t, s in [("back-i", "From an い-adjective form", BACK["i"][0]),
                                            ("back-na", "From a な-adjective form", BACK["na"][0]),
                                            ("back-ii", "From いい (よ-)", BACK["ii"][0])]
      if any(q["point"] == p for q in qs)], qs)

SPRINT_TITLES = {"adj-i": ("い-adjectives: drop い + ending", "高い → 高くない, 高かった, 高くなかった."),
                 "adj-na": ("な-adjectives: add だ / じゃない / だった", "静か → 静かじゃない, 静かだった."),
                 "adj-ii": ("いい → よ- (except the present)", "いい → よくない, よかった, よくて.")}
drill_quiz("04_sprint", "verbs-adj-sprint", "Adjective Sprint: Negative & Past",
           "18 adjectives, four forms: not …, was …, wasn't … — plain and polite.", "adj", [
    ("高い", "a_neg", "adj-i"), ("静か", "a_neg", "adj-na"), ("いい", "a_neg", "adj-ii"), ("寒い", "a_past", "adj-i"),
    ("便利", "a_past", "adj-na"), ("いい", "a_past", "adj-ii"), ("楽しい", "a_pastneg", "adj-i"), ("きれい", "a_neg", "adj-na"),
    ("忙しい", "a_neg_p", "adj-i"), ("有名", "a_pastneg", "adj-na"), ("おいしい", "a_past_p", "adj-i"),
    ("嫌い", "a_past", "adj-na"), ("かっこいい", "a_past", "adj-ii"), ("難しい", "a_pastneg_p", "adj-i"),
    ("暇", "a_neg_p", "adj-na"), ("大きい", "a_te", "adj-i"), ("元気", "a_te", "adj-na"), ("いい", "a_te", "adj-ii"),
], SPRINT_TITLES, rule_hints=True)

TE_TITLES = {"te-i": ("い-adjectives: drop い + くて", "安くて, 広くて — '… and …' / 'because …'."),
             "te-na": ("な-adjectives: + で", "静かで, 便利で."),
             "adv-i": ("Adverb: drop い + く", "早く起きる, 高くなる."),
             "adv-na": ("Adverb: + に", "静かに話す, 上手になる."),
             "te-ii": ("いい → よくて / よく", "Also with いい: よくて, よく分かる.")}
drill_quiz("05_sprint_te", "adj-sprint-te", "て-Form & Adverb Sprint: くて / で and く / に",
           "Joining two adjectives and turning them into adverbs — the forms you need for longer sentences.", "adj", [
    ("安い", "a_te", "te-i"), ("便利", "a_te", "te-na"), ("早い", "a_adv", "adv-i"), ("静か", "a_adv", "adv-na"),
    ("広い", "a_te", "te-i"), ("いい", "a_te", "te-ii"), ("きれい", "a_te", "te-na"), ("上手", "a_adv", "adv-na"),
    ("短い", "a_adv", "adv-i"), ("明るい", "a_te", "te-i"), ("親切", "a_te", "te-na"), ("いい", "a_adv", "te-ii"),
    ("丁寧", "a_adv", "adv-na"), ("強い", "a_adv", "adv-i"), ("簡単", "a_te", "te-na"), ("甘い", "a_te", "te-i"),
], TE_TITLES, rule_hints=True)

LADDER = ["a_desu", "a_neg", "a_past", "a_pastneg", "a_te", "a_adv", "a_noun", "a_ba"]
drill_quiz("06_ladder", "adj-ladder", "Ladder 高い, 静か & いい: One Adjective, All Forms",
           "Three adjectives, each through eight forms in order — see where い changes and where な stays.", "adj",
           [("高い", f, "ladder-i") for f in LADDER] + [("静か", f, "ladder-na") for f in LADDER]
           + [("いい", f, "ladder-ii") for f in LADDER],
           {"ladder-i": ("い-adjective ladder (高い)", "高い, 高くない, 高かった, 高くなかった, 高くて, 高く, 高い + noun, 高ければ."),
            "ladder-na": ("な-adjective ladder (静か)", "静かです, 静かじゃない, 静かだった, 静かで, 静かに, 静かな + noun, 静かなら."),
            "ladder-ii": ("いい ladder", "いいです, よくない, よかった, よくて, よく, いい + noun, よければ.")}, keep_order=True)

drill_quiz("07_sprint_mixed", "adj-sprint-mixed", "Mixed Adjective Sprint: Any Adjective, Any Form",
           "20 adjectives, each in a different form. Decide い or な first, then the ending.", "mixed", [
    ("長い", "a_neg", "mixed"), ("自由", "a_past", "mixed"), ("重い", "a_pastneg", "mixed"), ("複雑", "a_neg_p", "mixed"),
    ("若い", "a_te", "mixed"), ("安全", "a_noun", "mixed"), ("冷たい", "a_past_p", "mixed"), ("必要", "a_pastneg", "mixed"),
    ("遠い", "a_ba", "mixed"), ("大丈夫", "a_te", "mixed"), ("涼しい", "a_naru", "mixed"), ("特別", "a_adv", "mixed"),
    ("かっこいい", "a_neg", "mixed"), ("失礼", "a_neg", "mixed"), ("少ない", "a_past", "mixed"), ("賑やか", "a_noun", "mixed"),
    ("つまらない", "a_pastneg_p", "mixed"), ("残念", "a_past_p", "mixed"), ("危ない", "a_tara", "mixed"),
    ("素敵", "a_tara", "mixed"),
], {"mixed": ("Mixed review", "All forms, shuffled.")})

# ---------------------------------------------------------------- step 3: in context
context_quiz("08_context", "verbs-adj-context", "Adjectives in Use: Reviews, Trips & Small Talk",
             "Joining (くて / で), adverbs (く / に), なる, そう, すぎる, before nouns — the adjective forms you use every day.", "adj", [
    ("この{店|みせ}のラーメンは（　）、{安|やす}いです。", "おいしい", "a_te", "The ramen here is tasty and cheap."),
    ("{昨日|きのう}の{試験|しけん}は{全然|ぜんぜん}（　）。", "難しい", "a_pastneg", "Yesterday's exam wasn't hard at all."),
    ("{京都|きょうと}はとても（　）{町|まち}でした。", "きれい", "a_noun", "Kyoto was a really beautiful town."),
    ("{掃除|そうじ}したので、{部屋|へや}が（　）なりました。", "きれい", "a_adv", "I cleaned, so the room is nice and tidy now."),
    ("{明日|あした}、{天気|てんき}が（　）、{公園|こうえん}に{行|い}きませんか。", "いい", "a_ba", "If the weather's good tomorrow, shall we go to the park?"),
    ("このケーキ、（　）ね！", "おいしい", "a_sou", "This cake looks delicious!"),
    ("この{靴|くつ}は{私|わたし}には（　）。", "大きい", "a_sugiru", "These shoes are too big for me."),
    ("{先週|せんしゅう}は{仕事|しごと}がとても（　）。", "忙しい", "a_past_p", "Work was very busy last week."),
    ("{図書館|としょかん}では（　）してください。", "静か", "a_adv", "Please be quiet in the library."),
    ("{冬|ふゆ}は5{時|じ}にはもう（　）なります。", "暗い", "a_adv", "In winter it's already dark by five."),
    ("この{映画|えいが}はあまり（　）。", "面白い", "a_neg_p", "This film isn't very interesting."),
    ("{田中|たなか}さんはとても（　）{人|ひと}です。", "親切", "a_noun", "Tanaka is a very kind person."),
    ("{子供|こども}のころ、{野菜|やさい}が（　）。", "嫌い", "a_past", "As a child I hated vegetables."),
    ("{旅行|りょこう}はどうでしたか。— とても（　）。", "いい", "a_past_p", "How was the trip? — It was great."),
    ("{最近|さいきん}、{日本語|にほんご}が（　）ね。", "上手", "a_naru_ta", "Your Japanese has got really good lately."),
    ("{去年|きょねん}より{野菜|やさい}の{値段|ねだん}が（　）。", "高い", "a_naru_ta", "Vegetables have got more expensive than last year."),
    ("この{部屋|へや}は{駅|えき}に{近|ちか}くて、とても（　）。", "便利", "a_desu", "This flat is close to the station and very convenient."),
    ("{昨日|きのう}は{頭|あたま}が（　）、{学校|がっこう}を{休|やす}みました。", "痛い", "a_te", "I had a headache yesterday, so I stayed home from school."),
], {"ctx-i": ("い-adjectives in context", "The ending changes: くて, く, かった, くない."),
    "ctx-na": ("な-adjectives in context", "The word stays: で, に, な, でした."),
    "ctx-ii": ("いい in context", "Every form but the present uses よ-: よくて, よければ, よかった.")},
   pid_fn=lambda key, form: "ctx-" + ADJ[key][2])  # point ids kept from when this lesson was in the Verb Lab

context_quiz("09_small_talk", "adj-small-talk", "Polite & Plain: Talking about Your Town",
             "Describe places in the present and past, polite (です) and casual — the eight basic adjective forms.", "adj", [
    ("{私|わたし}の{町|まち}は{小|ちい}さいですが、とても（　）。", "静か", "a_desu", "My town is small but very quiet.", "", "polite"),
    ("{駅|えき}から{少|すこ}し{遠|とお}いので、あまり（　）。", "便利", "a_neg_p", "It's a bit far from the station, so it isn't very convenient.", "", "polite"),
    ("{先週|せんしゅう}の{祭|まつ}りはとても（　）。", "楽しい", "a_past_p", "Last week's festival was a lot of fun.", "", "polite"),
    ("{昔|むかし}はこの{辺|へん}はあまり（　）。", "賑やか", "a_pastneg_p", "This area didn't use to be very lively.", "", "polite"),
    ("{家賃|やちん}は{東京|とうきょう}ほど（　）よ。", "高い", "a_neg_p", "The rent isn't as high as in Tokyo.", "", "polite"),
    ("{冬|ふゆ}は{雪|ゆき}が{多|おお}くて、とても（　）。", "寒い", "a_desu", "Winter brings a lot of snow and it's very cold.", "", "polite"),
    ("{去年|きょねん}の{夏|なつ}は{本当|ほんとう}に（　）。", "暑い", "a_past_p", "Last summer was really hot.", "", "polite"),
    ("{新|あたら}しい{図書館|としょかん}は{思|おも}ったほど（　）。", "大きい", "a_pastneg_p", "The new library wasn't as big as I'd expected.", "", "polite"),
    ("うちの{近|ちか}くのパン{屋|や}、すごく（　）よ。", "おいしい", "a_plain", "The bakery near my place is really good.", "", "plain"),
    ("この{公園|こうえん}、{夜|よる}はあまり（　）。", "安全", "a_neg", "This park isn't very safe at night.", "", "plain"),
    ("{昨日|きのう}の{花火|はなび}、すごく（　）ね。", "きれい", "a_past", "Yesterday's fireworks were really pretty, weren't they?", "", "plain"),
    ("{引|ひ}っ{越|こ}す{前|まえ}の{部屋|へや}は{全然|ぜんぜん}（　）。", "広い", "a_pastneg", "My old flat wasn't spacious at all.", "", "plain"),
    ("{駅前|えきまえ}の{新|あたら}しいカフェ、なかなか（　）よ。", "いい", "a_plain", "The new café by the station is pretty good.", "", "plain"),
    ("{日曜日|にちようび}の{朝|あさ}は{道|みち}が{空|す}いていて、{全然|ぜんぜん}（　）。", "うるさい", "a_neg", "On Sunday mornings the roads are empty and it isn't noisy at all.", "", "plain"),
    ("あのレストラン、{前|まえ}は（　）けど、{今|いま}は{人気|にんき}だよ。", "有名", "a_pastneg", "That restaurant wasn't well known before, but it's popular now.", "", "plain"),
    ("{子供|こども}のころ、この{川|かわ}はもっと（　）。", "汚い", "a_past", "When I was a child, this river was dirtier.", "", "plain"),
], {"polite": ("Polite: です・でした", "い-adj.: 高いです, 高くないです, 高かったです; な-adj.: 静かです, 静かじゃありません, 静かでした."),
    "plain": ("Plain (casual)", "い-adj.: 高い, 高くない, 高かった; な-adj.: 静か(だ), 静かじゃない, 静かだった.")})


context_quiz("10_compare", "adj-compare", "Comparing: より, 一番, ほど … ない",
             "Which is bigger, the best, not as … as — comparisons just use the adjective forms you know.", "adj", [
    ("{東京|とうきょう}は{大阪|おおさか}より（　）。", "大きい", "a_desu", "Tokyo is bigger than Osaka.", "", "cmp-yori"),
    ("{電車|でんしゃ}のほうがバスより（　）。", "便利", "a_desu", "The train is more convenient than the bus.", "", "cmp-yori"),
    ("{今日|きょう}は{昨日|きのう}より（　）ね。", "暖かい", "a_desu", "It's warmer today than yesterday, isn't it?", "", "cmp-yori"),
    ("{前|まえ}の{仕事|しごと}より{今|いま}の{仕事|しごと}のほうが（　）。", "楽", "a_desu", "My current job is easier than my last one.", "", "cmp-yori"),
    ("{犬|いぬ}と{猫|ねこ}と、どちらが（　）か。", "好き", "a_desu", "Which do you like better, dogs or cats?", "", "cmp-yori"),
    ("{家族|かぞく}の{中|なか}で{父|ちち}が{一番|いちばん}{背|せ}が（　）。", "高い", "a_desu", "My father is the tallest in my family.", "", "cmp-ichiban"),
    ("{日本料理|にほんりょうり}の{中|なか}で、{何|なに}が{一番|いちばん}（　）か。", "好き", "a_desu", "What's your favourite Japanese food?", "", "cmp-ichiban"),
    ("{一年|いちねん}で{一番|いちばん}（　）{月|つき}は{二月|にがつ}です。", "寒い", "a_noun", "The coldest month of the year is February.", "", "cmp-ichiban"),
    ("このクラスで{一番|いちばん}（　）{人|ひと}は{誰|だれ}ですか。", "真面目", "a_noun", "Who's the most serious student in this class?", "", "cmp-ichiban"),
    ("{今年|ことし}の{夏|なつ}は{去年|きょねん}ほど（　）。", "暑い", "a_neg_p", "This summer isn't as hot as last year.", "", "cmp-hodo"),
    ("{日本語|にほんご}は{思|おも}ったほど（　）。", "難しい", "a_pastneg_p", "Japanese wasn't as hard as I'd thought.", "", "cmp-hodo"),
    ("この{町|まち}は{東京|とうきょう}ほど（　）。", "賑やか", "a_neg", "This town isn't as lively as Tokyo.", "", "cmp-hodo"),
    ("{新幹線|しんかんせん}は{飛行機|ひこうき}ほど（　）けど、{便利|べんり}だ。", "速い", "a_neg", "The bullet train isn't as fast as a plane, but it's convenient.", "", "cmp-hodo"),
    ("{前|まえ}より{発音|はつおん}がずっと（　）ね。", "いい", "a_naru_ta", "Your pronunciation has got much better than before.", "", "cmp-yori"),
], {"cmp-yori": ("A は B より … (A is more … than B)", "The adjective stays in its normal form: 東京は大阪より大きい. のほうが marks the winner."),
    "cmp-ichiban": ("… で一番 … (the most …)", "一番 + adjective: 一番高い山, 一番好きな食べ物."),
    "cmp-hodo": ("A は B ほど … ない (not as … as)", "Always with a negative: 去年ほど暑くない, 東京ほど賑やかじゃない.")})

# ---------------------------------------------------------------- verb or adjective?
VS_TITLES = {"v": ("Verbs", "ない / ます / た on the verb: 行かない, 行きました."),
             "i": ("い-adjectives", "The い changes: 高くない, 高かったです."),
             "na": ("な-adjectives", "The word stays: 静かじゃない, 静かでした.")}

context_quiz("11_vs_feelings", "adj-vs-feelings", "English Verb, Japanese Adjective: 好き, 欲しい, 上手",
             "Like, hate, want, be good at, be scared, hurt — verbs in English and German, adjectives in Japanese.", "vs", [
    ("{私|わたし}は{猫|ねこ}が（　）。", "好き", "a_desu", "I like cats.", "'Like' is a verb in English (mögen), but 好き is a な-adjective — and what you like takes が."),
    ("{新|あたら}しいパソコンが（　）。", "欲しい", "a_desu", "I want a new computer.", "'Want (a thing)' = 欲しい, an い-adjective. The thing you want takes が."),
    ("{子供|こども}のころは{魚|さかな}が（　）。", "嫌い", "a_past_p", "As a child I hated fish.", "'Hate' is a verb in English, but 嫌い is a な-adjective (with a sneaky い at the end)."),
    ("{姉|あね}は{料理|りょうり}がとても（　）。", "上手", "a_desu", "My older sister is very good at cooking.", "'Be good at' = 上手, a な-adjective; the skill takes が."),
    ("{私|わたし}は{歌|うた}が（　）から、カラオケはちょっと…。", "下手", "a_plain", "I'm bad at singing, so karaoke's not really my thing…", "下手 is a な-adjective, so before から it needs だ: 下手だから."),
    ("{小|ちい}さいころ、{犬|いぬ}が（　）。", "怖い", "a_past", "When I was small I was scared of dogs.", "'Be scared of' = 怖い, an い-adjective: 犬が怖い, 怖かった."),
    ("{昨日|きのう}から{歯|は}が（　）。", "痛い", "a_desu", "My tooth has been hurting since yesterday.", "'Hurt' is a verb in English (wehtun), but 痛い is an い-adjective."),
    ("{家族|かぞく}に{会|あ}えなくて、（　）。", "寂しい", "a_desu", "I can't see my family, and I miss them.", "'Miss someone' is often 寂しい (I'm lonely), an い-adjective."),
    ("{今|いま}は{何|なに}も（　）。", "欲しい", "a_neg_p", "I don't want anything right now.", "欲しい is an い-adjective, so 'don't want' is 欲しくないです / 欲しくありません."),
    ("{数学|すうがく}は{前|まえ}から（　）。", "得意", "a_desu", "I've always been good at maths.", "得意 (な-adjective) = your strong point; use it about yourself. 上手 is more for praising others."),
    ("{実|じつ}は{朝|あさ}が（　）。", "苦手", "a_desu", "To be honest, I'm not a morning person.", "苦手 (な-adjective) = be bad at / not get on with."),
    ("{試験|しけん}に{合格|ごうかく}して、とても（　）。", "嬉しい", "a_past_p", "I passed the exam and was really happy.", "'Be glad' = 嬉しい, an い-adjective: 嬉しかったです."),
    ("{弟|おとうと}は{新|あたら}しいゲームを（　）。", "欲しがる", "teiru", "My little brother wants the new game.", "For someone else's wishes, 欲しい becomes the verb 欲しがる (and the thing takes を): 欲しがっている."),
    ("{田中|たなか}さんはテニスがあまり（　）。", "上手", "a_neg_p", "Tanaka isn't very good at tennis.", "上手 is a な-adjective: 上手じゃありません."),
    ("あの{映画|えいが}、{前|まえ}は（　）けど、{今|いま}は{大好|だいす}き。", "好き", "a_pastneg", "I didn't like that film before, but now I love it.", "好き is a な-adjective: 好きじゃなかった (not 好かなかった)."),
    ("{熱|ねつ}があって{頭|あたま}も（　）、{今日|きょう}は{休|やす}みます。", "痛い", "a_te", "I have a fever and a headache too, so I'm taking today off.", "痛い is an い-adjective: 痛くて (and / so)."),
], VS_TITLES)

context_quiz("12_vs_negative", "adj-vs-negative", "Saying Not: くない, じゃない or ない?",
             "Three ways to say 'not' — the word class decides. Includes the traps きれい, 嫌い and ある.", "vs", [
    ("この{辞書|じしょ}はあまり（　）。", "高い", "a_neg", "This dictionary isn't very expensive."),
    ("この{町|まち}は{夜|よる}も（　）。", "静か", "a_neg", "This town isn't quiet at night either."),
    ("{今日|きょう}は{雨|あめ}だから、{公園|こうえん}には（　）。", "行く", "nai", "It's raining today, so I'm not going to the park."),
    ("{私|わたし}の{部屋|へや}は{全然|ぜんぜん}（　）。", "きれい", "a_neg", "My room isn't tidy at all."),
    ("{野菜|やさい}は（　）けど、あまり{食|た}べない。", "嫌い", "a_neg", "I don't dislike vegetables, but I don't eat many."),
    ("{日本語|にほんご}の{新聞|しんぶん}はまだ（　）。", "分かる", "nai", "I can't understand Japanese newspapers yet."),
    ("{今日|きょう}は{全然|ぜんぜん}（　）。", "寒い", "a_neg", "It isn't cold at all today."),
    ("この{映画|えいが}は{思|おも}ったほど（　）。", "面白い", "a_neg", "This film isn't as interesting as I thought."),
    ("あの{店|みせ}は{有名|ゆうめい}だけど、そんなに（　）。", "おいしい", "a_neg", "That place is famous, but it isn't that good."),
    ("{明日|あした}は（　）から、{一緒|いっしょ}に{遊|あそ}ぼう。", "忙しい", "a_neg", "I'm not busy tomorrow, so let's hang out."),
    ("{彼|かれ}はお{酒|さけ}を（　）。", "飲む", "nai", "He doesn't drink alcohol."),
    ("このアプリは{便利|べんり}だけど、{使|つか}い{方|かた}が（　）。", "簡単", "a_neg", "This app is handy, but it isn't easy to use."),
    ("{今日|きょう}は{天気|てんき}が（　）ね。", "いい", "a_neg", "The weather isn't good today, is it?"),
    ("{時間|じかん}が（　）から、タクシーで{行|い}こう。", "ある", "nai", "We don't have time, so let's take a taxi.", "ある → ない (not あらない). And ない itself then conjugates like an い-adjective: なかった."),
    ("{有名|ゆうめい}な{歌手|かしゅ}らしいけど、{私|わたし}は（　）。", "知る", "nai", "Apparently she's a famous singer, but I don't know her."),
    ("{駅|えき}はここからそんなに（　）。", "遠い", "a_neg", "The station isn't that far from here."),
    ("{答|こた}えはそれと（　）。", "違う", "nai", "The answer is no different from that.", "違う is a verb, so its negative is 違わない."),
    ("ここは（　）から、{入|はい}らないでください。", "安全", "a_neg", "It isn't safe here, so please don't go in."),
], VS_TITLES)

context_quiz("13_vs_polite_past", "adj-vs-polite-past", "Polite Past: かったです, でした or ました?",
             "Telling someone about a trip: the polite past of verbs and both adjective types — and the classic 高いでした mistake.", "vs", [
    ("{旅行|りょこう}はとても（　）。", "楽しい", "a_past_p", "The trip was a lot of fun."),
    ("ホテルの{部屋|へや}はとても（　）。", "きれい", "a_past_p", "The hotel room was very clean."),
    ("{京都|きょうと}でお{寺|てら}をたくさん（　）。", "見る", "mashita", "I saw lots of temples in Kyoto."),
    ("{料理|りょうり}はあまり（　）。", "おいしい", "a_pastneg_p", "The food wasn't very good."),
    ("{天気|てんき}はずっと（　）。", "いい", "a_past_p", "The weather was good the whole time."),
    ("{店員|てんいん}さんはとても（　）。", "親切", "a_past_p", "The shop staff were very kind."),
    ("{朝|あさ}{早|はや}く{起|お}きたので、{飛行機|ひこうき}の{中|なか}でずっと（　）。", "寝る", "mashita", "I got up early, so I slept the whole flight."),
    ("{美術館|びじゅつかん}は{思|おも}ったほど（　）。", "静か", "a_pastneg_p", "The museum wasn't as quiet as I'd expected."),
    ("{新幹線|しんかんせん}の{切符|きっぷ}は（　）。", "高い", "a_past_p", "The bullet-train ticket was expensive."),
    ("{温泉|おんせん}には（　）。{時間|じかん}がなかったので。", "入る", "masendeshita", "I didn't go in the hot spring — there wasn't time."),
    ("{山道|やまみち}は（　）けど、{景色|けしき}が{素晴|すば}らしかったです。", "大変", "a_past_p", "The mountain path was tough, but the view was wonderful."),
    ("{空港|くうこう}までのバスは（　）。", "便利", "a_pastneg_p", "The bus to the airport wasn't convenient."),
    ("お{土産|みやげ}をたくさん（　）。", "買う", "mashita", "I bought lots of souvenirs."),
    ("{駅|えき}から{旅館|りょかん}までは（　）。", "遠い", "a_pastneg_p", "The inn wasn't far from the station."),
    ("{夜|よる}は{少|すこ}し（　）。", "寒い", "a_past_p", "It was a bit cold at night."),
    ("{一人|ひとり}だったけど、{全然|ぜんぜん}（　）。", "寂しい", "a_pastneg_p", "I was on my own, but I wasn't lonely at all."),
], VS_TITLES)

context_quiz("14_vs_states", "adj-vs-states", "English Adjective, Japanese Verb: 疲れた, 混んでいる",
             "Tired, crowded, married, broken, different — adjectives in English and German, verbs in Japanese.", "vs", [
    ("{今日|きょう}はたくさん{歩|ある}いたので、とても（　）。", "疲れる", "ta", "I walked a lot today, so I'm really tired.", "'Tired' is an adjective in English, but Japanese uses the verb 疲れる (get tired): 疲れた = I've got tired, i.e. I'm tired.", "st-ta"),
    ("{朝|あさ}の{電車|でんしゃ}はいつも（　）。", "混む", "teiru", "The morning trains are always crowded.", "'Crowded' → 混む (get crowded) + ている = is crowded.", "st-teiru"),
    ("{日曜日|にちようび}の{朝|あさ}は{道|みち}が（　）。", "空く", "teimasu", "On Sunday mornings the roads are empty.", "'Empty, not crowded' → 空く + ている.", "st-teiru"),
    ("{兄|あに}はもう（　）。", "結婚する", "teimasu", "My older brother is married.", "'Married' → 結婚する + ている describes the state.", "st-teiru"),
    ("{彼女|かのじょ}はお{母|かあ}さんによく（　）。", "似る", "teimasu", "She looks a lot like her mother.", "'Similar / looks like' → the verb 似る, almost always as 似ている.", "st-teiru"),
    ("{今日|きょう}は{朝|あさ}からよく（　）。", "晴れる", "teimasu", "It's been nice and sunny since the morning.", "'Sunny' → the verb 晴れる (clear up) + ている.", "st-teiru"),
    ("{空|そら}が（　）から、{傘|かさ}を{持|も}って{行|い}こう。", "曇る", "teiru", "It's cloudy, so let's take an umbrella.", "'Cloudy' → 曇る (cloud over) + ている.", "st-teiru"),
    ("このパソコンは（　）から、{使|つか}えません。", "壊れる", "teiru", "This computer is broken, so you can't use it.", "'Broken' → 壊れる (break) + ている.", "st-teiru"),
    ("{窓|まど}が（　）よ。{閉|し}めてください。", "開く", "teiru", "The window is open. Please close it.", "'Open' (adjective) → the verb 開く + ている.", "st-teiru"),
    ("{答|こた}えが（　）よ。", "違う", "masu", "The answer is wrong.", "'Different / wrong' is a verb: 違う, 違います — not an adjective.", "st-verb"),
    ("{前|まえ}より{少|すこ}し（　）ね。", "痩せる", "ta", "You've got a bit slimmer than before.", "'Slim' → the verb 痩せる (lose weight): 痩せた / 痩せている.", "st-ta"),
    ("{冬|ふゆ}になって、{少|すこ}し（　）。", "太る", "ta", "Since winter came I've put on a bit of weight.", "'Fat' → the verb 太る (put on weight): 太った / 太っている.", "st-ta"),
    ("{田中|たなか}さんの{電話番号|でんわばんごう}を（　）か。", "知る", "teimasu", "Do you know Tanaka's phone number?", "'Know' → 知っている (with ている), but 'don't know' is 知らない.", "st-teiru"),
    ("{雨|あめ}で{服|ふく}が（　）。", "濡れる", "ta", "My clothes got wet in the rain.", "'Wet' → the verb 濡れる (get wet).", "st-ta"),
    ("{部屋|へや}が{少|すこ}し（　）ね。{掃除|そうじ}しよう。", "汚れる", "teiru", "The room's a bit dirty. Let's clean up.", "汚い (い-adjective) also means 'dirty'; 汚れている stresses that it has got dirty.", "st-teiru"),
    ("{何|なに}か（　）ことがあったら、{言|い}ってください。", "困る", "ta", "If anything's a problem, just tell me.", "'Be in trouble / have a problem' is a verb: 困る, 困った.", "st-verb"),
], {"st-teiru": ("Verb + ている = a state", "混んでいる (is crowded), 結婚している (is married), 壊れている (is broken)."),
    "st-ta": ("Verb + た = has just become", "疲れた (I'm tired), 太った (I've put on weight)."),
    "st-verb": ("Simply a verb", "違う (be different), 困る (be in trouble) — no adjective at all.")})

context_quiz("15_vs_nouns", "adj-vs-nouns", "Before a Noun: 高い本, 静かな部屋, 読んだ本",
             "All three can describe a noun: い-adjectives as they are, な-adjectives with な, verbs in a plain form.", "vs", [
    ("{駅|えき}の{近|ちか}くに（　）カフェがあります。", "新しい", "a_noun", "There's a new café near the station."),
    ("もっと（　）{部屋|へや}がいいです。", "静か", "a_noun", "I'd prefer a quieter room."),
    ("{昨日|きのう}（　）{本|ほん}はとても{面白|おもしろ}かった。", "読む", "ta", "The book I read yesterday was really interesting.", "A verb goes straight before a noun in a plain form: 読んだ本 (the book I read)."),
    ("{日本|にほん}で{一番|いちばん}（　）{山|やま}は{富士山|ふじさん}です。", "高い", "a_noun", "The highest mountain in Japan is Mt Fuji."),
    ("{田中|たなか}さんは（　）{人|ひと}ですね。", "親切", "a_noun", "Tanaka is a kind person, isn't he?"),
    ("あそこで{本|ほん}を（　）{人|ひと}は{私|わたし}の{兄|あに}です。", "読む", "teiru", "The person reading a book over there is my brother.", "ている works before a noun too: 読んでいる人 (the person reading)."),
    ("{毎朝|まいあさ}（　）{電車|でんしゃ}は8{時|じ}{発|はつ}です。", "乗る", "dict", "The train I take every morning leaves at eight."),
    ("{来週|らいしゅう}の{会|かい}に（　）{人|ひと}は{教|おし}えてください。", "来る", "nai", "If you're not coming to next week's meeting, please let me know.", "Negatives work too: 来ない人 (people who aren't coming)."),
    ("ここは（　）{店|みせ}なので、いつも{混|こ}んでいます。", "有名", "a_noun", "This is a famous shop, so it's always crowded."),
    ("{今日|きょう}は（　）{天気|てんき}ですね。", "いい", "a_noun", "Lovely weather today, isn't it?"),
    ("{日本語|にほんご}が（　）{人|ひと}を{探|さが}しています。", "話す", "potential", "We're looking for someone who can speak Japanese."),
    ("{一番|いちばん}（　）{食|た}べ{物|もの}は{何|なん}ですか。", "好き", "a_noun", "What's your favourite food?", "好き is a な-adjective, so before a noun it's 好きな — even though 'like' is a verb in English."),
    ("（　）{時|とき}、よくこの{公園|こうえん}で{遊|あそ}びました。", "小さい", "a_noun", "When I was little I often played in this park."),
    ("{先週|せんしゅう}（　）{映画|えいが}をもう{一度|いちど}{見|み}たい。", "見る", "ta", "I want to see the film I saw last week again."),
    ("{子供|こども}のころ（　）{野菜|やさい}は{何|なん}でしたか。", "嫌い", "a_noun", "Which vegetables did you hate as a child?"),
    ("{困|こま}ったときに（　）{人|ひと}が{本当|ほんとう}の{友達|ともだち}だ。", "手伝う", "dict", "A real friend is someone who helps when you're in trouble."),
], VS_TITLES)

context_quiz("16_vs_change", "adj-vs-change", "Becoming & Making: くなる, になる, ようになる",
             "Getting warmer, getting good at something, being able to — and making things quieter or shorter.", "vs", [
    ("{三月|さんがつ}になって、{少|すこ}しずつ（　）なりました。", "暖かい", "a_adv", "Since March it's been getting gradually warmer.", "", "ch-adj"),
    ("{毎日|まいにち}{練習|れんしゅう}して、ピアノが（　）なりました。", "上手", "a_adv", "I practised every day and got good at the piano.", "", "ch-adj"),
    ("{練習|れんしゅう}して、{漢字|かんじ}が（　）ようになりました。", "読む", "potential", "I practised and can now read kanji.", "Verbs don't take くなる / になる: potential + ようになった = 'became able to'.", "ch-verb"),
    ("{薬|くすり}を{飲|の}んだら、{体|からだ}の{調子|ちょうし}が（　）。", "いい", "a_naru_ta", "I took the medicine and felt better.", "", "ch-adj"),
    ("{日本|にほん}に{来|き}てから、{納豆|なっとう}が（　）。", "好き", "a_naru_ta", "Since coming to Japan I've come to like natto.", "好き is a な-adjective: 好きになる = come to like.", "ch-adj"),
    ("{最近|さいきん}、{朝|あさ}{早|はや}く（　）ようになった。", "起きる", "dict", "Recently I've started getting up early.", "Dictionary form + ようになる = 'have started doing (as a habit)'.", "ch-verb"),
    ("{美容院|びよういん}で{髪|かみ}を（　）しました。", "短い", "a_adv", "I had my hair cut short at the salon.", "くする / にする = make something …: 短くする.", "ch-make"),
    ("{部屋|へや}を（　）してから{出|で}かけてね。", "きれい", "a_adv", "Tidy up your room before you go out.", "", "ch-make"),
    ("テレビの{音|おと}を{少|すこ}し（　）してもらえますか。", "小さい", "a_adv", "Could you turn the TV down a little?", "", "ch-make"),
    ("{赤|あか}ちゃんが{寝|ね}ているので、（　）してね。", "静か", "a_adv", "The baby's asleep, so keep it quiet.", "", "ch-make"),
    ("{毎日|まいにち}{聞|き}いていたら、{日本語|にほんご}のニュースが（　）ようになった。", "分かる", "dict", "Listening every day, I've come to understand the Japanese news.", "分かる already means 'can understand', so it takes ようになる as it is.", "ch-verb"),
    ("{電気|でんき}を{消|け}したら、{部屋|へや}が（　）。", "暗い", "a_naru_ta", "When I turned off the light, the room went dark.", "", "ch-adj"),
    ("{夜|よる}になって、{町|まち}が（　）。", "静か", "a_naru_ta", "When night came, the town went quiet.", "", "ch-adj"),
    ("{先生|せんせい}のおかげで、{数学|すうがく}が（　）なりました。", "面白い", "a_adv", "Thanks to my teacher, maths became interesting.", "", "ch-adj"),
], {"ch-adj": ("Adjective + なる: become …", "暖かくなる, 上手になる, よくなる — い → く, な-adjectives + に."),
    "ch-verb": ("Verb + ようになる: start to / become able to", "読めるようになった, 起きるようになった."),
    "ch-make": ("Adjective + する: make something …", "短くする, きれいにする, 静かにする.")})

context_quiz("17_vs_too_looks", "adj-vs-too-looks", "Too Much & Looks Like: すぎる and そう",
             "Too spicy, ate too much, looks tasty, looks like rain — the same endings on adjectives and verbs.", "vs", [
    ("このカレーは（　）よ。", "辛い", "a_sugiru", "This curry is too spicy.", "", "too-adj"),
    ("{昨日|きのう}の{夜|よる}、{少|すこ}し（　）。", "食べる", "v_sugita", "I ate a bit too much last night.", "", "too-verb"),
    ("この{問題|もんだい}は{私|わたし}には（　）。", "難しい", "a_sugiru", "This problem is too hard for me.", "", "too-adj"),
    ("この{部屋|へや}は{一人|ひとり}だと（　）。", "静か", "a_sugiru", "This room is too quiet when I'm on my own.", "", "too-adj"),
    ("{昨日|きのう}はお{酒|さけ}を（　）。", "飲む", "v_sugita", "I drank too much yesterday.", "", "too-verb"),
    ("{毎日|まいにち}ゲームを（　）のはよくないよ。", "する", "v_sugiru", "Playing games too much every day isn't good.", "", "too-verb"),
    ("{見|み}て、このパン、（　）！", "おいしい", "a_sou", "Look, this bread looks delicious!", "", "sou-adj"),
    ("{空|そら}が{暗|くら}い。{雨|あめ}が（　）。", "降る", "v_sou", "The sky's dark. It looks like it's going to rain.", "With a verb, そう means 'looks like it's about to …'.", "sou-verb"),
    ("{田中|たなか}さん、{今日|きょう}は（　）ですね。", "元気", "a_sou", "You look well today, Tanaka.", "", "sou-adj"),
    ("この{本|ほん}、（　）ね。{貸|か}してくれる？", "面白い", "a_sou", "This book looks interesting. Could you lend it to me?", "", "sou-adj"),
    ("{棚|たな}の{上|うえ}の{箱|はこ}が（　）。", "落ちる", "v_sou", "The box on the shelf looks like it's about to fall.", "", "sou-verb"),
    ("{明日|あした}は{天気|てんき}が（　）ですね。", "いい", "a_sou", "Looks like the weather will be good tomorrow.", "いい → よさそう (irregular).", "sou-adj"),
    ("{彼女|かのじょ}は{今|いま}にも（　）な{顔|かお}をしていた。", "泣く", "v_sou", "She looked as if she was about to cry.", "", "sou-verb"),
    ("このかばんは（　）けど、{全然|ぜんぜん}{重|おも}くないよ。", "重い", "a_sou", "This bag looks heavy, but it isn't heavy at all.", "", "sou-adj"),
], {"too-adj": ("Adjective + すぎる: too …", "い → すぎる (辛すぎる), な + すぎる (静かすぎる)."),
    "too-verb": ("Verb + すぎる: … too much", "ます-stem + すぎる: 食べすぎる, 飲みすぎた, しすぎる."),
    "sou-adj": ("Adjective + そう: looks …", "おいしそう, 元気そう; いい → よさそう."),
    "sou-verb": ("Verb + そう: looks like it's about to …", "ます-stem + そう: 降りそう, 落ちそう, 泣きそう.")})

drill_quiz("18_vs_mixed", "adj-vs-mixed", "Verb & Adjective Sprint: Same Cues, Different Endings",
           "24 words, same kinds of cues: decide verb, い or な first — then the ending.", "vs", [
    ("高い", "a_neg", "v-mix"), ("書く", "nai", "v-mix"), ("静か", "a_neg", "v-mix"), ("好き", "a_past", "v-mix"),
    ("寝る", "ta", "v-mix"), ("欲しい", "a_past", "v-mix"), ("分かる", "nai", "v-mix"), ("きれい", "a_pastneg", "v-mix"),
    ("行く", "ta", "v-mix"), ("いい", "a_past", "v-mix"), ("違う", "nai", "v-mix"), ("便利", "a_te", "v-mix"),
    ("読む", "te", "v-mix"), ("寒い", "a_te", "v-mix"), ("嫌い", "a_neg_p", "v-mix"), ("来る", "masen", "v-mix"),
    ("有名", "a_past_p", "v-mix"), ("楽しい", "a_past_p", "v-mix"), ("見る", "mashita", "v-mix"), ("元気", "a_neg", "v-mix"),
    ("痛い", "a_neg", "v-mix"), ("疲れる", "ta", "v-mix"), ("上手", "a_naru_ta", "v-mix"), ("する", "nakatta", "v-mix"),
], {"v-mix": ("Verbs and adjectives mixed", "Verbs: ない / ます / た. い-adjectives: くない / かった. な-adjectives: じゃない / だった.")})


def write(folder):
    os.makedirs(folder, exist_ok=True)
    for f in os.listdir(folder):
        if f.endswith(".json"):
            os.remove(os.path.join(folder, f))
    total = 0
    for fname, d in sorted(QZ.items()):
        d["category"], d["level"] = CAT, LEVEL
        cnt = collections.Counter(q["point"] for q in d["questions"])
        assert {p["id"] for p in d["points"]} == set(cnt), (fname, cnt)
        ids = [x["id"] for x in QZ.values()]
        assert ids.count(d["id"]) == 1, d["id"]
        for q in d["questions"]:
            if q["options"]:
                assert q["notes"][q["answer"]] == "" and all(n for i, n in enumerate(q["notes"]) if i != q["answer"]), q["prompt"]
            else:
                assert q["accept"] and "（　）" in q["prompt"], q["prompt"]
                assert not set(q["accept"]) & set(q.get("wrong_forms", {})), q["prompt"]
        with open(f"{folder}/{fname}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        total += len(d["questions"])
        print(f"{fname:20} {len(d['points'])} pts {len(d['questions'])} Q")
    print(f"{len(QZ)} quizzes, {total} questions")


if __name__ == "__main__":
    write("quizzes/07_adjectives")
