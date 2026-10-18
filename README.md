# 文法 Grammar Practice

Multiple-choice grammar quizzes for Japanese (JLPT N5–N2) and Mandarin (A1–B2), modelled on the Meiji Academy placement test. It runs as a small Rust web server, or as a static site on GitHub Pages.

## Run

```sh
cargo run --release
# then open http://127.0.0.1:3000
```

Set `PORT=8080` to use another port, or `QUIZ_DIR=/path` to load quizzes from elsewhere.
By default only this computer can connect; `HOST=:: cargo run --release` listens on all interfaces (needed for IPv6 hosting).

## Static site (GitHub Pages)

The same site can be exported as plain files, with no server:

```sh
cargo run --release -- export site
# try it locally:
cd site && python3 -m http.server 8000   # then open http://127.0.0.1:8000
```

The export validates every quiz like the server does. It writes the pages plus each quiz as JSON under `site/data/`; Mandarin quizzes also get a `.trad.json` with traditional characters. In the exported `index.html`, `window.QUIZ_STATIC = true` switches `app.js` to answering the API itself in the browser: checking answers, the no-repeat ordering, and the random mix. Links are relative, so the site also works under a sub-path like `user.github.io/repo/`.

The difference from the server is that the answers are in the JSON files, so anyone opening the developer tools could see them.

`.github/workflows/pages.yml` runs the export on every push to `main` and publishes it. One-time setup: push the repository to GitHub, then under **Settings → Pages** set the source to **GitHub Actions**.

## Features

- 10 themed quizzes plus a **Random mix** of 20 questions drawn from all of them
- After each answer: why *your* choice is wrong, the grammar point, and a translation
- Answer order is shuffled each time; furigana can be toggled on and off
- Results page lists your mistakes, with a **Retry my mistakes** button; best scores are saved in the browser
- Keyboard: `A`–`D` / `1`–`4` to answer, `0` for わかりません, `Enter` for next
- **Verb Lab**: typed answers. You type the verb form yourself (kana, kanji or romaji, which turns into hiragana as you type). A **Hint** shows the first kana, and the answer then counts as "with hint".
- **Review (spaced repetition)**: every first answer moves the question between Leitner boxes (due again after 0, 1, 3, 7, 14 or 30 days). Wrong answers and answers given with a hint start over. When questions are due, the home page offers a review session of up to 20 of them.

## Account & sync (optional)

Signing in (GitHub or an email link, through Supabase) syncs best scores, the review schedule and an unfinished quiz across devices. Without signing in, everything stays in the browser's localStorage. The page talks to Supabase directly, so this works on GitHub Pages and with the Rust server alike.

- Project URL and publishable key are at the top of the sync section in `static/app.js`. Both are public by design.
- The table and its row-level-security rules are in `supabase/schema.sql`; run it once in the Supabase SQL editor.
- Merging: best scores keep the higher value, review items keep the most recent answer, and the newer unfinished quiz wins.

## Adding quizzes

Drop a JSON file anywhere under `quizzes/`. Subfolders are allowed, and files load in path order (`01_n5/` before `90_mixed/`). Restart the server to pick up changes; no recompile is needed.

```json
{
  "id": "unique-id",
  "category": "JLPT N5",
  "title": "Title",
  "description": "Short description",
  "level": "N5",
  "points": [
    {
      "id": "de-place",
      "title": "で: place of action",
      "summary": "One-line summary shown in the collapsed guide.",
      "body": "Full explanation. A blank line starts a new paragraph.\n\n- lines starting with '- ' become bullets",
      "examples": [["{図書館|としょかん}で{勉強|べんきょう}します。", "I study at the library."]]
    }
  ],
  "questions": [
    {
      "point": "de-place",
      "prompt": "{図書館|としょかん}（　）{勉強|べんきょう}します。",
      "options": ["に", "で", "を", "へ"],
      "answer": 1,
      "explanation": "Why the correct answer is right. **bold** is supported.",
      "notes": ["why に is wrong", "", "why を is wrong", "why へ is wrong"],
      "translation": "I study at the library."
    }
  ]
}
```

- `{漢字|かんじ}` renders as furigana.
- `answer` is the 0-based index of the correct option.
- `notes` holds one entry per option, with an empty string for the correct one.
- `points` and `point` are optional. When a question has a `point`, its full guide appears in the feedback and on the quiz's study page.
- `category` groups quizzes into sections on the home page.
- `language` is `"ja"` (the default) or `"zh"`. The home page shows one language at a time, and for Mandarin the reading aid becomes pinyin: `{汉字|hànzì}`.
- `"fixed_order": true` on a question keeps its options in the given order. Use it for position questions whose options are the markers A–D in the sentence.
- **Typed questions**: leave `options` empty and list every accepted spelling in `"accept": ["起きます", "おきます"]`. The optional `"hint"` is shown on request. Answers are compared after removing spaces and punctuation, with katakana treated as hiragana.
- `"keep_order": true` on a quiz asks its questions in file order instead of shuffling them (used for the conjugation ladders). A `hint` ending in `…` is shown as "Starts with …"; any other hint is shown as-is (e.g. a rule).
- `tools/gen_ja_verbs.py` generates the Verb Lab (`quizzes/06_verbs/`). It has a small conjugation engine covering る/う-verbs, する and 来る, keigo special verbs and the regular お〜になる / お〜する patterns. Step 1 teaches how to recognise る-verbs, う-verbs and the irregular verbs, including the う-verb exceptions that end in -iる / -eる and lookalike pairs. Step 2 has drills: back to the dictionary form, て/ない sprints and ladders. Step 3 has forms in context. The accepted answers, hints and "how it's formed" explanations are all derived from it.
- Write Mandarin quizzes in simplified characters. The server converts them to traditional at startup (crate `zhconv`), and the 简/繁 switch picks the version through `script=simp|trad`.
- `tools/gen_zh_a1.py`, `gen_zh_a2.py`, `gen_zh_b1.py` and `gen_zh_b2.py` generate the Mandarin quizzes from a compact `汉字/pīnyīn` notation, using the helpers in `tools/zhquiz.py`. The helpers include HSK formats (true/false, reading, A/B/C ordering). Run them from the repo root.
