"""Applies tools/distractor_fixes.json to the hand-written quiz files (the generated ones apply it themselves).

Each fix replaces one wrong option (matched by its plain text) and its note; the answer index stays the same.
Run from the repo root. Safe to run repeatedly: fixes already applied are skipped.
"""
import glob, json, re

plain = lambda t: re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", t)
fixes = json.load(open("tools/distractor_fixes.json", encoding="utf-8"))["fixes"]
by_quiz = {}
for f in fixes:
    by_quiz.setdefault(f["quiz"], []).append(f)

for path in sorted(glob.glob("quizzes/*/*.json")):
    d = json.load(open(path, encoding="utf-8"))
    todo = by_quiz.get(d["id"])
    if not todo or path.split("/")[1] in ("05_n1",) or path.split("/")[1].startswith("5"):
        continue
    changed = 0
    for f in todo:
        q = d["questions"][f["i"]]
        opts = [plain(o) for o in q["options"]]
        if plain(f["new"]) in opts:
            continue
        j = opts.index(f["old"])
        assert j != q["answer"], (path, f)
        q["options"][j], q["notes"][j] = f["new"], f["note"]
        changed += 1
    if changed:
        open(path, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print(f"{path}: {changed}")
