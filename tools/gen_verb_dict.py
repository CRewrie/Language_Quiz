"""Builds static/verbs/verbs.json for the verb lookup page from tools/jlpt_verbs.py.

Each verb gets its English gloss in four shapes (base, past, past participle, -ing) for the example sentences.
The conjugation itself happens in the browser (static/verbs/conjugate.js); if node is installed, this script also
checks that engine against the Verb Lab's (gen_ja_verbs.forms) for every verb of both lists. Run from the repo root.
"""
import json, os, re, shutil, subprocess, sys

sys.path.insert(0, os.path.dirname(__file__))
from jlpt_verbs import VERBS

CLASSES = {"ru", "u", "iku", "aru", "suru", "kuru", "honor", "tou"}

# Irregular English verbs: base → (past, past participle)
IRREGULAR = {
    "be": ("was", "been"), "bear": ("bore", "borne"), "become": ("became", "become"), "bet": ("bet", "bet"),
    "bind": ("bound", "bound"), "bite": ("bit", "bitten"), "blow": ("blew", "blown"), "break": ("broke", "broken"),
    "bring": ("brought", "brought"), "build": ("built", "built"), "buy": ("bought", "bought"), "catch": ("caught", "caught"),
    "choose": ("chose", "chosen"), "come": ("came", "come"), "cut": ("cut", "cut"), "do": ("did", "done"),
    "draw": ("drew", "drawn"), "drink": ("drank", "drunk"), "drive": ("drove", "driven"), "eat": ("ate", "eaten"),
    "fall": ("fell", "fallen"), "feel": ("felt", "felt"), "fight": ("fought", "fought"), "find": ("found", "found"),
    "fly": ("flew", "flown"), "forget": ("forgot", "forgotten"), "freeze": ("froze", "frozen"), "get": ("got", "got"),
    "give": ("gave", "given"), "go": ("went", "gone"), "grow": ("grew", "grown"), "hang": ("hung", "hung"),
    "hide": ("hid", "hidden"), "hit": ("hit", "hit"), "hold": ("held", "held"), "keep": ("kept", "kept"),
    "leave": ("left", "left"), "lend": ("lent", "lent"), "let": ("let", "let"), "lose": ("lost", "lost"),
    "make": ("made", "made"), "meet": ("met", "met"), "overtake": ("overtook", "overtaken"), "pay": ("paid", "paid"),
    "put": ("put", "put"), "quit": ("quit", "quit"), "read": ("read", "read"), "ride": ("rode", "ridden"),
    "ring": ("rang", "rung"), "rise": ("rose", "risen"), "run": ("ran", "run"), "say": ("said", "said"),
    "see": ("saw", "seen"), "sell": ("sold", "sold"), "send": ("sent", "sent"), "shake": ("shook", "shaken"),
    "shine": ("shone", "shone"), "shoot": ("shot", "shot"), "show": ("showed", "shown"), "sing": ("sang", "sung"),
    "sink": ("sank", "sunk"), "sit": ("sat", "sat"), "sleep": ("slept", "slept"), "sow": ("sowed", "sown"),
    "speak": ("spoke", "spoken"), "spend": ("spent", "spent"), "split": ("split", "split"), "spread": ("spread", "spread"),
    "stand": ("stood", "stood"), "steal": ("stole", "stolen"), "stick": ("stuck", "stuck"), "strike": ("struck", "struck"),
    "sweep": ("swept", "swept"), "swim": ("swam", "swum"), "take": ("took", "taken"), "teach": ("taught", "taught"),
    "tear": ("tore", "torn"), "tell": ("told", "told"), "think": ("thought", "thought"), "understand": ("understood", "understood"),
    "wake": ("woke", "woken"), "weave": ("wove", "woven"), "win": ("won", "won"), "wind": ("wound", "wound"),
    "write": ("wrote", "written"), "lead": ("led", "led"), "slide": ("slid", "slid"), "panic": ("panicked", "panicked"),
}
# Short verbs whose last consonant doubles (stop → stopped, stopping)
DOUBLE = {"stop", "drop", "plan", "chat", "skip", "step", "rob", "rot", "omit", "occur", "permit", "wrap", "rub", "stab",
          "fit", "wet", "regret", "prefer", "travel", "slip", "grab", "nod", "beg", "run", "swim", "cut", "put", "sit", "get",
          "hit", "begin", "forget", "win", "set", "bet", "dig", "shop", "hug", "pat", "tap", "trip", "ship", "knit", "spin",
          "split", "let", "quit", "excel", "transfer"}


def english(gloss):
    """'take (a shower), …' → base, past, past participle, -ing of the first meaning ('took (a shower)' …)."""
    first = re.split(r",(?![^(]*\))", gloss)[0].strip()  # commas inside (…) belong to the meaning
    for tag in (" (honorific)", " (humble)"):
        first = first.replace(tag, "")
    verb, _, rest = first.partition(" ")
    rest = " " + rest if rest else ""
    if verb in IRREGULAR:
        past, pp = IRREGULAR[verb]
    elif verb.endswith("e"):
        past = pp = verb + "d"
    elif verb.endswith("y") and verb[-2] not in "aeiou":
        past = pp = verb[:-1] + "ied"
    elif verb in DOUBLE:
        past = pp = verb + verb[-1] + "ed"
    else:
        past = pp = verb + "ed"
    if verb == "be":
        ing = "being"
    elif verb == "panic":
        ing = "panicking"
    elif verb.endswith("ie"):
        ing = verb[:-2] + "ying"
    elif verb.endswith("e") and not verb.endswith(("ee", "ye", "oe")):
        ing = verb[:-1] + "ing"
    elif verb in DOUBLE:
        ing = verb + verb[-1] + "ing"
    else:
        ing = verb + "ing"
    return [w + rest for w in (verb, past, pp, ing)]


def load():
    verbs, seen = [], set()
    for line in VERBS.strip().splitlines():
        kanji, reading, cls, level, gloss = line.split(" ", 4)
        assert cls in CLASSES and level in ("N5", "N4", "N3") and (kanji, reading) not in seen, line
        assert all("ぁ" <= c <= "ゖ" or c == "ー" or "ァ" <= c <= "ヺ" for c in reading), line
        assert reading.endswith("る") or cls not in ("ru", "suru", "kuru"), line
        seen.add((kanji, reading))
        verbs.append({"k": kanji, "r": reading, "c": cls, "l": int(level[1]), "g": gloss, "e": english(gloss)})
    return verbs


def check_engine(verbs):
    """Compares conjugate.js with the Verb Lab's engine (tools/gen_ja_verbs.py) on every verb either list has."""
    if not shutil.which("node"):
        print("node not found: skipped the engine check")
        return
    import gen_ja_verbs as lab
    cases = [{"k": k, "r": r, "c": c} for k, r, c in lab.VERBS.values()] + [v for v in verbs if v["c"] in lab.CLASS_NAME]
    # Verb Lab key → this page's form id
    same = {"masu": "masu", "masen": "masen", "mashita": "mashita", "masendeshita": "masendeshita", "mashou": "mashou",
            "dict": "dict", "nai": "nai", "ta": "ta", "nakatta": "nakatta", "te": "te", "teiru": "teiru", "tara": "tara",
            "volitional": "volitional", "ba": "ba", "potential": "potential", "passive_ta": "passive_ta",
            "causative_ta": "causative_ta", "caus_pass_ta": "caus_pass_ta"}
    js = os.path.join(os.path.dirname(__file__), "..", "static", "verbs", "conjugate.js")
    script = ("const C = require(process.argv[1]); const vs = JSON.parse(require('fs').readFileSync(0, 'utf8'));"
              "console.log(JSON.stringify(vs.map(v => C.conjugate(v))));")
    out = subprocess.run(["node", "-e", script, os.path.abspath(js)], input=json.dumps(cases), capture_output=True,
                         text=True, check=True).stdout
    bad = 0
    for v, got in zip(cases, json.loads(out)):
        want = lab.forms(v["r"], v["c"])
        for lk, jk in same.items():
            if got.get(jk) is None:
                continue
            if got[jk][0] != want[lk][0]:
                bad += 1
                print(f"  {v['k']} {jk}: page {got[jk][0]} ≠ Verb Lab {want[lk][0]}")
    assert not bad, f"{bad} forms differ from the Verb Lab"
    print(f"engine check: {len(cases)} verbs agree with the Verb Lab")


if __name__ == "__main__":
    verbs = load()
    os.makedirs("static/verbs", exist_ok=True)
    with open("static/verbs/verbs.json", "w", encoding="utf-8") as f:
        f.write("[\n" + ",\n".join(json.dumps(v, ensure_ascii=False, separators=(",", ":")) for v in verbs) + "\n]\n")
    levels = {n: sum(v["l"] == n for v in verbs) for n in (5, 4, 3)}
    print(f"static/verbs/verbs.json: {len(verbs)} verbs (N5 {levels[5]}, N4 {levels[4]}, N3 {levels[3]})")
    check_engine(verbs)
