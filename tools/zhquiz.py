"""Helpers for writing Mandarin quizzes in a compact notation.

'汉字/pīnyīn' tokens are separated by ASCII spaces; a following pure-pinyin token joins the
previous reading ('不有/bù yǒu'). '@A' is a position marker, '//' a line break, and '**' around
a token makes it bold. Any other token is copied as-is.
"""
import collections, json, random, re

PINYIN = r"[A-Za-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü-]+"


def zh(s):
    out = []
    for tok in s.split(" "):
        if not tok:
            continue
        if tok == "//":
            out.append("\n"); continue
        if tok.startswith("@"):
            out.append(f"［{tok[1:]}］"); continue
        if re.fullmatch(PINYIN, tok) and out and out[-1].endswith("}"):
            out[-1] = out[-1][:-1] + " " + tok + "}"; continue
        m = re.match(r"^(\**)([^/*]+)/([^*]+?)(\**)$", tok)
        out.append(f"{m[1]}{{{m[2]}|{m[3]}}}{m[4]}" if m else tok)
    return "".join(out)


def P(id, title, summary, body, examples):
    return {"id": id, "title": title, "summary": summary, "body": body,
            "examples": [[zh(a), b] for a, b in examples]}


def Q(point, prompt, options, notes, explanation, translation="", answer=0, fixed=False, raw_opts=False):
    assert len(options) == len(notes) >= 2 and notes[answer] == "", (prompt, notes)
    q = {"point": point, "prompt": prompt, "options": options if raw_opts else [zh(o) for o in options],
         "answer": answer, "explanation": explanation, "notes": notes, "translation": translation}
    if fixed:
        q["fixed_order"] = True
    return q


def pos(point, word, sentence, answer, notes, explanation, translation):
    """HSK-style 'where does the word go?' question."""
    return Q(point, f"Where does **{zh(word)}** go?\n" + zh(sentence), ["A", "B", "C", "D"], notes,
             explanation, translation, answer=answer, fixed=True, raw_opts=True)


def star(point, sentence_with_blanks, pieces_shown, options, notes, explanation, translation):
    """★ ordering: options[0] is the piece in the ★ slot."""
    prompt = (zh(sentence_with_blanks).replace("＿", "　＿＿　").replace("★", "　★　")
              + "\n（" + "・".join(zh(p) for p in pieces_shown) + "）")
    return Q(point, prompt, options, notes, explanation, translation)


def tf(point, passage, statement, true, note, explanation, translation):
    """HSK 判断对错: is the ★ statement true according to the passage?"""
    notes = ["", note] if true else [note, ""]
    return Q(point, zh(passage) + "\n\n★ " + zh(statement), ["对/duì （true）", "错/cuò （false）"], notes,
             explanation, translation, answer=0 if true else 1, fixed=True)


def reading(point, passage, question, options, notes, explanation, translation):
    """HSK 阅读理解: a short passage and a ★ question; options[0] is correct."""
    return Q(point, zh(passage) + "\n\n★ " + zh(question), options, notes, explanation, translation)


def order3(point, parts, correct, wrong, notes_wrong, explanation, translation):
    """HSK 排列顺序: put A/B/C in order. Options are shown sorted, in fixed order."""
    prompt = "Put the parts in order:\n" + "\n".join(f"{k}　{zh(v)}" for k, v in zip("ABC", parts))
    opts = sorted([correct] + wrong)
    notes = [("" if o == correct else notes_wrong[wrong.index(o)]) for o in opts]
    return Q(point, prompt, opts, notes, explanation, translation, answer=opts.index(correct), fixed=True, raw_opts=True)


def apply_fixes(d):
    """tools/distractor_fixes.json: swap a wrong option for another point of the same quiz."""
    import os
    plain = lambda t: re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", t)
    fixes = json.load(open(os.path.join(os.path.dirname(__file__), "distractor_fixes.json"), encoding="utf-8"))["fixes"]
    for f in fixes:
        if f["quiz"] != d["id"]:
            continue
        q = d["questions"][f["i"]]
        opts = [plain(o).replace(" ", "") for o in q["options"]]
        j = opts.index(f["old"])
        assert j != q["answer"] and plain(f["new"]) not in opts, (d["id"], f)
        q["options"][j], q["notes"][j] = f["new"], f["note"]


def write(quizzes, folder, category, level, seed):
    random.seed(seed)
    for d in quizzes.values():
        apply_fixes(d)
    for fname, d in quizzes.items():
        d = {"id": d["id"], "category": category, "language": "zh", "title": d["title"],
             "description": d["description"], "level": level, "points": d["points"], "questions": d["questions"]}
        ids = {p["id"] for p in d["points"]}
        cnt = collections.Counter(q["point"] for q in d["questions"])
        assert set(cnt) == ids and min(cnt.values()) >= 2, (fname, cnt, ids)
        prev = None
        for q in d["questions"]:
            assert len(set(q["options"])) == len(q["options"]), q["prompt"]
            if not q.get("fixed_order"):
                n = len(q["options"])
                while True:
                    perm = list(range(n)); random.shuffle(perm)
                    if perm.index(q["answer"]) != prev:
                        break
                q["options"] = [q["options"][i] for i in perm]; q["notes"] = [q["notes"][i] for i in perm]
                q["answer"] = perm.index(q["answer"])
            assert q["notes"][q["answer"]] == ""
            prev = q["answer"]
        open(f"{folder}/{fname}.json", "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print(f"{fname:22} {len(d['points'])} pts {len(d['questions'])} Q")
