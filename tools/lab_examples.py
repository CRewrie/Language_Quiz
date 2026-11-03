"""Example sentences for the Verb Lab and Adjective Lab drills, shown after answering.

FORM: one line per word and form: key | form id | sentence with the form | English.
WORD: one line per word, for the "what type is it?" questions: key | sentence | English.
The generators check that each sentence contains the form it illustrates.
"""

FORM = """
ある|nai|{時間|じかん}が**ない**から、タクシーで{行|い}こう。|We don't have time, so let's take a taxi.
会う|nai|{日曜日|にちようび}は{誰|だれ}にも**{会|あ}わない**。|I'm not meeting anyone on Sunday.
住む|ta|{昔|むかし}、{大阪|おおさか}に**{住|す}んだ**ことがある。|I once lived in Osaka.
住む|teiru|{今|いま}は{東京|とうきょう}に**{住|す}んでいる**。|I live in Tokyo now.
予約する|ta|{駅前|えきまえ}のレストランを**{予約|よやく}した**。|I booked the restaurant by the station.
借りる|masu|{図書館|としょかん}で{本|ほん}を**{借|か}ります**。|I borrow books from the library.
入る|masu|{毎晩|まいばん}お{風呂|ふろ}に**{入|はい}ります**。|I take a bath every evening.
入る|nai|{寒|さむ}いから、{海|うみ}には**{入|はい}らない**。|It's cold, so I'm not going in the sea.
分かる|nai|この{漢字|かんじ}の{意味|いみ}が**{分|わ}からない**。|I don't understand this kanji.
切る|ba|{髪|かみ}を**{切|き}れば**、すっきりするよ。|If you cut your hair, you'll feel fresh.
切る|te|{野菜|やさい}を**{切|き}って**、{鍋|なべ}に{入|い}れてください。|Cut the vegetables and put them in the pot.
勉強する|potential|{図書館|としょかん}なら{静|しず}かに**{勉強|べんきょう}できる**。|At the library I can study in peace.
勝つ|ta|{昨日|きのう}の{試合|しあい}はうちのチームが**{勝|か}った**。|Our team won yesterday's match.
始める|volitional|そろそろ{会議|かいぎ}を**{始|はじ}めよう**。|Let's start the meeting.
寝る|potential|どこでも**{寝|ね}られる**のが{私|わたし}の{特技|とくぎ}です。|Being able to sleep anywhere is my special talent.
寝る|volitional|{明日|あした}は{早|はや}いから、もう**{寝|ね}よう**。|We have an early start tomorrow, so let's go to bed.
寝る|ta|{昨日|きのう}は11{時|じ}に**{寝|ね}た**。|I went to bed at eleven yesterday.
帰る|te|{家|いえ}に**{帰|かえ}って**、すぐ{寝|ね}た。|I went home and went straight to bed.
帰る|nai|{今夜|こんや}は{家|いえ}に**{帰|かえ}らない**。|I'm not going home tonight.
帰る|potential|{明日|あした}は{早|はや}く**{帰|かえ}れる**。|I can go home early tomorrow.
帰る|volitional|もう{遅|おそ}いから**{帰|かえ}ろう**。|It's late, so let's go home.
待つ|ta|{駅|えき}で30{分|ぷん}も**{待|ま}った**。|I waited a whole thirty minutes at the station.
待つ|potential|あと5{分|ふん}なら**{待|ま}てる**よ。|I can wait five more minutes.
待つ|volitional|{雨|あめ}がやむまで**{待|ま}とう**。|Let's wait until the rain stops.
待つ|nai|もうこれ{以上|いじょう}**{待|ま}たない**。|I'm not waiting any longer.
待つ|te|ちょっと**{待|ま}って**ください。|Please wait a moment.
心配する|ta|{連絡|れんらく}がなかったので、**{心配|しんぱい}した**よ。|You didn't get in touch, so I was worried.
忘れる|nai|この{日|ひ}のことは{一生|いっしょう}**{忘|わす}れない**。|I'll never forget this day.
思う|masen|{私|わたし}はそうは**{思|おも}いません**。|I don't think so.
急ぐ|te|**{急|いそ}いで**{駅|えき}まで{走|はし}った。|I hurried to the station.
手伝う|nai|{弟|おとうと}は{家事|かじ}を{全然|ぜんぜん}**{手伝|てつだ}わない**。|My little brother never helps with the housework.
払う|ta|お{昼|ひる}ご{飯|はん}は{私|わたし}が**{払|はら}った**。|I paid for lunch.
探す|volitional|{一緒|いっしょ}に{鍵|かぎ}を**{探|さが}そう**。|Let's look for the key together.
探す|ta|{部屋|へや}{中|じゅう}**{探|さが}した**けど、なかった。|I searched the whole room, but it wasn't there.
散歩する|volitional|{天気|てんき}がいいから、{公園|こうえん}を**{散歩|さんぽ}しよう**。|The weather's nice, so let's take a walk in the park.
書く|masu|{毎日|まいにち}{日記|にっき}を**{書|か}きます**。|I write in my diary every day.
書く|ta|{昨日|きのう}、{母|はは}に{手紙|てがみ}を**{書|か}いた**。|I wrote a letter to my mother yesterday.
書く|potential|ひらがなならもう**{書|か}ける**よ。|I can already write hiragana.
書く|ba|{名前|なまえ}を**{書|か}けば**、{誰|だれ}のか{分|わ}かる。|If you write your name on it, we'll know whose it is.
書く|volitional|{先生|せんせい}にお{礼|れい}のメールを**{書|か}こう**。|I'll write my teacher a thank-you email.
書く|nai|{最近|さいきん}、{手紙|てがみ}はあまり**{書|か}かない**。|I don't write many letters these days.
書く|te|ここに{名前|なまえ}を**{書|か}いて**ください。|Please write your name here.
来る|te|{明日|あした}も**{来|き}て**ください。|Please come tomorrow too.
来る|nai|バスがなかなか**{来|こ}ない**。|The bus just isn't coming.
来る|potential|{明日|あした}のパーティー、**{来|こ}られる**？|Can you come to the party tomorrow?
来る|ba|{早|はや}く**{来|く}れば**、いい{席|せき}に{座|すわ}れるよ。|If you come early, you'll get a good seat.
来る|volitional|ここ、いい{店|みせ}だね。また**{来|こ}よう**。|This is a nice place. Let's come again.
来る|ta|{昨日|きのう}、{友達|ともだち}が{家|いえ}に**{来|き}た**。|A friend came to my place yesterday.
来る|masen|{田中|たなか}さんは{今日|きょう}**{来|き}ません**。|Tanaka isn't coming today.
来る|masu|{先生|せんせい}は{毎週|まいしゅう}{火曜日|かようび}に**{来|き}ます**。|The teacher comes every Tuesday.
する|potential|{日本語|にほんご}で{自己紹介|じこしょうかい}が**できる**ようになった。|I can now introduce myself in Japanese.
する|ba|{毎日|まいにち}{練習|れんしゅう}**すれば**、{上手|じょうず}になるよ。|If you practise every day, you'll get good.
する|volitional|{週末|しゅうまつ}は{何|なに}を**しよう**か。|What shall we do at the weekend?
する|nai|{日曜日|にちようび}は{仕事|しごと}を**しない**。|I don't work on Sundays.
する|nakatta|{昨日|きのう}は{何|なに}も**しなかった**。|I didn't do anything yesterday.
する|ta|{昨日|きのう}、{友達|ともだち}とテニスを**した**。|I played tennis with a friend yesterday.
する|masu|{毎朝|まいあさ}ジョギングを**します**。|I go jogging every morning.
する|te|{宿題|しゅくだい}を**して**から{遊|あそ}ぶ。|I'll play after I've done my homework.
死ぬ|te|{祖父|そふ}が**{死|し}んで**、もう5{年|ねん}になる。|It's been five years since my grandfather died.
泳ぐ|potential|{私|わたし}は1キロ**{泳|およ}げる**。|I can swim a kilometre.
泳ぐ|te|{海|うみ}で**{泳|およ}いで**、{楽|たの}しかった。|We swam in the sea and had fun.
洗う|nai|この{服|ふく}は{家|いえ}で**{洗|あら}わない**ほうがいい。|You'd better not wash these clothes at home.
洗う|te|{手|て}を**{洗|あら}って**から{食|た}べてね。|Wash your hands before you eat.
渡す|ba|このメモを**{渡|わた}せば**{分|わ}かります。|If you hand over this note, they'll understand.
渡す|ta|プレゼントを{彼女|かのじょ}に**{渡|わた}した**。|I gave her the present.
疲れる|ta|{今日|きょう}は{本当|ほんとう}に**{疲|つか}れた**。|I'm really tired today.
着る|te|{浴衣|ゆかた}を**{着|き}て**{祭|まつ}りに{行|い}った。|I wore a yukata and went to the festival.
着る|nai|{夏|なつ}はコートを**{着|き}ない**。|I don't wear a coat in summer.
着る|potential|この{服|ふく}はまだ**{着|き}られる**。|These clothes can still be worn.
着替える|te|**{着替|きが}えて**から{出|で}かけます。|I'll get changed and then go out.
知る|nai|その{話|はなし}は**{知|し}らない**。|I don't know that story.
知る|te|この{店|みせ}、**{知|し}って**いる？|Do you know this shop?
磨く|causative_ta|{母|はは}は{子供|こども}に{歯|は}を**{磨|みが}かせた**。|The mother had her child brush his teeth.
磨く|ta|{寝|ね}る{前|まえ}に{歯|は}を**{磨|みが}いた**。|I brushed my teeth before bed.
笑う|passive_ta|{変|へん}な{発音|はつおん}をして、みんなに**{笑|わら}われた**。|I mispronounced something and everyone laughed at me.
笑う|ta|その{話|はなし}を{聞|き}いて、みんな**{笑|わら}った**。|Everyone laughed when they heard that story.
答える|ba|{全部|ぜんぶ}{正|ただ}しく**{答|こた}えれば**、{合格|ごうかく}です。|If you answer everything correctly, you pass.
答える|ta|{先生|せんせい}の{質問|しつもん}に**{答|こた}えた**。|I answered the teacher's question.
結婚する|volitional|{彼|かれ}に「**{結婚|けっこん}しよう**」と{言|い}われた。|He said to me, 'Let's get married.'
置く|tara|{荷物|にもつ}を**{置|お}いたら**、すぐ{出|で}かけよう。|Once we've put our bags down, let's head out.
置く|ta|{鍵|かぎ}をどこに**{置|お}いた**か{忘|わす}れた。|I forgot where I put the key.
習う|volitional|{来年|らいねん}はピアノを**{習|なら}おう**。|I'll take piano lessons next year.
習う|ta|{子供|こども}のころ、{書道|しょどう}を**{習|なら}った**。|I learned calligraphy as a child.
考える|masu|{明日|あした}までに**{考|かんが}えます**。|I'll think about it by tomorrow.
脱ぐ|ta|{玄関|げんかん}で{靴|くつ}を**{脱|ぬ}いだ**。|I took my shoes off at the entrance.
行く|volitional|{週末|しゅうまつ}、{海|うみ}に**{行|い}こう**。|Let's go to the sea at the weekend.
行く|ta|{去年|きょねん}、{京都|きょうと}に**{行|い}った**。|I went to Kyoto last year.
行く|te|{駅|えき}まで**{行|い}って**、{電車|でんしゃ}に{乗|の}った。|I went to the station and got on the train.
見る|masu|{毎晩|まいばん}ニュースを**{見|み}ます**。|I watch the news every evening.
見る|potential|この{映画|えいが}はネットで**{見|み}られる**。|You can watch this film online.
見る|volitional|{今夜|こんや}、{一緒|いっしょ}に{映画|えいが}を**{見|み}よう**。|Let's watch a film together tonight.
見る|nai|{最近|さいきん}テレビを**{見|み}ない**。|I don't watch TV these days.
見る|mashita|{昨日|きのう}、{花火|はなび}を**{見|み}ました**。|I watched fireworks yesterday.
見る|te|この{写真|しゃしん}を**{見|み}て**ください。|Please look at this photo.
言う|nai|{彼|かれ}は{本当|ほんとう}のことを**{言|い}わない**。|He doesn't tell the truth.
話す|ta|{先生|せんせい}と{将来|しょうらい}について**{話|はな}した**。|I talked with my teacher about the future.
話す|potential|{姉|あね}は{英語|えいご}と{中国語|ちゅうごくご}が**{話|はな}せる**。|My sister can speak English and Chinese.
話す|volitional|{後|あと}でゆっくり**{話|はな}そう**。|Let's have a proper talk later.
話す|nai|{彼|かれ}は{会議|かいぎ}であまり**{話|はな}さない**。|He doesn't say much in meetings.
話す|te|もう{少|すこ}しゆっくり**{話|はな}して**ください。|Please speak a little more slowly.
読む|potential|{日本語|にほんご}の{新聞|しんぶん}が**{読|よ}める**ようになった。|I can now read Japanese newspapers.
読む|nai|{最近|さいきん}、{本|ほん}を**{読|よ}まない**。|I don't read books these days.
読む|te|{毎晩|まいばん}{本|ほん}を**{読|よ}んで**から{寝|ね}る。|Every night I read before going to sleep.
調べる|ta|{辞書|じしょ}で{意味|いみ}を**{調|しら}べた**。|I looked up the meaning in a dictionary.
買う|potential|この{店|みせ}なら{安|やす}く**{買|か}える**。|You can buy it cheaply at this shop.
買う|volitional|{新|あたら}しい{靴|くつ}を**{買|か}おう**。|I'll buy new shoes.
買う|nai|{高|たか}いから**{買|か}わない**。|It's expensive, so I won't buy it.
買う|te|パンを**{買|か}って**{帰|かえ}る。|I'll buy some bread on the way home.
貸す|te|ペンを**{貸|か}して**ください。|Could you lend me a pen?
走る|ta|{遅|おく}れそうだったので、{駅|えき}まで**{走|はし}った**。|I was about to be late, so I ran to the station.
起きる|potential|{明日|あした}、6{時|じ}に**{起|お}きられる**？|Can you get up at six tomorrow?
起きる|nai|{休|やす}みの{日|ひ}は{昼|ひる}まで**{起|お}きない**。|On my days off I don't get up until noon.
起きる|te|{朝|あさ}**{起|お}きて**、まずコーヒーを{飲|の}む。|When I get up in the morning, I have a coffee first.
遅れる|ta|{電車|でんしゃ}が10{分|ぷん}**{遅|おく}れた**。|The train was ten minutes late.
遊ぶ|ta|{公園|こうえん}で{子供|こども}と**{遊|あそ}んだ**。|I played with the kids in the park.
遊ぶ|potential|この{公園|こうえん}なら{安全|あんぜん}に**{遊|あそ}べる**。|Kids can play safely in this park.
遊ぶ|volitional|{放課後|ほうかご}、{一緒|いっしょ}に**{遊|あそ}ぼう**。|Let's hang out after school.
遊ぶ|te|**{遊|あそ}んで**ばかりいないで、{勉強|べんきょう}しなさい。|Stop playing all the time and study.
運ぶ|potential|この{箱|はこ}、{一人|ひとり}で**{運|はこ}べる**？|Can you carry this box on your own?
運ぶ|ta|{重|おも}い{箱|はこ}を{二階|にかい}に**{運|はこ}んだ**。|I carried the heavy box upstairs.
違う|nai|{二人|ふたり}の{意見|いけん}はあまり**{違|ちが}わない**。|Their opinions aren't very different.
選ぶ|ta|{迷|まよ}ったけど、{赤|あか}いほうを**{選|えら}んだ**。|I couldn't decide, but I chose the red one.
選ぶ|masu|{私|わたし}ならこっちを**{選|えら}びます**。|If it were me, I'd choose this one.
間違える|nakatta|{今日|きょう}のテストは{一問|いちもん}も**{間違|まちが}えなかった**。|I didn't get a single question wrong in today's test.
頑張る|volitional|{試験|しけん}まであと{少|すこ}し。{一緒|いっしょ}に**{頑張|がんば}ろう**！|The exam's nearly here. Let's keep going together!
頼む|passive_ta|{部長|ぶちょう}に{資料|しりょう}のコピーを**{頼|たの}まれた**。|My manager asked me to copy the documents.
頼む|ta|{夕飯|ゆうはん}にピザを**{頼|たの}んだ**。|I ordered pizza for dinner.
食べる|potential|{辛|から}いものも**{食|た}べられる**よ。|I can eat spicy food too.
食べる|ba|{朝|あさ}ご{飯|はん}を**{食|た}べれば**、{元気|げんき}が{出|で}るよ。|If you eat breakfast, you'll have more energy.
食べる|volitional|お{昼|ひる}、{一緒|いっしょ}に**{食|た}べよう**。|Let's have lunch together.
食べる|nai|{私|わたし}は{肉|にく}を**{食|た}べない**。|I don't eat meat.
食べる|ta|{昨日|きのう}、すしを**{食|た}べた**。|I ate sushi yesterday.
食べる|masu|{毎朝|まいあさ}パンを**{食|た}べます**。|I eat bread every morning.
食べる|te|{冷|さ}めないうちに**{食|た}べて**ね。|Eat it before it gets cold.
飲む|volitional|{仕事|しごと}が{終|お}わったら、{一杯|いっぱい}**{飲|の}もう**。|Let's have a drink when work's over.
飲む|te|{薬|くすり}を**{飲|の}んで**{寝|ね}た。|I took my medicine and went to bed.
いい|a_adv|{先生|せんせい}の{説明|せつめい}は**よく**{分|わ}かった。|I understood the teacher's explanation well.
いい|a_noun|{今日|きょう}は**いい**{天気|てんき}ですね。|Lovely weather today, isn't it?
いい|a_ba|**よければ**、{一緒|いっしょ}に{来|き}ませんか。|If you like, why not come along?
いい|a_neg|{夜更|よふ}かしは{体|からだ}に**よくない**。|Staying up late isn't good for you.
いい|a_pastneg|{試験|しけん}の{結果|けっか}は**よくなかった**。|The exam results weren't good.
いい|a_past|{旅行|りょこう}の{間|あいだ}、ずっと{天気|てんき}が**よかった**。|The weather was good throughout the trip.
いい|a_desu|この{部屋|へや}は{景色|けしき}が**いいです**。|The view from this room is nice.
いい|a_te|{天気|てんき}が**よくて**、{気持|きも}ちがいい。|The weather's good and it feels great.
おいしい|a_past_p|ラーメン、とても**おいしかったです**。|The ramen was really good.
おいしい|a_sou|このケーキ、**おいしそう**！|This cake looks delicious!
かっこいい|a_neg|その{髪型|かみがた}、あまり**かっこよくない**よ。|That hairstyle isn't very cool.
かっこいい|a_past|{昨日|きのう}の{試合|しあい}の{彼|かれ}、**かっこよかった**ね。|He looked so cool in yesterday's match.
きれい|a_neg|{私|わたし}の{部屋|へや}は{全然|ぜんぜん}**きれいじゃない**。|My room isn't tidy at all.
きれい|a_pastneg|{昔|むかし}、この{川|かわ}は**きれいじゃなかった**。|This river didn't use to be clean.
きれい|a_te|この{町|まち}は**きれいで**、{静|しず}かです。|This town is clean and quiet.
つまらない|a_pastneg_p|その{映画|えいが}は{思|おも}ったほど**つまらなくなかったです**。|The film wasn't as boring as I'd expected.
丁寧|a_adv|{店員|てんいん}さんが**{丁寧|ていねい}に**{説明|せつめい}してくれた。|The shop assistant explained it carefully.
上手|a_adv|{娘|むすめ}は**{上手|じょうず}に**{絵|え}を{描|か}く。|My daughter draws well.
上手|a_naru_ta|{毎日|まいにち}{練習|れんしゅう}して、{料理|りょうり}が**{上手|じょうず}になった**。|I practised every day and got good at cooking.
便利|a_past|{前|まえ}の{家|いえ}は{駅|えき}に{近|ちか}くて**{便利|べんり}だった**。|My old house was close to the station and convenient.
便利|a_te|スマホは**{便利|べんり}で**、もう{手放|てばな}せない。|Smartphones are so handy that I can't do without mine.
便利|a_noun|**{便利|べんり}な**アプリを{見|み}つけた。|I found a handy app.
元気|a_neg|{今日|きょう}は{少|すこ}し**{元気|げんき}じゃない**。|I'm not feeling very lively today.
元気|a_te|{祖母|そぼ}は**{元気|げんき}で**、{毎日|まいにち}{散歩|さんぽ}している。|My grandmother is in good health and takes a walk every day.
冷たい|a_past_p|{川|かわ}の{水|みず}はとても**{冷|つめ}たかったです**。|The river water was very cold.
危ない|a_tara|**{危|あぶ}なかったら**、すぐにやめてください。|If it's dangerous, stop straight away.
大きい|a_te|この{部屋|へや}は**{大|おお}きくて**{明|あか}るい。|This room is big and bright.
大きい|a_sugiru|このシャツは{私|わたし}には**{大|おお}きすぎる**。|This shirt is too big for me.
大丈夫|a_te|この{傘|かさ}は{風|かぜ}が{強|つよ}くても**{大丈夫|だいじょうぶ}で**、{壊|こわ}れない。|This umbrella is fine even in strong wind and doesn't break.
失礼|a_neg|そんな{言|い}い{方|かた}は**{失礼|しつれい}じゃない**？|Isn't it rude to say it like that?
好き|a_past|{子供|こども}のころ、{電車|でんしゃ}が**{好|す}きだった**。|As a child I loved trains.
嫌い|a_past|{昔|むかし}は{野菜|やさい}が**{嫌|きら}いだった**。|I used to hate vegetables.
嫌い|a_neg_p|{魚|さかな}は**{嫌|きら}いじゃないです**。|I don't dislike fish.
安い|a_te|この{店|みせ}は**{安|やす}くて**おいしい。|This place is cheap and tasty.
安全|a_noun|**{安全|あんぜん}な**{場所|ばしょ}に{逃|に}げてください。|Please get to a safe place.
寒い|a_past|{昨日|きのう}はとても**{寒|さむ}かった**。|It was very cold yesterday.
寒い|a_te|**{寒|さむ}くて**、{手|て}が{冷|つめ}たい。|It's so cold my hands are freezing.
少ない|a_past|{雨|あめ}だったので、{今日|きょう}はお{客|きゃく}さんが**{少|すく}なかった**。|It rained, so there weren't many customers today.
広い|a_te|{新|あたら}しい{部屋|へや}は**{広|ひろ}くて**{気持|きも}ちがいい。|The new flat is spacious and pleasant.
強い|a_adv|ドアを**{強|つよ}く**{押|お}してください。|Push the door hard.
必要|a_pastneg|{結局|けっきょく}、{傘|かさ}は**{必要|ひつよう}じゃなかった**。|In the end, I didn't need the umbrella.
忙しい|a_neg_p|{今週|こんしゅう}はあまり**{忙|いそが}しくないです**。|I'm not very busy this week.
早い|a_adv|{明日|あした}は**{早|はや}く**{起|お}きます。|I'm getting up early tomorrow.
明るい|a_te|この{部屋|へや}は**{明|あか}るくて**{暖|あたた}かい。|This room is bright and warm.
暇|a_neg_p|すみません、{今日|きょう}は**{暇|ひま}じゃないです**。|Sorry, I'm not free today.
有名|a_pastneg|{十年前|じゅうねんまえ}、この{町|まち}は**{有名|ゆうめい}じゃなかった**。|Ten years ago this town wasn't famous.
有名|a_past_p|その{店|みせ}は{昔|むかし}から**{有名|ゆうめい}でした**。|That shop has long been famous.
有名|a_past|{祖父|そふ}は{村|むら}で**{有名|ゆうめい}だった**。|My grandfather was well known in the village.
楽しい|a_pastneg|{昨日|きのう}のパーティーはあまり**{楽|たの}しくなかった**。|Yesterday's party wasn't much fun.
楽しい|a_past_p|{京都|きょうと}の{旅行|りょこう}はとても**{楽|たの}しかったです**。|The trip to Kyoto was a lot of fun.
楽しい|a_past|{友達|ともだち}と{話|はな}せて**{楽|たの}しかった**。|It was fun talking with my friends.
欲しい|a_past|{子供|こども}のころ、ずっと{犬|いぬ}が**{欲|ほ}しかった**。|As a child I always wanted a dog.
残念|a_past_p|{試合|しあい}に{負|ま}けて、**{残念|ざんねん}でした**。|It was a shame we lost the match.
涼しい|a_naru|{九月|くがつ}になると、{朝|あさ}と{夜|よる}は**{涼|すず}しくなる**。|In September the mornings and evenings get cooler.
特別|a_adv|{今日|きょう}は**{特別|とくべつ}に**{安|やす}くしますよ。|Today I'll make it cheaper, just for you.
甘い|a_te|このりんごは**{甘|あま}くて**おいしい。|This apple is sweet and tasty.
痛い|a_neg|{薬|くすり}を{飲|の}んだら、もう{頭|あたま}は**{痛|いた}くない**。|I took some medicine and my head doesn't hurt any more.
短い|a_adv|{夏|なつ}なので、{髪|かみ}を**{短|みじか}く**{切|き}った。|It's summer, so I cut my hair short.
簡単|a_te|この{料理|りょうり}は**{簡単|かんたん}で**おいしい。|This dish is easy and tasty.
素敵|a_tara|{景色|けしき}が**{素敵|すてき}だったら**、{写真|しゃしん}を{撮|と}ろう。|If the view is lovely, let's take a photo.
自由|a_past|{大学|だいがく}{時代|じだい}は{時間|じかん}があって**{自由|じゆう}だった**。|At university I had time and was free.
若い|a_te|{新|あたら}しい{先生|せんせい}は**{若|わか}くて**{元気|げんき}だ。|The new teacher is young and full of energy.
複雑|a_neg_p|このゲームのルールは**{複雑|ふくざつ}じゃないです**。|The rules of this game aren't complicated.
親切|a_te|{店員|てんいん}さんが**{親切|しんせつ}で**、{嬉|うれ}しかった。|The staff were kind, and I was happy.
賑やか|a_noun|{駅前|えきまえ}は**{賑|にぎ}やかな**{通|とお}りです。|The street by the station is lively.
遠い|a_ba|**{遠|とお}ければ**、タクシーで{行|い}きましょう。|If it's far, let's take a taxi.
重い|a_pastneg|{荷物|にもつ}は{思|おも}ったほど**{重|おも}くなかった**。|The luggage wasn't as heavy as I'd thought.
長い|a_neg|{日本|にほん}の{夏休|なつやす}みはあまり**{長|なが}くない**。|Summer holidays in Japan aren't very long.
難しい|a_pastneg_p|{試験|しけん}は{思|おも}ったより**{難|むずか}しくなかったです**。|The exam wasn't as hard as I'd expected.
難しい|a_ba|**{難|むずか}しければ**、{先生|せんせい}に{聞|き}いてください。|If it's difficult, ask the teacher.
静か|a_adv|{図書館|としょかん}では**{静|しず}かに**{話|はな}してください。|Please speak quietly in the library.
静か|a_noun|**{静|しず}かな**{部屋|へや}で{勉強|べんきょう}したい。|I want to study in a quiet room.
静か|a_ba|**{静|しず}かなら**、どこでもいいです。|Anywhere is fine, as long as it's quiet.
静か|a_neg|この{辺|へん}は{夜|よる}も**{静|しず}かじゃない**。|This area isn't quiet even at night.
静か|a_pastneg|{昨日|きのう}の{電車|でんしゃ}は**{静|しず}かじゃなかった**。|The train yesterday wasn't quiet.
静か|a_past|{昨日|きのう}の{夜|よる}はとても**{静|しず}かだった**。|Last night was very quiet.
静か|a_desu|この{公園|こうえん}は{朝|あさ}がいちばん**{静|しず}かです**。|This park is quietest in the morning.
静か|a_te|この{町|まち}は**{静|しず}かで**{住|す}みやすい。|This town is quiet and easy to live in.
高い|a_adv|ボールを**{高|たか}く**{投|な}げた。|I threw the ball high.
高い|a_noun|{駅|えき}の{周|まわ}りに**{高|たか}い**ビルが{増|ふ}えた。|There are more tall buildings around the station.
高い|a_ba|**{高|たか}ければ**、{買|か}いません。|If it's expensive, I won't buy it.
高い|a_neg|この{店|みせ}は{思|おも}ったより**{高|たか}くない**。|This shop isn't as expensive as I thought.
高い|a_pastneg|その{時計|とけい}は**{高|たか}くなかった**。|That watch wasn't expensive.
高い|a_past|{昨日|きのう}のレストランは**{高|たか}かった**。|Yesterday's restaurant was expensive.
高い|a_desu|{東京|とうきょう}は{家賃|やちん}が**{高|たか}いです**。|Rent is high in Tokyo.
高い|a_te|このバッグは**{高|たか}くて**{買|か}えない。|This bag is too expensive for me to buy.
"""

WORD = """
書く|{毎日|まいにち}{日記|にっき}を**{書|か}いて**います。|I keep a diary every day.
食べる|{朝|あさ}ご{飯|はん}を**{食|た}べない**{人|ひと}が{増|ふ}えた。|More people skip breakfast.
分かる|すみません、よく**{分|わ}かりません**。|Sorry, I don't really understand.
する|{週末|しゅうまつ}はテニスを**します**。|I play tennis at weekends.
話す|{電話|でんわ}で{母|はは}と**{話|はな}した**。|I talked to my mother on the phone.
見る|{昨日|きのう}、{映画|えいが}を**{見|み}た**。|I saw a film yesterday.
作る|{日曜日|にちようび}にケーキを**{作|つく}った**。|I made a cake on Sunday.
来る|{田中|たなか}さんはまだ**{来|こ}ない**。|Tanaka still hasn't come.
待つ|{駅|えき}の{前|まえ}で**{待|ま}って**います。|I'm waiting in front of the station.
起きる|{毎朝|まいあさ}6{時|じ}に**{起|お}きます**。|I get up at six every morning.
乗る|{毎朝|まいあさ}バスに**{乗|の}って**{会社|かいしゃ}に{行|い}く。|I take the bus to work every morning.
勉強する|{毎晩|まいばん}{日本語|にほんご}を**{勉強|べんきょう}して**います。|I study Japanese every evening.
死ぬ|{飼|か}っていた{金魚|きんぎょ}が**{死|し}んで**しまった。|My goldfish died.
教える|{駅|えき}までの{道|みち}を**{教|おし}えて**ください。|Please tell me the way to the station.
取る|{塩|しお}を**{取|と}って**ください。|Please pass the salt.
遊ぶ|{子供|こども}たちが{公園|こうえん}で**{遊|あそ}んで**いる。|The children are playing in the park.
借りる|{友達|ともだち}に{傘|かさ}を**{借|か}りた**。|I borrowed an umbrella from a friend.
座る|どうぞ、ここに**{座|すわ}って**ください。|Please, have a seat here.
泳ぐ|{夏|なつ}は{毎日|まいにち}{海|うみ}で**{泳|およ}いだ**。|I swam in the sea every day in summer.
忘れる|{傘|かさ}を{電車|でんしゃ}に**{忘|わす}れた**。|I left my umbrella on the train.
買う|{駅前|えきまえ}の{店|みせ}でパンを**{買|か}った**。|I bought bread at the shop by the station.
閉める|{寒|さむ}いので、{窓|まど}を**{閉|し}めて**ください。|It's cold, so please close the window.
帰る|{今日|きょう}は{早|はや}く{家|いえ}に**{帰|かえ}らない**といけない。|I have to go home early today.
着る|{寒|さむ}いので、セーターを**{着|き}た**。|It was cold, so I put on a jumper.
入る|ノックしてから{部屋|へや}に**{入|はい}って**ください。|Please knock before you come into the room.
変える|{髪|かみ}の{色|いろ}を**{変|か}えた**。|I changed my hair colour.
走る|{毎朝|まいあさ}{公園|こうえん}を**{走|はし}って**います。|I run in the park every morning.
降りる|{次|つぎ}の{駅|えき}で**{降|お}ります**。|I'm getting off at the next station.
切る|はさみで{紙|かみ}を**{切|き}って**ください。|Please cut the paper with scissors.
浴びる|{朝|あさ}、シャワーを**{浴|あ}びて**から{出|で}かけた。|I had a shower in the morning before going out.
知る|その{人|ひと}の{名前|なまえ}は**{知|し}らない**。|I don't know that person's name.
信じる|{彼|かれ}の{話|はなし}は**{信|しん}じられない**。|I can't believe his story.
要る|{今日|きょう}は{傘|かさ}は**{要|い}らない**よ。|You won't need an umbrella today.
生きる|{祖母|そぼ}は100{歳|さい}まで**{生|い}きた**。|My grandmother lived to a hundred.
喋る|{授業中|じゅぎょうちゅう}に**{喋|しゃべ}らない**でください。|Please don't chat during class.
見せる|パスポートを**{見|み}せて**ください。|Please show me your passport.
滑る|{雪|ゆき}の{道|みち}で**{滑|すべ}って**{転|ころ}んだ。|I slipped on the snowy road and fell.
足りる|お{金|かね}が**{足|た}りない**。|I don't have enough money.
焦る|{時間|じかん}はあるから、**{焦|あせ}らない**で。|There's time, so don't rush.
覚える|{新|あたら}しい{単語|たんご}を{毎日|まいにち}**{覚|おぼ}えて**います。|I memorise new words every day.
減る|{最近|さいきん}、{体重|たいじゅう}が**{減|へ}った**。|I've lost weight recently.
握る|{子供|こども}が{母親|ははおや}の{手|て}を**{握|にぎ}った**。|The child took hold of its mother's hand.
蹴る|ボールを{強|つよ}く**{蹴|け}った**。|I kicked the ball hard.
限る|{参加者|さんかしゃ}は20{人|にん}に**{限|かぎ}ります**。|Participants are limited to twenty.
高い|この{時計|とけい}は**{高|たか}くない**。|This watch isn't expensive.
静か|この{辺|へん}は**{静|しず}かな**{町|まち}です。|This is a quiet town.
きれい|{部屋|へや}が**きれいじゃない**。|The room isn't tidy.
おいしい|この{店|みせ}のパンは**おいしくない**。|The bread at this shop isn't good.
便利|{駅|えき}に{近|ちか}くて**{便利|べんり}な**{家|いえ}です。|It's a convenient house close to the station.
嫌い|{私|わたし}は{雨|あめ}の{日|ひ}が**{嫌|きら}いじゃない**。|I don't mind rainy days.
新しい|**{新|あたら}しい**{靴|くつ}を{買|か}った。|I bought new shoes.
有名|ここは**{有名|ゆうめい}な**お{寺|てら}です。|This is a famous temple.
いい|{今日|きょう}は{天気|てんき}が**よくない**。|The weather isn't good today.
元気|{子供|こども}たちはみんな**{元気|げんき}な**{声|こえ}で{歌|うた}った。|All the children sang in lively voices.
楽しい|{昨日|きのう}のパーティーは**{楽|たの}しかった**。|Yesterday's party was fun.
丁寧|{先生|せんせい}は**{丁寧|ていねい}な**{言葉|ことば}で{話|はな}す。|The teacher speaks in polite language.
かっこいい|{彼|かれ}の{新|あたら}しい{車|くるま}、**かっこよかった**。|His new car looked cool.
簡単|この{問題|もんだい}は**{簡単|かんたん}じゃない**。|This problem isn't easy.
暗い|{冬|ふゆ}は5{時|じ}にもう**{暗|くら}くなる**。|In winter it's already dark by five.
好き|{私|わたし}は{猫|ねこ}が**{好|す}きです**。|I like cats.
優しい|{田中|たなか}さんはとても**{優|やさ}しい**{人|ひと}だ。|Tanaka is a very kind person.
大変|{引|ひ}っ{越|こ}しは**{大変|たいへん}だった**。|The move was hard work.
欲しい|{新|あたら}しいパソコンが**{欲|ほ}しい**。|I want a new computer.
疲れる|{今日|きょう}はたくさん{歩|ある}いて**{疲|つか}れた**。|I walked a lot today and I'm tired.
眠い|{昨日|きのう}あまり{寝|ね}なかったので、**{眠|ねむ}い**。|I didn't sleep much last night, so I'm sleepy.
上手|{姉|あね}は{料理|りょうり}が**{上手|じょうず}です**。|My older sister is good at cooking.
病気|{母|はは}は**{病気|びょうき}の**{祖母|そぼ}の{世話|せわ}をしている。|My mother looks after my grandmother, who is ill.
寒い|{今日|きょう}は**{寒|さむ}くない**ね。|It isn't cold today, is it?
違う|すみません、{番号|ばんごう}が**{違|ちが}います**。|Sorry, you have the wrong number.
困る|{財布|さいふ}をなくして**{困|こま}って**いる。|I've lost my wallet and I'm in trouble.
怖い|{子供|こども}のころ、{犬|いぬ}が**{怖|こわ}かった**。|As a child I was scared of dogs.
休み|{明日|あした}は**{休|やす}みの**{日|ひ}だから、ゆっくり{寝|ね}られる。|Tomorrow's a day off, so I can sleep in.
暇|**{暇|ひま}な**{時|とき}は{何|なに}をしていますか。|What do you do in your free time?
混む|{朝|あさ}の{電車|でんしゃ}はいつも**{混|こ}んで**いる。|The morning trains are always crowded.
痛い|{歯|は}が**{痛|いた}くて**、{何|なに}も{食|た}べられない。|My tooth hurts so much I can't eat anything.
学生|**{学生|がくせい}の**{時|とき}、よく{旅行|りょこう}した。|I travelled a lot when I was a student.
大丈夫|{怪我|けが}は**{大丈夫|だいじょうぶ}じゃない**かもしれない。|The injury might not be all right.
"""


def _parse(text, keys):
    """'key|form|sentence|English' (the sentence's furigana also uses |, so split keys from the left, English from the right)."""
    out = {}
    for line in text.strip().splitlines():
        *key, rest = line.split("|", keys)
        sentence, en = rest.rsplit("|", 1)
        out[tuple(key) if keys > 1 else key[0]] = (sentence, en)
    return out


FORM_EX = _parse(FORM, 2)
WORD_EX = _parse(WORD, 1)
