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

write(QZ, "quizzes/54_zh_deep", "Mandarin Deep Dives", "Deep dive", seed=5401)
