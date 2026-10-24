"""Generates the Verb Lab (quizzes/06_verbs): typed-answer drills of Japanese verb forms in everyday scenarios.

Each question is a sentence with a gap, a verb and a target form. This script conjugates the verb, so the
accepted answers (kanji and kana), the hint (first kana) and the explanation of the rule always match.
Run from the repo root.
"""
import collections, json, os

# ---------------------------------------------------------------- verbs
# key: (dictionary form, reading, class) — class: ru (ichidan), u (godan), iku, aru, suru, kuru
VERBS = {k: v for k, v in {
    "起きる": ("起きる", "おきる", "ru"), "見る": ("見る", "みる", "ru"), "食べる": ("食べる", "たべる", "ru"),
    "寝る": ("寝る", "ねる", "ru"), "出る": ("出る", "でる", "ru"), "出かける": ("出かける", "でかける", "ru"),
    "建てる": ("建てる", "たてる", "ru"), "開ける": ("開ける", "あける", "ru"), "いる": ("いる", "いる", "ru"),
    "行く": ("行く", "いく", "iku"), "来る": ("来る", "くる", "kuru"), "する": ("する", "する", "suru"),
    "ある": ("ある", "ある", "aru"),
    "飲む": ("飲む", "のむ", "u"), "話す": ("話す", "はなす", "u"), "聞く": ("聞く", "きく", "u"), "吸う": ("吸う", "すう", "u"),
    "引っ越す": ("引っ越す", "ひっこす", "u"), "歩く": ("歩く", "あるく", "u"), "休む": ("休む", "やすむ", "u"),
    "会う": ("会う", "あう", "u"), "帰る": ("帰る", "かえる", "u"), "言う": ("言う", "いう", "u"), "曲がる": ("曲がる", "まがる", "u"),
    "切る": ("切る", "きる", "u"), "割る": ("割る", "わる", "u"), "書く": ("書く", "かく", "u"), "待つ": ("待つ", "まつ", "u"),
    "働く": ("働く", "はたらく", "u"), "撮る": ("撮る", "とる", "u"), "押す": ("押す", "おす", "u"), "遊ぶ": ("遊ぶ", "あそぶ", "u"),
    "読む": ("読む", "よむ", "u"), "使う": ("使う", "つかう", "u"), "走る": ("走る", "はしる", "u"), "作る": ("作る", "つくる", "u"),
    "泳ぐ": ("泳ぐ", "およぐ", "u"), "飼う": ("飼う", "かう", "u"), "着く": ("着く", "つく", "u"), "降る": ("降る", "ふる", "u"),
    "当たる": ("当たる", "あたる", "u"), "返す": ("返す", "かえす", "u"), "踏む": ("踏む", "ふむ", "u"), "叱る": ("叱る", "しかる", "u"),
    "盗む": ("盗む", "ぬすむ", "u"), "歌う": ("歌う", "うたう", "u"), "呼ぶ": ("呼ぶ", "よぶ", "u"), "止む": ("止む", "やむ", "u"),
    "持つ": ("持つ", "もつ", "u"),
    "勉強する": ("勉強する", "べんきょうする", "suru"), "掃除する": ("掃除する", "そうじする", "suru"),
    "練習する": ("練習する", "れんしゅうする", "suru"), "案内する": ("案内する", "あんないする", "suru"),
    "電話する": ("電話する", "でんわする", "suru"),
    "着る": ("着る", "きる", "ru"), "変える": ("変える", "かえる", "ru"), "入れる": ("入れる", "いれる", "ru"),
    "覚える": ("覚える", "おぼえる", "ru"), "教える": ("教える", "おしえる", "ru"), "借りる": ("借りる", "かりる", "ru"),
    "降りる": ("降りる", "おりる", "ru"), "浴びる": ("浴びる", "あびる", "ru"), "忘れる": ("忘れる", "わすれる", "ru"),
    "生きる": ("生きる", "いきる", "ru"), "信じる": ("信じる", "しんじる", "ru"), "見せる": ("見せる", "みせる", "ru"),
    "閉める": ("閉める", "しめる", "ru"), "足りる": ("足りる", "たりる", "ru"),
    "要る": ("要る", "いる", "u"), "入る": ("入る", "はいる", "u"), "知る": ("知る", "しる", "u"), "限る": ("限る", "かぎる", "u"),
    "喋る": ("喋る", "しゃべる", "u"), "滑る": ("滑る", "すべる", "u"), "焦る": ("焦る", "あせる", "u"), "減る": ("減る", "へる", "u"),
    "蹴る": ("蹴る", "ける", "u"), "握る": ("握る", "にぎる", "u"), "散る": ("散る", "ちる", "u"),
    "分かる": ("分かる", "わかる", "u"), "乗る": ("乗る", "のる", "u"), "取る": ("取る", "とる", "u"), "座る": ("座る", "すわる", "u"),
    "終わる": ("終わる", "おわる", "u"), "死ぬ": ("死ぬ", "しぬ", "u"), "買う": ("買う", "かう", "u"), "洗う": ("洗う", "あらう", "u"),
    "立つ": ("立つ", "たつ", "u"), "急ぐ": ("急ぐ", "いそぐ", "u"), "貸す": ("貸す", "かす", "u"), "脱ぐ": ("脱ぐ", "ぬぐ", "u"),
    "運転する": ("運転する", "うんてんする", "suru"),
}.items()}

GLOSS = {
    "切る": "cut", "着る": "wear", "帰る": "go home", "変える": "change", "要る": "need", "いる": "be (people)",
    "入る": "enter", "入れる": "put in", "知る": "know", "走る": "run", "寝る": "sleep", "喋る": "chat", "滑る": "slip",
    "焦る": "rush, panic", "減る": "decrease", "蹴る": "kick", "握る": "grip", "限る": "limit", "散る": "scatter",
    "降りる": "get off", "浴びる": "take (a shower)", "信じる": "believe", "生きる": "live", "借りる": "borrow",
    "覚える": "remember", "教える": "teach", "忘れる": "forget", "見せる": "show", "閉める": "close", "足りる": "be enough",
    "分かる": "understand", "乗る": "ride", "取る": "take", "座る": "sit", "作る": "make", "書く": "write", "話す": "speak",
    "待つ": "wait", "死ぬ": "die", "遊ぶ": "play", "泳ぐ": "swim", "買う": "buy", "食べる": "eat", "見る": "see",
    "起きる": "get up", "する": "do", "来る": "come", "勉強する": "study", "運転する": "drive", "ある": "be (things)",
    "飲む": "drink", "読む": "read", "行く": "go", "終わる": "end", "洗う": "wash", "立つ": "stand", "急ぐ": "hurry",
    "貸す": "lend", "脱ぐ": "take off", "出る": "leave", "開ける": "open",
}

# Adjectives: (kanji, reading, kind) — kind: i, ii (いい and compounds), na
ADJ = {
    "高い": ("高い", "たかい", "i"), "安い": ("安い", "やすい", "i"), "新しい": ("新しい", "あたらしい", "i"),
    "古い": ("古い", "ふるい", "i"), "暑い": ("暑い", "あつい", "i"), "寒い": ("寒い", "さむい", "i"),
    "忙しい": ("忙しい", "いそがしい", "i"), "楽しい": ("楽しい", "たのしい", "i"), "難しい": ("難しい", "むずかしい", "i"),
    "おいしい": ("おいしい", "おいしい", "i"), "大きい": ("大きい", "おおきい", "i"), "小さい": ("小さい", "ちいさい", "i"),
    "面白い": ("面白い", "おもしろい", "i"), "暗い": ("暗い", "くらい", "i"), "優しい": ("優しい", "やさしい", "i"),
    "眠い": ("眠い", "ねむい", "i"), "早い": ("早い", "はやい", "i"), "痛い": ("痛い", "いたい", "i"),
    "いい": ("いい", "いい", "ii"), "かっこいい": ("かっこいい", "かっこいい", "ii"),
    "静か": ("静か", "しずか", "na"), "きれい": ("きれい", "きれい", "na"), "有名": ("有名", "ゆうめい", "na"),
    "便利": ("便利", "べんり", "na"), "元気": ("元気", "げんき", "na"), "好き": ("好き", "すき", "na"),
    "嫌い": ("嫌い", "きらい", "na"), "大変": ("大変", "たいへん", "na"), "簡単": ("簡単", "かんたん", "na"),
    "上手": ("上手", "じょうず", "na"), "下手": ("下手", "へた", "na"), "暇": ("暇", "ひま", "na"),
    "親切": ("親切", "しんせつ", "na"), "丁寧": ("丁寧", "ていねい", "na"), "大切": ("大切", "たいせつ", "na"),
}
LEX = collections.ChainMap(VERBS, ADJ)

ROW = {"う": "わいうえお", "く": "かきくけこ", "ぐ": "がぎぐげご", "す": "さしすせそ", "つ": "たちつてと",
       "ぬ": "なにぬねの", "ぶ": "ばびぶべぼ", "む": "まみむめも", "る": "らりるれろ"}
A, I, E, O = 0, 1, 3, 4


def shift(r, col):
    """Godan: change the last kana to another row (書く → 書か / 書き / 書け / 書こ)."""
    return r[:-1] + ROW[r[-1]][col]


VOWEL = {c: v for v, row in zip("aiueo", ["あかさたなはまやらわがざだばぱ", "いきしちにひみりぎじぢびぴ",
         "うくすつぬふむゆるぐずづぶぷ", "えけせてねへめれげぜでべぺ", "おこそとのほもよろごぞどぼぽ"]) for c in row}


def is_exception(key):
    """う-verbs that look like る-verbs: -iる / -eる (帰る, 切る, 入る …)."""
    _, r, cls = VERBS[key]
    return cls == "u" and r[-1] == "る" and VOWEL[r[-2]] in "ie"


def te(r, cls, ta=False):
    t, d = ("た", "だ") if ta else ("て", "で")
    if cls == "ru": return r[:-1] + t
    if cls == "suru": return r[:-2] + "し" + t
    if cls == "kuru": return "き" + t
    if cls == "iku": return r[:-1] + "っ" + t
    last = r[-1]
    if last in "うつる": return r[:-1] + "っ" + t
    if last in "ぬぶむ": return r[:-1] + "ん" + d
    if last == "く": return r[:-1] + "い" + t
    if last == "ぐ": return r[:-1] + "い" + d
    if last == "す": return r[:-1] + "し" + t
    raise ValueError(r)


def masu_stem(r, cls):
    if cls == "ru": return r[:-1]
    if cls == "suru": return r[:-2] + "し"
    if cls == "kuru": return "き"
    return shift(r, I)


def nai_stem(r, cls):
    if cls == "ru": return r[:-1]
    if cls == "suru": return r[:-2] + "し"
    if cls == "kuru": return "こ"
    if cls == "aru": return ""
    return shift(r, A)


def forms(r, cls):
    """Every plain kana form the drills use. Values are lists: first is the main answer, others are also accepted."""
    ms, ns = masu_stem(r, cls), nai_stem(r, cls)
    nai = "ない" if cls == "aru" else ns + "ない"
    f = {
        "masu": [ms + "ます"], "masen": [ms + "ません"], "mashita": [ms + "ました"],
        "masendeshita": [ms + "ませんでした"], "mashou": [ms + "ましょう"],
        "dict": [r], "nai": [nai], "ta": [te(r, cls, True)], "nakatta": [nai[:-1] + "かった"],
        "te": [te(r, cls)], "teiru": [te(r, cls) + "いる"], "teimasu": [te(r, cls) + "います"],
        "tekudasai": [te(r, cls) + "ください"], "temoii": [te(r, cls) + "もいい"], "tewaikenai": [te(r, cls) + "はいけない"],
        "tara": [te(r, cls, True) + "ら"], "tearu": [te(r, cls) + "ある"],
    }
    if cls == "ru": pot, vol, ba, pas, cau = r[:-1] + "られる", r[:-1] + "よう", r[:-1] + "れば", r[:-1] + "られる", r[:-1] + "させる"
    elif cls == "suru": p = r[:-2]; pot, vol, ba, pas, cau = p + "できる", p + "しよう", p + "すれば", p + "される", p + "させる"
    elif cls == "kuru": pot, vol, ba, pas, cau = "こられる", "こよう", "くれば", "こられる", "こさせる"
    else: pot, vol, ba, pas, cau = shift(r, E) + "る", shift(r, O) + "う", shift(r, E) + "ば", shift(r, A) + "れる", shift(r, A) + "せる"
    f.update({
        "potential": [pot], "potential_masu": [pot[:-1] + "ます"], "potential_masen": [pot[:-1] + "ません"],
        "volitional": [vol], "ba": [ba],
        "nakereba": [nai[:-1] + e for e in ("ければならない", "ければいけない", "くてはならない", "くてはいけない")] + [nai + "といけない"],
        "passive_ta": [pas[:-1] + "た"], "passive_teiru": [pas[:-1] + "ている"],
        "causative_ta": [cau[:-1] + "た"],
    })
    cp = [cau[:-1] + "られた"]
    if cls in ("u", "iku") and r[-1] != "す":
        cp.insert(0, shift(r, A) + "された")  # short form 飲まされた is the usual one
    f["caus_pass_ta"] = cp
    return f


# Special keigo verbs: polite present (kanji, kana). Past forms replace ます with ました.
HONORIFIC = {
    "来る": [("いらっしゃいます", "いらっしゃいます"), ("お見えになります", "おみえになります"), ("おいでになります", "おいでになります")],
    "行く": [("いらっしゃいます", "いらっしゃいます"), ("おいでになります", "おいでになります")],
    "いる": [("いらっしゃいます", "いらっしゃいます")],
    "食べる": [("召し上がります", "めしあがります")], "飲む": [("召し上がります", "めしあがります")],
    "言う": [("おっしゃいます", "おっしゃいます")], "見る": [("ご覧になります", "ごらんになります")],
    "する": [("なさいます", "なさいます")],
}
HUMBLE = {
    "行く": [("参ります", "まいります"), ("伺います", "うかがいます")], "来る": [("参ります", "まいります")],
    "言う": [("申します", "もうします")], "見る": [("拝見します", "はいけんします")], "する": [("いたします", "いたします")],
    "会う": [("お目にかかります", "おめにかかります"), ("お会いします", "おあいします")],
    "食べる": [("いただきます", "いただきます")], "飲む": [("いただきます", "いただきます")], "いる": [("おります", "おります")],
}


def okuri(kanji, reading):
    """Shared kana ending of the dictionary form, e.g. 食べる / たべる → 'べる'."""
    n = 0
    while n < min(len(kanji), len(reading)) and kanji[-1 - n] == reading[-1 - n]:
        n += 1
    return n


def to_kanji(kana, key):
    kanji, reading, cls = LEX[key]
    if kanji == reading:
        return kana
    if cls == "kuru":
        return "来" + kana[1:] if kana[:1] in "きくこ" else kana
    n = okuri(kanji, reading)
    kp, rp = kanji[:len(kanji) - n], reading[:len(reading) - n]
    return kp + kana[len(rp):] if kana.startswith(rp) else kana


def ruby(key):
    kanji, reading, _ = LEX[key]
    if kanji == reading:
        return kanji
    n = okuri(kanji, reading)
    return "{" + kanji[:len(kanji) - n] + "|" + reading[:len(reading) - n] + "}" + kanji[len(kanji) - n:]


def keigo(key, form):
    """(accepted answers, explanation) for hon / hon_ta / hum / hum_ta."""
    kanji, reading, cls = VERBS[key]
    past = form.endswith("_ta")
    table = HONORIFIC if form.startswith("hon") else HUMBLE
    adj = (lambda s: s[:-2] + "ました") if past else (lambda s: s)
    if key in table:
        pairs = table[key]
        ans = [adj(x) for p in pairs for x in p]
        kind = "honorific" if form.startswith("hon") else "humble"
        why = f"{ruby(key)} has a special {kind} verb: **{adj(pairs[0][0])}**."
        if len(pairs) > 1:
            why += " (" + " / ".join(adj(p[0]) for p in pairs[1:]) + " also work.)"
        return ans, why
    if cls == "suru":  # noun + する: ご〜します / お電話します
        noun_k, noun_r = kanji[:-2], reading[:-2]
        pre = "お" if noun_k == "電話" else "ご"
        if form.startswith("hon"):
            ans = [adj(pre + noun_k + "になります"), adj(pre + noun_r + "になります"), adj(noun_k + "なさいます")]
            return ans, f"する-noun, honorific: **{pre} + {noun_k} + になります** (or {noun_k}なさいます)."
        ans = [adj(pre + noun_k + "します"), adj(pre + noun_r + "します"), adj(pre + noun_k + "いたします"), adj(pre + noun_r + "いたします")]
        return ans, f"する-noun, humble: **{pre} + {noun_k} + します** (more humble: いたします)."
    stem_r = masu_stem(reading, cls)
    stem_k = to_kanji(stem_r + "ます", key)[:-2]
    if form.startswith("hon"):
        ans = [adj("お" + stem_k + "になります"), adj("お" + stem_r + "になります")]
        return ans, f"Regular honorific: **お + ます-stem ({stem_k}) + になります**."
    ans = [adj("お" + stem_k + "します"), adj("お" + stem_r + "します"), adj("お" + stem_k + "いたします"), adj("お" + stem_r + "いたします")]
    return ans, f"Regular humble: **お + ます-stem ({stem_k}) + します** (more humble: いたします)."


LABEL = {
    "masu": "polite present", "masen": "polite negative", "mashita": "polite past", "masendeshita": "polite past negative",
    "mashou": "polite 'let's'", "dict": "plain present", "nai": "plain negative", "ta": "plain past",
    "nakatta": "plain past negative", "te": "て-form", "teiru": "て-form + いる", "teimasu": "て-form + います",
    "tekudasai": "please do … (てください)", "temoii": "may … (てもいい)", "tewaikenai": "must not … (てはいけない)",
    "potential": "can … (plain)", "potential_masu": "can … (polite)", "potential_masen": "can't … (polite)",
    "tearu": "て-form + ある", "volitional": "let's / I'll … (plain volitional)", "ba": "if … (ば-form)", "tara": "if / when … (たら)",
    "nakereba": "must … (なければならない)", "passive_ta": "passive, past", "passive_teiru": "passive + ている",
    "causative_ta": "causative (make / let), past", "caus_pass_ta": "causative-passive (was made to), past",
    "hon": "honorific (polite)", "hon_ta": "honorific, past", "hum": "humble (polite)", "hum_ta": "humble, past",
}

CLASS_NAME = {"ru": "a る-verb (ichidan)", "u": "an う-verb (godan)", "iku": "an う-verb (godan) — with one exception",
              "aru": "an う-verb (godan) with an irregular negative", "suru": "irregular (する)", "kuru": "irregular (来る)"}


def explain(key, form, answer):
    why = _explain(key, form, answer)
    if is_exception(key):
        why += f" ⚠ {ruby(key)} ends in -{VOWEL[VERBS[key][1][-2]]}る like a る-verb, but it is one of the う-verb exceptions."
    return why


def _explain(key, form, answer):
    kanji, reading, cls = VERBS[key]
    v = ruby(key)
    ans = f"**{answer}**"
    if cls == "suru":
        return f"{v} is {CLASS_NAME[cls]}: する → " + {
            "potential": "できる", "potential_masu": "できます", "potential_masen": "できません", "volitional": "しよう", "ba": "すれば",
            "passive_ta": "された", "passive_teiru": "されている", "causative_ta": "させた", "caus_pass_ta": "させられた",
        }.get(form, "し + ending") + f" → {ans}."
    if cls == "kuru":
        return f"{v} is {CLASS_NAME[cls]}: the vowel changes — き(ます/て/た), こ(ない/よう/られる/させる), く(る/れば) → {ans}."
    last = reading[-1]
    if form == "dict":
        return f"Plain present = the dictionary form itself: {ans}. Casual speech just drops ます."
    if form in ("masu", "masen", "mashita", "masendeshita", "mashou"):
        how = "drop る" if cls == "ru" else f"{last} → {shift(reading, I)[-1]} (い-row)"
        return f"{v} is {CLASS_NAME[cls]}: {how} for the ます-stem, then add the ending → {ans}."
    if form in ("nai", "nakatta", "nakereba"):
        if cls == "aru":
            return f"ある is irregular in the negative: ない (not あらない) → {ans}."
        how = "drop る" if cls == "ru" else f"{last} → {shift(reading, A)[-1]} (あ-row{', う becomes わ' if last == 'う' else ''})"
        tail = {"nai": "+ ない", "nakatta": "+ なかった", "nakereba": "+ なければならない"}[form]
        return f"{v} is {CLASS_NAME[cls]}: {how} {tail} → {ans}."
    if form in ("te", "ta", "teiru", "teimasu", "tekudasai", "temoii", "tewaikenai", "tara", "tearu"):
        if cls == "ru":
            how = "drop る + て / た"
        elif cls == "iku":
            how = "行く is the exception: 行って / 行った (not 行いて)"
        else:
            how = {"う": "う・つ・る → って", "つ": "う・つ・る → って", "る": "う・つ・る → って", "ぬ": "ぬ・ぶ・む → んで",
                   "ぶ": "ぬ・ぶ・む → んで", "む": "ぬ・ぶ・む → んで", "く": "く → いて", "ぐ": "ぐ → いで", "す": "す → して"}[last]
        rest = {"teiru": " + いる", "teimasu": " + います", "tekudasai": " + ください", "temoii": " + もいい",
                "tewaikenai": " + はいけない", "tara": " (た-form) + ら", "tearu": " + ある"}.get(form, "")
        return f"{v} is {CLASS_NAME[cls]}: {how}{rest} → {ans}."
    fk = forms(reading, cls)
    step = lambda f, tail: to_kanji(fk[f][0][:-len(tail)] + "る", key) if tail else ""  # the derived verb's dictionary form
    if form.startswith("potential"):
        how = "drop る + られる" if cls == "ru" else f"{last} → {shift(reading, E)[-1]} (え-row) + る"
        pot = to_kanji(fk["potential"][0], key)
        then = {"potential": "", "potential_masu": " It's a る-verb now, so polite: drop る + ます",
                "potential_masen": " It's a る-verb now, so polite negative: drop る + ません"}[form]
        same = " (For る-verbs this looks like the passive — context tells you which.)" if cls in ("ru", "kuru") else ""
        if not then:
            return f"{v} is {CLASS_NAME[cls]}: {how} → {ans} ('can …'; it conjugates like a る-verb from here).{same}"
        return f"{v} is {CLASS_NAME[cls]}: {how} → {pot} ('can …').{then} → {ans}.{same}"
    if form == "volitional":
        how = "drop る + よう" if cls == "ru" else f"{last} → {shift(reading, O)[-1]} (お-row) + う"
        return f"{v} is {CLASS_NAME[cls]}: {how} → {ans} (plain 'let's / I'll'; polite: ましょう)."
    if form == "ba":
        how = "drop る + れば" if cls == "ru" else f"{last} → {shift(reading, E)[-1]} (え-row) + ば"
        return f"{v} is {CLASS_NAME[cls]}: {how} → {ans}."
    if form.startswith("passive"):
        how = "drop る + られる" if cls == "ru" else f"{last} → {shift(reading, A)[-1]} (あ-row) + れる"
        tail = "た" if form == "passive_ta" else "ている"
        then = "past: drop る + た" if tail == "た" else "drop る + ている (ongoing / generally)"
        return f"Passive: {v} is {CLASS_NAME[cls]}: {how} → {step(form, tail)}, then like a る-verb, {then} → {ans}."
    if form == "causative_ta":
        how = "drop る + させる" if cls == "ru" else f"{last} → {shift(reading, A)[-1]} (あ-row) + せる"
        return f"Causative: {v} is {CLASS_NAME[cls]}: {how} → {step(form, 'た')}, then past: drop る + た → {ans}."
    if form == "caus_pass_ta":
        how = "drop る + させられる" if cls == "ru" else f"{last} → {shift(reading, A)[-1]} (あ-row) + される (short form; せられる also works)"
        return f"Causative-passive: {v} is {CLASS_NAME[cls]}: {how} → {step(form, 'た')}, then past: drop る + た → {ans}."
    raise ValueError(form)


CONFUSABLE = ["dict", "nai", "ta", "nakatta", "te", "teiru", "masu", "masen", "mashita", "mashou", "potential",
              "potential_masu", "volitional", "ba", "tara", "passive_ta", "causative_ta"]


def wrong_forms(key, form, accept):
    """Typed answers that are a real form of the verb, just not the asked one (or the wrong verb class's pattern),
    mapped to a note: the server shows it after 'You wrote …'."""
    if form.startswith("a_"):
        return adj_wrong_forms(key, form, accept)
    kanji, r, cls = VERBS[key]
    fk = forms(r, cls)
    taken = set(accept)
    labels = collections.defaultdict(list)
    for f in CONFUSABLE:
        if f != form and fk[f][0] not in taken:
            labels[fk[f][0]].append(LABEL[f])
    out = {}
    for kana, names in labels.items():
        note = f"that's the {' / '.join(names)} form of {kanji}, but the cue asks for {LABEL[form]}."
        out[kana] = out[to_kanji(kana, key)] = note
    # ら-less potential (見れる, 来れる): common in speech, but not the standard form
    if form.startswith("potential") and cls in ("ru", "kuru"):
        stem = r[:-1] if cls == "ru" else "こ"
        tail = {"potential": "れる", "potential_masu": "れます", "potential_masen": "れません"}[form]
        kana = stem + tail
        if kana not in taken:
            note = (f"that's the casual 'ら-less' form — you'll hear it a lot, but the standard (and exam) form keeps ら: "
                    f"{accept[0]}.")
            out[kana] = out[to_kanji(kana, key)] = note
    # the other verb class's pattern: 帰ない for 帰る, 食べらない for 食べる
    if form in fk and r.endswith("る") and cls in ("ru", "u"):
        other = "u" if cls == "ru" else "ru"
        for kana in forms(r, other)[form][:1]:
            if kana not in taken and kana not in out:
                note = (f"that's the う-verb pattern, but {kanji} is a る-verb: just drop る." if cls == "ru" else
                        f"that's the る-verb pattern, but {kanji} is an う-verb" + (" (one of the -iる/-eる exceptions)." if is_exception(key) else "."))
                out[kana] = out[to_kanji(kana, key)] = note
    return out


def build(key, form):
    """(accepted answers, explanation, hint) for a verb and a target form."""
    if form.startswith("a_"):
        return adj_build(key, form)
    if form in ("hon", "hon_ta", "hum", "hum_ta"):
        accept, why = keigo(key, form)
        accept = list(dict.fromkeys(accept))
    else:
        kana = forms(VERBS[key][1], VERBS[key][2])[form]
        accept = []
        for k in kana:
            for a in (to_kanji(k, key), k):
                if a not in accept:
                    accept.append(a)
        why = explain(key, form, accept[0])
    kana_main = next((a for a in accept if all("぀" <= c <= "ゟ" for c in a)), accept[-1])
    # Hint: the unchanged part of the verb plus the first kana that changes (歩く → 歩き…, 行く → 行っ…),
    # so it points at the conjugation instead of giving away the verb's own first kana.
    reading = VERBS[key][1]
    n = 0
    while n < min(len(kana_main), len(reading)) and kana_main[n] == reading[n]:
        n += 1
    hint = kana_main[:max(1, min(n + 1, len(kana_main) - 1))]  # never the whole answer
    keigo_form = form in ("hon", "hon_ta", "hum", "hum_ta")
    if keigo_form and hint in ("お", "ご"):  # regular keigo: お/ご + first kana of the stem
        hint = kana_main[:2]
    return accept, why, (to_kanji(hint, key) if n and not keigo_form else hint) + "…"


# ---------------------------------------------------------------- quizzes
QZ = {}

# Focused explanation per grammar point: (summary, body). The guide's overview is appended below the body.
POINT_BODY = {
    "pot-u": ("う-verbs: the last sound moves to the え-row, then add る.",
              "- 書く → 書**け**る, 読む → 読**め**る, 話す → 話**せ**る, 待つ → 待**て**る, 買う → 買**え**る\n- The exceptions that look like る-verbs work the same: 帰る → 帰**れ**る, 走る → 走**れ**る."),
    "pot-ru": ("る-verbs: drop る and add られる.",
               "- 食べる → 食べ**られる**, 見る → 見**られる**, 起きる → 起き**られる**\n- Same shape as the passive (食べられる = can eat / is eaten): the sentence tells you which.\n- Casual speech often drops the ら (食べれる). Understand it, but write 食べられる."),
    "pot-irr": ("する → できる, 来る → 来(こ)られる.", "- 勉強する → 勉強**できる**, 運転する → 運転**できる**\n- 来る → **こ**られる (casual: これる)"),
    "can-yes": ("Polite 'can': the potential is a る-verb, so drop る + ます.",
                "- 話せる → 話せ**ます**, できる → でき**ます**, 来られる → 来られ**ます**\n- What you can do usually takes が: 日本語**が**話せます."),
    "can-no": ("Polite 'can't': drop る + ません.",
               "- 読める → 読め**ません**, 寝られる → 寝られ**ません**\n- Also for rules and impossibility: ここでは泳げません (you can't swim here), この水は飲めません."),
    "vol-u": ("う-verbs: the last sound moves to the お-row, then add う.",
              "- 書く → 書**こう**, 読む → 読**もう**, 話す → 話**そう**, 待つ → 待**とう**, 買う → 買**おう**, 行く → 行**こう**"),
    "vol-ru": ("る-verbs: drop る and add よう.", "- 食べる → 食べ**よう**, 見る → 見**よう**, 寝る → 寝**よう**, 始める → 始め**よう**"),
    "vol-irr": ("する → しよう, 来る → 来(こ)よう.", "- 散歩する → 散歩**しよう**, 勉強する → 勉強**しよう**\n- 来る → **こ**よう"),
    "will-plain": ("The plain volitional: let's, I'll, I was about to.",
                   "- **Let's / shall we?** 休もう(か), 一緒に見よう\n- **I think I'll …** 〜ようと思う · **I'm planning to …** 〜ようと思っている\n- **I was just about to / tried to …** 〜ようとしたら"),
    "will-polite": ("ましょう = polite 'let's'; ましょうか = 'shall I / shall we?'",
                    "- そろそろ帰り**ましょう** (let's head home)\n- 荷物を持ち**ましょうか** (shall I carry your bag?) — an offer of help."),
    "can": ("Ability, possibility, rules → potential.",
            "Signals: 〜ようになった (became able to), 〜ません (can't), でも (even), 何でも (anything), ここでは (rules)."),
    "will": ("Plans, invitations, decisions → volitional.",
             "Signals: さあ (come on), 〜と決めた (decided to), 〜としたら (was about to / tried to), 一緒に … よう."),
}


def point_entry(pid, title, guide, examples):
    gt, gs, gb = GUIDE[guide]
    if pid in POINT_BODY:
        summary, body = POINT_BODY[pid]
        return {"id": pid, "title": title, "summary": summary, "body": body + "\n\n" + gb, "examples": examples}
    return {"id": pid, "title": title, "summary": f"{gt}: {gs}", "body": gb, "examples": examples}

GUIDE = {
    "masu": ("ます-form (polite)", "ます-stem + ます / ません / ました / ませんでした / ましょう.",
             "- **る-verbs**: drop る → 食べ**ます**.\n- **う-verbs**: last sound to the い-row → 書く → 書**き**ます, 話す → 話**し**ます.\n- **する** → します, **来る** → 来(き)ます."),
    "plain": ("Plain (casual) forms", "Dictionary form, ない-form, た-form, なかった-form — how you talk to friends and family.",
              "- **ない**: る-verbs drop る (食べない); う-verbs go to the あ-row (書かない, 言う → 言**わ**ない); する → しない, 来る → こない, ある → **ない**.\n- **た**: same as the て-form with た (食べた, 書いた, 読んだ).\n- **なかった**: ない → なかった."),
    "te": ("て-form", "The connector for sequences, requests, permissions and ongoing actions.",
           "- る-verbs: 食べ**て**.\n- う・つ・る → **って** (買って, 待って, 帰って)\n- ぬ・ぶ・む → **んで** (死んで, 遊んで, 読んで)\n- く → **いて**, ぐ → **いで**, す → **して**\n- **行く → 行って** (exception)\n- Then: てください (please), ている (-ing / state), てもいい (may), てはいけない (must not)."),
    "potvol": ("Can & will (potential / volitional)", "Two verb forms that look alike but mean different things: 'can do' and 'let's / I'll do'.",
               """**Two forms, two meanings**

| | meaning | 書く | 食べる |
|---|---|---|---|
| **Potential** | can do | 書**ける** | 食べ**られる** |
| **Volitional** | let's / I'll do | 書**こう** | 食べ**よう** |

- Potential = ability or possibility: 漢字が**読める** (I can read kanji).
- Volitional = intention or invitation: 一緒に**読もう** (let's read it together).

**How to make the potential (can)**
- **う-verbs:** last sound → **え-row**, then る: 書く → 書**け**る, 読む → 読**め**る, 話す → 話**せ**る, 買う → 買**え**る.
- **る-verbs:** drop る → **られる**: 食べる → 食べ**られる**, 見る → 見**られる**.
- **する → できる**, **来る → 来(こ)られる**.
- The result is itself a る-verb: 書ける → 書け**ます** / 書け**ません** / 書け**ない**.
- The thing you can do usually takes **が**: 日本語**が**話せます (を is also heard).
- In casual speech る-verbs often drop the ら: 見れる, 来れる. Understand it, but write 見られる.

**How to make the volitional (let's / I'll)**
- **う-verbs:** last sound → **お-row**, then う: 書く → 書**こう**, 読む → 読**もう**, 行く → 行**こう**.
- **る-verbs:** drop る → **よう**: 食べる → 食べ**よう**, 寝る → 寝**よう**.
- **する → しよう**, **来る → 来(こ)よう**.
- It's the plain version of **ましょう**: 行こう = 行きましょう.

**What the volitional is used for**
- **Let's … / Shall we …?** — 休もう(か), 一緒に帰ろう.
- **I think I'll …** — 〜ようと思う; **I'm planning to …** — 〜ようと思っている.
- **was just about to …** — 〜ようとしたら (寝ようとしたら電話が鳴った).
- Polite offer: 〜ましょうか (荷物を持ちましょうか = shall I carry it?).

**Can or will? Ask what the sentence is about**
- ability, possibility, rules (〜ようになった, 〜ません, ここでは) → **potential**
- plans, invitations, decisions (一緒に, 〜と思う, そろそろ) → **volitional**"""),
    "cond": ("Conditionals & must", "ば (general if), たら (if / once), なければならない (must).",
             "- **ば**: る-verbs → れば (食べれば); う-verbs → え-row + ば (飲めば); する → すれば; 来る → くれば; ある → あれば.\n- **たら**: た-form + ら (着いたら) — also for 'once / when'.\n- **must**: ない-form → なければならない (いけない / なくてはいけない also work)."),
    "voice": ("Passive & causative", "Something is done to you (passive), you make / let someone do it (causative), and you're made to do it (causative-passive).",
              "- **Passive**: る-verbs + られる; う-verbs → あ-row + れる (踏まれる); する → される.\n- **Causative**: る-verbs + させる; う-verbs → あ-row + せる (書かせる); する → させる.\n- **Causative-passive**: る-verbs + させられる; う-verbs → あ-row + される (飲まされる; せられる also works; す-verbs only せられる); する → させられる."),
    "keigo": ("Keigo: honorific & humble", "Honorific raises the other person's actions; humble lowers your own.",
              "- **Special verbs** — honorific: いらっしゃる (行く・来る・いる), 召し上がる (食べる・飲む), おっしゃる (言う), ご覧になる (見る), なさる (する).\n- Humble: 参る (行く・来る), 伺う (行く・聞く), 申す (言う), 拝見する (見る), いたす (する), いただく (食べる・飲む・もらう), お目にかかる (会う), おる (いる).\n- **Regular**: honorific お + ます-stem + になる (お読みになる); humble お + ます-stem + する (お持ちする), する-nouns ご + noun + する (ご案内する)."),
    "mixed": ("Mixed review", "All forms, shuffled — the most effective way to make them stick.",
              "**Why mixed practice works**\nRecalling a form yourself (instead of choosing it) and having to work out *which* form a situation needs are the two things that make grammar stick. Mixing the forms forces exactly that.\n\n- Read the cue (→ polite past, → humble …) and the situation.\n- Say the sentence aloud before you type.\n- Use the hint only when stuck — it counts as 'with hint' and the question comes back sooner."),
}


def quiz(fname, id, title, description, guide, items, pid_fn=None, titles=None):
    gt, gs, gb = GUIDE[guide]
    point_ids = []
    questions = []
    for sentence, key, form, en in items:
        pid = pid_fn(key, form) if pid_fn else guide if guide in ("mixed",) else form
        accept, why, hint = build(key, form)
        gloss = f" ({GLOSS[key]})" if pid_fn and key in GLOSS else ""
        questions.append({
            "point": pid, "prompt": f"{sentence}\n→ {ruby(key)}{gloss} · {LABEL[form]}", "options": [], "answer": 0,
            "accept": accept, "hint": hint, "explanation": why, "notes": [], "translation": en,
            "wrong_forms": wrong_forms(key, form, accept),
        })
        if pid not in point_ids:
            point_ids.append(pid)
    points = []
    for pid in point_ids:
        if guide == "mixed":
            points.append({"id": pid, "title": gt, "summary": gs, "body": gb, "examples": []})
        else:
            ex = next(q for q in questions if q["point"] == pid)
            filled = ex["prompt"].split("\n")[0].replace("（　）", ex["accept"][0])
            t = titles[pid] if titles else LABEL[pid][0].upper() + LABEL[pid][1:]
            points.append(point_entry(pid, t, guide, [[filled, ex["translation"]]]))
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}


quiz("11_masu", "verbs-masu", "ます Forms: Meeting a New Colleague",
     "Polite present, negative, past and 'let's' — small talk with someone you've just met at work.", "masu", [
    ("{毎朝|まいあさ}7{時|じ}に（　）。", "起きる", "masu", "I get up at seven every morning."),
    ("{私|わたし}はお{酒|さけ}をあまり（　）。", "飲む", "masen", "I don't drink much alcohol."),
    ("{先週末|せんしゅうまつ}は{家族|かぞく}と{映画|えいが}を（　）。", "見る", "mashita", "Last weekend I watched a film with my family."),
    ("{昨日|きのう}は{忙|いそが}しくて、{昼|ひる}ご{飯|はん}を（　）。", "食べる", "masendeshita", "I was so busy yesterday that I didn't eat lunch."),
    ("{今度|こんど}、{一緒|いっしょ}に{飲|の}みに（　）。", "行く", "mashou", "Let's go for a drink together sometime."),
    ("{毎日|まいにち}{電車|でんしゃ}で{会社|かいしゃ}に（　）。", "来る", "masu", "I come to the office by train every day."),
    ("{日曜日|にちようび}は{仕事|しごと}を（　）。", "する", "masen", "I don't work on Sundays."),
    ("{大学|だいがく}で{経済|けいざい}を（　）。", "勉強する", "mashita", "I studied economics at university."),
    ("{前|まえ}の{会社|かいしゃ}では、あまり{英語|えいご}を（　）。", "話す", "masendeshita", "At my previous company I didn't speak much English."),
    ("{毎晩|まいばん}、{日本語|にほんご}のニュースを（　）。", "聞く", "masu", "Every evening I listen to the news in Japanese."),
    ("{私|わたし}はタバコは（　）。", "吸う", "masen", "I don't smoke."),
    ("{先月|せんげつ}この{町|まち}に（　）。", "引っ越す", "mashita", "I moved to this town last month."),
    ("{駅|えき}まで{一緒|いっしょ}に（　）。", "歩く", "mashou", "Let's walk to the station together."),
    ("{昨日|きのう}は{雨|あめ}だったので、どこにも（　）。", "出かける", "masendeshita", "It rained yesterday, so I didn't go anywhere."),
])

quiz("12_plain", "verbs-plain", "Plain Forms: Chatting with Friends",
     "Dictionary, ない, た and なかった forms — how you actually talk to friends.", "plain", [
    ("{明日|あした}、{何時|なんじ}に（　）？", "起きる", "dict", "What time are you getting up tomorrow?"),
    ("{今日|きょう}は{疲|つか}れたから、どこにも（　）。", "行く", "nai", "I'm tired today, so I'm not going anywhere."),
    ("{昨日|きのう}、{駅|えき}で{田中|たなか}さんに（　）よ。", "会う", "ta", "I bumped into Tanaka at the station yesterday."),
    ("{昨日|きのう}のパーティー、どうして（　）の？", "来る", "nakatta", "Why didn't you come to the party yesterday?"),
    ("{週末|しゅうまつ}は{家|いえ}でゆっくり（　）つもり。", "休む", "dict", "I'm planning to take it easy at home this weekend."),
    ("{辛|から}い{物|もの}はあまり（　）んだ。", "食べる", "nai", "I don't really eat spicy food."),
    ("{昨日|きのう}の{夜|よる}、{何|なに}を（　）？", "食べる", "ta", "What did you eat last night?"),
    ("{宿題|しゅくだい}、{全然|ぜんぜん}（　）。どうしよう。", "する", "nakatta", "I didn't do the homework at all. What do I do?"),
    ("{毎朝|まいあさ}コーヒーを（　）？", "飲む", "dict", "Do you drink coffee every morning?"),
    ("{電話|でんわ}したけど、{彼|かれ}は（　）。", "出る", "nakatta", "I called, but he didn't pick up."),
    ("{来週|らいしゅう}、{京都|きょうと}に（　）んだ。", "行く", "dict", "I'm going to Kyoto next week."),
    ("{彼女|かのじょ}はもう（　）よ。さっき{出|で}ていった。", "帰る", "ta", "She's already gone home — she left a moment ago."),
    ("{心配|しんぱい}しないで。{誰|だれ}にも（　）から。", "言う", "nai", "Don't worry, I won't tell anyone."),
    ("{子供|こども}のころ、{野菜|やさい}を{全然|ぜんぜん}（　）。", "食べる", "nakatta", "As a kid I didn't eat vegetables at all."),
])

quiz("13_te", "verbs-te", "て-Form: Directions, Recipes & Requests",
     "Sequences, requests, ongoing actions, permission and prohibition — the て-form at work.", "te", [
    ("{次|つぎ}の{角|かど}を{右|みぎ}に（　）、まっすぐ{行|い}ってください。", "曲がる", "te", "Turn right at the next corner and go straight on."),
    ("{野菜|やさい}を（　）、{鍋|なべ}に{入|い}れます。", "切る", "te", "Cut the vegetables and put them in the pot."),
    ("{卵|たまご}を（　）、よく{混|ま}ぜてください。", "割る", "te", "Crack the eggs and mix them well."),
    ("すみません、もう{少|すこ}しゆっくり（　）。", "話す", "tekudasai", "Excuse me, could you speak a little more slowly, please?"),
    ("ここに{名前|なまえ}を（　）。", "書く", "tekudasai", "Please write your name here."),
    ("ちょっと（　）。すぐ{戻|もど}ります。", "待つ", "tekudasai", "Please wait a moment — I'll be right back."),
    ("{今|いま}、{駅|えき}の{前|まえ}で{友達|ともだち}を（　）。", "待つ", "teimasu", "I'm waiting for a friend in front of the station right now."),
    ("{姉|あね}は{東京|とうきょう}の{銀行|ぎんこう}で（　）。", "働く", "teimasu", "My older sister works at a bank in Tokyo."),
    ("ここで{写真|しゃしん}を（　）ですか。", "撮る", "temoii", "May I take photos here?"),
    ("{疲|つか}れたら、{少|すこ}し（　）よ。", "休む", "temoii", "If you're tired, you can take a short break."),
    ("{美術館|びじゅつかん}の{中|なか}では、{写真|しゃしん}を（　）。", "撮る", "tewaikenai", "You mustn't take photos inside the museum."),
    ("このボタンは{絶対|ぜったい}に（　）。", "押す", "tewaikenai", "You must never press this button."),
    ("{駅|えき}に{着|つ}いたら、{電話|でんわ}を（　）。", "する", "tekudasai", "Please call me when you get to the station."),
    ("{子供|こども}たちは{公園|こうえん}で（　）。", "遊ぶ", "teimasu", "The children are playing in the park."),
])

quiz("14f_can_will", "verbs-can-will", "Step 6 · Can & will mixed review",
     "Abilities and plans mixed — the review after steps 1–5.", "potvol", [
    ("{弟|おとうと}はまだ5{歳|さい}なのに、ひらがなが（　）。", "読む", "potential", "My little brother is only five, but he can read hiragana."),
    ("{日本語|にほんご}で{電話|でんわ}が（　）ようになりました。", "する", "potential", "I've become able to make phone calls in Japanese."),
    ("このお{店|みせ}では、カードが（　）か。", "使う", "potential_masu", "Can I pay by card in this shop?"),
    ("{明日|あした}は{何時|なんじ}に（　）か。", "来る", "potential_masu", "What time can you come tomorrow?"),
    ("{彼女|かのじょ}は100メートルを12{秒|びょう}で（　）。", "走る", "potential", "She can run 100 metres in 12 seconds."),
    ("{明日|あした}は{早|はや}いので、{今日|きょう}は{早|はや}く（　）と{思|おも}います。", "寝る", "volitional", "I've got an early start tomorrow, so I think I'll go to bed early tonight."),
    ("{夏休|なつやす}みに{北海道|ほっかいどう}へ（　）と{思|おも}っています。", "行く", "volitional", "I'm thinking of going to Hokkaido in the summer holidays."),
    ("{疲|つか}れたね。{少|すこ}し（　）か。", "休む", "volitional", "We're tired — shall we take a break?"),
    ("{来年|らいねん}から{毎日|まいにち}{日記|にっき}を（　）と{思|おも}う。", "書く", "volitional", "From next year I'm going to write a diary every day."),
    ("このアパートではペットが（　）。", "飼う", "potential_masu", "You can keep pets in this flat."),
    ("{一緒|いっしょ}に{晩|ばん}ご{飯|はん}を（　）よ。", "作る", "volitional", "Let's cook dinner together."),
    ("{上手|じょうず}に（　）ように、{毎日|まいにち}{練習|れんしゅう}しています。", "泳ぐ", "potential", "I practise every day so that I can swim well."),
])

quiz("15_if_must", "verbs-if-must", "If & Must: Rules and Advice",
     "ば and たら conditionals, and なければならない for things you have to do.", "cond", [
    ("この{薬|くすり}を（　）、すぐ{治|なお}りますよ。", "飲む", "ba", "If you take this medicine, you'll soon get better."),
    ("わからないことがあれば、{先生|せんせい}に（　）いいですよ。", "聞く", "ba", "If there's anything you don't understand, just ask the teacher."),
    ("もっと{早|はや}く（　）、{間|ま}に{合|あ}ったのに。", "出る", "ba", "If we'd left earlier, we'd have made it."),
    ("{駅|えき}に（　）、{電話|でんわ}してください。", "着く", "tara", "Call me when you get to the station."),
    ("{雨|あめ}が（　）、{試合|しあい}は{中止|ちゅうし}です。", "降る", "tara", "If it rains, the match is off."),
    ("{宝|たから}くじが（　）、{何|なに}を{買|か}いますか。", "当たる", "tara", "If you won the lottery, what would you buy?"),
    ("{明日|あした}は{試験|しけん}だから、{今夜|こんや}は（　）。", "勉強する", "nakereba", "There's an exam tomorrow, so I have to study tonight."),
    ("9{時|じ}までに{会社|かいしゃ}に（　）。", "行く", "nakereba", "I have to be at the office by nine."),
    ("{図書館|としょかん}の{本|ほん}は{来週|らいしゅう}までに（　）。", "返す", "nakereba", "I have to return the library books by next week."),
    ("お{金|かね}が（　）、{世界中|せかいじゅう}を{旅行|りょこう}したい。", "ある", "ba", "If I had the money, I'd like to travel around the world."),
    ("{時間|じかん}が（　）、また{来|き}てください。", "ある", "ba", "If you have time, please come again."),
    ("{家|いえ}に（　）、すぐ{手|て}を{洗|あら}いなさい。", "帰る", "tara", "Wash your hands as soon as you get home."),
    ("この{薬|くすり}は{毎日|まいにち}（　）。", "飲む", "nakereba", "You have to take this medicine every day."),
])

quiz("16_voice", "verbs-voice", "Passive & Causative: Stories from School and Work",
     "Things that happened to you, things you made others do, and things you were made to do.", "voice", [
    ("{電車|でんしゃ}の{中|なか}で{足|あし}を（　）。", "踏む", "passive_ta", "Someone stepped on my foot on the train."),
    ("{遅刻|ちこく}して、{先生|せんせい}に（　）。", "叱る", "passive_ta", "I was late and got told off by the teacher."),
    ("{駅|えき}で{財布|さいふ}を（　）。", "盗む", "passive_ta", "My wallet was stolen at the station."),
    ("このお{寺|てら}は800{年前|ねんまえ}に（　）。", "建てる", "passive_ta", "This temple was built 800 years ago."),
    ("この{本|ほん}は{世界中|せかいじゅう}で（　）。", "読む", "passive_teiru", "This book is read all over the world."),
    ("この{歌|うた}は{今|いま}も{多|おお}くの{人|ひと}に（　）。", "歌う", "passive_teiru", "This song is still sung by many people."),
    ("{母|はは}は{弟|おとうと}に{部屋|へや}を（　）。", "掃除する", "causative_ta", "Mum made my little brother clean his room."),
    ("{先生|せんせい}は{学生|がくせい}に{作文|さくぶん}を（　）。", "書く", "causative_ta", "The teacher had the students write an essay."),
    ("{誕生日|たんじょうび}は、{子供|こども}に{好|す}きなものを（　）。", "食べる", "causative_ta", "On their birthday, we let the kids eat whatever they liked."),
    ("{部長|ぶちょう}は{私|わたし}を{一時間|いちじかん}も（　）。", "待つ", "causative_ta", "My manager kept me waiting for a whole hour."),
    ("{子供|こども}のころ、{毎日|まいにち}ピアノを（　）。", "練習する", "caus_pass_ta", "As a child I was made to practise the piano every day."),
    ("{飲|の}み{会|かい}で、{先輩|せんぱい}にお{酒|さけ}を（　）。", "飲む", "caus_pass_ta", "At the party my senior made me drink."),
    ("{昨日|きのう}、{駅|えき}で{一時間|いちじかん}も（　）。", "待つ", "caus_pass_ta", "Yesterday I was kept waiting at the station for a whole hour."),
    ("{給食|きゅうしょく}で、{嫌|きら}いな{野菜|やさい}を（　）。", "食べる", "caus_pass_ta", "At school lunch I was made to eat vegetables I hated."),
])

quiz("17_keigo", "verbs-keigo", "Keigo: At a Hotel and in Business",
     "Honorific verbs for other people's actions, humble verbs for your own — special verbs and the regular patterns.", "keigo", [
    ("{社長|しゃちょう}は{何時|なんじ}に（　）か。", "来る", "hon", "What time will the president arrive?"),
    ("{先生|せんせい}、お{飲|の}み{物|もの}は{何|なに}を（　）か。", "飲む", "hon", "Professor, what would you like to drink?"),
    ("{社長|しゃちょう}は{今|いま}、{会議室|かいぎしつ}に（　）。", "いる", "hon", "The president is in the meeting room at the moment."),
    ("{部長|ぶちょう}は{明日|あした}の{会議|かいぎ}について{何|なん}と（　）か。", "言う", "hon_ta", "What did the manager say about tomorrow's meeting?"),
    ("{先生|せんせい}は{毎朝|まいあさ}{新聞|しんぶん}を（　）。", "読む", "hon", "The professor reads the newspaper every morning."),
    ("お{客様|きゃくさま}はもうホテルに（　）。", "着く", "hon_ta", "The guest has already arrived at the hotel."),
    ("{社長|しゃちょう}は{週末|しゅうまつ}によくゴルフを（　）。", "する", "hon", "The president often plays golf at the weekend."),
    ("{明日|あした}、こちらから{御社|おんしゃ}に（　）。", "行く", "hum", "Tomorrow we'll come to your company."),
    ("はじめまして。{田中|たなか}と（　）。", "言う", "hum", "How do you do? My name is Tanaka."),
    ("{先週|せんしゅう}の{資料|しりょう}を（　）。", "見る", "hum_ta", "I've looked over last week's materials."),
    ("{私|わたし}がお{客様|きゃくさま}を{会議室|かいぎしつ}まで（　）。", "案内する", "hum", "I'll show the guest to the meeting room."),
    ("{重|おも}そうですね。お{荷物|にもつ}を（　）。", "持つ", "hum", "That looks heavy — let me carry your luggage."),
    ("{明日|あした}、またお{電話|でんわ}を（　）。", "する", "hum", "I'll call you again tomorrow."),
    ("{昨日|きのう}のパーティーで、{社長|しゃちょう}の{奥様|おくさま}に（　）。", "会う", "hum_ta", "At yesterday's party I met the president's wife."),
])

quiz("18_mixed", "verbs-mixed", "Mixed Review: All Forms",
     "Every form, shuffled. You have to work out which form each situation needs — the best practice for real conversations.", "mixed", [
    ("{毎朝|まいあさ}ジョギングを（　）。", "する", "masu", "I go jogging every morning."),
    ("{昨日|きのう}、レストランで{寿司|すし}を（　）よ。", "食べる", "ta", "I had sushi at a restaurant yesterday."),
    ("{暑|あつ}いですね。{窓|まど}を（　）もいいですか。", "開ける", "te", "It's hot, isn't it? May I open the window?"),
    ("{漢字|かんじ}はまだ{全然|ぜんぜん}（　）。", "読む", "potential_masen", "I still can't read kanji at all."),
    ("{週末|しゅうまつ}、{一緒|いっしょ}に{海|うみ}へ（　）よ。", "行く", "volitional", "Let's go to the beach together at the weekend."),
    ("{授業中|じゅぎょうちゅう}、{先生|せんせい}に{名前|なまえ}を（　）。", "呼ぶ", "passive_ta", "My name was called by the teacher in class."),
    ("{早|はや}く（　）、{間|ま}に{合|あ}うよ。", "出る", "ba", "If you leave now, you'll make it."),
    ("{会議|かいぎ}の{前|まえ}に{資料|しりょう}を（　）。", "読む", "nakereba", "I have to read the materials before the meeting."),
    ("{部長|ぶちょう}、どちらへ（　）か。", "行く", "hon", "Where are you going, sir?"),
    ("{子供|こども}のころ、{母|はは}によく{手伝|てつだ}いを（　）。", "する", "caus_pass_ta", "As a child, my mum often made me help out."),
    ("{雨|あめ}が（　）、{出|で}かけましょう。", "止む", "tara", "Let's go out once the rain stops."),
    ("{昨日|きのう}は{頭|あたま}が{痛|いた}くて、{何|なに}も（　）。", "食べる", "masendeshita", "I had a headache yesterday and didn't eat anything."),
    ("{今|いま}、{何|なに}を（　）の？", "する", "teiru", "What are you doing right now?"),
    ("{明日|あした}は{彼|かれ}、（　）よ。{用事|ようじ}があるって。", "来る", "nai", "He's not coming tomorrow — he says he's got something on."),
    ("{彼女|かのじょ}に{好|す}きだと（　）と{思|おも}う。", "言う", "volitional", "I think I'll tell her I like her."),
    ("お{客様|きゃくさま}、お{荷物|にもつ}は{私|わたし}が（　）。", "持つ", "hum", "Sir, I'll carry your luggage."),
])


# ---------------------------------------------------------------- verb types & drills (learn these first)

def kform(key, f):
    kanji, r, cls = VERBS[key]
    return to_kanji(forms(r, cls)[f][0], key)


def ruby_form(kana, key):
    """Conjugated form with furigana on the kanji: 読んで → {読|よ}んで."""
    kanji, reading, cls = VERBS[key]
    if kanji == reading:
        return kana
    if cls == "kuru":
        return "{来|" + kana[0] + "}" + kana[1:]
    n = okuri(kanji, reading)
    kp, rp = kanji[:len(kanji) - n], reading[:len(reading) - n]
    return "{" + kp + "|" + rp + "}" + kana[len(rp):]


def type_point(key):
    _, r, cls = VERBS[key]
    if cls in ("suru", "kuru"):
        return "irregular"
    if r[-1] != "る":
        return "not-ru"
    if VOWEL[r[-2]] in "auo":
        return "aou-ru"
    return "ie-ru" if cls == "ru" else "exception"


TYPE_OPTS = ["る-verb (ichidan)", "う-verb (godan)", "irregular (する / 来る)"]


def type_q(key):
    kanji, r, cls = VERBS[key]
    v, p = ruby(key), type_point(key)
    ans = 0 if cls == "ru" else 2 if cls in ("suru", "kuru") else 1
    nai, masu, te_ = kform(key, "nai"), kform(key, "masu"), kform(key, "te")
    fs = f"{nai}, {masu}, {te_}"
    vw = VOWEL.get(r[-2], "") if len(r) > 1 else ""
    if p == "irregular":
        why = (f"{v} is noun + する, so it conjugates exactly like する: {fs}." if kanji != "する" and cls == "suru"
               else f"する is one of only two irregular verbs: {fs}." if cls == "suru"
               else f"来る is irregular — its vowel changes: {fs} (こない, きます, きて).")
    elif p == "not-ru":
        why = f"{v} ends in {r[-1]}, not る. Every verb that doesn't end in る is an う-verb: {fs}."
    elif p == "aou-ru":
        why = f"The sound before る is {r[-2]} (-{vw}). Verbs in -{vw}る are always う-verbs: {fs}."
    elif p == "ie-ru":
        why = f"The sound before る is {r[-2]} (-{vw}), and -iる / -eる verbs are normally る-verbs: just drop る → {fs}."
    else:
        why = (f"Exception! {v} ends in -{vw}る ({r[-2]}る) like a る-verb, but it's an う-verb: {fs} — "
               f"not {to_kanji(r[:-1] + 'ない', key)}. Learn it with the exception list.")
    if cls in ("suru", "kuru"):
        n_ru = n_u = f"It doesn't follow the regular pattern: {fs}."
    else:
        n_ru = ("Only verbs ending in る can be る-verbs." if r[-1] != "る"
                else f"A る-verb would just drop る: {to_kanji(r[:-1] + 'ない', key)} — but it's {nai}.")
        n_u = f"An う-verb would turn る into ら: {to_kanji(r[:-1] + 'らない', key)} — but it's {nai}."
    notes = [n_ru, n_u, "Only する (with noun + する verbs) and 来る are irregular."]
    notes[ans] = ""
    return {"point": p, "prompt": f"What type of verb is **{v}**?", "options": TYPE_OPTS, "answer": ans,
            "fixed_order": True, "explanation": why, "notes": notes,
            "translation": f"{kanji} = to {GLOSS[key]}" if key in GLOSS else ""}


TYPE_POINTS = {
    "not-ru": ("Doesn't end in る → う-verb", "書く, 話す, 待つ, 死ぬ, 遊ぶ, 読む, 泳ぐ, 買う: always う-verbs."),
    "aou-ru": ("-aる / -uる / -oる → う-verb", "分かる, 作る, 乗る, 取る: the sound before る is not i or e, so it's an う-verb."),
    "ie-ru": ("-iる / -eる → usually る-verb", "見る, 起きる, 食べる, 教える: drop る for every form."),
    "exception": ("-iる / -eる う-verb exceptions", "帰る, 入る, 走る, 切る, 知る, 要る, 限る, 喋る, 滑る, 焦る, 減る, 蹴る, 握る, 散る."),
    "irregular": ("Irregular: する and 来る", "する (and every noun + する) and 来る — learn their forms by heart."),
}
TYPES_BODY = """**How to tell the verb type** — look at the dictionary form:

- Doesn't end in る (〜う, 〜く, 〜す, 〜つ …) → **う-verb**, always.
- Ends in る, and the sound before it is **a / u / o** (分**か**る, 作**る**→つく**る**, 乗**る**) → **う-verb**, always.
- Ends in **-iる / -eる** (見る, 起**き**る, 食**べ**る) → usually a **る-verb**.
- …except a short list of common う-verbs: **帰る, 入る, 走る, 切る, 知る, 要る, 限る, 喋る, 滑る, 焦る, 減る, 蹴る, 握る, 散る**.
- **する** and **来る** are irregular; 勉強する and other noun + する verbs conjugate like する.

**Why it matters**
- る-verbs drop る: 食べ**ない**, 食べ**ます**, 食べ**て**.
- う-verbs change the last sound: 帰**ら**ない, 帰**り**ます, 帰**って**.

**Check yourself:** if you know the ない-form, it tells you the type — 帰**ら**ない has an あ-row sound, so 帰る is an う-verb."""


def mc_quiz(fname, id, title, description, keys, summary):
    questions = [type_q(k) for k in keys]
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = [{"id": p, "title": TYPE_POINTS[p][0], "summary": TYPE_POINTS[p][1] + " " + summary, "body": TYPES_BODY,
               "examples": []} for p in pids]
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}


mc_quiz("01_types", "verbs-types", "Verb Types (る, う or Irregular?)",
        "Learn to tell a verb's type from its dictionary form — the first step for every conjugation.",
        ["書く", "食べる", "分かる", "する", "話す", "見る", "作る", "来る", "待つ", "起きる", "乗る", "勉強する",
         "死ぬ", "教える", "取る", "遊ぶ", "借りる", "座る", "泳ぐ", "忘れる", "買う", "閉める"], "")
mc_quiz("02_exceptions", "verbs-exceptions", "The Sneaky Exceptions: う-Verbs in Disguise",
        "Verbs in -iる / -eる are usually る-verbs — except a short list you just have to know.",
        ["帰る", "着る", "入る", "変える", "走る", "降りる", "切る", "浴びる", "知る", "信じる", "要る", "生きる",
         "喋る", "見せる", "滑る", "足りる", "焦る", "覚える", "減る", "握る", "蹴る", "限る"], "")

GUIDE["lookalike"] = ("Lookalike verbs", "Verbs that sound the same (or almost) but belong to different types.",
                      "- **切る** (cut) is an う-verb → 切って, 切らない — **着る** (wear) is a る-verb → 着て, 着ない.\n"
                      "- **帰る** (go home) → 帰って, 帰らない — **変える** (change) → 変えて, 変えない.\n"
                      "- **要る** (need) → 要らない — **いる** (be) → いない.\n"
                      "- **入る** (enter) → 入って — **入れる** (put in) → 入れて.\n"
                      "- **知る**, **走る**, **喋る**, **滑る**, **焦る**, **減る** look like る-verbs but are う-verbs.\n\n"
                      "Tip: learn each exception together with its ない-form (帰らない, 知らない) — that form gives the type away.")
quiz("03_lookalikes", "verbs-lookalikes", "Lookalike Verbs: 切る or 着る?",
     "Pairs that sound alike but conjugate differently — type the right form in context.", "lookalike", [
    ("{美容院|びよういん}で{髪|かみ}を{短|みじか}く（　）。", "切る", "mashita", "I had my hair cut short at the salon."),
    ("{寒|さむ}かったので、コートを（　）。", "着る", "mashita", "It was cold, so I wore a coat."),
    ("{玉|たま}ねぎを{細|こま}かく（　）ください。", "切る", "tekudasai", "Please chop the onion finely."),
    ("{結婚式|けっこんしき}で{着物|きもの}を（　）{写真|しゃしん}を{撮|と}った。", "着る", "te", "I wore a kimono at the wedding and had photos taken."),
    ("{彼|かれ}はもう{家|いえ}に（　）よ。", "帰る", "ta", "He's already gone home."),
    ("{髪|かみ}の{色|いろ}を{明|あか}るく（　）。", "変える", "ta", "I changed my hair to a lighter colour."),
    ("{雨|あめ}は{降|ふ}らないから、{傘|かさ}は（　）よ。", "要る", "nai", "It won't rain, so you don't need an umbrella."),
    ("{兄|あに}は{今|いま}、{家|いえ}に（　）よ。", "いる", "nai", "My brother isn't at home right now."),
    ("どうぞ、{中|なか}に（　）ください。", "入る", "tekudasai", "Please come in."),
    ("{牛乳|ぎゅうにゅう}を{冷蔵庫|れいぞうこ}に（　）ください。", "入れる", "tekudasai", "Please put the milk in the fridge."),
    ("その{人|ひと}の{名前|なまえ}は（　）。", "知る", "nai", "I don't know that person's name."),
    ("{毎朝|まいあさ}{公園|こうえん}を（　）。", "走る", "masu", "I run in the park every morning."),
    ("{毎晩|まいばん}11{時|じ}に（　）。", "寝る", "masu", "I go to bed at eleven every night."),
    ("{授業中|じゅぎょうちゅう}に（　）はいけません。", "喋る", "te", "You mustn't chat during class."),
    ("{凍|こお}った{道|みち}で（　）、{転|ころ}んでしまった。", "滑る", "te", "I slipped on the icy road and fell."),
    ("{時間|じかん}はあるから、（　）でゆっくりやって。", "焦る", "nai", "There's time, so don't rush — take it slowly."),
    ("{先月|せんげつ}より{体重|たいじゅう}が2キロ（　）。", "減る", "ta", "I've lost two kilos since last month."),
    ("{電車|でんしゃ}を（　）、{駅|えき}まで{歩|ある}いた。", "降りる", "te", "I got off the train and walked to the station."),
], pid_fn=lambda key, form: "lk-u" if VERBS[key][2] == "u" else "lk-ru",
   titles={"lk-u": "う-verbs that look like る-verbs", "lk-ru": "Real る-verbs (the lookalike partners)"})

# --- back to the dictionary form
TE_BACK = {"う": "って ← う, つ or る", "つ": "って ← う, つ or る", "る": "って ← う, つ or る", "ぬ": "んで ← ぬ, ぶ or む",
           "ぶ": "んで ← ぬ, ぶ or む", "む": "んで ← ぬ, ぶ or む", "く": "いて ← く", "ぐ": "いで ← ぐ", "す": "して ← す"}


def back_q(key, form, pid):
    kanji, r, cls = VERBS[key]
    src_kana = forms(r, cls)[form][0]
    src = ruby_form(src_kana, key)
    shown = to_kanji(src_kana, key)
    if cls == "kuru":
        hint, rule = "Irregular: き・こ・く", "き / こ belong to the irregular 来る (きます, こない, きて)"
    elif cls == "suru":
        hint, rule = "Irregular verb", "し + ending comes from する (します, しない, して)"
    elif form in ("te", "ta"):
        if cls == "ru":
            hint, rule = "Try a る-verb: is there a って / んで / いて?", "a plain て / た after an -i / -e sound: a る-verb, so add る"
        elif cls == "iku":
            hint, rule = "って ← う, つ, る … or the exception 行く", "行って is the one irregular て-form: 行く"
        else:
            hint = TE_BACK[r[-1]]
            rule = f"{hint}; with this kanji only {kanji} makes sense"
    elif form in ("nai",):
        if cls == "ru":
            hint, rule = "No あ-row sound before ない", "nothing but ない was added, so it's a る-verb: ない → る"
        else:
            hint = f"{src_kana[-3]} is an あ-row sound"
            rule = f"{src_kana[-3]} (あ-row) + ない → back to the う-row: {src_kana[-3]} → {r[-1]}"
    else:  # masu: an -e stem is always a る-verb; an -i stem can be either
        stem = src_kana[:-2]
        if VOWEL[stem[-1]] == "e":
            hint, rule = "-e sound before ます", "an -e sound before ます only happens with る-verbs: ます → る"
        else:
            hint = "-i sound before ます: る-verb (+る) or う-verb (i → u)?"
            to_u = {row[I]: u for u, row in ROW.items()}
            ks = shown[:-2]  # 見, 借り, 書き, 入り
            other = ks + "る" if cls == "u" else (ks[:-1] if ks[-1] == stem[-1] else ks) + to_u[stem[-1]]
            rule = (f"an -i sound before ます can be a る-verb (+る) or an う-verb (い-row → う-row). "
                    f"You have to know the verb: here it's {'a る-verb' if cls == 'ru' else 'an う-verb'}, not {other}")
    exc = " ⚠ An う-verb that looks like a る-verb." if is_exception(key) else ""
    return {"point": pid, "prompt": f"{src} → （　）\n→ dictionary form", "options": [], "answer": 0,
            "accept": list(dict.fromkeys([kanji, r])), "hint": hint,
            "explanation": f"{shown}: {rule} → **{kanji}**.{exc}", "notes": [],
            "translation": f"{kanji} = to {GLOSS[key]}" if key in GLOSS else ""}


def drill_quiz(fname, id, title, description, guide, items, titles, keep_order=False, maker=None, rule_hints=False):
    gt, gs, gb = GUIDE[guide]
    questions = []
    for key, form, pid in items:
        if maker:
            questions.append(maker(key, form, pid))
            continue
        accept, why, hint = build(key, form)
        if rule_hints:  # sprints: the group's rule, not the start of the answer
            hint = titles[pid]
        questions.append({"point": pid, "prompt": f"{ruby(key)} → （　）\n→ {LABEL[form]}", "options": [], "answer": 0,
                          "accept": accept, "hint": hint, "explanation": why, "notes": [],
                          "wrong_forms": wrong_forms(key, form, accept),
                          "translation": f"{VERBS[key][0]} = to {GLOSS[key]}" if key in GLOSS else ""})
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = [point_entry(p, titles[p], guide, []) for p in pids]
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}
    if keep_order:
        QZ[fname]["keep_order"] = True


GUIDE["back"] = ("Back to the dictionary form", "Reading or hearing a form, find the verb you'd look up.",
                 "- **て / た**: って ← う・つ・る, んで ← ぬ・ぶ・む, いて ← く, いで ← ぐ, して ← す; a plain て after -i / -e → る-verb (+る).\n"
                 "- **ない**: あ-row + ない → う-row (帰らない → 帰る, 買わない → 買う); no あ-row → る-verb (着ない → 着る).\n"
                 "- **ます**: い-row + ます → う-row (書きます → 書く); otherwise る-verb (見ます → 見る).\n"
                 "- Irregular: きて / こない → 来る, して / しない → する.")
drill_quiz("04_back", "verbs-back", "Back to the Dictionary Form",
           "See a form, find the verb: the skill you need when reading and listening.", "back", [
    ("読む", "te", "back-te"), ("買う", "te", "back-te"), ("待つ", "ta", "back-te"), ("帰る", "te", "back-te"),
    ("着る", "te", "back-te"), ("書く", "ta", "back-te"), ("急ぐ", "te", "back-te"), ("話す", "ta", "back-te"),
    ("遊ぶ", "ta", "back-te"), ("行く", "te", "back-te"), ("来る", "te", "back-te"),
    ("帰る", "nai", "back-nai"), ("着る", "nai", "back-nai"), ("知る", "nai", "back-nai"), ("買う", "nai", "back-nai"),
    ("来る", "nai", "back-nai"), ("見る", "masu", "back-masu"), ("書く", "masu", "back-masu"), ("借りる", "masu", "back-masu"),
    ("入る", "masu", "back-masu"),
], {"back-te": "From て / た", "back-nai": "From ない", "back-masu": "From ます"}, maker=back_q)

GUIDE["sprint_te"] = ("て-form sprint", "One form, many verbs in a row — build the rule first, then mix it.",
                      "- る-verbs: drop る + て (食べて, 見て)\n- う・つ・る → **って** (買って, 待って, 帰って)\n"
                      "- ぬ・ぶ・む → **んで** (死んで, 遊んで, 読んで)\n- く → **いて**, ぐ → **いで**, す → **して**\n"
                      "- Irregular: 行く → **行って**, する → して, 来る → 来(き)て\n\n"
                      "Say each group aloud as a chant: *う・つ・る って, ぬ・ぶ・む んで, く いて, ぐ いで, す して*.")
TE_TITLES = {"te-ru": "る-verbs: drop る + て", "te-tte": "う・つ・る → って", "te-nde": "ぬ・ぶ・む → んで",
             "te-ite": "く → いて, ぐ → いで", "te-shite": "す → して", "te-irr": "Irregular: 行く, する, 来る"}
drill_quiz("05_sprint_te", "verbs-sprint-te", "て-Form Sprint",
           "20 verbs, one form: get the て-form groups into your fingers.", "sprint_te", [
    ("買う", "te", "te-tte"), ("食べる", "te", "te-ru"), ("書く", "te", "te-ite"), ("飲む", "te", "te-nde"),
    ("待つ", "te", "te-tte"), ("話す", "te", "te-shite"), ("行く", "te", "te-irr"), ("見る", "te", "te-ru"),
    ("遊ぶ", "te", "te-nde"), ("帰る", "te", "te-tte"), ("泳ぐ", "te", "te-ite"), ("する", "te", "te-irr"),
    ("死ぬ", "te", "te-nde"), ("起きる", "te", "te-ru"), ("貸す", "te", "te-shite"), ("来る", "te", "te-irr"),
    ("切る", "te", "te-tte"), ("急ぐ", "te", "te-ite"), ("洗う", "te", "te-tte"), ("着る", "te", "te-ru"),
], TE_TITLES, rule_hints=True)

GUIDE["sprint_nai"] = ("ない-form sprint", "One form, many verbs in a row.",
                       "- る-verbs: drop る + ない (食べない, 見ない)\n- う-verbs: last sound → あ-row + ない (書かない, 待たない)\n"
                       "- **う → わ**: 買う → 買**わ**ない (not 買あない)\n- Irregular: する → しない, 来る → **こ**ない, ある → **ない**")
drill_quiz("06_sprint_nai", "verbs-sprint-nai", "ない-Form Sprint",
           "18 verbs, one form — including う → わ and the ones that don't follow the rules.", "sprint_nai", [
    ("書く", "nai", "nai-u"), ("食べる", "nai", "nai-ru"), ("買う", "nai", "nai-wa"), ("帰る", "nai", "nai-u"),
    ("見る", "nai", "nai-ru"), ("来る", "nai", "nai-irr"), ("話す", "nai", "nai-u"), ("会う", "nai", "nai-wa"),
    ("着る", "nai", "nai-ru"), ("ある", "nai", "nai-irr"), ("待つ", "nai", "nai-u"), ("する", "nai", "nai-irr"),
    ("知る", "nai", "nai-u"), ("起きる", "nai", "nai-ru"), ("言う", "nai", "nai-wa"), ("読む", "nai", "nai-u"),
    ("洗う", "nai", "nai-wa"), ("忘れる", "nai", "nai-ru"),
], {"nai-ru": "る-verbs: drop る + ない", "nai-u": "う-verbs: あ-row + ない", "nai-wa": "う → わ + ない",
    "nai-irr": "Irregular: する, 来る, ある"}, rule_hints=True)

GUIDE["ladder"] = ("Conjugation ladder", "One verb through all its forms, in order.",
                   "**う-verbs walk through the vowel rows** (書く):\n"
                   "- **あ** 書か + ない / れる / せる\n- **い** 書き + ます\n- **う** 書く (dictionary)\n"
                   "- **え** 書け + る (can) / ば (if)\n- **お** 書こ + う (let's)\n- て / た: 書いて, 書いた\n\n"
                   "**る-verbs** never change their stem: 食べ + ない / ます / る / られる / れば / よう / て / た.\n\n"
                   "**来る** changes its vowel (こ・き・く), **する** becomes し / さ / でき.")
LADDER = ["masu", "nai", "te", "ta", "potential", "volitional", "ba"]
drill_quiz("07_ladder", "verbs-ladder", "Ladder 書く & 食べる: One Verb, All Forms",
           "One う-verb and one る-verb, each through seven forms in order — see the vowel rows at work.", "ladder",
           [("書く", f, "ladder-u") for f in LADDER] + [("食べる", f, "ladder-ru") for f in LADDER],
           {"ladder-u": "う-verb ladder (書く)", "ladder-ru": "る-verb ladder (食べる)"}, keep_order=True)
drill_quiz("08_ladder_irregular", "verbs-ladder-irregular", "Ladder 来る & する: the Irregulars",
           "The two irregular verbs through seven forms in order.", "ladder",
           [("来る", f, "ladder-kuru") for f in LADDER] + [("する", f, "ladder-suru") for f in LADDER],
           {"ladder-kuru": "来る ladder", "ladder-suru": "する ladder"}, keep_order=True)


# ---------------------------------------------------------------- more verbs for the sprints

VERBS.update({
    "習う": ("習う", "ならう", "u"), "手伝う": ("手伝う", "てつだう", "u"), "払う": ("払う", "はらう", "u"),
    "笑う": ("笑う", "わらう", "u"), "思う": ("思う", "おもう", "u"), "勝つ": ("勝つ", "かつ", "u"), "頼む": ("頼む", "たのむ", "u"),
    "住む": ("住む", "すむ", "u"), "選ぶ": ("選ぶ", "えらぶ", "u"), "運ぶ": ("運ぶ", "はこぶ", "u"), "置く": ("置く", "おく", "u"),
    "磨く": ("磨く", "みがく", "u"), "探す": ("探す", "さがす", "u"), "渡す": ("渡す", "わたす", "u"), "脱ぐ": ("脱ぐ", "ぬぐ", "u"),
    "調べる": ("調べる", "しらべる", "ru"), "答える": ("答える", "こたえる", "ru"), "考える": ("考える", "かんがえる", "ru"),
    "疲れる": ("疲れる", "つかれる", "ru"), "遅れる": ("遅れる", "おくれる", "ru"), "間違える": ("間違える", "まちがえる", "ru"),
    "着替える": ("着替える", "きがえる", "ru"), "心配する": ("心配する", "しんぱいする", "suru"),
    "結婚する": ("結婚する", "けっこんする", "suru"), "予約する": ("予約する", "よやくする", "suru"),
    # transitive / intransitive pairs
    "開く": ("開く", "あく", "u"), "閉まる": ("閉まる", "しまる", "u"), "始まる": ("始まる", "はじまる", "u"),
    "始める": ("始める", "はじめる", "ru"), "壊れる": ("壊れる", "こわれる", "ru"), "壊す": ("壊す", "こわす", "u"),
    "落ちる": ("落ちる", "おちる", "ru"), "落とす": ("落とす", "おとす", "u"), "つく": ("つく", "つく", "u"),
    "つける": ("つける", "つける", "ru"), "消える": ("消える", "きえる", "ru"), "消す": ("消す", "けす", "u"),
    "止まる": ("止まる", "とまる", "u"), "止める": ("止める", "とめる", "ru"), "決まる": ("決まる", "きまる", "u"),
    "決める": ("決める", "きめる", "ru"), "集まる": ("集まる", "あつまる", "u"), "集める": ("集める", "あつめる", "ru"),
    "見つかる": ("見つかる", "みつかる", "u"), "見つける": ("見つける", "みつける", "ru"), "割れる": ("割れる", "われる", "ru"),
    "掛かる": ("掛かる", "かかる", "u"), "掛ける": ("掛ける", "かける", "ru"), "変わる": ("変わる", "かわる", "u"),
    "並ぶ": ("並ぶ", "ならぶ", "u"), "並べる": ("並べる", "ならべる", "ru"),
})
GLOSS.update({
    "習う": "learn", "手伝う": "help", "払う": "pay", "笑う": "laugh", "思う": "think", "勝つ": "win", "頼む": "ask for",
    "住む": "live", "選ぶ": "choose", "運ぶ": "carry", "置く": "put", "磨く": "brush, polish", "探す": "look for",
    "渡す": "hand over", "調べる": "look up", "答える": "answer", "考える": "think about", "疲れる": "get tired",
    "遅れる": "be late", "間違える": "make a mistake", "着替える": "get changed", "心配する": "worry",
    "結婚する": "marry", "予約する": "book", "開く": "open (by itself)", "開ける": "open (something)",
    "閉まる": "close (by itself)", "閉める": "close (something)", "始まる": "begin", "始める": "begin (something)",
    "壊れる": "break (by itself)", "壊す": "break (something)", "落ちる": "fall", "落とす": "drop (something)",
    "つく": "come on (light)", "つける": "switch on", "消える": "go out (light)", "消す": "switch off",
    "止まる": "stop (by itself)", "止める": "stop, park (something)", "決まる": "be decided", "決める": "decide",
    "集まる": "gather", "集める": "collect", "見つかる": "be found", "見つける": "find", "割れる": "break (glass)",
    "掛かる": "hang", "掛ける": "hang (something)", "変わる": "change (by itself)", "入れる": "put in", "入る": "enter",
    "書く": "write", "作る": "make", "割る": "break (something)", "並ぶ": "line up", "並べる": "line up (something)",
})

GUIDE["sprint_ta"] = ("た-form sprint", "The た-form is the て-form with た instead of て (だ instead of で).",
                      GUIDE["sprint_te"][2].replace("て-form", "た-form"))
drill_quiz("09_sprint_ta", "verbs-sprint-ta", "た-Form Sprint: 20 More Verbs",
           "The past tense follows the て-form groups exactly — now with verbs you haven't drilled yet.", "sprint_ta", [
    ("習う", "ta", "te-tte"), ("調べる", "ta", "te-ru"), ("置く", "ta", "te-ite"), ("頼む", "ta", "te-nde"),
    ("勝つ", "ta", "te-tte"), ("探す", "ta", "te-shite"), ("選ぶ", "ta", "te-nde"), ("答える", "ta", "te-ru"),
    ("脱ぐ", "ta", "te-ite"), ("払う", "ta", "te-tte"), ("住む", "ta", "te-nde"), ("心配する", "ta", "te-irr"),
    ("磨く", "ta", "te-ite"), ("渡す", "ta", "te-shite"), ("疲れる", "ta", "te-ru"), ("走る", "ta", "te-tte"),
    ("運ぶ", "ta", "te-nde"), ("行く", "ta", "te-irr"), ("笑う", "ta", "te-tte"), ("来る", "ta", "te-irr"),
], {**TE_TITLES, "te-irr": "Irregular: 行く → 行った, する → した, 来る → 来た"}, rule_hints=True)

drill_quiz("10_sprint_mixed", "verbs-sprint-mixed", "Mixed Sprint: Any Verb, Any Form",
           "24 verbs, each in a different form. Work out the type first, then the form — that's the real skill.", "mixed", [
    ("手伝う", "nai", "mixed"), ("考える", "masu", "mixed"), ("運ぶ", "potential", "mixed"), ("遅れる", "ta", "mixed"),
    ("結婚する", "volitional", "mixed"), ("渡す", "ba", "mixed"), ("間違える", "nakatta", "mixed"), ("習う", "volitional", "mixed"),
    ("帰る", "potential", "mixed"), ("着替える", "te", "mixed"), ("頼む", "passive_ta", "mixed"), ("思う", "masen", "mixed"),
    ("磨く", "causative_ta", "mixed"), ("知る", "te", "mixed"), ("答える", "ba", "mixed"), ("住む", "teiru", "mixed"),
    ("来る", "potential", "mixed"), ("探す", "volitional", "mixed"), ("入る", "nai", "mixed"), ("選ぶ", "masu", "mixed"),
    ("予約する", "ta", "mixed"), ("置く", "tara", "mixed"), ("笑う", "passive_ta", "mixed"), ("切る", "ba", "mixed"),
], {"mixed": "Mixed review"})


# ---------------------------------------------------------------- adjectives

ADJ_LABEL = {
    "a_plain": "plain present", "a_desu": "polite present", "a_neg": "plain negative", "a_neg_p": "polite negative",
    "a_past": "plain past", "a_past_p": "polite past", "a_pastneg": "plain past negative",
    "a_pastneg_p": "polite past negative", "a_te": "て-form (… and …)", "a_adv": "adverb (…ly / に・く)",
    "a_naru_ta": "became … (なった)", "a_sou": "looks … (そう)", "a_sugiru": "too … (すぎる)", "a_noun": "before a noun",
    "a_ba": "if … (ば / なら)",
}
LABEL.update(ADJ_LABEL)
NA_TRAPS = {"きれい", "嫌い", "有名", "丁寧"}  # な-adjectives that end in an い sound


def adj_forms(key):
    kanji, r, kind = ADJ[key]
    if kind == "na":
        b = r
        return {
            "a_plain": [b + "だ"], "a_desu": [b + "です"],
            "a_neg": [b + "じゃない", b + "ではない"],
            "a_neg_p": [b + "じゃないです", b + "じゃありません", b + "ではありません", b + "ではないです"],
            "a_past": [b + "だった"], "a_past_p": [b + "でした"],
            "a_pastneg": [b + "じゃなかった", b + "ではなかった"],
            "a_pastneg_p": [b + "じゃなかったです", b + "じゃありませんでした", b + "ではありませんでした", b + "ではなかったです"],
            "a_te": [b + "で"], "a_adv": [b + "に"], "a_naru_ta": [b + "になった"], "a_sou": [b + "そう"],
            "a_sugiru": [b + "すぎる"], "a_noun": [b + "な"], "a_ba": [b + "なら", b + "ならば", b + "であれば"],
        }
    stem = r[:-2] + "よ" if kind == "ii" else r[:-1]
    return {
        "a_plain": [r], "a_desu": [r + "です"], "a_neg": [stem + "くない"],
        "a_neg_p": [stem + "くないです", stem + "くありません"], "a_past": [stem + "かった"], "a_past_p": [stem + "かったです"],
        "a_pastneg": [stem + "くなかった"], "a_pastneg_p": [stem + "くなかったです", stem + "くありませんでした"],
        "a_te": [stem + "くて"], "a_adv": [stem + "く"], "a_naru_ta": [stem + "くなった"],
        "a_sou": [stem + ("さそう" if kind == "ii" else "そう")], "a_sugiru": [stem + "すぎる"], "a_noun": [r],
        "a_ba": [stem + "ければ"],
    }


ADJ_ENDING_I = {"a_neg": "くない", "a_neg_p": "くないです / くありません", "a_past": "かった", "a_past_p": "かったです",
                "a_pastneg": "くなかった", "a_pastneg_p": "くなかったです / くありませんでした", "a_te": "くて", "a_adv": "く",
                "a_naru_ta": "くなった", "a_sou": "そう", "a_sugiru": "すぎる", "a_ba": "ければ"}
ADJ_ENDING_NA = {"a_plain": "だ", "a_desu": "です", "a_neg": "じゃない (written: ではない)",
                 "a_neg_p": "じゃありません / じゃないです", "a_past": "だった", "a_past_p": "でした",
                 "a_pastneg": "じゃなかった", "a_pastneg_p": "じゃありませんでした / じゃなかったです", "a_te": "で",
                 "a_adv": "に", "a_naru_ta": "になった", "a_sou": "そう", "a_sugiru": "すぎる", "a_noun": "な",
                 "a_ba": "なら"}


def adj_explain(key, form, ans):
    kanji, r, kind = ADJ[key]
    v, a = ruby(key), f"**{ans}**"
    if kind == "na":
        why = f"{v} is a な-adjective: {kanji} + {ADJ_ENDING_NA[form]} → {a}."
        if key in NA_TRAPS:
            why += f" ⚠ It ends in an い sound, but that い is part of the word — {kanji} is a な-adjective (not {to_kanji(r[:-1] + 'くない', key)})."
        return why
    if form in ("a_plain", "a_desu", "a_noun"):
        return f"{v} is an い-adjective: {'it goes straight before a noun — no な' if form == 'a_noun' else 'the dictionary form'} → {a}."
    if kind == "ii":
        return f"{v} is irregular: every form except the present uses よ- instead of い- ({'かっこよ' if key != 'いい' else 'よ'} + {ADJ_ENDING_I[form]}) → {a}."
    return f"{v} is an い-adjective: drop the last い → {to_kanji(r[:-1], key) or r[:-1]} + {ADJ_ENDING_I[form]} → {a}."


def adj_accept(key, form):
    out = []
    for k in adj_forms(key)[form]:
        for x in (to_kanji(k, key), k):
            if x not in out:
                out.append(x)
    return out


def adj_build(key, form):
    accept = adj_accept(key, form)
    kana = adj_forms(key)[form][0]
    r = ADJ[key][1]
    n = 0
    while n < min(len(kana), len(r)) and kana[n] == r[n]:
        n += 1
    hint = kana[:max(1, min(n + 1, len(kana) - 1))]
    return accept, adj_explain(key, form, accept[0]), (to_kanji(hint, key) if n else hint) + "…"


def adj_wrong_forms(key, form, accept):
    kanji, r, kind = ADJ[key]
    taken = set(accept)
    out = {}
    for f, vals in adj_forms(key).items():
        if f != form and vals[0] not in taken:
            note = f"that's the {ADJ_LABEL[f]} form of {kanji}, but the cue asks for {ADJ_LABEL[form]}."
            out.setdefault(vals[0], note)
            out.setdefault(to_kanji(vals[0], key), note)
    # the other adjective type's pattern
    if form in ADJ_ENDING_I and form not in ("a_sou", "a_sugiru"):
        if kind == "na":
            base = r[:-1] if r.endswith("い") else r
            ending = ADJ_ENDING_I[form].split(" / ")[0]
            wrong = base + ending
            note = f"that's the い-adjective pattern, but {kanji} is a な-adjective: {kanji} + {ADJ_ENDING_NA[form].split(' (')[0]}."
        else:
            ending = ADJ_ENDING_NA.get(form, "").split(" (")[0].split(" / ")[0]
            wrong = r + ending
            note = (f"いい changes to よ- in every form but the present: {accept[0]}." if kind == "ii" else
                    f"that's the な-adjective pattern, but {kanji} is an い-adjective: drop い + {ADJ_ENDING_I[form].split(' / ')[0]}.")
        if wrong not in taken:
            out[wrong] = out[to_kanji(wrong, key)] = note
    if kind == "ii":
        wrong = r[:-1] + ADJ_ENDING_I.get(form, "").split(" / ")[0]
        if form in ADJ_ENDING_I and wrong not in taken:
            out[wrong] = f"いい is irregular: it uses よ- in every form except the present → {accept[0]}."
    return out


ADJ_TYPE_POINTS = {
    "adj-i": ("い-adjectives", "End in い and conjugate themselves: 高い → 高くない, 高かった."),
    "adj-na": ("な-adjectives", "Take な before a noun and だ / じゃない / だった after: 静かな町, 静かじゃない."),
    "adj-trap": ("な-adjectives that end in い", "きれい, 嫌い, 有名, 丁寧: the い belongs to the word, so they're な-adjectives."),
    "adj-ii": ("いい (and かっこいい)", "Irregular: よくない, よかった, よくて — every form except the present uses よ-."),
}
ADJ_BODY = """**Two kinds of adjectives**

- **い-adjectives** (高い, 新しい, おいしい) change their ending: drop い → 高**くない**, 高**かった**, 高**くなかった**, 高**くて**, 高**く** (adverb).
- **な-adjectives** (静か, 便利, 有名) never change; the words after them do: 静か**だ**, 静か**じゃない**, 静か**だった**, 静か**で**, 静か**に**, 静か**な**町.
- **Traps:** きれい, 嫌い, 有名, 丁寧 end in an い sound but are **な-adjectives** → きれいじゃない (not きれくない).
- **いい** is irregular: よくない, よかった, よくて, よさそう — only the present stays いい. かっこいい works the same way.

**Quick check:** before a noun, a な-adjective needs な (静か**な**部屋), an い-adjective doesn't (高い部屋)."""


def adj_type_q(key):
    kanji, r, kind = ADJ[key]
    v = ruby(key)
    p = "adj-ii" if kind == "ii" else "adj-trap" if key in NA_TRAPS else "adj-na" if kind == "na" else "adj-i"
    f = adj_forms(key)
    k = lambda form: to_kanji(f[form][0], key)
    shown = f"{k('a_neg')}, {k('a_past')}, {k('a_noun')}{'' if kind == 'na' else ''}"
    if kind == "na":
        ans = 1
        why = f"{v} is a な-adjective: {k('a_neg')}, {k('a_past')}, {k('a_noun')} + noun."
        if p == "adj-trap":
            why = f"Trap! {v} ends in an い sound, but it's a な-adjective: {k('a_neg')} (not {to_kanji(r[:-1] + 'くない', key)}), {k('a_noun')} + noun."
        notes = [f"An い-adjective would give {to_kanji((r[:-1] if r.endswith('い') else r) + 'くない', key)} — but it's {k('a_neg')}.", ""]
    else:
        ans = 0
        why = (f"{v} is an い-adjective, and an irregular one: {k('a_neg')}, {k('a_past')} — every form but the present uses よ-."
               if kind == "ii" else f"{v} is an い-adjective: drop い → {k('a_neg')}, {k('a_past')}; before a noun just {k('a_noun')} (no な).")
        notes = ["", f"A な-adjective would give {to_kanji(r + 'じゃない', key)} and {to_kanji(r + 'な', key)} + noun — but it's {k('a_neg')}."]
    return {"point": p, "prompt": f"い-adjective or な-adjective: **{v}**?",
            "options": ["い-adjective", "な-adjective"], "answer": ans, "fixed_order": True,
            "explanation": why, "notes": notes, "translation": ""}


def adj_types_quiz(fname, id, title, description, keys):
    questions = [adj_type_q(k) for k in keys]
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = [{"id": p, "title": ADJ_TYPE_POINTS[p][0], "summary": ADJ_TYPE_POINTS[p][1], "body": ADJ_BODY, "examples": []}
              for p in pids]
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}


adj_types_quiz("21_adj_types", "verbs-adj-types", "Adjective Types: い or な?",
               "Tell the two adjective types apart — including the な-adjectives that end in い.",
               ["高い", "静か", "きれい", "おいしい", "便利", "嫌い", "新しい", "有名", "いい", "元気", "楽しい", "丁寧",
                "かっこいい", "簡単", "暗い", "好き", "優しい", "大変"])

GUIDE["adj"] = ("Adjective forms", "い-adjectives change their ending; な-adjectives keep it and add だ / じゃない / な.", ADJ_BODY)
ADJ_SPRINT_TITLES = {"adj-i": "い-adjectives: drop い + ending", "adj-na": "な-adjectives: add だ / じゃない / だった",
                     "adj-ii": "いい → よ- (except the present)"}
drill_quiz("22_adj_sprint", "verbs-adj-sprint", "Adjective Sprint: Negative & Past",
           "18 adjectives, four forms: not …, was …, wasn't … — plain and polite.", "adj", [
    ("高い", "a_neg", "adj-i"), ("静か", "a_neg", "adj-na"), ("いい", "a_neg", "adj-ii"), ("寒い", "a_past", "adj-i"),
    ("便利", "a_past", "adj-na"), ("いい", "a_past", "adj-ii"), ("楽しい", "a_pastneg", "adj-i"), ("きれい", "a_neg", "adj-na"),
    ("忙しい", "a_neg_p", "adj-i"), ("有名", "a_pastneg", "adj-na"), ("おいしい", "a_past_p", "adj-i"),
    ("嫌い", "a_past", "adj-na"), ("かっこいい", "a_past", "adj-ii"), ("難しい", "a_pastneg_p", "adj-i"),
    ("暇", "a_neg_p", "adj-na"), ("大きい", "a_te", "adj-i"), ("元気", "a_te", "adj-na"), ("いい", "a_te", "adj-ii"),
], ADJ_SPRINT_TITLES, rule_hints=True)

quiz("23_adj_context", "verbs-adj-context", "Adjectives in Use: Reviews, Trips & Small Talk",
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
], pid_fn=lambda key, form: {"i": "ctx-i", "na": "ctx-na", "ii": "ctx-ii"}[ADJ[key][2]],
   titles={"ctx-i": "い-adjectives in context", "ctx-na": "な-adjectives in context", "ctx-ii": "いい in context"})


# ---------------------------------------------------------------- transitive / intransitive

PAIR = {}
for a, b in [("開く", "開ける"), ("閉まる", "閉める"), ("始まる", "始める"), ("壊れる", "壊す"), ("落ちる", "落とす"),
             ("つく", "つける"), ("消える", "消す"), ("止まる", "止める"), ("決まる", "決める"), ("集まる", "集める"),
             ("見つかる", "見つける"), ("入る", "入れる"), ("割れる", "割る"), ("掛かる", "掛ける"), ("変わる", "変える"), ("並ぶ", "並べる")]:
    PAIR[a], PAIR[b] = b, a
INTRANSITIVE = {"開く", "閉まる", "始まる", "壊れる", "落ちる", "つく", "消える", "止まる", "決まる", "集まる", "見つかる", "入る",
                "割れる", "掛かる", "変わる", "並ぶ"}

GUIDE["trans"] = ("Transitive & intransitive pairs", "Something happens (が + intransitive) or someone does it (を + transitive).",
                  "- **Intransitive** (自動詞): the thing itself is the subject, nobody acts on it — ドア**が開く**, 電気**が消える**.\n"
                  "- **Transitive** (他動詞): someone does it to something marked with を — ドア**を開ける**, 電気**を消す**.\n"
                  "- Typical pairs: 開く / 開ける, 閉まる / 閉める, 始まる / 始める, 壊れる / 壊す, 落ちる / 落とす, つく / つける, "
                  "消える / 消す, 止まる / 止める, 決まる / 決める, 集まる / 集める, 見つかる / 見つける, 入る / 入れる.\n"
                  "- Patterns that help: -aru ↔ -eru (始まる / 始める), -reru ↔ -su (壊れる / 壊す), -eru ↔ -asu (消える / 消す).\n\n"
                  "**Check:** is there a を? Then you need the transitive verb.")
GUIDE["state"] = ("ている or てある", "Both describe a state — てある says someone did it on purpose.",
                  "- **Intransitive + ている**: the state is just there — 窓**が開いている** (the window is open; maybe the wind did it).\n"
                  "- **Transitive + てある**: someone did it deliberately, usually for a reason — 窓**が開けてある** (someone has opened it, e.g. to air the room).\n"
                  "- てある only works with transitive verbs, and the thing becomes the subject with が.\n"
                  "- Transitive + **ている** is different again: 窓を開けている = someone *is opening* it right now.\n\n"
                  "**Look for clues** such as ために, もう, 準備, or 'nobody did it' (風で, いつの間にか).")


def pair_note(key, form, typed_key, typed_form):
    vi = key in INTRANSITIVE
    if typed_key != key:
        return (f"that's {typed_key} (transitive: someone does it to something with を). Here the subject just changes by itself, "
                f"so use the intransitive {key}." if vi else
                f"that's {typed_key} (intransitive: it happens by itself). Here someone does it to something, so use the transitive {key}.")
    return None


def pair_quiz(fname, id, title, description, guide, items, state=False):
    gt, gs, gb = GUIDE[guide]
    questions = []
    for sentence, key, form, en in items:
        accept, why, hint = build(key, form)
        partner = PAIR.get(key)
        cue = f"{ruby(key)} / {ruby(partner)}" if partner and (key in INTRANSITIVE) else (
            f"{ruby(partner)} / {ruby(key)}" if partner else ruby(key))
        label = "resulting state (ている or てある)" if state else LABEL[form]
        wf = wrong_forms(key, form, accept)
        if partner:
            for k2, f2 in ([(partner, "tearu" if form == "teiru" else "teiru"), (partner, form)] if state else [(partner, form)]):
                for kana in forms(VERBS[k2][1], VERBS[k2][2])[f2][:1]:
                    if kana in accept:
                        continue
                    if state and form == "teiru":
                        note = ("てある means someone did it on purpose — nothing suggests that here, so: intransitive + ている."
                                if f2 == "tearu" else
                                f"{to_kanji(kana, k2)} means someone is doing it right now; here the state is just there → intransitive {key} + ている.")
                    elif state:
                        note = ("てある only goes with transitive verbs." if f2 == "tearu" else
                                f"{to_kanji(kana, k2)} just describes the state; the sentence gives a reason someone did it → transitive {key} + てある.")
                    else:
                        note = pair_note(key, form, k2, f2)
                    wf[kana] = wf[to_kanji(kana, k2)] = note
        if state:  # same verb, wrong auxiliary
            other = "tearu" if form == "teiru" else "teiru"
            kana = forms(VERBS[key][1], VERBS[key][2])[other][0]
            note = ("てある only goes with transitive verbs." if form == "teiru" else
                    f"{to_kanji(kana, key)} means someone is doing it right now; for a finished, deliberate state use てある.")
            wf[kana] = wf[to_kanji(kana, key)] = note
        vi = key in INTRANSITIVE
        pid = (("state-teiru" if form == "teiru" else "state-tearu") if state else ("vi" if vi else "vt"))
        kind = "intransitive (it happens by itself, が)" if vi else "transitive (someone does it, を)"
        lead = (f"{ruby(key)} is {kind}. " if partner else "")
        if state:
            lead = (f"Nobody did this on purpose — the state is just there, so: intransitive {ruby(key)} + ている. "
                    if form == "teiru" else
                    f"The sentence gives a reason, so someone did it on purpose: transitive {ruby(key)} + てある. " if partner else
                    f"{ruby(key)} has no intransitive partner, so the result of someone's action is always + てある (書いてある = it's written there). ")
        questions.append({"point": pid, "prompt": f"{sentence}\n→ {cue} · {label}", "options": [], "answer": 0,
                          "accept": accept, "hint": hint, "explanation": lead + why, "notes": [], "translation": en,
                          "wrong_forms": wf})
    titles = {"vi": "Intransitive: it happens (が)", "vt": "Transitive: someone does it (を)",
              "state-teiru": "Intransitive + ている: the state is just there", "state-tearu": "Transitive + てある: done on purpose"}
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = [{"id": p, "title": titles[p], "summary": f"{gt}: {gs}", "body": gb, "examples": []} for p in pids]
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}


pair_quiz("31_pairs", "verbs-pairs", "Transitive or Intransitive: 開く or 開ける?",
          "Pick the right verb of the pair and put it in the right form — が and を are your clues.", "trans", [
    ("{授業|じゅぎょう}は9{時|じ}に（　）。", "始まる", "masu", "Class starts at nine."),
    ("{先生|せんせい}が{授業|じゅぎょう}を（　）。", "始める", "ta", "The teacher started the class."),
    ("{風|かぜ}でドアが（　）。", "開く", "ta", "The door blew open in the wind."),
    ("{暑|あつ}いので、{窓|まど}を（　）ください。", "開ける", "tekudasai", "It's hot — please open the window."),
    ("{棚|たな}からコップが（　）。", "落ちる", "ta", "A glass fell off the shelf."),
    ("{駅|えき}で{財布|さいふ}を（　）しまった。", "落とす", "te", "I dropped my wallet at the station."),
    ("{急|きゅう}に{部屋|へや}の{電気|でんき}が（　）。", "消える", "ta", "Suddenly the light in the room went out."),
    ("{寝|ね}る{前|まえ}に{電気|でんき}を（　）ください。", "消す", "tekudasai", "Please switch off the light before you go to bed."),
    ("{古|ふる}いパソコンがとうとう（　）。", "壊れる", "ta", "The old computer finally broke."),
    ("{弟|おとうと}が{私|わたし}のカメラを（　）。", "壊す", "ta", "My little brother broke my camera."),
    ("{会議|かいぎ}の{日|ひ}がやっと（　）。", "決まる", "ta", "The date of the meeting has finally been decided."),
    ("{旅行|りょこう}の{行|い}き{先|さき}を{一緒|いっしょ}に（　）。", "決める", "mashou", "Let's decide where to go on our trip together."),
    ("{駅|えき}の{前|まえ}に{人|ひと}がたくさん（　）。", "集まる", "teiru", "Lots of people have gathered in front of the station."),
    ("{趣味|しゅみ}は{切手|きって}を（　）ことです。", "集める", "dict", "My hobby is collecting stamps."),
    ("なくした{鍵|かぎ}がやっと（　）。", "見つかる", "ta", "The key I lost has finally turned up."),
    ("いいアパートを（　）のは{大変|たいへん}です。", "見つける", "dict", "Finding a good flat is hard work."),
    ("{次|つぎ}の{駅|えき}で{電車|でんしゃ}が{少|すこ}し（　）。", "止まる", "masu", "The train stops briefly at the next station."),
    ("ここに{車|くるま}を（　）はいけません。", "止める", "te", "You mustn't park here."),
])

pair_quiz("32_state", "verbs-state", "ている or てある: Describing a State",
          "Is it just open, or has someone opened it on purpose? Choose the verb and the ending.", "state", [
    ("{風|かぜ}で{窓|まど}が（　）。", "開く", "teiru", "The window is open — the wind blew it open."),
    ("{空気|くうき}を{入|い}れ{替|か}えるために、{窓|まど}が（　）。", "開ける", "tearu", "The window has been opened to air the room."),
    ("{誰|だれ}もいないのに、{電気|でんき}が（　）。", "つく", "teiru", "The light is on although nobody's there."),
    ("{夜|よる}{遅|おそ}く{帰|かえ}る{子供|こども}のために、{玄関|げんかん}の{電気|でんき}が（　）。", "つける", "tearu", "The hall light has been left on for the child coming home late."),
    ("パーティーのために、{飲|の}み{物|もの}が{冷蔵庫|れいぞうこ}に（　）。", "入れる", "tearu", "The drinks have been put in the fridge for the party."),
    ("{箱|はこ}の{中|なか}に{何|なに}か（　）よ。", "入る", "teiru", "There's something in the box."),
    ("{予定|よてい}を{忘|わす}れないように、{壁|かべ}にカレンダーが（　）。", "掛ける", "tearu", "A calendar has been hung on the wall so I don't forget my plans."),
    ("{道|みち}が{混|こ}んでいて、{車|くるま}がたくさん（　）。", "止まる", "teiru", "The road is jammed and lots of cars are standing still."),
    ("{店|みせ}の{前|まえ}に「{駐車禁止|ちゅうしゃきんし}」と（　）。", "書く", "tearu", "In front of the shop it says 'No parking'."),
    ("コップが（　）から、{気|き}をつけて。", "割れる", "teiru", "The glass is broken, so be careful."),
    ("{明日|あした}の{会議|かいぎ}のために、{資料|しりょう}がもう（　）。", "作る", "tearu", "The materials for tomorrow's meeting have already been prepared."),
    ("{道|みち}に{財布|さいふ}が（　）。", "落ちる", "teiru", "There's a wallet lying on the road."),
    ("{会議|かいぎ}のために、{椅子|いす}がきれいに（　）。", "並べる", "tearu", "The chairs have been set out neatly for the meeting."),
    ("いつの{間|ま}にか{店|みせ}のドアが（　）。", "閉まる", "teiru", "Before we knew it, the shop door was shut."),
], state=True)


# ---------------------------------------------------------------- deep dive: can (potential) & will (volitional)

VERBS.update({"受ける": ("受ける", "うける", "ru"), "やる": ("やる", "やる", "u"), "頑張る": ("頑張る", "がんばる", "u"),
              "散歩する": ("散歩する", "さんぽする", "suru")})
GLOSS.update({"受ける": "take (an exam)", "やる": "do", "頑張る": "do one's best", "散歩する": "go for a walk"})

POT_TITLES = {"pot-u": "う-verbs: え-row + る (書ける)", "pot-ru": "る-verbs: drop る + られる (食べられる)",
              "pot-irr": "Irregular: する → できる, 来る → 来られる"}
VOL_TITLES = {"vol-u": "う-verbs: お-row + う (書こう)", "vol-ru": "る-verbs: drop る + よう (食べよう)",
              "vol-irr": "Irregular: する → しよう, 来る → 来よう"}


def grp(key, prefix):
    cls = VERBS[key][2]
    return f"{prefix}-{'irr' if cls in ('suru', 'kuru') else 'ru' if cls == 'ru' else 'u'}"


drill_quiz("14a_can_form", "verbs-can-form", "Step 1 · Making 'can' (読める)",
           "Dictionary form → potential (読む → 読める). One rule per verb group — the hint shows it.", "potvol",
           [(k, "potential", grp(k, "pot")) for k in
            ["書く", "読む", "食べる", "話す", "見る", "する", "待つ", "起きる", "泳ぐ", "来る", "買う", "寝る",
             "帰る", "着る", "遊ぶ", "勉強する"]], POT_TITLES, rule_hints=True)

quiz("14b_can_polite", "verbs-can-polite", "Step 2 · I can / I can't (話せます)",
     "Talking about abilities and rules politely: 話せます, 読めません.", "potvol", [
    ("{私|わたし}は{日本語|にほんご}が{少|すこ}し（　）。", "話す", "potential_masu", "I can speak a little Japanese."),
    ("{漢字|かんじ}はまだあまり（　）。", "読む", "potential_masen", "I can't read many kanji yet."),
    ("この{川|かわ}では（　）。{危|あぶ}ないですから。", "泳ぐ", "potential_masen", "You can't swim in this river — it's dangerous."),
    ("{明日|あした}のパーティーに（　）か。", "来る", "potential_masu", "Can you come to the party tomorrow?"),
    ("{辛|から}い{物|もの}は（　）か。", "食べる", "potential_masu", "Can you eat spicy food?"),
    ("{最近|さいきん}、{夜|よる}あまり（　）。", "寝る", "potential_masen", "Lately I can't sleep well at night."),
    ("{車|くるま}の{運転|うんてん}が（　）か。", "する", "potential_masu", "Can you drive?"),
    ("{一人|ひとり}で{着物|きもの}が（　）。", "着る", "potential_masu", "I can put on a kimono by myself."),
    ("{今週|こんしゅう}は{忙|いそが}しくて、{会|あ}いに（　）。", "行く", "potential_masen", "I'm busy this week, so I can't come and see you."),
    ("{明日|あした}、{朝|あさ}{六時|ろくじ}に（　）か。", "起きる", "potential_masu", "Can you get up at six tomorrow morning?"),
    ("{自転車|じてんしゃ}に（　）か。", "乗る", "potential_masu", "Can you ride a bike?"),
    ("この{水|みず}は（　）。", "飲む", "potential_masen", "You can't drink this water."),
], pid_fn=lambda key, form: "can-yes" if form == "potential_masu" else "can-no",
   titles={"can-yes": "Can (〜られます / 〜えます)", "can-no": "Can't (〜られません / 〜えません)"})

drill_quiz("14c_will_form", "verbs-will-form", "Step 3 · Making 'let's / I'll' (読もう)",
           "Dictionary form → volitional (読む → 読もう). The plain version of ましょう.", "potvol",
           [(k, "volitional", grp(k, "vol")) for k in
            ["行く", "食べる", "書く", "見る", "飲む", "する", "話す", "寝る", "待つ", "来る", "遊ぶ", "始める",
             "帰る", "頑張る", "買う", "散歩する"]], VOL_TITLES, rule_hints=True)

quiz("14d_will_uses", "verbs-will-uses", "Step 4 · Let's, I'll, I was about to",
     "What the volitional does: invitations (休もうか), plans (〜ようと思う), 'was about to' (〜ようとしたら), offers (ましょうか).", "potvol", [
    ("{疲|つか}れたね。ちょっと（　）か。", "休む", "volitional", "We're tired — shall we take a short break?"),
    ("{週末|しゅうまつ}、{一緒|いっしょ}に{映画|えいが}を（　）よ。", "見る", "volitional", "Let's watch a film together at the weekend."),
    ("{今年|ことし}こそ{日本語|にほんご}の{試験|しけん}を（　）と{思|おも}います。", "受ける", "volitional", "This year I think I'll finally take the Japanese exam."),
    ("{来年|らいねん}から{日本|にほん}に（　）と{思|おも}っています。", "住む", "volitional", "I'm planning to live in Japan from next year."),
    ("{新|あたら}しいパソコンを（　）と{思|おも}っている。", "買う", "volitional", "I'm thinking of buying a new computer."),
    ("{家|いえ}を（　）としたら、{雨|あめ}が{降|ふ}ってきた。", "出る", "volitional", "Just as I was about to leave the house, it started to rain."),
    ("{寝|ね}る{前|まえ}に{本|ほん}を（　）としたら、{電気|でんき}が{消|き}えた。", "読む", "volitional", "Just as I was about to read before bed, the lights went out."),
    ("{重|おも}そうですね。{荷物|にもつ}を（　）か。", "持つ", "mashou", "That looks heavy — shall I carry your bag?"),
    ("もう{遅|おそ}いですね。そろそろ（　）。", "帰る", "mashou", "It's late. Let's head home soon."),
    ("{毎日|まいにち}{少|すこ}しずつ（　）。", "練習する", "volitional", "Let's practise a little every day."),
    ("{明日|あした}は{試験|しけん}だから、{早|はや}く（　）。", "寝る", "volitional", "I've got an exam tomorrow, so I'll go to bed early."),
    ("{今度|こんど}の{休|やす}みは{何|なに}を（　）かな。", "する", "volitional", "What shall I do next holiday?"),
    ("{失敗|しっぱい}しても{大丈夫|だいじょうぶ}。もう{一度|いちど}（　）！", "やる", "volitional", "It's fine to fail. Let's try once more!"),
    ("{来週|らいしゅう}、{田中|たなか}さんにもう{一度|いちど}（　）と{思|おも}います。", "会う", "volitional", "I think I'll meet Tanaka once more next week."),
], pid_fn=lambda key, form: "will-polite" if form == "mashou" else "will-plain",
   titles={"will-plain": "Volitional: let's / I'll / was about to", "will-polite": "Polite: ましょう / ましょうか"})


def choice_quiz(fname, id, title, description, guide, items):
    """The cue doesn't say which form: the sentence has to tell you whether it's 'can' or 'let's / I'll'."""
    gt, gs, gb = GUIDE[guide]
    questions = []
    for sentence, key, form, en in items:
        accept, why, hint = build(key, form)
        can = form.startswith("potential")
        wf = wrong_forms(key, form, accept)
        fk = forms(VERBS[key][1], VERBS[key][2])
        others = ["volitional", "mashou"] if can else ["potential", "potential_masu", "potential_masen"]
        for f2 in others:
            kana = fk[f2][0]
            note = (f"that's the volitional ('let's / I'll'), but this sentence is about being able to → potential."
                    if can else
                    f"that's the potential ('can'), but this sentence is about a plan or an invitation → volitional.")
            wf[kana] = wf[to_kanji(kana, key)] = note
        lead = ("Ability / possibility → potential ('can'). " if can else "Plan / invitation → volitional ('let's / I'll'). ")
        hint = "Ability, possibility, rules (ようになる, ません, でも) → can · plan, invitation, decision (さあ, と決めた, としたら) → let's / I'll"
        questions.append({"point": "can" if can else "will",
                          "prompt": f"{sentence}\n→ {ruby(key)} · can … or let's / I'll …? (the sentence decides)",
                          "options": [], "answer": 0, "accept": accept, "hint": hint, "explanation": lead + why,
                          "notes": [], "translation": en, "wrong_forms": wf})
    titles = {"can": "Potential: ability, possibility, rules", "will": "Volitional: plans, invitations, decisions"}
    pids = list(dict.fromkeys(q["point"] for q in questions))
    points = [point_entry(p, titles[p], guide, []) for p in pids]
    QZ[fname] = {"id": id, "category": "Verb Lab", "title": title, "description": description,
                 "level": "Verbs", "points": points, "questions": questions}


choice_quiz("14e_can_or_will", "verbs-can-or-will", "Step 5 · Can or let's? The sentence decides",
            "The cue no longer tells you the form — read the sentence and decide: ability or plan?", "potvol", [
    ("{漢字|かんじ}が{少|すこ}し（　）ようになりました。", "読む", "potential", "I've become able to read a few kanji."),
    ("さあ、この{本|ほん}を{一緒|いっしょ}に（　）！", "読む", "volitional", "Come on, let's read this book together!"),
    ("{明日|あした}は{試験|しけん}だから、{早|はや}く（　）と{決|き}めた。", "起きる", "volitional", "I've got an exam tomorrow, so I decided to get up early."),
    ("{目覚|めざ}まし{時計|どけい}がなくても、{六時|ろくじ}に（　）か。", "起きる", "potential_masu", "Can you get up at six even without an alarm clock?"),
    ("{疲|つか}れたね。さあ、（　）。", "帰る", "volitional", "We're tired. Come on, let's go home."),
    ("{仕事|しごと}が{多|おお}くて、{今日|きょう}は{早|はや}く（　）。", "帰る", "potential_masen", "There's a lot of work, so I can't go home early today."),
    ("さあ、{一緒|いっしょ}に{晩|ばん}ご{飯|はん}を（　）。", "作る", "volitional", "Come on, let's make dinner together."),
    ("{彼女|かのじょ}は{料理|りょうり}が{上手|じょうず}で、{何|なん}でも（　）。", "作る", "potential", "She's a good cook — she can make anything."),
    ("{暑|あつ}いね。さあ、{海|うみ}で（　）！", "泳ぐ", "volitional", "It's hot! Come on, let's swim in the sea!"),
    ("{子供|こども}でも{簡単|かんたん}に（　）{歌|うた}です。", "歌う", "potential", "It's a song even children can sing easily."),
    ("{歌|うた}を（　）としたら、{声|こえ}が{出|で}なかった。", "歌う", "volitional", "When I tried to sing, no sound came out."),
    ("ここではタバコは（　）。", "吸う", "potential_masen", "You can't smoke here."),
    ("{日本|にほん}では{日本語|にほんご}だけで（　）と{決|き}めています。", "話す", "volitional", "I've made up my mind to speak only Japanese in Japan."),
    ("{日本語|にほんご}で{電話|でんわ}が（　）ようになった。", "する", "potential", "I've become able to make phone calls in Japanese."),
])


def write(folder):
    os.makedirs(folder, exist_ok=True)
    for f in os.listdir(folder):
        if f.endswith(".json"):
            os.remove(os.path.join(folder, f))
    for fname, d in sorted(QZ.items()):
        cnt = collections.Counter(q["point"] for q in d["questions"])
        assert {p["id"] for p in d["points"]} == set(cnt) and (d["id"] == "verbs-mixed" or min(cnt.values()) >= 2), (fname, cnt)
        for q in d["questions"]:
            if q["options"]:
                assert q["notes"][q["answer"]] == "" and all(n for i, n in enumerate(q["notes"]) if i != q["answer"]), q["prompt"]
            else:
                assert q["accept"] and "（　）" in q["prompt"], q["prompt"]
        with open(f"{folder}/{fname}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print(f"{fname:16} {len(d['points'])} pts {len(d['questions'])} Q")


if __name__ == "__main__":
    write("quizzes/06_verbs")
