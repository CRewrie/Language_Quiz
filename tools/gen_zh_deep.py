"""Generates quizzes/54_zh_deep/*.json: Mandarin deep dives, one grammar point through several steps (run from the repo root).

Each deep dive builds the point up step by step (meaning → contrast → the tricky case → mixed drill → production →
a story to finish), with the same overview table in every guide, so a learner can open any step and see the big picture.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from zhquiz import zh, P, Q, star, tf, reading, write

QZ = {}


def quiz(fname, id, title, description, points, questions):
    QZ[fname] = {"id": id, "title": title, "description": description, "points": points, "questions": questions}


YES, NO = "✔ Yes — it happened", "✘ No — it didn't happen"


def did(point, sentence, question, happened, why, translation):
    """'Did it happen?': the core skill for 差点 / 差点没."""
    return Q(point, "「" + zh(sentence) + "」\n" + question, [YES, NO],
             ["", why] if happened else [why, ""], why, translation, answer=0 if happened else 1, fixed=True, raw_opts=True)


# ================================================================ 差点 vs 差点没
TABLE = """**The whole picture: 差点 vs 差点没**

| | 😅 unwanted (摔倒) | 🎯 wanted (赶上) |
|---|---|---|
| **差点** | didn't happen | didn't happen 😢 |
| **差点没** | didn't happen (same!) | **did** happen 🎉 |

**Two questions decide it**
1. Is the event something the speaker **wants** (赶上, 考上, 买到) or **doesn't want** (摔倒, 迟到, 丢)?
2. Unwanted → it **didn't happen**, with or without 没. Wanted → 差点 = didn't happen, 差点没 = **did** happen.

**Memory hooks**
- 坏事加「没」，意思不变 — for bad things, 没 changes nothing.
- 好事加「没」，意思反转 — for good things, 没 flips it.

**Mood words give it away**
- Relief (it went well): **幸亏 / 还好 / 好在** (luckily), **总算** (in the end), **好险** (that was close!)
- Regret (it didn't): **可惜** (what a pity), **就差一点** (just a tiny bit short), **真遗憾** (what a shame)"""


def p(id, title, summary, body, examples):
    return P(id, title, summary, body + "\n\n" + TABLE, examples)


# ---------------------------------------------------------------- step 1
quiz("01_chadian_1", "zh-dd-chadian-1", "差点 Step 1 · Phew, Almost! The Basic 差点",
     "差点 + verb = it came this close — but didn't happen. Where 差点 goes, 差点儿 and 差一点, and the dramatic 差点就…了.",
     [p("s1_meaning", "差点 + verb: almost (but it didn't happen)",
        "差点 (chàdiǎn, 'short by a little') + verb = it nearly happened, but in the end it didn't.",
        "Picture a goalkeeper: the ball **almost** goes in — 差一点 — and then it doesn't.\n\n"
        "- 我**差点**摔倒。 I almost fell. (I didn't.)\n- 他**差点**迟到。 He was almost late. (He made it.)\n- 我**差点**忘了！ I almost forgot! (I remembered.)",
        [("地上/dìshang 很/hěn 滑/huá ， 我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。", "The floor was slippery — I almost fell.")]),
      p("s1_shape", "Where it goes: subject + 差点(儿) + (就) + verb (+ 了)",
        "Like other adverbs, 差点 sits after the subject and before the verb. 差点儿 and 差一点 mean the same.",
        "- 差点儿 (chàdiǎnr) is the northern, spoken form; 差一点(儿) sounds a little more emphatic.\n"
        "- For drama, add 就 … 了: 我**差点儿就**迟到**了**！\n- Never after the verb: ~~我摔倒差点~~.",
        [("他/tā 差点儿/chàdiǎnr 就/jiù 迟到/chídào 了/le 。", "He very nearly was late.")])],
     [Q("s1_meaning", "What does 「" + zh("我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。") + "」 mean?",
        ["I almost fell — but I didn't.", "I fell a little.", "I fell badly.", "I'm about to fall."],
        ["", "差点 isn't 'a little' — it means 'almost'.", "差点 = it didn't happen.", "That's 我快要摔倒了."],
        "差点 + verb = **almost** — it didn't happen.", "I almost fell.", raw_opts=True),
      did("s1_meaning", "他/tā 差点/chàdiǎn 迟到/chídào 。", "Was he late?", False,
          "差点迟到 = almost late — he made it in time. 😅", "He was almost late."),
      Q("s1_meaning", zh("地上/dìshang 都/dōu 是/shì 水/shuǐ ， 我/wǒ （　） 摔倒/shuāidǎo 了/le 。"), ["差点/chàdiǎn", "差不多/chàbuduō", "一点/yìdiǎn", "终于/zhōngyú"],
        ["", "差不多 = 'roughly, about' — not 'almost (happened)'.", "一点 = 'a little' — 摔倒一点 isn't a thing.", "终于 = 'finally' — as if you'd been hoping to fall!"],
        "Almost (but didn't): **差点**.", "There was water all over the floor — I almost fell."),
      Q("s1_meaning", zh("我/wǒ （　） 忘/wàng 了/le 今天/jīntiān 是/shì 妈妈/māma 的/de 生日/shēngrì ！ 还好/háihǎo 想/xiǎng 起来/qǐlai 了/le 。"),
        ["差点/chàdiǎn", "已经/yǐjīng", "一点儿/yìdiǎnr", "差不多/chàbuduō"],
        ["", "已经忘了 = 'I've already forgotten' — but you remembered in time.", "一点儿 doesn't go before a verb like this.", "差不多忘了 = 'more or less forgot' — wrong idea."],
        "Remembered in the end → **差点**忘了.", "I almost forgot it's Mum's birthday today! Luckily I remembered."),
      did("s1_meaning", "手机/shǒujī 差点/chàdiǎn 掉/diào 进/jìn 水/shuǐ 里/li 。", "Did the phone fall into the water?", False,
          "差点掉进水里 = almost fell in — it's still dry. 😅", "The phone almost fell into the water."),
      Q("s1_meaning", "What does 「" + zh("这/zhè 道/dào 题/tí 太/tài 难/nán 了/le ， 我/wǒ 差点/chàdiǎn 放弃/fàngqì 。") + "」 mean?",
        ["The problem was so hard I almost gave up (but I kept going).", "The problem was so hard I gave up.", "I gave up a little on the problem.", "I'm going to give up soon."],
        ["", "差点 = it didn't happen — you kept going.", "差点 isn't 'a little'.", "That would be 我快要放弃了."],
        "差点放弃 = **almost** gave up.", "This problem is so hard I almost gave up.", raw_opts=True),
      star("s1_shape", "他/tā ＿ ＿ ★ ＿ 。", ["了/le", "迟到/chídào", "就/jiù", "差点儿/chàdiǎnr"],
           ["迟到/chídào", "差点儿/chàdiǎnr", "就/jiù", "了/le"],
           ["", "差点儿 comes first, right after the subject — slot 1.", "就 follows 差点儿 — slot 2.", "了 closes the sentence — slot 4."],
           "他 **差点儿 就 迟到 了**。", "He very nearly was late."),
      Q("s1_shape", "Which sentence is correct?",
        ["我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。", "我/wǒ 摔倒/shuāidǎo 差点/chàdiǎn 了/le 。", "我/wǒ 摔/shuāi 差点/chàdiǎn 倒/dǎo 了/le 。", "我/wǒ 差点/chàdiǎn 了/le 摔倒/shuāidǎo 。"],
        ["", "差点 goes **before** the verb.", "差点 can't split 摔倒.", "了 comes after the verb, not after 差点."],
        "Subject + **差点** + verb (+ 了).", "I almost fell."),
      Q("s1_shape", "Which sentence means the same as 「" + zh("我/wǒ 差点儿/chàdiǎnr 哭/kū 了/le 。") + "」?",
        ["我/wǒ 差一点/chà yìdiǎn 哭/kū 了/le 。", "我/wǒ 哭/kū 了/le 一点/yìdiǎn 。", "我/wǒ 快/kuài 要/yào 哭/kū 了/le 。", "我/wǒ 哭/kū 了/le 一下/yíxià 。"],
        ["", "哭了一点 = 'cried a little' — you did cry.", "快要哭了 = 'about to cry' (right now), not 'almost cried'.", "哭了一下 = 'cried for a moment' — you did cry."],
        "差点儿 = 差一点 = **almost**.", "I almost cried."),
      Q("s1_shape", zh("好险/hǎo xiǎn ！ 我/wǒ 差点/chàdiǎn （　） 撞/zhuàng 到/dào 那/nà 辆/liàng 车/chē 了/le 。"), ["就/jiù", "才/cái", "都/dōu", "还/hái"],
        ["", "才 = 'only then / not until' — doesn't go with 差点.", "都 doesn't fit here.", "还 = 'still' — doesn't fit."],
        "The dramatic pattern: 差点 + **就** + verb + 了.", "That was close! I very nearly hit that car."),
      Q("s1_shape", "You nearly missed the train (but caught it). Which sentence says so?",
        ["我/wǒ 差点/chàdiǎn 错过/cuòguò 火车/huǒchē 。", "我/wǒ 错过/cuòguò 火车/huǒchē 一点/yìdiǎn 。", "我/wǒ 差不多/chàbuduō 错过/cuòguò 火车/huǒchē 。", "我/wǒ 错过/cuòguò 火车/huǒchē 差点/chàdiǎn 。"],
        ["", "错过…一点 = 'missed it a little' — not a thing.", "差不多 = 'roughly' — not 'almost (happened)'.", "差点 goes before the verb."],
        "**差点**错过 = almost missed.", "I almost missed the train."),
      Q("s1_shape", zh("A： 你/nǐ 的/de 钱包/qiánbāo 呢/ne ？ // B： 在/zài 这儿/zhèr ， 刚才/gāngcái （　） 丢/diū 了/le ！"), ["差点/chàdiǎn", "已经/yǐjīng", "一点/yìdiǎn", "终于/zhōngyú"],
        ["", "已经丢了 = 'already lost' — but it's right here.", "一点丢了 isn't Chinese.", "终于丢了 = 'finally lost it' — as if you wanted to!"],
        "It's still here → **差点**丢了.", "A: Where's your wallet? B: Here — I almost lost it just now!")])

# ---------------------------------------------------------------- step 2
quiz("02_chadian_2", "zh-dd-chadian-2", "差点 Step 2 · The 没 That Changes Nothing: 差点没 + Bad Things",
     "The famous puzzle: with things nobody wants (falling, being late, forgetting), 差点 and 差点没 mean exactly the same.",
     [p("s2_same", "Bad events: 差点 = 差点没",
        "With unwanted events, adding 没 changes nothing: 我差点摔倒 = 我差点没摔倒 — I almost fell, and didn't.",
        "Here's the puzzle: 没 means 'not' — so why doesn't it flip the meaning?\n\n"
        "Because nobody **wants** to fall. Whether you say 'almost fell' or 'very nearly didn't-not-fall', the picture is the same: "
        "the bad thing came close and missed you. 😅 The 没 just adds feeling — it sounds more dramatic.\n\n"
        "- 我差点摔倒 = 我差点**没**摔倒 → I almost fell.\n- 他差点迟到 = 他差点**没**迟到 → he was almost late.\n"
        "- Word order: 差点**没** — never ~~没差点~~.",
        [("我/wǒ 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。", "I almost fell. (= 我差点摔倒)")]),
      p("s2_bad", "Spotting a bad (unwanted) event",
        "Ask: would anyone hope for this? 摔倒, 迟到, 忘, 丢, 撞车, 哭出来, 笑出来 (at the wrong moment), 吵架 …",
        "- Typical unwanted events: 摔倒 (fall), 迟到 (be late), 忘 (forget), 丢 (lose), 撞车 (crash), 生病 (get ill), "
        "哭出来 (burst into tears), 笑出来 (burst out laughing at the wrong moment), 吵起来 (start a quarrel).\n"
        "- Spoken exaggerations love 差点没: 差点没**饿死** (I nearly starved!), 差点没**笑死** (I nearly died laughing!), 差点没**气死** (I was furious!). Of course nobody died. 😄",
        [("这个/zhège 电影/diànyǐng 太/tài 好笑/hǎoxiào 了/le ， 我/wǒ 差点/chàdiǎn 没/méi 笑死/xiào sǐ 。", "The film was so funny I nearly died laughing.")])],
     [Q("s2_same", "「" + zh("我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 。") + "」 and 「" + zh("我/wǒ 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。") + "」 — do they mean the same?",
        ["Yes — both: I almost fell, but didn't.", "No — the second means I did fall.", "No — the second means I wasn't even close to falling."],
        ["", "摔倒 is unwanted, so 没 doesn't flip it — you didn't fall.", "差点没 still says it came close."],
        "Unwanted event: **差点 = 差点没**. 坏事加「没」，意思不变.", "I almost fell.", fixed=True, raw_opts=True),
      did("s2_same", "他/tā 差点/chàdiǎn 没/méi 迟到/chídào 。", "Was he late?", False,
          "迟到 is unwanted → 差点没迟到 = 差点迟到 = he made it in time. 😅", "He was almost late."),
      did("s2_bad", "开会/kāihuì 的/de 时候/shíhou ， 我/wǒ 差点/chàdiǎn 没/méi 笑/xiào 出来/chūlai 。", "Did I burst out laughing in the meeting?", False,
          "Laughing out loud in a meeting is unwanted → 差点没笑出来 = I almost laughed, but held it in. 😅", "I almost burst out laughing in the meeting."),
      Q("s2_bad", "What does 「" + zh("昨天/zuótiān 我/wǒ 差点/chàdiǎn 没/méi 饿死/è sǐ 。") + "」 mean?",
        ["I was starving yesterday! (exaggeration)", "I wasn't hungry at all yesterday.", "I almost didn't eat yesterday.", "I ate too much yesterday."],
        ["", "差点没饿死 = I nearly starved — very hungry, not 'not hungry'.", "It's about starving, not about eating.", "That would be 吃得太多了."],
        "饿死 is unwanted → 差点没饿死 = **nearly starved** (spoken exaggeration).", "I nearly starved yesterday.", raw_opts=True),
      Q("s2_same", "In which sentence does 没 change **nothing**?",
        ["我/wǒ 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。", "我/wǒ 差点/chàdiǎn 没/méi 考上/kǎoshàng 大学/dàxué 。", "我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 票/piào 。", "我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 飞机/fēijī 。"],
        ["", "考上 is something you want — there 没 does flip it (step 4).", "买到票 is wanted — there 没 flips it (step 4).", "赶上 is wanted — there 没 flips it (step 4)."],
        "Only the unwanted event (**摔倒**) ignores the 没.", "I almost fell."),
      Q("s2_same", "Which sentence means the same as 「" + zh("我/wǒ 差点/chàdiǎn 哭/kū 了/le 。") + "」?",
        ["我/wǒ 差点/chàdiǎn 没/méi 哭/kū 。", "我/wǒ 哭/kū 了/le 。", "我/wǒ 差点/chàdiǎn 想/xiǎng 哭/kū 。", "我/wǒ 没/méi 差点/chàdiǎn 哭/kū 。"],
        ["", "That says you did cry.", "差点想哭 isn't natural.", "没 must come after 差点: 差点没."],
        "Crying is unwanted here → 差点哭了 = **差点没哭**.", "I almost cried."),
      Q("s2_bad", zh("太/tài 危险/wēixiǎn 了/le ！ 刚才/gāngcái 我们/wǒmen 差点/chàdiǎn 没/méi （　） ！"), ["撞车/zhuàngchē", "买到/mǎidào", "考上/kǎoshàng", "赢/yíng"],
        ["", "买到 is something you want — doesn't fit 'dangerous'.", "考上 doesn't fit 'dangerous'.", "赢 doesn't fit 'dangerous'."],
        "Danger → an unwanted event: **撞车** (crash). 差点没撞车 = almost crashed.", "That was dangerous! We almost crashed just now!"),
      Q("s2_same", zh("A： 听说/tīngshuō 你/nǐ 昨天/zuótiān 差点/chàdiǎn 没/méi 迟到/chídào ？ // B： 是/shì 啊/a ， （　） 。"),
        ["还好/háihǎo 最后/zuìhòu 赶上/gǎnshàng 了/le", "我/wǒ 迟到/chídào 了/le 一个/yí ge 小时/xiǎoshí", "我/wǒ 很/hěn 早/zǎo 就/jiù 到/dào 了/le", "我/wǒ 不/bù 想/xiǎng 去/qù"],
        ["", "差点没迟到 = you weren't late.", "差点 means it was close — not early and relaxed.", "That doesn't answer the question."],
        "差点没迟到 = almost late, **made it** → 还好最后赶上了.", "A: I heard you were almost late yesterday? B: Yes — luckily I made it in the end."),
      did("s2_bad", "他/tā 差点/chàdiǎn 没/méi 把/bǎ 杯子/bēizi 打破/dǎpò 。", "Did he break the cup?", False,
          "Breaking a cup is unwanted → 差点没打破 = he almost broke it. 😅", "He almost broke the cup."),
      Q("s2_same", "「" + zh("我/wǒ 差点/chàdiǎn 忘/wàng 了/le 。") + "」 vs 「" + zh("我/wǒ 差点/chàdiǎn 没/méi 忘/wàng 了/le 。") + "」 — what's the difference?",
        ["None in meaning — the 没 version just sounds more dramatic.", "The 没 version means I forgot.", "The 没 version means I remembered easily.", "The 没 version is a question."],
        ["", "Forgetting is unwanted → 没 changes nothing.", "差点 still means it was close.", "There's no question word or 吗."],
        "Unwanted event: same meaning; 没 adds **emphasis**.", "I almost forgot.", raw_opts=True),
      Q("s2_bad", "What does 「" + zh("这个/zhège 电影/diànyǐng 太/tài 好笑/hǎoxiào 了/le ， 我/wǒ 差点/chàdiǎn 没/méi 笑死/xiào sǐ 。") + "」 mean?",
        ["The film was so funny I nearly died laughing.", "The film wasn't funny at all.", "I almost didn't laugh at the film.", "I laughed so much I died."],
        ["", "太好笑了 = very funny.", "笑死 is the (fun) 'bad' event — 差点没 keeps it unhappened.", "It's an exaggeration — nobody died."],
        "Exaggeration: 差点没**笑死** = nearly died laughing.", "The film was so funny I nearly died laughing.", raw_opts=True),
      Q("s2_same", zh("地上/dìshang 都/dōu 是/shì 冰/bīng ， 我/wǒ （　） 摔倒/shuāidǎo 。"), ["差点/chàdiǎn 没/méi", "没/méi 差点/chàdiǎn", "没有/méiyǒu 差点/chàdiǎn", "差/chà 没/méi 点/diǎn"],
        ["", "没 comes **after** 差点.", "没有 can't go before 差点.", "差点 can't be split."],
        "Word order: **差点没** + verb.", "The ground was all ice — I almost fell.")])

# ---------------------------------------------------------------- step 3
quiz("03_chadian_3", "zh-dd-chadian-3", "差点 Step 3 · So Close! 差点 + Good Things",
     "When the event is something you want (winning, passing, getting tickets), 差点 means it didn't happen — and the mood is regret.",
     [p("s3_regret", "Good events with 差点: it didn't happen 😢",
        "差点 + something you want = you came close but missed it: 我差点中奖 = I almost won (I didn't).",
        "差点 still means 'almost' — and almost winning means you **didn't** win.\n\n"
        "- 我**差点**中奖。 I almost won the lottery. 😢\n- 我们**差点**赢了。 We almost won. (We lost.)\n- 我**差点**买到票。 I almost got a ticket. (No ticket.)\n\nThe feeling is **regret**: so close!",
        [("我/wǒ 差点/chàdiǎn 就/jiù 中奖/zhòngjiǎng 了/le ！", "I nearly won the prize! (but didn't)")]),
      p("s3_clues", "Regret clues: 可惜, 就差一点, 真遗憾",
        "可惜 (what a pity), 就差一点 (just a tiny bit short) and 真遗憾 (what a shame) tell you the good thing didn't happen.",
        "- **可惜** (kěxī): 可惜，他差点就考上了。\n- **就差一点** (jiù chà yìdiǎn): 就差一点，我就拿到第一名了。\n- **真遗憾** (zhēn yíhàn): 真遗憾，我们差点赢了。\n\n"
        "Relief words (幸亏, 还好, 好在) don't fit here — they mean the good thing **did** happen.",
        [("可惜/kěxī ， 他/tā 差点/chàdiǎn 就/jiù 考上/kǎoshàng 了/le 。", "What a pity — he very nearly got in.")])],
     [did("s3_regret", "我/wǒ 差点/chàdiǎn 中奖/zhòngjiǎng 。", "Did I win?", False,
          "中奖 is wanted; 差点 = so close → **no win**. 😢", "I almost won the prize."),
      Q("s3_regret", "What does 「" + zh("我们/wǒmen 差点/chàdiǎn 就/jiù 赢/yíng 了/le 。") + "」 mean?",
        ["We nearly won — but we lost.", "We won easily.", "We won, but only just.", "We didn't play."],
        ["", "差点 = it didn't happen.", "'Won, but only just' would be 差点没赢 (step 4).", "They played — and almost won."],
        "Wanted event + 差点 → **didn't happen**: so close!", "We very nearly won.", raw_opts=True),
      Q("s3_clues", zh("（　） ， 他/tā 差点/chàdiǎn 就/jiù 考上/kǎoshàng 了/le 。"), ["可惜/kěxī", "幸亏/xìngkuī", "好在/hǎozài", "还好/háihǎo"],
        ["", "幸亏 = 'luckily' — but he didn't get in.", "好在 = 'fortunately' — but he didn't get in.", "还好 = 'luckily' — but he didn't get in."],
        "He didn't get in → regret: **可惜**.", "What a pity — he very nearly got in."),
      did("s3_regret", "她/tā 差点/chàdiǎn 买到/mǎidào 那/nà 双/shuāng 鞋/xié 。", "Did she get the shoes?", False,
          "买到 is wanted; 差点买到 = almost got them → **no shoes**. 😢", "She almost got those shoes."),
      Q("s3_regret", "You ran for the bus, but the doors closed in front of you. Which sentence fits?",
        ["我/wǒ 差点/chàdiǎn 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。", "我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。", "我/wǒ 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 了/le 。", "我/wǒ 没/méi 差点/chàdiǎn 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。"],
        ["", "差点没赶上 = you **caught** it, just barely (step 4).", "That says you caught it.", "没 can't go before 差点."],
        "Missed it after a close race → **差点赶上** (almost caught).", "I almost caught the bus."),
      Q("s3_clues", "What does 「" + zh("就/jiù 差/chà 一点/yìdiǎn ， 我/wǒ 就/jiù 拿到/nádào 第一名/dì-yī míng 了/le 。") + "」 mean?",
        ["I came so close to first place — but didn't get it.", "I easily got first place.", "I got first place by a tiny margin.", "I didn't take part."],
        ["", "就差一点 = just a tiny bit short — no first place.", "'By a tiny margin' would be 差点没拿到.", "You took part and nearly won."],
        "**就差一点** = just short → didn't happen.", "Just a little more and I'd have got first place.", raw_opts=True),
      Q("s3_clues", "Your friend says 「" + zh("我/wǒ 差点/chàdiǎn 抢到/qiǎngdào 演唱会/yǎnchànghuì 的/de 票/piào 。") + "」 Which reply fits?",
        ["太/tài 可惜/kěxī 了/le ！", "太/tài 好/hǎo 了/le ， 恭喜/gōngxǐ ！", "好险/hǎo xiǎn 啊/a ！", "你/nǐ 真/zhēn 倒霉/dǎoméi ， 被/bèi 骗/piàn 了/le 。"],
        ["", "Congratulations would mean they got a ticket — they didn't.", "好险 (that was close!) is for dangers you escaped.", "Nobody was cheated."],
        "No ticket → regret: **太可惜了**.", "I almost got concert tickets."),
      Q("s3_regret", zh("最后/zuìhòu 一/yì 秒/miǎo ， 球/qiú 打/dǎ 在/zài 门柱/ménzhù 上/shang — — 我们/wǒmen （　） 进球/jìnqiú 了/le ！"),
        ["差点/chàdiǎn", "差点/chàdiǎn 没/méi", "终于/zhōngyú", "已经/yǐjīng"],
        ["", "差点没进球 = you **did** score, just barely.", "终于 = 'finally' — but the ball hit the post.", "已经进球了 = 'already scored' — it hit the post."],
        "Hit the post, no goal → **差点**进球 (almost scored).", "In the last second the ball hit the post — we almost scored!"),
      Q("s3_regret", "'We nearly caught the last train (but missed it).' Which sentence says so?",
        ["我们/wǒmen 差点/chàdiǎn 赶上/gǎnshàng 末班车/mòbānchē 。", "我们/wǒmen 差点/chàdiǎn 没/méi 赶上/gǎnshàng 末班车/mòbānchē 。", "我们/wǒmen 赶上/gǎnshàng 末班车/mòbānchē 了/le 。", "我们/wǒmen 末班车/mòbānchē 差点/chàdiǎn 赶上/gǎnshàng 。"],
        ["", "差点没赶上 = you **caught** it, barely.", "That says you caught it.", "The subject comes first, then 差点 + verb + object."],
        "Wanted + 差点 → missed: **差点赶上**.", "We nearly caught the last train."),
      did("s3_regret", "他/tā 差点/chàdiǎn 考上/kǎoshàng 北京/Běijīng 大学/Dàxué 。", "Did he get into Peking University?", False,
          "考上 is wanted; 差点考上 = so close → **didn't get in**. 😢", "He very nearly got into Peking University."),
      Q("s3_regret", "「" + zh("差点/chàdiǎn 摔倒/shuāidǎo") + "」 and 「" + zh("差点/chàdiǎn 中奖/zhòngjiǎng") + "」 — in which did the event happen?",
        ["Neither — 差点 on its own always means it didn't happen.", "Only 摔倒.", "Only 中奖.", "Both."],
        ["", "差点摔倒 = didn't fall.", "差点中奖 = didn't win.", "差点 = almost — neither happened."],
        "Plain **差点** = didn't happen, whatever the event. Only 差点没 + a good thing means it did.", "")])

# ---------------------------------------------------------------- step 4
quiz("04_chadian_4", "zh-dd-chadian-4", "差点 Step 4 · Phew, Made It! 差点没 + Good Things",
     "With things you want, 没 really flips it: 差点没赶上 = almost missed it — so you caught it, just barely. The mood is relief.",
     [p("s4_relief", "Good events with 差点没: it DID happen 🎉",
        "差点没 + something you want = it almost didn't happen — so it did, by a hair: 我差点没赶上飞机 = I made the plane, just.",
        "Here 没 does its normal job ('not'): **almost didn't** happen → **did** happen.\n\n"
        "- 我**差点没**赶上飞机。 I almost missed the plane — I made it. 🎉\n- 他**差点没**考上。 He nearly failed — but he got in.\n"
        "- 我**差点没**认出你来！ I almost didn't recognise you! (but I did)\n\nThe feeling is **relief**: phew!",
        [("我/wǒ 差点/chàdiǎn 没/méi 认/rèn 出/chū 你/nǐ 来/lái ！", "I almost didn't recognise you!")]),
      p("s4_clues", "Relief clues: 幸亏, 还好, 好在, 总算, 好险",
        "幸亏 / 还好 / 好在 (luckily), 总算 (in the end) and 好险 (that was close!) tell you it worked out.",
        "- **幸亏** (xìngkuī) / **还好** (háihǎo) / **好在** (hǎozài): luckily.\n- **总算** (zǒngsuàn): in the end, at last — 差点没赶上，总算赶上了。\n"
        "- **好险** (hǎo xiǎn): phew, that was close!\n\nRegret words (可惜, 就差一点) don't fit — they mean the good thing did **not** happen.",
        [("我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng ， 总算/zǒngsuàn 赶上/gǎnshàng 了/le 。", "I very nearly missed it — but I made it in the end.")])],
     [did("s4_relief", "我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 飞机/fēijī 。", "Did I catch the plane?", True,
          "赶上 is wanted; 差点没 = almost didn't → I **did** catch it. 🎉", "I almost missed the plane."),
      Q("s4_relief", "What does 「" + zh("他/tā 差点/chàdiǎn 没/méi 考上/kǎoshàng 大学/dàxué 。") + "」 mean?",
        ["He only just got into university.", "He didn't get into university.", "He got in easily.", "He almost took the entrance exam."],
        ["", "考上 is wanted → 差点没 = he **did** get in.", "差点 says it was close — not easy.", "考上 = pass the entrance exam."],
        "Wanted + 差点没 → **did happen**, barely.", "He only just got into university.", raw_opts=True),
      did("s4_relief", "我/wǒ 差点/chàdiǎn 没/méi 认/rèn 出/chū 你/nǐ 来/lái ！", "Did I recognise you?", True,
          "Recognising a friend is wanted → 差点没认出 = I **did** recognise you, just. 🎉", "I almost didn't recognise you!"),
      Q("s4_clues", zh("路/lù 上/shang 太/tài 堵/dǔ 了/le ， 我们/wǒmen 差点/chàdiǎn 没/méi 赶上/gǎnshàng 火车/huǒchē ， （　） 最后/zuìhòu 一/yì 分钟/fēnzhōng 上/shàng 了/le 车/chē 。"),
        ["幸亏/xìngkuī", "可惜/kěxī", "差点/chàdiǎn", "本来/běnlái"],
        ["", "可惜 = 'what a pity' — but you got on.", "差点 = 'almost' — but you did get on.", "本来 = 'originally' — doesn't fit."],
        "It worked out → relief: **幸亏** (luckily).", "The traffic was terrible — we almost missed the train; luckily we got on in the last minute."),
      Q("s4_relief", "「" + zh("我/wǒ 差点/chàdiǎn 买到/mǎidào 票/piào 。") + "」 vs 「" + zh("我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 票/piào 。") + "」 — who has a ticket?",
        ["Only the second speaker.", "Only the first speaker.", "Both.", "Neither."],
        ["", "差点买到 = almost got one → no ticket.", "差点买到 = no ticket; 差点没买到 = ticket.", "差点没买到 = got one, just."],
        "Wanted event: 差点 → no; **差点没 → yes**. 好事加「没」，意思反转.", "", fixed=True, raw_opts=True),
      Q("s4_relief", "The concert sold out right after you bought the last ticket. Which sentence fits?",
        ["我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 票/piào 。", "我/wǒ 差点/chàdiǎn 买到/mǎidào 票/piào 。", "我/wǒ 没/méi 买到/mǎidào 票/piào 。", "我/wǒ 买到/mǎidào 票/piào 差点/chàdiǎn 。"],
        ["", "差点买到 = almost got one — no ticket.", "That says you didn't get one.", "差点 goes before the verb."],
        "Got it, just → **差点没买到**.", "I almost didn't get a ticket."),
      Q("s4_clues", "Your friend says 「" + zh("我/wǒ 差点/chàdiǎn 没/méi 通过/tōngguò 考试/kǎoshì 。") + "」 Which reply fits?",
        ["好险/hǎo xiǎn ！ 恭喜/gōngxǐ 你/nǐ 过/guò 了/le ！", "太/tài 可惜/kěxī 了/le ， 下次/xiàcì 再/zài 努力/nǔlì 。", "你/nǐ 怎么/zěnme 不/bù 考试/kǎoshì ？", "别/bié 难过/nánguò ， 没/méi 通过/tōngguò 也/yě 没关系/méi guānxi 。"],
        ["", "可惜 means they failed — they passed.", "They did take the exam.", "They passed — no need for comfort."],
        "Passed, just → relief: **好险！恭喜！**", "I almost didn't pass the exam."),
      Q("s4_relief", "What does 「" + zh("这/zhè 道/dào 题/tí 太/tài 难/nán 了/le ， 我/wǒ 差点/chàdiǎn 没/méi 做/zuò 出来/chūlai 。") + "」 mean?",
        ["The problem was so hard — I only just managed to solve it.", "The problem was so hard I couldn't solve it.", "I almost solved it.", "I didn't try."],
        ["", "Solving it is wanted → 差点没 = you **did** solve it.", "'Almost solved it' would be 差点做出来.", "You tried hard."],
        "Wanted + 差点没 → **did** happen: solved it, just.", "This problem was so hard I only just managed it.", raw_opts=True),
      Q("s4_relief", "「" + zh("最后/zuìhòu 一/yì 秒/miǎo 才/cái 进球/jìnqiú — — 我们/wǒmen 差点/chàdiǎn 没/méi 赢/yíng ！") + "」 What happened?",
        ["We won, but only just.", "We lost by a hair.", "It was a draw.", "We didn't play."],
        ["", "'Lost by a hair' would be 差点赢了.", "Winning is the wanted event — and you won.", "You played — and scored."],
        "Wanted + 差点没 → **won**, barely. 🎉", "We only scored in the last second — we very nearly didn't win!", raw_opts=True),
      Q("s4_relief", "'I almost couldn't find you! (but I did)' Which sentence says so?",
        ["我/wǒ 差点/chàdiǎn 没/méi 找到/zhǎodào 你/nǐ ！", "我/wǒ 差点/chàdiǎn 找到/zhǎodào 你/nǐ ！", "我/wǒ 没/méi 找到/zhǎodào 你/nǐ ！", "我/wǒ 找到/zhǎodào 你/nǐ 差点/chàdiǎn ！"],
        ["", "差点找到 = almost found you — so you didn't.", "That says you didn't find them.", "差点 goes before the verb."],
        "Found them, just → **差点没找到**.", "I almost couldn't find you!"),
      Q("s4_clues", zh("A： 你/nǐ 考/kǎo 得/de 怎么样/zěnmeyàng ？ // B： 别提了/bié tí le ， 差点/chàdiǎn 没/méi 及格/jígé 。 // A： （　）"),
        ["那/nà 还好/háihǎo ， 总算/zǒngsuàn 过/guò 了/le ！", "那/nà 太/tài 可惜/kěxī 了/le ， 下次/xiàcì 加油/jiāyóu ！", "你/nǐ 怎么/zěnme 没/méi 去/qù 考/kǎo ？", "没/méi 及格/jígé 也/yě 没关系/méi guānxi 。"],
        ["", "可惜 means they failed — they passed.", "They did take the exam.", "They didn't fail."],
        "差点没及格 = **passed**, just → 还好，总算过了！", "A: How did the exam go? B: Don't ask — I very nearly failed. A: Well, at least you passed!"),
      Q("s4_relief", "In 差点没 + **good thing**, what does 没 do?",
        ["It flips it: it almost didn't happen — so it did.", "Nothing — it means the same as 差点.", "It makes it a question.", "It means it happened twice."],
        ["", "That's true for **bad** things only.", "There's no question word.", "No — it's about whether it happened at all."],
        "Good thing: **没 flips it**. 好事加「没」，意思反转.", "", fixed=True, raw_opts=True)])

# ---------------------------------------------------------------- step 5
BAD = "😅 {e} is unwanted → 差点 and 差点没 both mean it **didn't happen**."
GOOD_NO = "😢 {e} is wanted; plain 差点 = so close → it **didn't happen**."
GOOD_MEI = "🎉 {e} is wanted; 差点没 = almost didn't → it **did happen**, just barely."
quiz("05_chadian_5", "zh-dd-chadian-5", "差点 Step 5 · Did It Happen? The Big Sort",
     "17 quick sentences, one question each: did it really happen? Decide wanted or unwanted, then look for the 没.",
     [p("s5_bad", "Unwanted events: never happened",
        "Unwanted event: with or without 没, it didn't happen.", "Falling, being late, losing things, starting a quarrel …",
        [("我/wǒ 差点/chàdiǎn 把/bǎ 钥匙/yàoshi 丢/diū 了/le 。", "I almost lost my keys.")]),
      p("s5_good", "Wanted events: look for the 没",
        "Wanted event: 差点 = didn't happen (so close!), 差点没 = did happen (phew!).", "Winning, buying tickets, getting in, catching the train …",
        [("我们/wǒmen 差点/chàdiǎn 没/méi 赶上/gǎnshàng 末班车/mòbānchē 。", "We very nearly missed the last train (but caught it).")])],
     [did("s5_bad", "他/tā 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。", "Did he fall?", False, BAD.format(e="Falling"), "He almost fell."),
      did("s5_good", "她/tā 差点/chàdiǎn 赢/yíng 了/le 。", "Did she win?", False, GOOD_NO.format(e="Winning"), "She almost won."),
      did("s5_bad", "他/tā 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。", "Did he fall?", False, BAD.format(e="Falling"), "He almost fell."),
      did("s5_good", "她/tā 差点/chàdiǎn 没/méi 赢/yíng 。", "Did she win?", True, GOOD_MEI.format(e="Winning"), "She very nearly didn't win."),
      did("s5_bad", "我/wǒ 差点/chàdiǎn 迟到/chídào 。", "Was I late?", False, BAD.format(e="Being late"), "I was almost late."),
      did("s5_good", "我/wǒ 差点/chàdiǎn 买到/mǎidào 票/piào 。", "Did I get a ticket?", False, GOOD_NO.format(e="Getting a ticket"), "I almost got a ticket."),
      did("s5_bad", "我/wǒ 差点/chàdiǎn 没/méi 迟到/chídào 。", "Was I late?", False, BAD.format(e="Being late"), "I was almost late."),
      did("s5_good", "我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 票/piào 。", "Did I get a ticket?", True, GOOD_MEI.format(e="Getting a ticket"), "I almost didn't get a ticket."),
      did("s5_bad", "我/wǒ 差点/chàdiǎn 把/bǎ 钥匙/yàoshi 丢/diū 了/le 。", "Did I lose the keys?", False, BAD.format(e="Losing your keys"), "I almost lost my keys."),
      did("s5_good", "他/tā 差点/chàdiǎn 考上/kǎoshàng 。", "Did he get in?", False, GOOD_NO.format(e="Getting in (考上)"), "He very nearly got in."),
      did("s5_bad", "孩子/háizi 差点/chàdiǎn 没/méi 哭/kū 出来/chūlai 。", "Did the child burst into tears?", False, BAD.format(e="Bursting into tears"), "The child almost burst into tears."),
      did("s5_good", "他/tā 差点/chàdiǎn 没/méi 考上/kǎoshàng 。", "Did he get in?", True, GOOD_MEI.format(e="Getting in (考上)"), "He only just got in."),
      did("s5_bad", "我们/wǒmen 差点/chàdiǎn 吵/chǎo 起来/qǐlai 。", "Did we start arguing?", False, BAD.format(e="Starting a quarrel"), "We almost started arguing."),
      did("s5_good", "我/wǒ 差点/chàdiǎn 没/méi 认/rèn 出/chū 她/tā 来/lái 。", "Did I recognise her?", True, GOOD_MEI.format(e="Recognising someone"), "I almost didn't recognise her."),
      did("s5_good", "我们/wǒmen 差点/chàdiǎn 赶上/gǎnshàng 末班车/mòbānchē 。", "Did we catch the last train?", False, GOOD_NO.format(e="Catching the train"), "We almost caught the last train."),
      did("s5_bad", "手机/shǒujī 差点/chàdiǎn 没/méi 掉/diào 进/jìn 水/shuǐ 里/li 。", "Did the phone fall into the water?", False, BAD.format(e="Dropping your phone in water"), "The phone almost fell into the water."),
      did("s5_good", "我们/wǒmen 差点/chàdiǎn 没/méi 赶上/gǎnshàng 末班车/mòbānchē 。", "Did we catch the last train?", True, GOOD_MEI.format(e="Catching the train"), "We very nearly missed the last train.")])

# ---------------------------------------------------------------- step 6
quiz("06_chadian_6", "zh-dd-chadian-6", "差点 Step 6 · Say It Right: Build, Choose, Fix",
     "Now you make the sentences: put the words in order, pick the right version for a situation, and catch the mistakes.",
     [p("s6_build", "Building the sentence", "Subject + 差点(儿) + (没) + (就) + verb + (了).",
        "- 我 **差点儿 没** 赶上 飞机。\n- 他 **差一点 就** 摔倒 **了**。\n- 我 **差点 没** 认出 你 **来**！ (认出…来 = recognise)",
        [("我/wǒ 差点儿/chàdiǎnr 没/méi 赶上/gǎnshàng 飞机/fēijī 。", "I very nearly missed the plane (but made it).")]),
      p("s6_choose", "Choosing 差点 or 差点没", "Decide what happened and what the speaker wanted — then pick the form from the table.",
        "- Wanted it and got it, barely → **差点没**.\n- Wanted it and missed it → **差点**.\n- Didn't want it, and it didn't happen → **差点** or **差点没**.\n"
        "- Written Chinese also uses **险些** (xiǎnxiē) for 差点 with bad events: 他险些出了车祸。",
        [("他/tā 险些/xiǎnxiē 出/chū 了/le 车祸/chēhuò 。", "He nearly had a car accident.")]),
      p("s6_fix", "Spotting mistakes", "没 goes after 差点, 差点 goes before the verb, and the mood word must match what happened.",
        "- ~~我没差点迟到~~ → 我差点没迟到.\n- ~~我摔倒差点了~~ → 我差点摔倒了.\n- ~~可惜，我差点没买到票~~ — 可惜 (pity) doesn't fit: you got the ticket!",
        [("可惜/kěxī ， 我/wǒ 差点/chàdiǎn 就/jiù 中奖/zhòngjiǎng 了/le 。", "What a pity — I nearly won.")])],
     [star("s6_build", "我/wǒ ＿ ＿ ★ ＿ 。", ["飞机/fēijī", "没/méi", "赶上/gǎnshàng", "差点儿/chàdiǎnr"],
           ["赶上/gǎnshàng", "差点儿/chàdiǎnr", "没/méi", "飞机/fēijī"],
           ["", "差点儿 comes first — slot 1.", "没 follows 差点儿 — slot 2.", "The object comes last — slot 4."],
           "我 **差点儿 没 赶上 飞机**。", "I very nearly missed the plane."),
      star("s6_build", "他/tā ＿ ＿ ★ ＿ 。", ["就/jiù", "了/le", "差一点/chà yìdiǎn", "摔倒/shuāidǎo"],
           ["摔倒/shuāidǎo", "差一点/chà yìdiǎn", "就/jiù", "了/le"],
           ["", "差一点 comes first — slot 1.", "就 follows 差一点 — slot 2.", "了 closes the sentence — slot 4."],
           "他 **差一点 就 摔倒 了**。", "He very nearly fell."),
      star("s6_build", "我/wǒ ＿ ＿ ★ ＿ 来/lái ！", ["你/nǐ", "认出/rènchū", "差点/chàdiǎn", "没/méi"],
           ["认出/rènchū", "差点/chàdiǎn", "没/méi", "你/nǐ"],
           ["", "差点 comes first — slot 1.", "没 follows 差点 — slot 2.", "The person sits between 认出 and 来 — slot 4."],
           "我 **差点 没 认出 你** 来！", "I almost didn't recognise you!"),
      Q("s6_choose", "You wanted the last cake, but the person in front of you took it. Which sentence fits?",
        ["我/wǒ 差点/chàdiǎn 买到/mǎidào 最后/zuìhòu 一个/yí ge 蛋糕/dàngāo 。", "我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 最后/zuìhòu 一个/yí ge 蛋糕/dàngāo 。", "我/wǒ 买到/mǎidào 了/le 最后/zuìhòu 一个/yí ge 蛋糕/dàngāo 。", "我/wǒ 没/méi 差点/chàdiǎn 买到/mǎidào 蛋糕/dàngāo 。"],
        ["", "差点没买到 = you **got** it, just.", "That says you got it.", "没 can't go before 差点."],
        "Wanted it, missed it → **差点买到**. 😢", "I almost got the last cake."),
      Q("s6_choose", "You slipped on the ice but grabbed the railing in time. Which sentence does **not** describe it?",
        ["我/wǒ 摔倒/shuāidǎo 了/le 。", "我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。", "我/wǒ 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。", "我/wǒ 差点儿/chàdiǎnr 就/jiù 摔倒/shuāidǎo 了/le 。"],
        ["", "Correct: almost fell.", "Correct: unwanted event, 没 changes nothing.", "Correct: the dramatic version."],
        "Only **我摔倒了** says you actually fell. The other three all mean 'almost fell'.", "I almost fell."),
      Q("s6_choose", "Your train left ten seconds after you jumped on. What do you tell your friend?",
        ["我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 火车/huǒchē ！", "我/wǒ 差点/chàdiǎn 赶上/gǎnshàng 火车/huǒchē ！", "我/wǒ 没/méi 赶上/gǎnshàng 火车/huǒchē ！", "我/wǒ 赶上/gǎnshàng 火车/huǒchē 差点/chàdiǎn ！"],
        ["", "差点赶上 = almost caught it — so you missed it.", "That says you missed it.", "差点 goes before the verb."],
        "Caught it, just → **差点没赶上**. 🎉", "I very nearly missed the train!"),
      Q("s6_fix", "Which sentence is **wrong**?",
        ["我/wǒ 没/méi 差点/chàdiǎn 迟到/chídào 。", "我/wǒ 差点/chàdiǎn 没/méi 迟到/chídào 。", "我/wǒ 差点儿/chàdiǎnr 迟到/chídào 了/le 。", "我/wǒ 差一点/chà yìdiǎn 就/jiù 迟到/chídào 了/le 。"],
        ["", "Correct: 没 after 差点.", "Correct: 差点儿 + verb + 了.", "Correct: 差一点就…了."],
        "没 goes **after** 差点: 差点没, never 没差点.", "I was almost late."),
      Q("s6_fix", "Which sentence is **wrong**?",
        ["我/wǒ 摔倒/shuāidǎo 差点/chàdiǎn 了/le 。", "我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 了/le 。", "我/wǒ 差点/chàdiǎn 没/méi 摔倒/shuāidǎo 。", "我/wǒ 差点儿/chàdiǎnr 就/jiù 摔倒/shuāidǎo 了/le 。"],
        ["", "Correct.", "Correct.", "Correct."],
        "差点 goes **before** the verb.", "I almost fell."),
      Q("s6_fix", "Which sentence doesn't make sense?",
        ["可惜/kěxī ， 我/wǒ 差点/chàdiǎn 没/méi 买到/mǎidào 票/piào 。", "好险/hǎo xiǎn ， 我/wǒ 差点/chàdiǎn 摔倒/shuāidǎo 。", "可惜/kěxī ， 我/wǒ 差点/chàdiǎn 就/jiù 中奖/zhòngjiǎng 了/le 。", "我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 飞机/fēijī ， 还好/háihǎo 最后/zuìhòu 赶上/gǎnshàng 了/le 。"],
        ["", "Fine: 好险 + an escaped danger.", "Fine: 可惜 + a prize you missed.", "Fine: made it — 还好 fits."],
        "差点没买到 = you **got** the ticket — so 可惜 (what a pity) doesn't fit. Use 好险 or 幸亏.", "What a pity, I almost didn't get a ticket. (contradictory)"),
      Q("s6_choose", "险些 (xiǎnxiē) is a written word for 差点. Which sentence means the same as 「" + zh("他/tā 险些/xiǎnxiē 出/chū 了/le 车祸/chēhuò 。") + "」?",
        ["他/tā 差点/chàdiǎn 出/chū 了/le 车祸/chēhuò 。", "他/tā 出/chū 了/le 车祸/chēhuò 。", "他/tā 很/hěn 小心/xiǎoxīn 地/de 开车/kāichē 。", "他/tā 差点/chàdiǎn 没/méi 开车/kāichē 。"],
        ["", "That says the accident happened.", "That's about driving carefully, not a near-accident.", "That's about (almost) not driving."],
        "险些 = **差点** (written): he nearly had an accident.", "He nearly had a car accident."),
      Q("s6_choose", "'I almost didn't recognise you — you've changed so much!' Which sentence says so?",
        ["我/wǒ 差点/chàdiǎn 没/méi 认/rèn 出/chū 你/nǐ 来/lái ， 你/nǐ 变化/biànhuà 太/tài 大/dà 了/le ！", "我/wǒ 差点/chàdiǎn 认/rèn 出/chū 你/nǐ 来/lái ， 你/nǐ 变化/biànhuà 太/tài 大/dà 了/le ！", "我/wǒ 没/méi 认/rèn 出/chū 你/nǐ 来/lái ， 你/nǐ 变化/biànhuà 太/tài 大/dà 了/le ！", "我/wǒ 认/rèn 出/chū 你/nǐ 来/lái 差点/chàdiǎn ， 你/nǐ 变化/biànhuà 太/tài 大/dà 了/le ！"],
        ["", "差点认出 = almost recognised — so you didn't.", "That says you didn't recognise them.", "差点 goes before the verb."],
        "Recognised them, just → **差点没认出你来**.", "I almost didn't recognise you — you've changed so much!"),
      Q("s6_choose", "'We very nearly won the final (so close!).' Which sentence says so?",
        ["我们/wǒmen 差点/chàdiǎn 就/jiù 赢/yíng 了/le 决赛/juésài 。", "我们/wǒmen 差点/chàdiǎn 没/méi 赢/yíng 决赛/juésài 。", "我们/wǒmen 赢/yíng 了/le 决赛/juésài 。", "我们/wǒmen 没/méi 差点/chàdiǎn 赢/yíng 决赛/juésài 。"],
        ["", "差点没赢 = you **won**, just.", "That says you won.", "没 can't go before 差点."],
        "Wanted, missed → **差点就赢了**. 😢", "We very nearly won the final.")])

# ---------------------------------------------------------------- step 7
STORY_A = ("星期一/xīngqīyī 早上/zǎoshang ， 小林/Xiǎo Lín 的/de 闹钟/nàozhōng 没/méi 响/xiǎng ， 他/tā 差点/chàdiǎn 没/méi 起来/qǐlai 。 "
           "他/tā 跑/pǎo 到/dào 车站/chēzhàn ， 差点/chàdiǎn 没/méi 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。 下/xià 车/chē 的/de 时候/shíhou ， 他/tā 差点/chàdiǎn 摔倒/shuāidǎo 。 "
           "到/dào 了/le 公司/gōngsī ， 他/tā 以为/yǐwéi 把/bǎ 电脑/diànnǎo 忘/wàng 在/zài 家/jiā 里/li 了/le — — 还好/háihǎo ， 电脑/diànnǎo 就/jiù 在/zài 包/bāo 里/li 。")
STORY_A_EN = ("On Monday morning Xiao Lin's alarm didn't go off, and he only just managed to get up. He ran to the bus stop and only just caught the bus. "
              "Getting off, he almost fell. At work he thought he'd left his laptop at home — luckily it was in his bag.")
STORY_B = ("中午/zhōngwǔ ， 公司/gōngsī 抽奖/chōujiǎng 。 小林/Xiǎo Lín 差点/chàdiǎn 中/zhòng 了/le 一等奖/yīděngjiǎng — — 就/jiù 差/chà 一/yí 个/ge 号码/hàomǎ 。 "
           "不过/búguò ， 他/tā 差点/chàdiǎn 没/méi 吃/chī 上/shang 午饭/wǔfàn ： 食堂/shítáng 只/zhǐ 剩/shèng 最后/zuìhòu 一/yí 份/fèn 了/le 。")
STORY_B_EN = ("At lunchtime the company held a prize draw. Xiao Lin nearly won first prize — he was one number short. "
              "And he only just got lunch: the canteen had one portion left.")
STORY_C = ("晚上/wǎnshang ， 小林/Xiǎo Lín 看/kàn 了/le 一个/yí ge 很/hěn 好笑/hǎoxiào 的/de 电影/diànyǐng ， 差点/chàdiǎn 没/méi 笑死/xiào sǐ 。 "
           "回家/huí jiā 的/de 路/lù 上/shang ， 他/tā 差点/chàdiǎn 迷路/mílù ， 幸亏/xìngkuī 有/yǒu 手机/shǒujī 地图/dìtú 。")
STORY_C_EN = ("In the evening Xiao Lin watched a really funny film and nearly died laughing. "
              "On the way home he almost got lost — luckily he had the map on his phone.")
quiz("07_chadian_7", "zh-dd-chadian-7", "差点 Step 7 · Boss Level: 小林's Crazy Monday",
     "One very unlucky (and lucky) day, HSK-style: read 小林's story and decide what really happened — then the final mixed challenge.",
     [p("s7_story", "Reading for what really happened", "In a story, mark each 差点 sentence: wanted or unwanted? With 没 or without? Then you know what happened.",
        "Check every 差点 against the table — then the true/false questions are easy.",
        [("他/tā 差点/chàdiǎn 没/méi 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。", "He only just caught the bus.")]),
      p("s7_mixed", "Final mixed challenge", "Everything together: meaning, form and mood.",
        "If in doubt, run the two questions: wanted or unwanted? 没 or no 没?",
        [("我/wǒ 差点/chàdiǎn 没/méi 认/rèn 出/chū 你/nǐ 来/lái ！", "I almost didn't recognise you!")])],
     [tf("s7_story", STORY_A, "小林/Xiǎo Lín 没/méi 赶上/gǎnshàng 公共汽车/gōnggòng qìchē 。", False,
         "差点没赶上 + wanted (赶上) → he **did** catch it.", "赶上 is wanted → 差点没赶上 = **caught it**, just. So the statement is false.",
         STORY_A_EN + " ★ Xiao Lin missed the bus."),
      tf("s7_story", STORY_A, "小林/Xiǎo Lín 下/xià 车/chē 的/de 时候/shíhou 摔倒/shuāidǎo 了/le 。", False,
         "差点摔倒 = almost fell — he didn't.", "Unwanted event + 差点 → **didn't fall**.",
         STORY_A_EN + " ★ Xiao Lin fell when getting off."),
      tf("s7_story", STORY_A, "小林/Xiǎo Lín 最后/zuìhòu 起床/qǐchuáng 了/le 。", True,
         "差点没起来 + wanted (getting up) → he **did** get up.", "Getting up is wanted → 差点没起来 = he **got up**, just in time.",
         STORY_A_EN + " ★ Xiao Lin did get up in the end."),
      tf("s7_story", STORY_A, "小林/Xiǎo Lín 把/bǎ 电脑/diànnǎo 忘/wàng 在/zài 家/jiā 里/li 了/le 。", False,
         "以为 = he wrongly thought so — the laptop was in his bag.", "以为 = **mistakenly thought**: 电脑就在包里. False.",
         STORY_A_EN + " ★ Xiao Lin left his laptop at home."),
      reading("s7_story", STORY_B, "小林/Xiǎo Lín 中/zhòng 了/le 一等奖/yīděngjiǎng 吗/ma ？",
              ["没有/méiyǒu ， 就/jiù 差/chà 一/yí 个/ge 号码/hàomǎ", "中/zhòng 了/le", "他/tā 中/zhòng 了/le 二等奖/èrděngjiǎng", "他/tā 没/méi 参加/cānjiā"],
              ["", "差点中了 + wanted → he did **not** win.", "The story doesn't mention a second prize.", "He took part — and was one number short."],
              "差点中了 + 就差一个号码 → **didn't win**. 😢", STORY_B_EN + " ★ Did Xiao Lin win first prize?"),
      reading("s7_story", STORY_B, "小林/Xiǎo Lín 吃/chī 上/shang 午饭/wǔfàn 了/le 吗/ma ？",
              ["吃/chī 上/shang 了/le ， 是/shì 最后/zuìhòu 一/yí 份/fèn", "没/méi 吃/chī 上/shang", "他/tā 不/bú 饿/è", "他/tā 在/zài 家/jiā 吃/chī 的/de"],
              ["", "差点没吃上 + wanted → he **did** get lunch.", "The story doesn't say he wasn't hungry.", "He ate at the canteen."],
              "差点没吃上 + 只剩最后一份 → **got the last portion**. 🎉", STORY_B_EN + " ★ Did Xiao Lin get lunch?"),
      tf("s7_story", STORY_C, "小林/Xiǎo Lín 迷路/mílù 了/le 。", False,
         "差点迷路 + 幸亏有手机地图 → he didn't get lost.", "Unwanted + 差点 → **didn't get lost** — thanks to the map.",
         STORY_C_EN + " ★ Xiao Lin got lost."),
      tf("s7_story", STORY_C, "这个/zhège 电影/diànyǐng 很/hěn 好笑/hǎoxiào 。", True,
         "差点没笑死 = he nearly died laughing — very funny.", "差点没笑死 is an exaggeration: the film was **very funny**.",
         STORY_C_EN + " ★ The film was funny."),
      Q("s7_mixed", "Which rule is right?",
        ["Bad thing: 差点 = 差点没 (didn't happen). Good thing: 差点 = didn't happen, 差点没 = did happen.",
         "Bad thing: 差点没 = did happen. Good thing: 差点 = 差点没.",
         "差点没 always means it happened.",
         "差点 always means it happened, a little."],
        ["", "Swapped: with bad things the 没 changes nothing.", "Not for bad things: 差点没摔倒 = didn't fall.", "差点 means 'almost' — it didn't happen."],
        "坏事加「没」，意思不变；好事加「没」，意思反转。", "", fixed=True, raw_opts=True),
      Q("s7_mixed", zh("小林/Xiǎo Lín 跑/pǎo 到/dào 站台/zhàntái 的/de 时候/shíhou ， 车门/chēmén 刚/gāng 关/guān 上/shang 。 他/tā 差点/chàdiǎn （　） 末班车/mòbānchē 。"),
        ["赶上/gǎnshàng", "没/méi 赶上/gǎnshàng", "摔倒/shuāidǎo", "迟到/chídào"],
        ["", "差点没赶上 = he **caught** it — but the doors had closed.", "Doesn't fit the doors closing.", "迟到 doesn't take an object like 末班车."],
        "Doors closed → missed it: 差点**赶上** (almost caught).", "When Xiao Lin reached the platform, the doors had just closed. He almost caught the last train."),
      Q("s7_mixed", "Which reply fits 「" + zh("我/wǒ 差点/chàdiǎn 没/méi 赶上/gǎnshàng 你/nǐ 的/de 婚礼/hūnlǐ ！") + "」?",
        ["幸亏/xìngkuī 你/nǐ 来/lái 了/le ！", "真/zhēn 可惜/kěxī ， 你/nǐ 没/méi 来/lái 。", "你/nǐ 为什么/wèishénme 不/bù 来/lái ？", "没关系/méi guānxi ， 下次/xiàcì 吧/ba 。"],
        ["", "差点没赶上 = they made it — 可惜 doesn't fit.", "They did come.", "There's nothing to make up for — they came."],
        "差点没赶上 + wanted → **made it** → 幸亏你来了！", "I nearly missed your wedding!"),
      Q("s7_mixed", "Which sentence means 'Luckily I left early — otherwise I'd have been late'?",
        ["幸亏/xìngkuī 我/wǒ 出门/chūmén 早/zǎo ， 不然/bùrán 就/jiù 迟到/chídào 了/le 。", "可惜/kěxī 我/wǒ 出门/chūmén 早/zǎo ， 差点/chàdiǎn 迟到/chídào 了/le 。", "幸亏/xìngkuī 我/wǒ 差点/chàdiǎn 没/méi 出门/chūmén 。", "我/wǒ 差点/chàdiǎn 出门/chūmén 早/zǎo 。"],
        ["", "可惜 (pity) doesn't fit leaving early.", "That says you almost didn't leave at all.", "差点出门早 isn't natural."],
        "**幸亏…，不然…** = luckily …, otherwise … — the relief pattern that often sits next to 差点.", "Luckily I left early, otherwise I'd have been late.")])


# ================================================================ 以上 / 以下
YS_TABLE = """**以上 / 以下 at a glance**

| | 以上 | 以下 |
|---|---|---|
| numbers 数目 | 18岁以上: 18 and over | 1.2米以下: 1.2 m and under |
| levels 级别 | HSK四级以上: level 4 or higher | 三星级以下: three stars or fewer |
| order 次序 | 以上几点: the points above | 以下几点: the following points |

**Three rules**
1. **Position:** after the number + measure word (or the level): 三个小时**以上**, 本科**以上**. Before a noun add 的: 六十岁以上**的**老人.
2. **Does the number count?** In rules and laws: **yes** (Chinese law says so: 以上、以下…包括本数). In everyday talk it's fuzzy, so notices often add **(含)** 'inclusive' or **(不含)**. For strictly more / less: **超过 / 高于** and **不到 / 不满 / 低于**.
3. **Don't mix up:** 以前 / 以后 (time points: 三点以前), 左右 (about), 以内 (within: 三天以内), 多 (三十多个 = thirty-odd), **零下** (minus: 零下五度 = −5°)."""


def yp(id, title, summary, body, examples):
    return P(id, title, summary, body + "\n\n" + YS_TABLE, examples)


def yn(point, sentence, question, yes, why, translation):
    """A yes/no check of a notice or a rule."""
    return Q(point, "「" + zh(sentence) + "」\n" + question, ["✔ Yes", "✘ No"],
             ["", why] if yes else [why, ""], why, translation, answer=0 if yes else 1, fixed=True, raw_opts=True)


# ---------------------------------------------------------------- step 1
quiz("11_yishang_1", "zh-dd-yishang-1", "以上 / 以下 Step 1 · Numbers: 18岁以上, 100块以下",
     "Number + 以上 = that much or more, number + 以下 = that much or less. Where it goes, and 的 before a noun.",
     [yp("y1_meaning", "Number + 以上 / 以下", "以上 (yǐshàng) = and above, 以下 (yǐxià) = and below — after a number.",
         "- 十八岁**以上** — 18 and over\n- 一百块**以下** — 100 kuai or less\n- 三十度**以上** — 30 degrees or more\n- 三个小时**以上** — three hours or more",
         [("这/zhè 部/bù 电影/diànyǐng 十八/shíbā 岁/suì 以上/yǐshàng 才/cái 能/néng 看/kàn 。", "Only people aged 18 and over can watch this film.")]),
      yp("y1_shape", "Where it goes: number + measure word + 以上 (+ 的 + noun)", "以上 / 以下 come after the whole number phrase; before a noun add 的.",
         "- 五**年**以上, 一百**块**以下, 三十**个人**以上\n- With a noun: 六十岁以上**的**老人 (people over 60), 一千块以上**的**手机\n"
         "- Never in front: ~~以上十八岁~~, and not inside: ~~十八以上岁~~.",
         [("六十/liùshí 岁/suì 以上/yǐshàng 的/de 老人/lǎorén 坐/zuò 公交/gōngjiāo 免费/miǎnfèi 。", "People aged 60 and over ride the bus for free.")])],
     [Q("y1_meaning", "What does 「" + zh("十八/shíbā 岁/suì 以上/yǐshàng") + "」 mean?",
        ["18 and over", "under 18", "about 18", "18 years ago"],
        ["", "That's 十八岁以下.", "That's 十八岁左右.", "That's 十八年以前."],
        "Number + **以上** = that number and above.", "", raw_opts=True),
      Q("y1_meaning", "What does 「" + zh("一百/yìbǎi 块/kuài 以下/yǐxià 的/de 礼物/lǐwù") + "」 mean?",
        ["presents of 100 kuai or less", "presents of more than 100 kuai", "presents of about 100 kuai", "100 presents"],
        ["", "That's 一百块以上.", "That's 一百块左右.", "That would be 一百个礼物."],
        "以下 = **and below**: 100 kuai or less.", "presents costing 100 kuai or less", raw_opts=True),
      Q("y1_meaning", zh("今天/jīntiān 很/hěn 热/rè ， 气温/qìwēn 三十五/sānshíwǔ 度/dù （　） 。"), ["以上/yǐshàng", "以下/yǐxià", "以前/yǐqián", "零下/língxià"],
        ["", "以下 = 35 or less — 'very hot' points the other way.", "以前 is for time, not temperature.", "零下 = minus — it comes before the number: 零下五度."],
        "Very hot → 35 degrees **以上**.", "It's very hot today — over 35 degrees."),
      yn("y1_meaning", "六十/liùshí 岁/suì 以上/yǐshàng 的/de 老人/lǎorén 坐/zuò 公交/gōngjiāo 免费/miǎnfèi 。", "Does a 70-year-old ride free?", True,
         "70 is above 60 → 以上 covers it.", "People aged 60 and over ride the bus for free."),
      yn("y1_meaning", "身高/shēngāo 一米二/yì mǐ èr 以下/yǐxià 的/de 儿童/értóng 免票/miǎnpiào 。", "Does a 1.35 m child go free?", False,
         "1.35 m is above 1.2 m → not covered by 以下.", "Children 1.2 m and under go free."),
      Q("y1_shape", "Which sentence is correct?",
        ["我/wǒ 每天/měitiān 学习/xuéxí 两/liǎng 个/ge 小时/xiǎoshí 以上/yǐshàng 。", "我/wǒ 每天/měitiān 学习/xuéxí 以上/yǐshàng 两/liǎng 个/ge 小时/xiǎoshí 。", "我/wǒ 每天/měitiān 学习/xuéxí 两/liǎng 个/ge 以上/yǐshàng 小时/xiǎoshí 了/le 。", "我/wǒ 每天/měitiān 以上/yǐshàng 学习/xuéxí 两/liǎng 个/ge 小时/xiǎoshí 。"],
        ["", "以上 goes **after** the number, not before.", "Put 以上 after the whole phrase 两个小时.", "以上 belongs to the amount, not the verb."],
        "Number phrase + **以上**: 两个小时以上.", "I study for more than two hours every day."),
      Q("y1_shape", zh("（　） 老人/lǎorén 可以/kěyǐ 买/mǎi 半价/bànjià 票/piào 。"),
        ["六十/liùshí 岁/suì 以上/yǐshàng 的/de", "以上/yǐshàng 六十/liùshí 岁/suì 的/de", "六十/liùshí 以上/yǐshàng 岁/suì 的/de", "六十/liùshí 岁/suì 以上/yǐshàng"],
        ["", "以上 comes after the number.", "以上 comes after the whole 六十岁.", "Before a noun you need 的."],
        "Before a noun: number + 以上 + **的** + noun.", "People over 60 can buy half-price tickets."),
      star("y1_shape", "＿ ＿ ★ ＿ 免费/miǎnfèi 。", ["的/de", "以下/yǐxià", "六/liù 岁/suì", "儿童/értóng"],
           ["的/de", "六/liù 岁/suì", "以下/yǐxià", "儿童/értóng"],
           ["", "六岁 starts the phrase — slot 1.", "以下 follows the number — slot 2.", "The noun comes last, after 的 — slot 4."],
           "**六岁 以下 的 儿童** 免费。", "Children six and under go free."),
      Q("y1_meaning", "Which means 'more than 5,000 people'?",
        ["五千/wǔqiān 人/rén 以上/yǐshàng", "五千/wǔqiān 人/rén 以下/yǐxià", "五千/wǔqiān 人/rén 左右/zuǒyòu", "以上/yǐshàng 五千/wǔqiān 人/rén"],
        ["", "以下 = or fewer.", "左右 = about.", "以上 goes after the number."],
        "**五千人以上** = 5,000 or more.", "more than 5,000 people"),
      Q("y1_meaning", zh("这/zhè 家/jiā 店/diàn 的/de 手机/shǒujī 都/dōu 很/hěn 便宜/piányi ， 一千/yìqiān 块/kuài （　） 。"), ["以下/yǐxià", "以上/yǐshàng", "以后/yǐhòu", "之间/zhījiān"],
        ["", "以上 = 1,000 or more — not 'cheap'.", "以后 is for time.", "之间 needs two numbers: 五百到一千块之间."],
        "Cheap → 1,000 kuai **以下**.", "The phones in this shop are all cheap — under 1,000 kuai."),
      Q("y1_meaning", "What does 「" + zh("这/zhè 个/ge 包/bāo 重/zhòng 二十/èrshí 公斤/gōngjīn 以上/yǐshàng 。") + "」 mean?",
        ["This bag weighs 20 kg or more.", "This bag weighs 20 kg or less.", "This bag weighs about 20 kg.", "This bag is 20 kg lighter."],
        ["", "That's 以下.", "That's 左右.", "That would be 轻二十公斤."],
        "**以上** = that much or more.", "This bag weighs over 20 kg.", raw_opts=True),
      Q("y1_shape", "Which is **wrong**?",
        ["十八/shíbā 以上/yǐshàng 岁/suì 的/de 人/rén", "十八/shíbā 岁/suì 以上/yǐshàng 的/de 人/rén", "十八/shíbā 岁/suì 以下/yǐxià 的/de 人/rén", "六十/liùshí 岁/suì 以上/yǐshàng 的/de 人/rén"],
        ["", "Correct.", "Correct.", "Correct."],
        "以上 comes after the **whole** number phrase: 十八岁以上, not 十八以上岁.", "")])

# ---------------------------------------------------------------- step 2
quiz("12_yishang_2", "zh-dd-yishang-2", "以上 / 以下 Step 2 · Does the Number Count? 以上 vs 超过, 以下 vs 不到",
     "Is an 18-year-old allowed when the sign says 18岁以上? How rules and laws read it, (含) on notices, and the strict words 超过 / 不到 / 不满.",
     [yp("y2_incl", "In rules: the number counts", "In laws, rules and official notices, 以上 / 以下 include the number itself.",
         "- Chinese law states it outright: 以上、以下、以内 **包括本数** (include the number itself).\n"
         "- So 18岁以上 in a rule = 18 **and** older; 60分以下 = 60 and lower.\n"
         "- In everyday speech it's fuzzy, so notices often spell it out: 18岁以上**(含18岁)** — '18 included'; 1.2米以下**(不含)** — 'not included'.",
         [("十八/shíbā 岁/suì 以上/yǐshàng （ 含/hán 十八/shíbā 岁/suì ） 可以/kěyǐ 报名/bàomíng 。", "Ages 18 and over (18 included) can sign up.")]),
      yp("y2_strict", "Strictly more / less: 超过, 高于, 不到, 不满, 低于", "When the number itself must not count, use 超过 / 高于 (more than) or 不到 / 不满 / 低于 (less than).",
         "- **超过** (chāoguò) 一百块 = more than 100 (100 itself doesn't count)\n- **不到** (bú dào) 十个人 = fewer than ten\n"
         "- **不满** (bùmǎn) 十八岁 = not yet 18 (under 18)\n- **至少** (zhìshǎo) = at least (≈ 以上), **最多** (zuìduō) = at most (≈ 以下)",
         [("不满/bùmǎn 十八/shíbā 岁/suì 的/de 人/rén 不能/bù néng 喝/hē 酒/jiǔ 。", "People under 18 may not drink alcohol.")])],
     [yn("y2_incl", "十八/shíbā 岁/suì 以上/yǐshàng （ 含/hán 十八/shíbā 岁/suì ） 可以/kěyǐ 报名/bàomíng 。", "Can an 18-year-old sign up?", True,
         "(含十八岁) = 18 included.", "Ages 18 and over (18 included) can sign up."),
      yn("y2_strict", "身高/shēngāo 超过/chāoguò 一米五/yì mǐ wǔ 的/de 儿童/értóng 要/yào 买/mǎi 全价/quánjià 票/piào 。", "A child is exactly 1.5 m. Full-price ticket?", False,
         "超过 = strictly more than → exactly 1.5 m isn't over the limit.", "Children taller than 1.5 m need a full-price ticket."),
      Q("y2_incl", "In a law or official rule, 「" + zh("六十/liùshí 岁/suì 以上/yǐshàng") + "」 means …",
        ["60 and older — 60 included", "older than 60 — 60 not included", "about 60", "younger than 60"],
        ["", "In rules and laws 以上 **includes** the number.", "That's 六十岁左右.", "That's 以下."],
        "Rules and laws: 以上、以下 **包括本数** — the number counts.", "", raw_opts=True),
      yn("y2_strict", "不满/bùmǎn 十八/shíbā 岁/suì 的/de 人/rén 不能/bù néng 喝/hē 酒/jiǔ 。", "Can a 17-year-old drink?", False,
         "不满十八岁 = not yet 18 → 17 is covered by the ban.", "People under 18 may not drink."),
      yn("y2_strict", "消费/xiāofèi 超过/chāoguò 一百/yìbǎi 元/yuán 打/dǎ 九/jiǔ 折/zhé 。", "You spend exactly 100 yuan. Do you get the discount?", False,
         "超过 = strictly more than → 100 itself doesn't qualify.", "Spend more than 100 yuan and get 10% off."),
      Q("y2_strict", "Which phrase means 'fewer than ten people' — ten **not** included?",
        ["不到/bú dào 十/shí 个/ge 人/rén", "十/shí 个/ge 人/rén 以下/yǐxià", "十/shí 个/ge 人/rén 以上/yǐshàng", "十/shí 多/duō 个/ge 人/rén"],
        ["", "以下 often includes ten (always in rules).", "That's ten or more.", "十多个 = more than ten (eleven to nineteen)."],
        "Strictly fewer: **不到**.", "fewer than ten people"),
      Q("y2_strict", zh("这/zhè 家/jiā 饭馆/fànguǎn 每/měi 人/rén （　） 消费/xiāofèi 五十/wǔshí 块/kuài ， 也/yě 就是/jiùshì 说/shuō 五十/wǔshí 块/kuài 以上/yǐshàng 。"),
        ["至少/zhìshǎo", "最多/zuìduō", "不到/bú dào", "左右/zuǒyòu"],
        ["", "最多 = at most — the opposite of 以上.", "不到 = less than.", "左右 goes after the number."],
        "以上 ≈ **至少** (at least).", "At this restaurant everyone spends at least 50 kuai — that is, 50 or more."),
      Q("y2_incl", "Why do some notices say 「" + zh("一米二/yì mǐ èr 以下/yǐxià （ 含/hán ）") + "」?",
        ["To make clear that exactly 1.2 m counts.", "To say 1.2 m does not count.", "Because 以下 means 'above'.", "Because 含 means 'about'."],
        ["", "That would be (不含).", "以下 = and below.", "含 = including."],
        "In everyday use 以上/以下 can be fuzzy, so notices add **(含)** = inclusive.", "1.2 m and under (inclusive)", raw_opts=True),
      Q("y2_strict", "Which phrase means 'at most 20 kg'?",
        ["最多/zuìduō 二十/èrshí 公斤/gōngjīn", "至少/zhìshǎo 二十/èrshí 公斤/gōngjīn", "超过/chāoguò 二十/èrshí 公斤/gōngjīn", "二十/èrshí 公斤/gōngjīn 以上/yǐshàng"],
        ["", "至少 = at least.", "超过 = more than.", "以上 = 20 or more."],
        "以下 ≈ **最多** (at most).", "at most 20 kg"),
      yn("y2_incl", "六十/liùshí 分/fēn 以上/yǐshàng （ 含/hán 六十/liùshí 分/fēn ） 为/wéi 及格/jígé 。", "You scored exactly 60. Did you pass?", True,
         "(含六十分) = 60 included → pass.", "60 and above (60 included) is a pass."),
      Q("y2_strict", zh("考试/kǎoshì （　） 六十/liùshí 分/fēn 就/jiù 不/bù 及格/jígé 。"), ["不到/bú dào", "以上/yǐshàng", "至少/zhìshǎo", "超过/chāoguò"],
        ["", "以上 goes after the number — and 'above 60' would pass.", "至少六十分 = at least 60 — that's a pass.", "超过六十分 = more than 60 — that's a pass."],
        "Below 60 → fail: **不到**六十分.", "If you get less than 60 in the exam, you fail."),
      Q("y2_incl", "A sign says 「" + zh("限高/xiàn gāo 三/sān 米/mǐ") + "」 (height limit 3 m). Which phrase means the same?",
        ["三/sān 米/mǐ 以下/yǐxià 的/de 车/chē 可以/kěyǐ 通过/tōngguò", "三/sān 米/mǐ 以上/yǐshàng 的/de 车/chē 可以/kěyǐ 通过/tōngguò", "三/sān 米/mǐ 左右/zuǒyòu 的/de 车/chē 可以/kěyǐ 通过/tōngguò", "超过/chāoguò 三/sān 米/mǐ 的/de 车/chē 可以/kěyǐ 通过/tōngguò"],
        ["", "Taller vehicles are exactly what the limit stops.", "左右 = about — a limit is not 'about'.", "超过三米 = taller than 3 m — not allowed."],
        "A height limit lets through vehicles **三米以下**.", "Vehicles 3 m and under may pass.")])

# ---------------------------------------------------------------- step 3
quiz("13_yishang_3", "zh-dd-yishang-3", "以上 / 以下 Step 3 · Levels & Ranks: HSK四级以上, 本科以上",
     "级别: levels, grades, stars and job ranks. HSK四级以上, 本科以上学历, 三星级以上酒店, 经理以上 — and what counts as 'higher'.",
     [yp("y3_levels", "Levels: HSK四级以上, 本科以上学历", "With levels, 以上 = that level or higher, 以下 = that level or lower.",
         "- HSK**四级以上** — HSK level 4 or higher\n- **本科以上**学历 — a bachelor's degree or higher (本科 → 硕士 → 博士)\n"
         "- **三星级以上**的酒店 — three-star hotels or better\n- 地震**五级以下** — an earthquake of magnitude 5 or less",
         [("应聘者/yìngpìnzhě 需要/xūyào 本科/běnkē 以上/yǐshàng 学历/xuélì 。", "Applicants need a bachelor's degree or higher.")]),
      yp("y3_ranks", "Ranks: 经理以上, 科长以下", "With job ranks, 以上 = that rank and the ranks above it.",
         "- **经理以上**的员工 — managers and above\n- **科长以下** — section chief and below\n- Think of a ladder: 以上 = this rung and higher, 以下 = this rung and lower.",
         [("经理/jīnglǐ 以上/yǐshàng 的/de 员工/yuángōng 明天/míngtiān 开会/kāihuì 。", "Managers and above have a meeting tomorrow.")])],
     [yn("y3_levels", "应聘者/yìngpìnzhě 需要/xūyào 本科/běnkē 以上/yǐshàng 学历/xuélì 。", "Can someone with a master's degree (硕士) apply?", True,
         "硕士 is above 本科 → 以上 covers it.", "Applicants need a bachelor's degree or higher."),
      yn("y3_levels", "应聘者/yìngpìnzhě 需要/xūyào 本科/běnkē 以上/yǐshàng 学历/xuélì 。", "Can someone with only a high-school diploma (高中) apply?", False,
         "高中 is below 本科 → not enough.", "Applicants need a bachelor's degree or higher."),
      yn("y3_levels", "申请/shēnqǐng 者/zhě 需要/xūyào 通过/tōngguò HSK 四级/sì jí 以上/yǐshàng 。", "Is HSK level 5 enough?", True,
         "Level 5 is above level 4 → 以上 covers it.", "Applicants need to have passed HSK level 4 or higher."),
      Q("y3_levels", "What does 「" + zh("三/sān 星级/xīngjí 以上/yǐshàng 的/de 酒店/jiǔdiàn") + "」 mean?",
        ["hotels with three stars or more", "hotels with fewer than three stars", "about three hotels", "three hotels above us"],
        ["", "That's 三星级以下.", "That's 三家左右的酒店.", "以上 here is about the star level, not position."],
        "Level + **以上** = that level or higher.", "hotels of three stars or more", raw_opts=True),
      Q("y3_ranks", zh("这/zhè 个/ge 会/huì 只/zhǐ 有/yǒu 经理/jīnglǐ （　） 的/de 人/rén 才/cái 能/néng 参加/cānjiā 。"), ["以上/yǐshàng", "以下/yǐxià", "以前/yǐqián", "左右/zuǒyòu"],
        ["", "以下 would let in everyone below manager — not exclusive.", "以前 is for time.", "Ranks aren't 'about'."],
        "Exclusive meeting → 经理**以上** (managers and up).", "Only people at manager level and above can attend this meeting."),
      Q("y3_ranks", "「" + zh("科长/kēzhǎng 以下/yǐxià 的/de 员工/yuángōng") + "」 — who is included?",
        ["section chiefs and everyone below them", "only people above section chief", "only the section chief", "people who sit downstairs"],
        ["", "That's 科长以上 (and it would include the chief too).", "以下 covers a whole range, not one person.", "以下 here is about rank, not floors."],
        "Rank + **以下** = this rank and lower.", "", raw_opts=True),
      Q("y3_levels", zh("这/zhè 个/ge 班/bān 是/shì 给/gěi HSK 二级/èr jí （　） 的/de 学生/xuésheng 的/de ， 太/tài 简单/jiǎndān 了/le ， 你/nǐ 不/bú 用/yòng 来/lái 。"), ["以下/yǐxià", "以上/yǐshàng", "以后/yǐhòu", "之间/zhījiān"],
        ["", "以上 would be for advanced students — not 'too easy'.", "以后 is for time.", "之间 needs two levels: 二级到三级之间."],
        "Too easy for you → a class for level 2 **以下**.", "This class is for students at HSK level 2 or below — it's too easy, you needn't come."),
      Q("y3_levels", "Which phrase means 'magnitude 6 or above' (earthquakes)?",
        ["六/liù 级/jí 以上/yǐshàng", "以上/yǐshàng 六/liù 级/jí", "六/liù 以上/yǐshàng 级/jí", "六/liù 级/jí 以下/yǐxià"],
        ["", "以上 comes after the level.", "以上 comes after the whole 六级.", "以下 = 6 or below."],
        "**六级以上** = magnitude 6 or more.", "magnitude 6 or above"),
      yn("y3_ranks", "经理/jīnglǐ 以上/yǐshàng 的/de 员工/yuángōng 明天/míngtiān 开会/kāihuì 。", "Is the managing director (总经理, above manager) in the meeting?", True,
         "总经理 is above 经理 → included.", "Managers and above have a meeting tomorrow."),
      yn("y3_ranks", "经理/jīnglǐ 以上/yǐshàng 的/de 员工/yuángōng 明天/míngtiān 开会/kāihuì 。", "Is an ordinary employee (普通员工) in the meeting?", False,
         "普通员工 is below 经理 → not included.", "Managers and above have a meeting tomorrow."),
      Q("y3_levels", "'You need HSK level 5 or higher.' Which sentence says so?",
        ["你/nǐ 需要/xūyào HSK 五级/wǔ jí 以上/yǐshàng 。", "你/nǐ 需要/xūyào 以上/yǐshàng HSK 五级/wǔ jí 。", "你/nǐ 需要/xūyào HSK 五级/wǔ jí 以下/yǐxià 。", "你/nǐ 需要/xūyào HSK 五级/wǔ jí 左右/zuǒyòu 。"],
        ["", "以上 goes after the level.", "以下 = level 5 or lower.", "左右 = about."],
        "Level + **以上**.", "You need HSK level 5 or higher."),
      Q("y3_ranks", "Which is **wrong**?",
        ["他/tā 比/bǐ 我/wǒ 以上/yǐshàng 。", "他/tā 是/shì 经理/jīnglǐ 以上/yǐshàng 的/de 级别/jíbié 。", "我/wǒ 的/de 中文/Zhōngwén 是/shì 四级/sì jí 以上/yǐshàng 。", "三/sān 星级/xīngjí 以上/yǐshàng 的/de 酒店/jiǔdiàn 都/dōu 有/yǒu 早餐/zǎocān 。"],
        ["", "Correct: a rank + 以上.", "Correct: a level + 以上.", "Correct: a star level + 以上 + 的."],
        "以上 follows a **number or level**, not a comparison with a person. For 'higher than me' say 他的级别比我高.", "")])

# ---------------------------------------------------------------- step 4
quiz("14_yishang_4", "zh-dd-yishang-4", "以上 / 以下 Step 4 · Order: 前三名, 以上几点, 以下是…",
     "次序: positions in a ranking (前三名, 第十名以下) and order in a text — 以上 = the above, 以下 = the following.",
     [yp("y4_rank", "Positions in a ranking", "In rankings, 'higher' means better: 前三名 = the top three; 第十名以下 = tenth place and below.",
         "- **前三名** (qián sān míng) — the top three\n- 第十名**以下** — tenth place or worse\n- 第三名**以上** — third place or better (1st, 2nd, 3rd)",
         [("比赛/bǐsài 前/qián 三/sān 名/míng 可以/kěyǐ 拿到/nádào 奖金/jiǎngjīn 。", "The top three in the competition get prize money.")]),
      yp("y4_text", "In a text: 以上 = the above, 以下 = the following", "以上 points back to what was just said, 以下 points forward to what comes next.",
         "- **以上**就是我的介绍。 — That's all for my introduction. (lit. the above is my introduction)\n"
         "- **以上**几点请大家注意。 — Please note the points above.\n- 请看**以下**几点。 — Please look at the following points.\n"
         "- **以下**是今天的安排。 — Here is today's schedule.\n- Spoken equivalents: 上面 / 下面 (下面是…).",
         [("以上/yǐshàng 就是/jiùshì 我/wǒ 的/de 发言/fāyán ， 谢谢/xièxie 大家/dàjiā 。", "That's all from me — thank you, everyone.")])],
     [Q("y4_text", "At the end of a speech: 「" + zh("以上/yǐshàng 就是/jiùshì 我/wǒ 的/de 发言/fāyán 。") + "」 What does it mean?",
        ["That's all from me.", "My speech starts now.", "My speech is above average.", "I'll speak upstairs."],
        ["", "以上 points back — the speech is over.", "以上 here is about order, not quality.", "以上 here is about the text, not floors."],
        "**以上** = what was just said.", "That's all for my speech.", raw_opts=True),
      Q("y4_text", zh("（　） 是/shì 今天/jīntiān 的/de 安排/ānpái ： 九/jiǔ 点/diǎn 开会/kāihuì ， 十二/shí'èr 点/diǎn 吃饭/chīfàn 。"), ["以下/yǐxià", "以上/yǐshàng", "以后/yǐhòu", "以前/yǐqián"],
        ["", "以上 points back — but the schedule comes after.", "以后 = after (time).", "以前 = before (time)."],
        "Pointing forward to a list: **以下**是….", "Here is today's schedule: meeting at nine, lunch at twelve."),
      Q("y4_text", "「" + zh("请/qǐng 注意/zhùyì 以下/yǐxià 几/jǐ 点/diǎn 。") + "」 — where are the points?",
        ["Right after this sentence.", "Before this sentence.", "Below the page.", "Nowhere — it means 'a few o'clock'."],
        ["", "That would be 以上几点.", "以下 here means the following text, not the bottom of the page.", "几点 here = 'a few points'."],
        "**以下** = the following.", "Please note the following points.", raw_opts=True),
      Q("y4_text", "In speech, which word can replace 以下 in 「" + zh("以下/yǐxià 是/shì 今天/jīntiān 的/de 新闻/xīnwén") + "」?",
        ["下面/xiàmian", "上面/shàngmian", "下次/xiàcì", "以后/yǐhòu"],
        ["", "上面 = the above.", "下次 = next time.", "以后 = after (time)."],
        "Spoken: **下面**是… = 以下是….", "Here is today's news."),
      Q("y4_rank", "「" + zh("比赛/bǐsài 前/qián 三/sān 名/míng 有/yǒu 奖/jiǎng 。") + "」 Who wins a prize?",
        ["1st, 2nd and 3rd place", "everyone after 3rd place", "the first three people to arrive", "3rd place only"],
        ["", "That's 第三名以下.", "名 here is about ranking, not arriving.", "前三名 = the top three."],
        "**前三名** = the top three.", "The top three in the competition get prizes.", raw_opts=True),
      yn("y4_rank", "第/dì 三/sān 名/míng 以上/yǐshàng 可以/kěyǐ 进/jìn 决赛/juésài 。", "You came 2nd. Do you go to the final?", True,
         "2nd is better (higher) than 3rd → included.", "Third place or better goes through to the final."),
      yn("y4_rank", "第/dì 三/sān 名/míng 以上/yǐshàng 可以/kěyǐ 进/jìn 决赛/juésài 。", "You came 5th. Do you go to the final?", False,
         "5th is below 3rd → out.", "Third place or better goes through to the final."),
      Q("y4_rank", "「" + zh("第/dì 十/shí 名/míng 以下/yǐxià") + "」 — which places?",
        ["10th place and worse", "places 1 to 10", "exactly 10th", "about 10th"],
        ["", "That's 前十名.", "以下 covers a range.", "That's 第十名左右."],
        "In rankings, **以下** = this place and worse.", "", raw_opts=True),
      Q("y4_text", zh("老师/lǎoshī 说/shuō 了/le 三/sān 件/jiàn 事/shì 。 （　） 三/sān 件/jiàn 事/shì ， 大家/dàjiā 一定/yídìng 要/yào 记住/jìzhu 。"), ["以上/yǐshàng", "以下/yǐxià", "以前/yǐqián", "上次/shàngcì"],
        ["", "以下 points forward — but the three things were already said.", "以前 = before (time) — doesn't fit.", "上次 = last time — they were said just now."],
        "Pointing back to what was just said: **以上**三件事.", "The teacher said three things. Everyone must remember the three things above."),
      Q("y4_text", "Which ending fits a short self-introduction?",
        ["以上/yǐshàng 就是/jiùshì 我/wǒ 的/de 自我/zìwǒ 介绍/jièshào ， 谢谢/xièxie ！", "以下/yǐxià 就是/jiùshì 我/wǒ 的/de 自我/zìwǒ 介绍/jièshào ， 谢谢/xièxie ！", "以后/yǐhòu 就是/jiùshì 我/wǒ 的/de 自我/zìwǒ 介绍/jièshào ， 谢谢/xièxie ！", "以前/yǐqián 就是/jiùshì 我/wǒ 的/de 自我/zìwǒ 介绍/jièshào ， 谢谢/xièxie ！"],
        ["", "以下 would announce an introduction still to come.", "以后 = afterwards (time).", "以前 = before (time)."],
        "Finishing: **以上**就是….", "That's my self-introduction — thank you!"),
      star("y4_text", "请/qǐng ＿ ＿ ★ ＿ 。", ["几/jǐ 点/diǎn", "以下/yǐxià", "看/kàn", "大家/dàjiā"],
           ["以下/yǐxià", "大家/dàjiā", "看/kàn", "几/jǐ 点/diǎn"],
           ["", "大家 comes right after 请 — slot 1.", "The verb 看 follows — slot 2.", "几点 ends the sentence — slot 4."],
           "请 **大家 看 以下 几点**。", "Everyone, please look at the following points.")])

# ---------------------------------------------------------------- step 5
quiz("15_yishang_5", "zh-dd-yishang-5", "以上 / 以下 Step 5 · Which Word? 以上, 以下 and Their Look-Alikes",
     "The big sort: 以上 / 以下 next to 以前 / 以后, 左右, 以内, 之间, 多, 零下 and 超过 / 不到. Each sentence needs exactly one of them.",
     [yp("y5_time", "Time point or amount? 以前 / 以后 vs 以上 / 以下", "A point in time takes 以前 / 以后 (三点以前); an amount of time takes 以上 / 以下 (三个小时以上).",
         "- 三**点**以前 — before three o'clock (a point)\n- 三个**小时**以上 — three hours or more (an amount)\n- 2010年以后 — after 2010; 十年以上 — ten years or more",
         [("我/wǒ 每天/měitiān 工作/gōngzuò 十/shí 个/ge 小时/xiǎoshí 以上/yǐshàng 。", "I work more than ten hours every day.")]),
      yp("y5_others", "左右, 以内, 之间, 多, 零下", "左右 = about, 以内 = within, A到B之间 = between, 多 = -odd, 零下 = minus.",
         "- 二十岁**左右** — about 20\n- 三天**以内** — within three days\n- 二十到三十岁**之间** — between 20 and 30\n- 三十**多**个 — thirty-odd\n"
         "- **零下**五度 = −5° — but 五度**以下** = 5° or below. 零下 goes **before** the number!",
         [("明天/míngtiān 最/zuì 低/dī 气温/qìwēn 零下/língxià 五/wǔ 度/dù 。", "Tomorrow's low is minus five degrees.")])],
     [Q("y5_time", zh("请/qǐng 在/zài 下午/xiàwǔ 三/sān 点/diǎn （　） 交/jiāo 作业/zuòyè 。"), ["以前/yǐqián", "以上/yǐshàng", "以下/yǐxià", "左右/zuǒyòu"],
        ["", "三点 is a point in time — 以上 is for amounts.", "以下 is for amounts, not deadlines.", "左右 = about — a deadline isn't 'about'."],
        "A point in time → **以前**.", "Please hand in your homework before 3 p.m."),
      Q("y5_time", zh("这/zhè 个/ge 电影/diànyǐng 很/hěn 长/cháng ， 有/yǒu 三/sān 个/ge 小时/xiǎoshí （　） 。"), ["以上/yǐshàng", "以前/yǐqián", "以后/yǐhòu", "零下/língxià"],
        ["", "以前 is for points in time.", "以后 is for points in time.", "零下 is for temperatures."],
        "An amount of time → **以上**.", "This film is long — over three hours."),
      Q("y5_others", zh("明天/míngtiān 很/hěn 冷/lěng ， 最/zuì 低/dī 气温/qìwēn （　） 十/shí 度/dù 。"), ["零下/língxià", "以下/yǐxià", "以上/yǐshàng", "左右/zuǒyòu"],
        ["", "以下 goes **after** the number: 十度以下.", "以上 goes after the number — and isn't 'very cold'.", "左右 goes after the number."],
        "Before the number, for minus: **零下**十度 = −10°.", "Tomorrow will be very cold — the low is minus ten."),
      Q("y5_others", "「" + zh("零下/língxià 五/wǔ 度/dù") + "」 vs 「" + zh("五/wǔ 度/dù 以下/yǐxià") + "」 — which is right?",
        ["零下五度 is −5°; 五度以下 is 5° or colder.", "Both mean −5°.", "Both mean 5° or colder.", "零下五度 is 5° or colder; 五度以下 is −5°."],
        ["", "五度以下 can be +3°, for example.", "零下五度 is one exact temperature.", "Swapped."],
        "**零下** = minus (before the number); **以下** = and below (after it).", "", raw_opts=True),
      Q("y5_others", zh("他/tā 看/kàn 起来/qǐlai 二十/èrshí 岁/suì （　） ， 不/bú 太/tài 清楚/qīngchu 。"), ["左右/zuǒyòu", "以上/yǐshàng", "以下/yǐxià", "以内/yǐnèi"],
        ["", "以上 is a limit — but you're guessing.", "以下 is a limit — but you're guessing.", "以内 = within — doesn't fit an age guess."],
        "A guess, 'about': **左右**.", "He looks about twenty — I'm not sure."),
      Q("y5_others", zh("请/qǐng 在/zài 三/sān 天/tiān （　） 回复/huífù 。"), ["以内/yǐnèi", "以上/yǐshàng", "左右/zuǒyòu", "零下/língxià"],
        ["", "三天以上 = after waiting three days or more — the opposite.", "A deadline isn't 'about'.", "零下 is for temperatures."],
        "Within: **以内**.", "Please reply within three days."),
      Q("y5_others", zh("参加/cānjiā 的/de 人/rén 年龄/niánlíng 都/dōu 在/zài 二十/èrshí 到/dào 三十/sānshí 岁/suì （　） 。"), ["之间/zhījiān", "以上/yǐshàng", "以下/yǐxià", "左右/zuǒyòu"],
        ["", "以上 takes one number.", "以下 takes one number.", "左右 takes one number."],
        "A到B + **之间** = between A and B.", "The participants are all between 20 and 30."),
      Q("y5_others", zh("教室/jiàoshì 里/lǐ 有/yǒu 三十/sānshí （　） 个/ge 学生/xuésheng 。"), ["多/duō", "以上/yǐshàng", "以下/yǐxià", "左右/zuǒyòu"],
        ["", "以上 comes after 个学生 — not before 个.", "以下 comes after the whole phrase.", "左右 also comes after the phrase: 三十个左右."],
        "Number + **多** + measure word = thirty-odd.", "There are thirty-odd students in the classroom."),
      Q("y5_time", zh("我/wǒ 在/zài 北京/Běijīng 住/zhù 了/le 五/wǔ 年/nián （　） ， 很/hěn 熟悉/shúxī 这儿/zhèr 。"), ["以上/yǐshàng", "以前/yǐqián", "以内/yǐnèi", "零下/língxià"],
        ["", "五年以前 = five years ago — a point.", "以内 = within — doesn't fit 'very familiar'.", "零下 is for temperatures."],
        "An amount of time → **以上**.", "I've lived in Beijing for more than five years — I know it well."),
      Q("y5_time", zh("二〇一〇年/èr líng yī líng nián （　） ， 我/wǒ 一直/yìzhí 住/zhù 在/zài 上海/Shànghǎi 。"), ["以后/yǐhòu", "以上/yǐshàng", "以下/yǐxià", "多/duō"],
        ["", "A year like 2010 is a point in time.", "A year is a point in time.", "多 doesn't fit."],
        "A point in time → **以后**.", "Since 2010 I've lived in Shanghai."),
      Q("y5_others", zh("这/zhè 条/tiáo 路/lù 限速/xiànsù 六十/liùshí 公里/gōnglǐ ， 你/nǐ 开/kāi 了/le 八十/bāshí ， （　） 了/le ！"), ["超速/chāosù", "以下/yǐxià", "以内/yǐnèi", "左右/zuǒyòu"],
        ["", "以下 would mean you were within the limit.", "以内 would mean within the limit.", "左右 = about."],
        "Over the limit → **超速** (speeding; 超 = exceed, as in 超过).", "The limit on this road is 60 km/h — you did 80, you were speeding!"),
      Q("y5_others", "'Fewer than 100 people came' — 100 not included. Which is best?",
        ["来/lái 的/de 人/rén 不到/bú dào 一百/yìbǎi 个/ge 。", "来/lái 的/de 人/rén 一百/yìbǎi 个/ge 以上/yǐshàng 。", "来/lái 的/de 人/rén 有/yǒu 一百/yìbǎi 多/duō 个/ge 。", "来/lái 的/de 人/rén 一百/yìbǎi 个/ge 左右/zuǒyòu 。"],
        ["", "以上 = 100 or more.", "一百多 = more than 100.", "左右 = about 100."],
        "Strictly fewer → **不到**.", "Fewer than 100 people came."),
      Q("y5_time", "Which is **wrong**?",
        ["三/sān 点/diǎn 以上/yǐshàng 我/wǒ 有/yǒu 空/kòng 。", "三/sān 点/diǎn 以后/yǐhòu 我/wǒ 有/yǒu 空/kòng 。", "三/sān 个/ge 小时/xiǎoshí 以上/yǐshàng", "三/sān 天/tiān 以内/yǐnèi"],
        ["", "Correct: a point in time + 以后.", "Correct: an amount + 以上.", "Correct: within three days."],
        "三点 is a point in time → 三点**以后**, not 以上.", "I'm free after three."),
      Q("y5_others", zh("零下/língxià 的/de 天气/tiānqì ， 水/shuǐ 会/huì 结冰/jiébīng 。 意思/yìsi 是/shì 零/líng 度/dù （　） 。"), ["以下/yǐxià", "以上/yǐshàng", "左右/zuǒyòu", "以前/yǐqián"],
        ["", "Above zero, water doesn't freeze.", "左右 = about zero — not the meaning of 零下.", "以前 is for time."],
        "零下 = below zero = 零度**以下**.", "In sub-zero weather water freezes — that means below zero degrees.")])

# ---------------------------------------------------------------- step 6
quiz("16_yishang_6", "zh-dd-yishang-6", "以上 / 以下 Step 6 · Read the Sign: Build, Choose, Fix",
     "Notices, ads and rules: who's allowed, who pays, who's in? Then build the phrases yourself and catch the mistakes.",
     [yp("y6_signs", "Reading signs and rules", "Check the number, the direction (以上 / 以下) and whether the number itself counts (含 / 超过 / 不到).",
         "- 身高一米四**以上**才能乘坐 — only riders 1.4 m and taller\n- 消费满一百元**以上**打九折 — spend 100 or more, get 10% off\n- 托运行李二十公斤**以下**免费 — checked luggage up to 20 kg is free",
         [("身高/shēngāo 一米四/yì mǐ sì 以上/yǐshàng 才/cái 能/néng 乘坐/chéngzuò 。", "Riders must be 1.4 m or taller.")]),
      yp("y6_fix", "Spotting mistakes", "以上 / 以下 go after the number phrase, need 的 before a noun, and are for amounts and levels, not points in time.",
         "- ~~以上一百块~~ → 一百块以上\n- ~~六十岁以上老人~~ → 六十岁以上**的**老人 (in notices 的 is sometimes dropped, but learn it with 的)\n- ~~下午三点以上~~ → 下午三点**以后**",
         [("一百/yìbǎi 块/kuài 以上/yǐshàng 的/de 东西/dōngxi 包邮/bāoyóu 。", "Items over 100 kuai ship free.")])],
     [yn("y6_signs", "身高/shēngāo 一米四/yì mǐ sì 以上/yǐshàng 才/cái 能/néng 乘坐/chéngzuò 过山车/guòshānchē 。", "Can a 1.3 m child ride the roller coaster?", False,
         "1.3 m is below 1.4 m.", "Only riders 1.4 m and taller may ride the roller coaster."),
      yn("y6_signs", "托运/tuōyùn 行李/xíngli 二十/èrshí 公斤/gōngjīn 以下/yǐxià 免费/miǎnfèi 。", "Your suitcase weighs 18 kg. Is it free?", True,
         "18 kg is under 20 kg.", "Checked luggage of 20 kg or less is free."),
      yn("y6_signs", "消费/xiāofèi 满/mǎn 二百/èrbǎi 元/yuán 以上/yǐshàng 送/sòng 一/yì 杯/bēi 咖啡/kāfēi 。", "You spend 150 yuan. Do you get a free coffee?", False,
         "150 is below 200.", "Spend 200 yuan or more and get a free coffee."),
      Q("y6_signs", "Ticket rules: 「" + zh("六/liù 岁/suì 以下/yǐxià 免票/miǎnpiào ， 六十五/liùshíwǔ 岁/suì 以上/yǐshàng 半价/bànjià 。") + "」 Who pays full price?",
        ["a 30-year-old", "a 4-year-old", "a 70-year-old", "nobody"],
        ["", "4 is under 6 → free.", "70 is over 65 → half price.", "Everyone between 6 and 65 pays full price."],
        "Between the two limits → **full price**.", "Children six and under go free; people 65 and over pay half price.", raw_opts=True),
      Q("y6_signs", "A job ad: 「" + zh("要求/yāoqiú ： 三/sān 年/nián 以上/yǐshàng 工作/gōngzuò 经验/jīngyàn ， 三十五/sānshíwǔ 岁/suì 以下/yǐxià 。") + "」 Who fits?",
        ["29 years old, 4 years' experience", "40 years old, 10 years' experience", "25 years old, 1 year's experience", "38 years old, 2 years' experience"],
        ["", "40 is over 35.", "One year is under three.", "38 is over 35, and two years is under three."],
        "Experience **三年以上** and age **三十五岁以下** — only the first fits both.", "Requirements: three or more years' experience, aged 35 or under.", raw_opts=True),
      star("y6_signs", "＿ ＿ ★ ＿ 包邮/bāoyóu 。", ["以上/yǐshàng", "东西/dōngxi", "的/de", "一百/yìbǎi 块/kuài"],
           ["的/de", "一百/yìbǎi 块/kuài", "以上/yǐshàng", "东西/dōngxi"],
           ["", "The amount comes first — slot 1.", "以上 follows the amount — slot 2.", "The noun comes last — slot 4."],
           "**一百块 以上 的 东西** 包邮。", "Items over 100 kuai ship free."),
      star("y6_signs", "这/zhè 家/jiā 酒店/jiǔdiàn ＿ ＿ ★ ＿ 。", ["以上/yǐshàng", "五/wǔ 星级/xīngjí", "是/shì", "的/de"],
           ["以上/yǐshàng", "是/shì", "五/wǔ 星级/xīngjí", "的/de"],
           ["", "是 comes first — slot 1.", "The level follows — slot 2.", "的 closes the 是…的 phrase — slot 4."],
           "这家酒店 **是 五星级 以上 的**。", "This hotel is five-star or above."),
      Q("y6_fix", "Which is **wrong**?",
        ["以上/yǐshàng 一百/yìbǎi 块/kuài 的/de 东西/dōngxi", "一百/yìbǎi 块/kuài 以上/yǐshàng 的/de 东西/dōngxi", "一百/yìbǎi 块/kuài 以下/yǐxià 的/de 东西/dōngxi", "不到/bú dào 一百/yìbǎi 块/kuài 的/de 东西/dōngxi"],
        ["", "Correct.", "Correct.", "Correct: 不到 goes **before** the number."],
        "以上 goes **after** the number. (不到 goes before — that one's right.)", ""),
      Q("y6_fix", "Which is **wrong**?",
        ["我/wǒ 下午/xiàwǔ 三/sān 点/diǎn 以上/yǐshàng 有/yǒu 空/kòng 。", "我/wǒ 下午/xiàwǔ 三/sān 点/diǎn 以后/yǐhòu 有/yǒu 空/kòng 。", "我/wǒ 每天/měitiān 睡/shuì 八/bā 个/ge 小时/xiǎoshí 以上/yǐshàng 。", "会议/huìyì 一般/yìbān 一/yí 个/ge 小时/xiǎoshí 以内/yǐnèi 。"],
        ["", "Correct: a point in time + 以后.", "Correct: an amount + 以上.", "Correct: within an hour."],
        "三点 is a point in time → **以后**, not 以上.", "I'm free after three this afternoon."),
      Q("y6_fix", "Which is **wrong**?",
        ["明天/míngtiān 五/wǔ 度/dù 零下/língxià 。", "明天/míngtiān 零下/língxià 五/wǔ 度/dù 。", "明天/míngtiān 五/wǔ 度/dù 以下/yǐxià 。", "明天/míngtiān 五/wǔ 度/dù 左右/zuǒyòu 。"],
        ["", "Correct: minus five.", "Correct: five or colder.", "Correct: about five."],
        "零下 goes **before** the number: 零下五度.", "Tomorrow: minus five."),
      Q("y6_signs", "'Applicants must be 18 or over — 18 included.' Which says it most precisely?",
        ["申请人/shēnqǐngrén 须/xū 年满/nián mǎn 十八/shíbā 岁/suì （ 含/hán 十八/shíbā 岁/suì ） 以上/yǐshàng 。", "申请人/shēnqǐngrén 须/xū 超过/chāoguò 十八/shíbā 岁/suì 。", "申请人/shēnqǐngrén 须/xū 不满/bùmǎn 十八/shíbā 岁/suì 。", "申请人/shēnqǐngrén 须/xū 十八/shíbā 岁/suì 左右/zuǒyòu 。"],
        ["", "超过 = older than 18 — 18 itself is out.", "不满 = under 18 — the opposite.", "左右 = about 18."],
        "(含) makes 以上 explicitly **inclusive**.", "Applicants must be 18 or over (18 included)."),
      Q("y6_signs", "A shop sign: 「" + zh("全场/quánchǎng 商品/shāngpǐn 五十/wǔshí 元/yuán 以下/yǐxià") + "」 What does it tell you?",
        ["Everything in the shop costs 50 yuan or less.", "Everything costs more than 50 yuan.", "Everything is 50% off.", "There are 50 items below."],
        ["", "That would be 以上.", "50% off = 五折.", "以下 here is about price, not position."],
        "Price + **以下** = that price or less.", "Everything in the shop is 50 yuan or less.", raw_opts=True)])

# ---------------------------------------------------------------- step 7
YS_AD = ("招聘/zhāopìn ： 中文/Zhōngwén 老师/lǎoshī 一/yì 名/míng 。 要求/yāoqiú ： 硕士/shuòshì 以上/yǐshàng 学历/xuélì ， HSK 六级/liù jí 以上/yǐshàng ， "
         "两/liǎng 年/nián 以上/yǐshàng 教学/jiàoxué 经验/jīngyàn ， 四十/sìshí 岁/suì 以下/yǐxià 。 每/měi 周/zhōu 工作/gōngzuò 二十/èrshí 个/ge 小时/xiǎoshí 左右/zuǒyòu 。")
YS_AD_EN = ("Wanted: one Chinese teacher. Requirements: a master's degree or higher, HSK level 6 or above, two or more years' teaching experience, "
            "aged 40 or under. About 20 hours a week.")
YS_PARK = ("欢乐/Huānlè 公园/Gōngyuán 票价/piàojià ： 成人/chéngrén 一百二十/yìbǎi èrshí 元/yuán 。 身高/shēngāo 一米二/yì mǐ èr 以下/yǐxià （ 含/hán ） 的/de 儿童/értóng 免票/miǎnpiào ， "
           "六十/liùshí 岁/suì 以上/yǐshàng 的/de 老人/lǎorén 半价/bànjià 。 过山车/guòshānchē ： 身高/shēngāo 一米四/yì mǐ sì 以上/yǐshàng 才/cái 能/néng 乘坐/chéngzuò 。")
YS_PARK_EN = ("Happy Park ticket prices: adults 120 yuan. Children 1.2 m and under (inclusive) free; people 60 and over half price. "
              "Roller coaster: riders must be 1.4 m or taller.")
YS_TRIP = ("以下/yǐxià 是/shì 小林/Xiǎo Lín 周末/zhōumò 的/de 安排/ānpái ： 星期六/xīngqīliù 上午/shàngwǔ 十/shí 点/diǎn 以前/yǐqián 到/dào 机场/jīchǎng ， "
           "托运/tuōyùn 行李/xíngli 不/bù 能/néng 超过/chāoguò 二十三/èrshísān 公斤/gōngjīn 。 天气/tiānqì 预报/yùbào 说/shuō 哈尔滨/Hā'ěrbīn 最/zuì 低/dī 零下/língxià 二十/èrshí 度/dù 。")
YS_TRIP_EN = ("Here is Xiao Lin's weekend plan: be at the airport before 10 a.m. on Saturday; checked luggage may not exceed 23 kg. "
              "The forecast says Harbin will drop to minus 20 degrees.")
quiz("17_yishang_7", "zh-dd-yishang-7", "以上 / 以下 Step 7 · Boss Level: 小林 Reads the Fine Print",
     "A job ad, a theme park and a winter trip: read the notices HSK-style and decide who qualifies, who pays and what to pack.",
     [yp("y7_read", "Reading notices for limits", "Underline every number with 以上 / 以下 / 以内 / 超过 / 零下, and check each person against it.",
         "Work through one limit at a time — a person must pass **all** of them.",
         [("硕士/shuòshì 以上/yǐshàng 学历/xuélì ， 四十/sìshí 岁/suì 以下/yǐxià 。", "A master's degree or higher, aged 40 or under.")]),
      yp("y7_mixed", "Final mixed challenge", "Numbers, levels, order and look-alikes — all together.",
         "If in doubt: amount or point in time? Before or after the number? Does the number count?",
         [("以上/yǐshàng 就是/jiùshì 今天/jīntiān 的/de 内容/nèiróng 。", "That's all for today.")])],
     [reading("y7_read", YS_AD, "谁/shéi 可以/kěyǐ 申请/shēnqǐng 这个/zhège 工作/gōngzuò ？",
              ["三十二/sānshí'èr 岁/suì ， 博士/bóshì ， HSK 六级/liù jí ， 教/jiāo 了/le 五/wǔ 年/nián", "四十五/sìshíwǔ 岁/suì ， 硕士/shuòshì ， HSK 六级/liù jí ， 教/jiāo 了/le 十/shí 年/nián",
               "二十八/èrshíbā 岁/suì ， 本科/běnkē ， HSK 六级/liù jí ， 教/jiāo 了/le 三/sān 年/nián", "三十/sānshí 岁/suì ， 硕士/shuòshì ， HSK 五级/wǔ jí ， 教/jiāo 了/le 四/sì 年/nián"],
              ["", "45 is over 40.", "本科 is below 硕士.", "HSK 5 is below level 6."],
              "博士 is above 硕士, 32 ≤ 40, HSK 6, five years ≥ two → the **first** person.", YS_AD_EN + " ★ Who can apply?"),
      tf("y7_read", YS_AD, "这个/zhège 工作/gōngzuò 每/měi 周/zhōu 正好/zhènghǎo 二十/èrshí 个/ge 小时/xiǎoshí 。", False,
         "二十个小时左右 = about 20 — not exactly.", "左右 = **about** — not exactly 20 hours.", YS_AD_EN + " ★ The job is exactly 20 hours a week."),
      tf("y7_read", YS_AD, "有/yǒu 一/yì 年/nián 教学/jiàoxué 经验/jīngyàn 的/de 人/rén 也/yě 可以/kěyǐ 申请/shēnqǐng 。", False,
         "两年以上 = two years or more — one year isn't enough.", "Experience must be **两年以上**. False.", YS_AD_EN + " ★ Someone with one year's experience can also apply."),
      reading("y7_read", YS_PARK, "小林/Xiǎo Lín （ 三十/sānshí 岁/suì ） 、 他/tā 女儿/nǚ'ér （ 一米二/yì mǐ èr ） 和/hé 他/tā 妈妈/māma （ 六十二/liùshí'èr 岁/suì ） 一共/yígòng 要/yào 花/huā 多少/duōshao 钱/qián ？",
              ["一百八十/yìbǎi bāshí 元/yuán", "二百四十/èrbǎi sìshí 元/yuán", "三百六十/sānbǎi liùshí 元/yuán", "一百二十/yìbǎi èrshí 元/yuán"],
              ["", "That leaves out the daughter's free ticket — and charges someone twice.", "That's three full tickets.", "That forgets his mother's half-price ticket."],
              "Xiao Lin 120 + daughter (1.2 m, inclusive → free) 0 + mother (62 ≥ 60 → half) 60 = **180 yuan**.", YS_PARK_EN + " ★ How much do Xiao Lin (30), his daughter (1.2 m) and his mother (62) pay in total?"),
      tf("y7_read", YS_PARK, "小林/Xiǎo Lín 的/de 女儿/nǚ'ér （ 一米二/yì mǐ èr ） 可以/kěyǐ 坐/zuò 过山车/guòshānchē 。", False,
         "过山车 needs 一米四以上 — 1.2 m is too short.", "1.2 m < 1.4 m → **not allowed**.", YS_PARK_EN + " ★ Xiao Lin's daughter (1.2 m) can ride the roller coaster."),
      tf("y7_read", YS_PARK, "一米二/yì mǐ èr 的/de 孩子/háizi 不用/bú yòng 买票/mǎi piào 。", True,
         "(含) = 1.2 m itself counts → free.", "一米二以下**(含)** → 1.2 m included → **free**.", YS_PARK_EN + " ★ A 1.2 m child doesn't need a ticket."),
      reading("y7_read", YS_TRIP, "小林/Xiǎo Lín 的/de 行李/xíngli 最/zuì 重/zhòng 可以/kěyǐ 是/shì 多少/duōshao ？",
              ["二十三/èrshísān 公斤/gōngjīn", "二十三/èrshísān 公斤/gōngjīn 以上/yǐshàng 都/dōu 可以/kěyǐ", "二十/èrshí 公斤/gōngjīn", "没有/méiyǒu 限制/xiànzhì"],
              ["", "不能超过 = may not be more than 23.", "The limit is 23, not 20.", "There is a limit."],
              "不能**超过**二十三公斤 → at most **23 kg**.", YS_TRIP_EN + " ★ What's the most Xiao Lin's luggage can weigh?"),
      tf("y7_read", YS_TRIP, "哈尔滨/Hā'ěrbīn 最/zuì 低/dī 二十/èrshí 度/dù 左右/zuǒyòu ， 不/bù 太/tài 冷/lěng 。", False,
         "零下二十度 = −20° — very cold!", "**零下**二十度 = minus 20. Pack a warm coat!", YS_TRIP_EN + " ★ Harbin's low is about 20 degrees — not very cold."),
      tf("y7_read", YS_TRIP, "小林/Xiǎo Lín 十/shí 点/diǎn 以后/yǐhòu 到/dào 机场/jīchǎng 也/yě 可以/kěyǐ 。", False,
         "十点以前 = before ten.", "The plan says **十点以前** — before ten.", YS_TRIP_EN + " ★ Xiao Lin can also get to the airport after ten."),
      Q("y7_mixed", zh("（　） 是/shì 小林/Xiǎo Lín 周末/zhōumò 的/de 安排/ānpái ： …"), ["以下/yǐxià", "以上/yǐshàng", "以前/yǐqián", "左右/zuǒyòu"],
        ["", "以上 points back — the plan follows.", "以前 = before (time).", "左右 = about."],
        "Pointing forward: **以下**是….", "Here is Xiao Lin's weekend plan: …"),
      Q("y7_mixed", "Which sentence is correct?",
        ["六十/liùshí 岁/suì 以上/yǐshàng 的/de 老人/lǎorén 半价/bànjià 。", "以上/yǐshàng 六十/liùshí 岁/suì 的/de 老人/lǎorén 半价/bànjià 。", "六十/liùshí 以上/yǐshàng 岁/suì 的/de 老人/lǎorén 半价/bànjià 。", "六十/liùshí 岁/suì 以前/yǐqián 的/de 老人/lǎorén 半价/bànjià 。"],
        ["", "以上 goes after the number.", "以上 goes after the whole 六十岁.", "以前 is for points in time, not ages as a limit."],
        "Number phrase + **以上** + 的 + noun.", "People aged 60 and over pay half price."),
      Q("y7_mixed", "Which pair is right?",
        ["三个小时以上 = 3 hours or more; 三点以后 = after 3 o'clock",
         "三个小时以后 = 3 hours or more; 三点以上 = after 3 o'clock",
         "三个小时以上 = after 3 o'clock; 三点以后 = 3 hours or more",
         "Both pairs mean the same."],
        ["", "Swapped: amounts take 以上, points in time take 以后.", "Swapped meanings.", "One is an amount, the other a point in time."],
        "Amount → **以上 / 以下**; point in time → **以前 / 以后**.", "", fixed=True, raw_opts=True)])

write(QZ, "quizzes/54_zh_deep", "Mandarin Deep Dives", "Deep dive", seed=5401)
