"""Google Cloud Text-to-Speech for the quiz sentences.

The API key is read from TTS_Key.txt in the repo root (git-ignored) or $GOOGLE_TTS_KEY and is never printed.
Every request is logged to tools/tts_usage.jsonl with its billed character count, so `python3 tools/tts.py usage`
shows how much of the monthly free tier has been used.

    python3 tools/tts.py samples <out_dir>   # small comparison batch of voices (an index.html to listen)
    python3 tools/tts.py usage               # characters used per month and voice tier
    python3 tools/tts.py build <voice> <quiz folder>...   # voice every sentence (skips files that exist)

`build` writes audio/<lang>/<hash>.mp3 and audio/manifest.json, one section per voice:
    {"voices": {"<voice>": {"q": {"<quiz id>#<question index>": file}, "t": {"<sentence as written>": file}}}}
"q" voices a question's sentence with the answer filled in (played after answering); "t" covers guide examples.
"""
import base64, collections, concurrent.futures, datetime, glob, hashlib, html, json, os, re, sys, threading, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "tools", "tts_usage.jsonl")
# Free characters per month (check https://cloud.google.com/text-to-speech/pricing; Google changes these now and then).
FREE = {"Standard": 4_000_000, "Wavenet": 1_000_000, "Neural2": 1_000_000, "Chirp3": 1_000_000}


def key():
    k = os.environ.get("GOOGLE_TTS_KEY")
    if not k:
        with open(os.path.join(ROOT, "TTS_Key.txt"), encoding="utf-8") as f:
            k = f.read().strip()
    return k


def tier(voice):
    return next((t for t in FREE if f"-{t}" in voice), "other")


LEDGER_LOCK = threading.Lock()


def synth(text, voice, out, rate=0.95):
    """Writes an MP3 for text with the given voice (e.g. ja-JP-Neural2-B) and logs the billed characters."""
    lang = "-".join(voice.split("-")[:2])
    body = {"input": {"text": text}, "voice": {"languageCode": lang, "name": voice},
            "audioConfig": {"audioEncoding": "MP3", "speakingRate": rate}}
    if "Chirp3" in voice:  # Chirp 3 HD voices don't take a speaking rate
        del body["audioConfig"]["speakingRate"]
    req = urllib.request.Request(f"https://texttospeech.googleapis.com/v1/text:synthesize?key={key()}",
                                 data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    for attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                audio = base64.b64decode(json.load(r)["audioContent"])
            break
        except urllib.error.HTTPError as e:  # the message never contains the key
            if e.code in (429, 500, 503) and attempt < 7:  # per-minute rate limit or a hiccup: wait and retry
                time.sleep(min(60, 2 ** attempt * 2))
                continue
            raise SystemExit(f"TTS error {e.code}: {e.read().decode()[:300]}")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "wb") as f:
        f.write(audio)
    with LEDGER_LOCK, open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps({"at": datetime.datetime.now().isoformat(timespec="seconds"), "voice": voice,
                            "tier": tier(voice), "chars": len(text), "file": os.path.relpath(out, ROOT)},
                           ensure_ascii=False) + "\n")
    return len(text)


def plain(t):
    """Text as written: {漢字|かんじ} → 漢字, without bold markers."""
    return re.sub(r"\{([^|{}]+)\|[^{}]+\}", r"\1", t).replace("**", "")


def reading(t):
    """Japanese as kana: {漢字|かんじ} → かんじ."""
    return re.sub(r"\{([^|{}]+)\|([^{}]+)\}", r"\2", t).replace("**", "")


def usage():
    rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8")] if os.path.exists(LEDGER) else []
    by = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        b = by[(r["at"][:7], r["tier"])]
        b[0] += r["chars"]; b[1] += 1
    if not by:
        print("No requests logged yet.")
    for (month, t), (chars, n) in sorted(by.items()):
        free = FREE.get(t)
        share = f"{chars / free:.2%} of the free {free:,}" if free else "no free tier known"
        print(f"{month}  {t:9} {n:5} requests  {chars:8,} characters  ({share})")


SAMPLES_JA = [
    "{今日|きょう}は{雨|あめ}が{降|ふ}っているので、{家|いえ}で{本|ほん}を{読|よ}みます。",
    "{駅|えき}に{着|つ}いたら、{電話|でんわ}してください。",
    "{社長|しゃちょう}は{何時|なんじ}にいらっしゃいますか。",
    "{一日中|いちにちじゅう}{何|なに}も{食|た}べなかった。",
]
SAMPLES_ZH = ["我昨天去商店买了一本书。", "你喝咖啡还是喝茶？", "这个问题我已经想了很久了。"]
VOICES_JA = ["ja-JP-Neural2-B", "ja-JP-Neural2-C", "ja-JP-Chirp3-HD-Aoede", "ja-JP-Chirp3-HD-Charon"]
VOICES_ZH = ["cmn-CN-Wavenet-A", "cmn-CN-Wavenet-B", "cmn-CN-Chirp3-HD-Aoede", "cmn-CN-Chirp3-HD-Charon"]


def samples(out):
    rows, total = [], 0
    for i, s in enumerate(SAMPLES_JA):
        for v in VOICES_JA:
            variants = [("kanji", plain(s))] + ([("kana", reading(s))] if i in (0, 3) else [])
            for kind, text in variants:
                f = f"ja{i}_{v}_{kind}.mp3"
                total += synth(text, v, os.path.join(out, f))
                rows.append((plain(s), f"{v} ({kind})", f))
    for i, s in enumerate(SAMPLES_ZH):
        for v in VOICES_ZH:
            f = f"zh{i}_{v}.mp3"
            total += synth(s, v, os.path.join(out, f))
            rows.append((s, v, f))
    page = ["<!doctype html><meta charset=utf-8><title>TTS samples</title>",
            "<style>body{font-family:system-ui;max-width:900px;margin:2em auto;padding:0 16px}"
            "td{padding:4px 10px;border-bottom:1px solid #ddd}h3{margin-top:2em}</style><h1>TTS voice samples</h1>"]
    last = None
    for sent, label, f in rows:
        if sent != last:
            page.append(f"</table><h3>{html.escape(sent)}</h3><table>")
            last = sent
        page.append(f"<tr><td>{html.escape(label)}</td><td><audio controls preload=none src='{f}'></audio></td></tr>")
    page.append("</table>")
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(page))
    print(f"{len(rows)} files, {total:,} characters → {out}/index.html")


AUDIO = os.path.join(ROOT, "audio")
MANIFEST = os.path.join(AUDIO, "manifest.json")


def question_sentence(q):
    """The question's sentence with the answer filled in, or None (ordering, position and passage questions)."""
    if q.get("fixed_order"):
        return None
    if q.get("accept"):
        ans = q["accept"][0]
    elif q.get("options"):
        ans = q["options"][q["answer"]]
    else:
        return None
    lines = [l for l in q["prompt"].split("\n") if l.count("（　）") == 1]
    if len(lines) != 1 or "［" in lines[0]:
        return None
    s = plain(lines[0].replace("（　）", ans)).strip()
    s = re.sub(r"[AB]：", "", s).strip()  # dialogue: voice the speech without the speaker labels
    return s or None


def load_manifest():
    m = json.load(open(MANIFEST, encoding="utf-8")) if os.path.exists(MANIFEST) else {}
    if "q" in m:  # first version had a single voice
        m = {"voices": {"ja-JP-Chirp3-HD-Charon": m}}
    m.setdefault("voices", {})
    return m


def build(voice, folders, workers=3):
    lang = voice.split("-")[0]
    manifest = load_manifest()
    section = manifest["voices"].setdefault(voice, {"q": {}, "t": {}})
    todo = {}  # file → text, voiced in parallel below

    def file_for(text):
        h = hashlib.sha1(f"{voice}|{text}".encode()).hexdigest()[:16]
        rel = f"{lang}/{h}.mp3"
        if not os.path.exists(os.path.join(AUDIO, rel)):
            todo[rel] = text
        return rel

    for folder in folders:
        for path in sorted(glob.glob(os.path.join(ROOT, folder, "*.json"))):
            d = json.load(open(path, encoding="utf-8"))
            if d.get("language", "ja") != lang:
                continue
            for i, q in enumerate(d["questions"]):
                s = question_sentence(q)
                if s:
                    section["q"][f"{d['id']}#{i}"] = file_for(s)
            for p in d.get("points", []):
                for ex in p.get("examples", []):
                    section["t"][plain(ex[0])] = file_for(plain(ex[0]))
    print(f"{voice}: {len(todo)} sentences to voice ({sum(map(len, todo.values())):,} characters)")
    chars = done = 0
    with concurrent.futures.ThreadPoolExecutor(workers) as pool:
        jobs = [pool.submit(synth, text, voice, os.path.join(AUDIO, rel)) for rel, text in todo.items()]
        for job in concurrent.futures.as_completed(jobs):
            chars += job.result()
            done += 1
            if done % 100 == 0:
                print(f"  … {done} of {len(todo)}")
    os.makedirs(AUDIO, exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=0, sort_keys=True)
    print(f"{done} new files ({chars:,} characters); {voice}: {len(section['q'])} questions, "
          f"{len(section['t'])} example sentences")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "usage"
    if cmd == "samples":
        samples(sys.argv[2])
    elif cmd == "build":
        build(sys.argv[2], sys.argv[3:])
    else:
        usage()
