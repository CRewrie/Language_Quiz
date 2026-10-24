"""Builds static/kana/content.json for the Hiragana Dojo from tools/kana_corpus.py.

Every word and sentence is checked (hiragana only), gets romaji, and the earliest lesson whose kana cover it:
lessons 0–9 are the kana rows, 10 adds ゛゜ (voiced), 11 adds the small kana. Run from the repo root.
"""
import collections, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from kana_corpus import FAQ, KANA, SENTENCES, WORDS

ROWS = [("Vowels", "あいうえお"), ("K-row", "かきくけこ"), ("S-row", "さしすせそ"), ("T-row", "たちつてと"),
        ("N-row", "なにぬねの"), ("H-row", "はひふへほ"), ("M-row", "まみむめも"), ("Y-row", "やゆよ"),
        ("R-row", "らりるれろ"), ("W-row & ん", "わをん"),
        ("゛ & ゜ (voiced)", "がぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽ"), ("Small kana", "ゃゅょっ")]
LEVEL = {c: i for i, (_, row) in enumerate(ROWS) for c in row}
PUNCT = " 。、！？"

ROMA = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so", "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro", "わ": "wa", "を": "o", "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do", "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po",
}
YOON = {"ゃ": "a", "ゅ": "u", "ょ": "o"}
PARTICLES = {"は": "wa", "へ": "e", "を": "o"}
SPECIAL = {"こんにちは": "konnichiwa", "こんばんは": "konbanwa"}


def romaji_word(w):
    if w in SPECIAL:
        return SPECIAL[w]
    out, i = "", 0
    while i < len(w):
        c = w[i]
        nxt = w[i + 1] if i + 1 < len(w) else ""
        if c == "っ":
            r = romaji_word(w[i + 1:i + 3] if w[i + 2:i + 3] in YOON else nxt)
            out += ("t" if r.startswith("ch") else r[:1]) if r else ""
            i += 1
            continue
        if nxt in YOON:  # きゃ → kya, しゃ → sha, ちゃ → cha, じゃ → ja
            base = ROMA[c]
            v = YOON[nxt]
            out += base[:-1] + v if base in ("shi", "chi", "ji") else base[:-1] + "y" + v
            i += 2
            continue
        if c == "ん" and nxt and (ROMA.get(nxt, "x")[0] in "aiueoy"):
            out += "n'"
            i += 1
            continue
        out += ROMA[c] if c in ROMA else c
        i += 1
    return out


def romaji(text):
    words = []
    for tok in text.split(" "):
        if not tok:
            continue
        core = tok.rstrip("。、！？")
        tail = tok[len(core):].replace("。", ".").replace("、", ",").replace("！", "!").replace("？", "?")
        words.append((PARTICLES.get(core) or romaji_word(core)) + tail)
    s = " ".join(words)
    if " " not in text.strip():
        return s
    return re.sub(r"(^|[.!?] )([a-z])", lambda m: m.group(1) + m.group(2).upper(), s)


def level(text):
    lv = [LEVEL[c] for c in text if c not in PUNCT]
    return max(lv)


def parse(block, kind):
    items = collections.OrderedDict()
    for n, line in enumerate(block.strip().splitlines(), 1):
        jp, en = (x.strip() for x in line.split("|"))
        bad = [c for c in jp if c not in LEVEL and c not in PUNCT]
        assert not bad, f"{kind} line {n}: {jp} has {bad}"
        if kind == "word":
            assert " " not in jp and "。" not in jp, f"word with space: {jp}"
        if jp in items:  # merge meanings of duplicates (はし: bridge / chopsticks)
            if en not in items[jp][2].split(", ") and en not in items[jp][2]:
                items[jp][2] += f"; {en}"
            continue
        items[jp] = [jp, romaji(jp), en, level(jp)]
    return list(items.values())


def main():
    words, sentences = parse(WORDS, "word"), parse(SENTENCES, "sentence")
    for k in "".join(r for _, r in ROWS[:10]):
        assert k in KANA, f"no notes for {k}"
    out = {
        "rows": [[name, kana] for name, kana in ROWS],
        "words": words, "sentences": sentences,
        "kana": {k: list(v) for k, v in KANA.items()},
        "faq": [list(x) for x in FAQ],
    }
    path = os.path.join("static", "kana", "content.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    by = collections.Counter(w[3] for w in words)
    bs = collections.Counter(s[3] for s in sentences)
    print(f"{len(words)} words, {len(sentences)} sentences → {path} ({os.path.getsize(path) // 1024} KB)")
    for i, (name, _) in enumerate(ROWS):
        print(f"  {i:2} {name:18} words {by[i]:4}  sentences {bs[i]:4}")


if __name__ == "__main__":
    main()
