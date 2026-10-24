"""JLPT N5–N1 verbs for the verb lookup (static/verbs). One per line: dictionary form, reading, class, JLPT level, short English gloss.

Class: ru (ichidan), u (godan), iku (行く), aru (ある), suru (する and noun + する), kuru (来る),
honor (いらっしゃる, おっしゃる, くださる, なさる: ます-stem and command end in い), tou (問う: 問うて / 問うた).
Noun + する with a one-kanji noun (愛する, 接する …) has no できる potential and no keigo form here.
The word list is based on the JLPT lists of tanos.co.uk via github.com/jamsinclair/open-anki-jlpt-decks (MIT);
classes were checked and glosses shortened by hand, and common noun + する verbs were added.
〜ずる verbs (信ずる …) are left out in favour of their 〜じる forms.
"""

VERBS = """
愛する あいする suru N3 love
会う あう u N5 meet
合う あう u N4 fit
遭う あう u N3 run into (trouble)
仰ぐ あおぐ u N1 look up to
扇ぐ あおぐ u N2 fan
明かす あかす u N1 reveal, spend (the night)
赤らむ あからむ u N1 turn red
上がる あがる u N4 go up
諦める あきらめる ru N3 give up
飽きる あきる ru N3 get tired of
呆れる あきれる ru N2 be amazed, be appalled
空く あく u N4 become empty
開く あく u N5 open
明ける あける ru N3 dawn, end (a year)
開ける あける ru N5 open
あげる あげる ru N4 give
上げる あげる ru N5 raise, give
挙げる あげる ru N3 raise, give (an example)
揚げる あげる ru N3 deep-fry
憧れる あこがれる ru N2 long for
欺く あざむく u N1 deceive
嘲笑う あざわらう u N1 sneer at
味わう あじわう u N2 taste, enjoy
預かる あずかる u N3 look after (for someone)
預ける あずける ru N3 leave (in someone's care)
焦る あせる u N1 be in a hurry
遊ぶ あそぶ u N5 play, hang out
値する あたいする suru N1 be worth
与える あたえる ru N3 give
暖まる あたたまる u N3 warm up
温まる あたたまる u N3 warm oneself
暖める あたためる ru N3 warm
温める あたためる ru N3 warm
当たる あたる u N3 hit, be correct
扱う あつかう u N3 treat
集まる あつまる u N4 gather
集める あつめる ru N4 collect
あつらえる あつらえる ru N1 order (custom-made)
当てはまる あてはまる u N2 apply to
当てはめる あてはめる ru N2 apply
宛てる あてる ru N3 address (a letter)
当てる あてる ru N3 hit, guess
暴れる あばれる ru N2 act violently
浴びる あびる ru N5 take (a shower)
あふれる あふれる ru N2 overflow
あぶる あぶる u N2 grill
甘える あまえる ru N1 act spoiled
甘やかす あまやかす u N2 spoil (a child)
余る あまる u N2 be left over
編む あむ u N2 knit
操る あやつる u N1 operate, manipulate
危ぶむ あやぶむ u N1 doubt
誤る あやまる u N1 make a mistake
謝る あやまる u N4 apologize
歩む あゆむ u N1 walk, follow (a path)
洗う あらう u N5 wash
荒らす あらす u N1 damage, raid
争う あらそう u N3 dispute
改まる あらたまる u N1 be renewed
改める あらためる ru N2 change, revise
現す あらわす u N3 show, reveal
著す あらわす u N3 write (a book)
表す あらわす u N3 express
現れる あらわれる ru N3 appear
ある ある aru N5 be, exist (things)
歩く あるく u N5 walk
荒れる あれる ru N2 be stormy, be rough
合わす あわす u N1 put together
合わせる あわせる ru N3 put together, match
慌てる あわてる ru N3 panic
安心する あんしんする suru N4 feel relieved
案じる あんじる ru N1 worry about
案内する あんないする suru N4 show around
言い出す いいだす u N2 bring up
言い付ける いいつける ru N2 order, tell on
言う いう u N5 say
生かす いかす u N1 make use of
意気込む いきごむ u N1 be eager
生きる いきる ru N4 live
行く いく iku N5 go
生ける いける ru N1 arrange (flowers)
いじめる いじめる ru N4 bully
いじる いじる u N1 fiddle with
急ぐ いそぐ u N4 hurry
致す いたす u N4 do (humble)
いただく いただく u N4 receive (humble)
傷める いためる ru N3 damage
炒める いためる ru N3 stir-fry
至る いたる u N3 reach, lead to
いたわる いたわる u N1 take care of
抱く いだく u N3 hold, embrace
営む いとなむ u N1 run (a business)
移動する いどうする suru N3 move
挑む いどむ u N1 challenge
祈る いのる u N4 pray
威張る いばる u N2 act big
嫌がる いやがる u N2 dislike
いらっしゃる いらっしゃる honor N4 come, go, be (honorific)
炒る いる u N2 roast
煎る いる u N2 roast
要る いる u N5 need
入れる いれる ru N5 put in
祝う いわう u N3 congratulate
植える うえる ru N4 plant
飢える うえる ru N2 starve
うかがう うかがう u N4 visit, ask (humble)
浮かぶ うかぶ u N2 float, come to mind
浮かべる うかべる ru N2 float, show (a smile)
受かる うかる u N1 pass (an exam)
浮く うく u N2 float
受け入れる うけいれる ru N1 accept
受け継ぐ うけつぐ u N1 inherit
受け付ける うけつける ru N1 accept (applications)
受け止める うけとめる ru N1 catch, accept
受け取る うけとる u N3 receive
受け持つ うけもつ u N2 take charge of
受ける うける ru N4 take (an exam), receive
動かす うごかす u N3 move
動く うごく u N4 move
失う うしなう u N3 lose
薄める うすめる ru N2 dilute
歌う うたう u N5 sing
疑う うたがう u N3 doubt
打ち明ける うちあける ru N1 confide
打ち切る うちきる u N1 cut short
打ち消す うちけす u N2 deny
打ち込む うちこむ u N1 devote oneself to, hammer in
訴える うったえる ru N3 sue, complain
打つ うつ u N4 hit
撃つ うつ u N3 shoot
討つ うつ u N3 attack
写す うつす u N4 copy, take (a photo)
映す うつす u N3 reflect, project
うつむく うつむく u N1 look down
写る うつる u N3 come out (in a photo)
映る うつる u N3 be reflected
移る うつる u N4 move
促す うながす u N1 urge
うなずく うなずく u N2 nod
うなる うなる u N3 groan
奪う うばう u N3 rob
埋まる うまる u N3 be buried, be filled
生まれる うまれる ru N5 be born
産む うむ u N3 give birth
埋め込む うめこむ u N1 embed
埋める うめる ru N3 bury
敬う うやまう u N2 respect
裏返す うらがえす u N2 turn over
裏切る うらぎる u N3 betray
占う うらなう u N2 tell fortunes
恨む うらむ u N2 bear a grudge
羨む うらやむ u N2 envy
売り切れる うりきれる ru N2 sell out
売り出す うりだす u N1 put on sale
売る うる u N5 sell
潤う うるおう u N1 be moist, profit
売れる うれる ru N3 be sold
上回る うわまわる u N1 exceed
植わる うわる u N1 be planted
運転する うんてんする suru N5 drive
運動する うんどうする suru N4 exercise
影響する えいきょうする suru N3 influence
描く えがく u N3 draw
選ぶ えらぶ u N4 choose
得る える ru N3 get, obtain
演じる えんじる ru N1 perform
遠慮する えんりょする suru N4 hold back
追いかける おいかける ru N2 chase
追い越す おいこす u N2 overtake
追い込む おいこむ u N1 drive into
追い出す おいだす u N1 drive out
追い付く おいつく u N3 overtake
老いる おいる ru N1 grow old
負う おう u N3 bear, owe
追う おう u N3 chase
応じる おうじる ru N3 respond to
終える おえる ru N3 finish
覆う おおう u N3 cover
侵す おかす u N1 invade
犯す おかす u N1 commit
拝む おがむ u N2 pray to
起きる おきる ru N5 get up
補う おぎなう u N2 make up for
置く おく u N5 put
遅らす おくらす u N1 delay
贈る おくる u N3 present
送る おくる u N4 send
遅れる おくれる ru N4 become late
起こす おこす u N4 wake (someone) up
怠る おこたる u N2 neglect
行う おこなう u N4 carry out
怒る おこる u N4 get angry
起こる おこる u N3 occur
押さえる おさえる ru N3 hold down
収まる おさまる u N1 fit in, settle
治まる おさまる u N1 calm down
納まる おさまる u N1 be paid, be settled
収める おさめる ru N3 store, put away
治める おさめる ru N3 govern
納める おさめる ru N3 pay, deliver
教える おしえる ru N5 teach, tell
押し切る おしきる u N1 push through
押し込む おしこむ u N1 push into
惜しむ おしむ u N1 value, regret
押し寄せる おしよせる ru N1 surge toward
押す おす u N5 push
襲う おそう u N1 attack
恐れ入る おそれいる u N1 be grateful, be sorry
恐れる おそれる ru N3 fear
教わる おそわる u N3 be taught
おだてる おだてる ru N1 flatter
落ち込む おちこむ u N1 get depressed
落ち着く おちつく u N2 calm down
落ちる おちる ru N4 fall, fail
おっしゃる おっしゃる honor N4 say (honorific)
落とす おとす u N4 drop
訪れる おとずれる ru N1 visit
劣る おとる u N3 fall behind
衰える おとろえる ru N1 decline
脅かす おどかす u N2 scare
脅す おどす u N1 threaten
踊る おどる u N4 dance
驚かす おどろかす u N2 surprise
驚く おどろく u N4 be surprised
怯える おびえる ru N1 be frightened
脅かす おびやかす u N1 threaten
帯びる おびる ru N1 take on
覚える おぼえる ru N5 remember, learn
溺れる おぼれる ru N3 drown
思い込む おもいこむ u N2 assume
思い出す おもいだす u N4 recall
思い付く おもいつく u N3 think of
思う おもう u N4 think
赴く おもむく u N1 proceed to
重んじる おもんじる ru N1 value
泳ぐ およぐ u N5 swim
及ぶ およぶ u N1 reach, extend
及ぼす およぼす u N3 exert
折り返す おりかえす u N1 turn back, call back
下りる おりる ru N4 go down
降りる おりる ru N5 get off
おる おる u N4 be (humble)
折る おる u N4 break, fold
織る おる u N3 weave
折れる おれる ru N4 break, snap
下す おろす u N3 hand down
卸す おろす u N3 sell wholesale
降ろす おろす u N3 take down, unload
終わる おわる u N5 end, finish
解決する かいけつする suru N3 solve
買い物する かいものする suru N5 go shopping
買う かう u N5 buy
飼う かう u N3 keep
帰す かえす u N3 send back
返す かえす u N5 give back
省みる かえりみる ru N1 reflect on
顧みる かえりみる ru N1 look back on
代える かえる ru N3 replace
反る かえる u N3 warp, bend
変える かえる ru N4 change (something)
帰る かえる u N5 go home
換える かえる ru N3 exchange
替える かえる ru N3 change (for another)
抱える かかえる ru N3 hold in one's arms
掲げる かかげる ru N1 hoist, raise
罹る かかる u N3 catch (an illness)
関わる かかわる u N2 be involved in
輝く かがやく u N3 shine
書き取る かきとる u N1 write down
掻き回す かきまわす u N1 stir
限る かぎる u N3 restrict
掻く かく u N3 scratch
描く かく u N3 draw
書く かく u N5 write
欠く かく u N3 lack
隠す かくす u N3 hide
確認する かくにんする suru N3 confirm
隠れる かくれる ru N3 hide
嗅ぐ かぐ u N3 sniff
かける かける ru N5 make (a phone call), sit down
掛ける かける ru N5 hang, put on (glasses)
欠ける かける ru N3 be chipped, be missing
賭ける かける ru N3 bet
駆ける かける ru N3 run
囲む かこむ u N3 surround
重なる かさなる u N3 be piled up
重ねる かさねる ru N3 pile up
かさばる かさばる u N1 be bulky
かさむ かさむ u N1 mount up
飾る かざる u N4 decorate
かじる かじる u N2 gnaw
貸す かす u N5 lend
霞む かすむ u N1 be hazy
稼ぐ かせぐ u N3 earn income
数える かぞえる ru N3 count
片付く かたづく u N3 be tidied up
片付ける かたづける ru N4 tidy up
固まる かたまる u N2 harden
傾く かたむく u N2 lean
傾ける かたむける ru N1 tilt
固める かためる ru N1 harden
片寄る かたよる u N2 lean to one side
語る かたる u N3 tell, talk about
勝つ かつ u N4 win
担ぐ かつぐ u N2 carry on the shoulder
叶う かなう u N1 come true
叶える かなえる ru N1 grant (a wish)
悲しむ かなしむ u N3 be sad
兼ねる かねる ru N2 double as
庇う かばう u N1 stand up for
被せる かぶせる ru N2 cover
かぶる かぶる u N5 put on (a hat)
被る かぶる u N3 put on (a hat)
かぶれる かぶれる ru N1 get a rash, be influenced
かまう かまう u N4 mind, care
構える かまえる ru N1 set up, take a stance
噛み切る かみきる u N1 bite off
噛む かむ u N4 bite
通う かよう u N4 commute, attend
からかう からかう u N2 tease
絡む からむ u N1 get tangled
借りる かりる ru N5 borrow
刈る かる u N3 cut (grass, hair)
枯れる かれる ru N2 wither
可愛がる かわいがる u N2 dote on
乾かす かわかす u N3 dry
乾く かわく u N4 get dry
渇く かわく u N3 be thirsty
交わす かわす u N1 exchange
代わる かわる u N3 take the place of
変わる かわる u N4 change
考える かんがえる ru N4 think
関係する かんけいする suru N3 be related
感謝する かんしゃする suru N3 thank
感心する かんしんする suru N3 be impressed
感じる かんじる ru N3 feel
関する かんする suru N3 be related to
感動する かんどうする suru N4 be moved
害する がいする suru N1 harm
我慢する がまんする suru N3 put up with
頑張る がんばる u N4 try one's best
消える きえる ru N5 go out, disappear
着飾る きかざる u N1 dress up
着替える きがえる ru N2 change clothes
効く きく u N3 work, be effective
聞く きく u N5 listen, ask
聞こえる きこえる ru N4 be audible
刻む きざむ u N2 chop, carve
きしむ きしむ u N1 creak
築く きずく u N3 build
傷付く きずつく u N1 get hurt
傷付ける きずつける ru N1 hurt
着せる きせる ru N2 dress (someone)
期待する きたいする suru N3 expect
鍛える きたえる ru N1 train
気付く きづく u N3 notice
気に入る きにいる u N3 like
決まる きまる u N4 be decided
決める きめる ru N4 decide
休憩する きゅうけいする suru N3 take a break
興じる きょうじる ru N1 enjoy oneself
競争する きょうそうする suru N4 compete
協力する きょうりょくする suru N3 cooperate
嫌う きらう u N3 hate
切る きる u N5 cut
斬る きる u N2 slash
着る きる ru N5 put on, wear
切れる きれる ru N3 run out, break
記録する きろくする suru N3 record
気を付ける きをつける ru N2 be careful
禁じる きんじる ru N1 forbid
緊張する きんちょうする suru N3 be nervous
食い違う くいちがう u N1 clash, differ
区切る くぎる u N2 divide, punctuate
くぐる くぐる u N1 pass under
腐る くさる u N3 rot
崩す くずす u N2 break down
崩れる くずれる ru N2 collapse
くたびれる くたびれる ru N2 get tired
砕く くだく u N2 crush
砕ける くだける ru N2 break, crumble
くださる くださる honor N4 give (to me, honorific)
下る くだる u N3 go down
口吟む くちずさむ u N1 hum
朽ちる くちる ru N1 rot
くっつく くっつく u N2 stick to
くっつける くっつける ru N2 attach
覆す くつがえす u N1 overturn
配る くばる u N2 hand out
組み合わせる くみあわせる ru N1 combine
組み込む くみこむ u N1 incorporate
組み立てる くみたてる ru N2 assemble
汲む くむ u N3 draw (water)
組む くむ u N3 put together
酌む くむ u N3 pour (sake)
曇る くもる u N5 cloud over
悔やむ くやむ u N2 regret
暮らす くらす u N3 live
比べる くらべる ru N4 compare
繰り返す くりかえす u N3 repeat
来る くる kuru N5 come
狂う くるう u N3 go mad, go wrong
苦しむ くるしむ u N3 suffer
くるむ くるむ u N2 wrap up
くれる くれる ru N4 give (to me)
暮れる くれる ru N4 get dark
加える くわえる ru N3 add
咥える くわえる ru N3 hold in the mouth
加わる くわわる u N3 join in
計画する けいかくする suru N4 plan
経験する けいけんする suru N4 experience
怪我する けがする suru N4 get hurt
消す けす u N5 turn off, erase
削る けずる u N2 shave, cut
結婚する けっこんする suru N5 marry
欠席する けっせきする suru N4 be absent
決定する けっていする suru N3 decide
蹴飛ばす けとばす u N1 kick away
けなす けなす u N1 speak ill of
煙る けむる u N1 smoke, be hazy
蹴る ける u N3 kick
研究する けんきゅうする suru N4 research
見物する けんぶつする suru N4 go sightseeing
減少する げんしょうする suru N3 decrease
恋する こいする suru N1 fall in love
超える こえる ru N3 exceed
越える こえる ru N3 cross over
凍る こおる u N3 freeze
焦がす こがす u N2 scorch
焦げる こげる ru N2 burn, be scorched
心得る こころえる ru N2 know, understand
心掛ける こころがける ru N1 keep in mind
志す こころざす u N1 aim for
試みる こころみる ru N1 try
凍える こごえる ru N2 freeze
腰掛ける こしかける ru N2 sit down
故障する こしょうする suru N4 break down
こしらえる こしらえる ru N2 make
こじれる こじれる ru N1 get complicated
超す こす u N3 exceed
越す こす u N3 go over, move
答える こたえる ru N5 answer
こだわる こだわる u N1 be particular about
言付ける ことづける ru N2 leave a message
異なる ことなる u N3 differ
断る ことわる u N3 refuse
好む このむ u N3 like
こぼす こぼす u N3 spill
こぼれる こぼれる ru N3 overflow
困る こまる u N5 be in trouble
込む こむ u N4 be crowded
込める こめる ru N1 put (feelings) into
籠もる こもる u N1 shut oneself in
堪える こらえる ru N2 bear, endure
凝らす こらす u N1 concentrate
懲りる こりる ru N1 learn one's lesson
凝る こる u N1 be absorbed in, get stiff
転がす ころがす u N2 roll
転がる ころがる u N2 roll
殺す ころす u N3 kill
転ぶ ころぶ u N3 fall down
壊す こわす u N4 break (something)
壊れる こわれる ru N4 break, be broken
合格する ごうかくする suru N4 pass (an exam)
ごまかす ごまかす u N1 cheat, gloss over
遮る さえぎる u N1 interrupt
さえずる さえずる u N1 chirp
冴える さえる ru N1 be clear, be sharp
栄える さかえる ru N1 flourish
遡る さかのぼる u N2 go back (in time)
逆らう さからう u N3 go against
探す さがす u N4 search
下がる さがる u N4 go down, hang
咲く さく u N5 bloom
裂く さく u N3 tear
探る さぐる u N2 probe
叫ぶ さけぶ u N3 shout
裂ける さける ru N3 split
避ける さける ru N3 avoid
下げる さげる ru N4 lower
捧げる ささげる ru N1 dedicate
囁く ささやく u N2 whisper
刺さる ささる u N3 get stuck (in)
差し上げる さしあげる ru N4 give (humble)
差し掛かる さしかかる u N1 approach
差し出す さしだす u N1 hold out
差し支える さしつかえる ru N1 be a problem
刺す さす u N3 stab, sting
射す さす u N3 shine (light)
差す さす u N5 put up (an umbrella)
指す さす u N3 point at
挿す さす u N3 insert
注す さす u N3 pour in, apply
授ける さずける ru N1 grant, teach
誘う さそう u N3 invite
定まる さだまる u N1 be decided
定める さだめる ru N1 decide, set
察する さっする suru N1 guess
さっぱりする さっぱりする suru N1 feel refreshed
悟る さとる u N1 realize
裁く さばく u N3 judge
錆びる さびる ru N2 rust
冷ます さます u N3 cool
覚ます さます u N3 awaken
妨げる さまたげる ru N2 prevent
冷める さめる ru N3 cool down
覚める さめる ru N3 wake up
去る さる u N3 leave
騒ぐ さわぐ u N4 make noise
触る さわる u N4 touch
障る さわる u N1 affect, harm
参加する さんかする suru N4 take part
賛成する さんせいする suru N3 agree
散歩する さんぽする suru N5 take a walk
残業する ざんぎょうする suru N4 work overtime
仕上がる しあがる u N2 be finished
仕上げる しあげる ru N1 finish up
強いる しいる ru N1 force
仕入れる しいれる ru N1 stock up
仕掛ける しかける ru N1 set (a trap), start
叱る しかる u N4 scold
仕切る しきる u N1 run, divide
敷く しく u N2 lay out
しくじる しくじる u N1 fail, blow it
湿気る しける u N1 get damp
茂る しげる u N2 grow thick
静まる しずまる u N2 quiet down
沈む しずむ u N3 sink
沈める しずめる ru N1 sink
慕う したう u N1 long for
従う したがう u N3 follow, obey
親しむ したしむ u N1 get familiar with
仕立てる したてる ru N1 tailor
失敗する しっぱいする suru N4 fail
躾ける しつける ru N1 discipline
質問する しつもんする suru N5 ask a question
萎びる しなびる ru N1 wilt
死ぬ しぬ u N5 die
凌ぐ しのぐ u N1 surpass, endure
支払う しはらう u N3 pay
縛る しばる u N2 tie
しびれる しびれる ru N2 go numb
しぼむ しぼむ u N2 wither
萎む しぼむ u N2 wither
絞る しぼる u N2 squeeze
閉まる しまる u N5 close
染みる しみる ru N1 soak in, sting
締め切る しめきる u N2 close (off)
示す しめす u N3 show
占める しめる ru N3 take up, occupy
湿る しめる u N3 get damp
締める しめる ru N5 tie, fasten
閉める しめる ru N5 close
しゃがむ しゃがむ u N2 squat
しゃぶる しゃぶる u N2 suck
しゃべる しゃべる u N3 chat
洒落る しゃれる ru N1 be stylish
就職する しゅうしょくする suru N4 find a job
修理する しゅうりする suru N3 repair
出席する しゅっせきする suru N4 attend
出発する しゅっぱつする suru N4 depart
紹介する しょうかいする suru N4 introduce
生じる しょうじる ru N3 occur
称する しょうする suru N1 call oneself
招待する しょうたいする suru N4 invite
知らせる しらせる ru N4 inform
調べる しらべる ru N4 check
知る しる u N5 get to know
記す しるす u N1 write down
信じる しんじる ru N3 believe
心配する しんぱいする suru N4 worry
信用する しんようする suru N3 trust
準じる じゅんじる ru N1 be based on
準備する じゅんびする suru N4 prepare
吸う すう u N5 smoke, breathe in
据え付ける すえつける ru N1 install
据える すえる ru N1 place, set
透き通る すきとおる u N2 be transparent
過ぎる すぎる ru N4 pass, be too much
空く すく u N4 become empty
救う すくう u N3 rescue from
優れる すぐれる ru N3 excel
過ごす すごす u N3 spend (time)
濯ぐ すすぐ u N1 rinse
進む すすむ u N4 advance
勧める すすめる ru N3 recommend
進める すすめる ru N3 advance
涼む すずむ u N2 cool off
滑る すべる u N4 slide
済ます すます u N1 finish
澄ます すます u N1 put on airs, listen carefully
済ませる すませる ru N3 finish, get done
住む すむ u N5 live (in)
済む すむ u N4 be finished, be settled
澄む すむ u N3 become clear
する する suru N5 do
刷る する u N3 print
擦る する u N3 rub
すれ違う すれちがう u N3 pass each other
擦れる すれる ru N1 rub
座る すわる u N5 sit down
ずらす ずらす u N2 shift
生活する せいかつする suru N4 live, make a living
成功する せいこうする suru N3 succeed
生産する せいさんする suru N4 produce
制する せいする suru N1 control
整理する せいりする suru N3 sort out
背負う せおう u N2 carry on one's back
急かす せかす u N1 rush (someone)
接する せっする suru N2 come into contact with
説明する せつめいする suru N4 explain
迫る せまる u N2 draw near
攻める せめる ru N3 attack
責める せめる ru N3 condemn
世話する せわする suru N4 look after
洗濯する せんたくする suru N5 do the laundry
選択する せんたくする suru N3 choose
沿う そう u N3 follow (along)
添う そう u N3 accompany
掃除する そうじする suru N5 clean
想像する そうぞうする suru N3 imagine
相談する そうだんする suru N4 consult
添える そえる ru N1 add, attach
即する そくする suru N1 conform to
損う そこなう u N1 damage
注ぐ そそぐ u N3 pour
育つ そだつ u N3 be brought up
育てる そだてる ru N4 raise
卒業する そつぎょうする suru N4 graduate
備え付ける そなえつける ru N1 equip
備える そなえる ru N3 prepare for
備わる そなわる u N1 be equipped with
聳える そびえる ru N1 tower
染まる そまる u N1 be dyed
背く そむく u N1 disobey
染める そめる ru N1 dye
そらす そらす u N1 avert
剃る そる u N2 shave
逸れる それる ru N2 stray
揃う そろう u N3 be complete, be gathered
揃える そろえる ru N3 arrange, gather
増加する ぞうかする suru N3 increase
属する ぞくする suru N2 belong to
退院する たいいんする suru N4 leave hospital
対する たいする suru N3 be directed at, face
堪える たえる ru N1 bear, endure
絶える たえる ru N1 die out
耐える たえる ru N1 endure
倒す たおす u N3 knock down
倒れる たおれる ru N4 fall over
高まる たかまる u N3 rise
高める たかめる ru N3 raise
耕す たがやす u N2 till
炊く たく u N3 cook (rice)
焚く たく u N3 burn (fuel)
蓄える たくわえる ru N2 store, save
確かめる たしかめる ru N3 make sure
足す たす u N4 add
助かる たすかる u N3 be saved
助ける たすける ru N3 help
携わる たずさわる u N1 be involved in
尋ねる たずねる ru N4 ask
訪ねる たずねる ru N4 visit
戦う たたかう u N3 fight
叩く たたく u N3 strike
畳む たたむ u N3 fold
漂う ただよう u N1 drift
立ち上がる たちあがる u N3 stand up
立ち去る たちさる u N1 leave
立ち止まる たちどまる u N2 stop (walking)
立ち寄る たちよる u N1 drop in
達する たっする suru N3 reach
建つ たつ u N3 be built
断つ たつ u N3 cut off
立つ たつ u N5 stand
立て替える たてかえる ru N1 pay for (someone)
建てる たてる ru N4 build
立てる たてる ru N4 stand (something) up
例える たとえる ru N2 compare
辿り着く たどりつく u N1 finally reach
辿る たどる u N1 follow (a path)
楽しむ たのしむ u N4 enjoy
頼む たのむ u N5 ask (a favour), order
束ねる たばねる ru N1 bundle
食べる たべる ru N5 eat
溜まる たまる u N3 collect
賜る たまわる u N1 receive (humble)
試す ためす u N3 attempt
ためらう ためらう u N2 hesitate
溜める ためる ru N3 save up
保つ たもつ u N1 keep
頼る たよる u N3 rely on
足りる たりる ru N4 be sufficient
足る たる u N2 be enough
弛む たるむ u N1 slacken
垂れる たれる ru N1 hang down, drip
担当する たんとうする suru N3 be in charge of
題する だいする suru N1 be titled
抱く だく u N3 hold, embrace
出す だす u N5 take out, send
脱する だっする suru N1 escape from
騙す だます u N3 trick
黙る だまる u N3 be silent
誓う ちかう u N2 swear
近付ける ちかづける ru N2 bring closer
近寄る ちかよる u N2 come near
違う ちがう u N5 be different, be wrong
違える ちがえる ru N1 mistake
ちぎる ちぎる u N2 tear off
遅刻する ちこくする suru N4 be late
縮まる ちぢまる u N1 shrink
縮む ちぢむ u N2 shrink
縮める ちぢめる ru N2 shorten
縮れる ちぢれる ru N2 be curly
注意する ちゅういする suru N4 pay attention, warn
注文する ちゅうもんする suru N3 order
調査する ちょうさする suru N3 investigate
散らかす ちらかす u N2 make a mess
散らかる ちらかる u N2 be messy
散らす ちらす u N3 scatter
散る ちる u N3 fall
費やす ついやす u N1 spend
通じる つうじる ru N3 get through, be understood
使う つかう u N5 use
仕える つかえる ru N1 serve
司る つかさどる u N1 be in charge of
捕まえる つかまえる ru N4 catch
捕まる つかまる u N3 be arrested
掴む つかむ u N3 seize
疲れる つかれる ru N5 get tired
付き合う つきあう u N3 go out with, keep company
突き当たる つきあたる u N2 run into
尽きる つきる ru N1 run out
付く つく u N3 stick to
就く つく u N3 take (a job)
点く つく u N4 come on (a light)
着く つく u N5 arrive
突く つく u N3 poke
尽くす つくす u N1 devote, exhaust
作る つくる u N5 make
繕う つくろう u N1 mend
接ぐ つぐ u N3 join
次ぐ つぐ u N3 come after
注ぐ つぐ u N3 pour
継ぐ つぐ u N3 succeed, inherit
付け加える つけくわえる ru N1 add
つける つける ru N5 turn on (a light)
付ける つける ru N3 attach
漬ける つける ru N4 pickle, soak
着ける つける ru N3 put on (accessories)
告げる つげる ru N1 tell, announce
伝える つたえる ru N4 convey
伝わる つたわる u N3 be handed down
突っ込む つっこむ u N2 thrust into
突っ突く つっつく u N1 poke
突っ張る つっぱる u N1 stiffen, insist
謹む つつしむ u N1 refrain
包む つつむ u N4 wrap
続く つづく u N4 continue
続ける つづける ru N4 continue
努める つとめる ru N2 try hard
務める つとめる ru N2 serve as
勤める つとめる ru N5 work (for)
繋がる つながる u N3 be connected to
繋ぐ つなぐ u N3 tie
繋げる つなげる ru N3 connect
つねる つねる u N1 pinch
募る つのる u N1 recruit, grow stronger
潰す つぶす u N2 crush
呟く つぶやく u N1 mutter
潰れる つぶれる ru N2 be crushed, go bankrupt
躓く つまずく u N2 stumble
詰まる つまる u N2 be blocked
摘む つむ u N3 pick (flowers)
積む つむ u N3 pile up, load
詰める つめる ru N3 pack, stuff
積もる つもる u N3 pile up
強まる つよまる u N3 get strong
強める つよめる ru N3 strengthen
連なる つらなる u N1 stretch in a row
貫く つらぬく u N1 pierce, persist
連ねる つらねる ru N1 put in a row
釣り合う つりあう u N2 balance
吊る つる u N2 hang
釣る つる u N4 fish
吊るす つるす u N2 hang
連れる つれる ru N4 take (a person) along
提出する ていしゅつする suru N3 hand in
手掛ける てがける ru N1 handle
適する てきする suru N3 be suitable
徹する てっする suru N1 devote oneself to
手伝う てつだう u N4 help
照らす てらす u N2 light up
照り返す てりかえす u N1 reflect
照る てる u N2 shine
転じる てんじる ru N1 turn, change
出会う であう u N3 meet by chance
出かける でかける ru N5 go out
出来上がる できあがる u N2 be completed
できる できる ru N5 be able to, can do
出くわす でくわす u N1 run into
出迎える でむかえる ru N2 meet (someone arriving)
出る でる ru N5 leave, go out
電話する でんわする suru N5 phone
問い合わせる といあわせる ru N1 inquire
問う とう tou N3 ask, question
到着する とうちゃくする suru N3 arrive
尊ぶ とうとぶ u N1 value
登録する とうろくする suru N3 register
遠ざかる とおざかる u N1 move away
通す とおす u N3 let pass
通り掛かる とおりかかる u N2 happen to pass by
通り過ぎる とおりすぎる ru N3 pass by
通る とおる u N4 go through
溶かす とかす u N2 melt
とがめる とがめる ru N1 blame
尖る とがる u N2 be pointed
とぎれる とぎれる ru N1 break off
溶く とく u N3 dissolve
解く とく u N3 untie, solve
説く とく u N3 explain, preach
研ぐ とぐ u N1 sharpen
溶け込む とけこむ u N2 blend in
溶ける とける ru N3 melt
解ける とける ru N3 come undone, be solved
遂げる とげる ru N1 accomplish
綴じる とじる ru N3 bind (pages)
閉じる とじる ru N3 close (eyes, a book)
途絶える とだえる ru N1 stop, cease
整う ととのう u N2 be ready
整える ととのえる ru N1 put in order
届く とどく u N3 reach
届ける とどける ru N4 deliver
滞る とどこおる u N1 be delayed
留まる とどまる u N2 stay
唱える となえる ru N1 recite, advocate
飛ばす とばす u N3 skip over
飛び込む とびこむ u N2 jump in
飛び出す とびだす u N3 jump out
飛ぶ とぶ u N5 fly
とぼける とぼける ru N1 play dumb
止まる とまる u N5 stop
泊まる とまる u N4 stay
留まる とまる u N2 stop, perch
富む とむ u N1 be rich in
止める とめる ru N4 stop (something)
泊める とめる ru N3 put (someone) up
留める とめる ru N3 fasten
伴う ともなう u N1 accompany
捕らえる とらえる ru N2 catch
取り上げる とりあげる ru N3 pick up, take away
取り扱う とりあつかう u N1 handle
取り入れる とりいれる ru N2 take in, adopt
取り替える とりかえる ru N4 exchange
取り組む とりくむ u N1 tackle
取り消す とりけす u N2 cancel
取り締まる とりしまる u N1 crack down on
取り調べる とりしらべる ru N1 investigate
取り立てる とりたてる ru N1 collect (debts)
取り出す とりだす u N2 take out
取り次ぐ とりつぐ u N1 pass on (a message)
取り付ける とりつける ru N1 install
取り除く とりのぞく u N1 remove
取り巻く とりまく u N1 surround
取り混ぜる とりまぜる ru N1 mix together
取り戻す とりもどす u N1 get back
取り寄せる とりよせる ru N1 order (from a supplier)
取る とる u N5 take
捕る とる u N2 catch
採る とる u N2 adopt, pick
撮る とる u N5 take (a photo)
取れる とれる ru N3 come off
とろける とろける ru N1 melt
退く どく u N3 get out of the way
退ける どける ru N2 move (something) aside
怒鳴る どなる u N2 shout
努力する どりょくする suru N3 make an effort
直す なおす u N4 fix, correct
治る なおる u N4 get better (illness)
直る なおる u N4 be fixed
流す ながす u N3 drain
長引く ながびく u N2 drag on
眺める ながめる ru N3 gaze at
流れる ながれる ru N3 flow
泣く なく u N4 cry
鳴く なく u N5 cry (animals)
亡くす なくす u N3 lose (a loved one)
無くす なくす u N5 lose
亡くなる なくなる u N4 pass away
無くなる なくなる u N4 disappear
慰める なぐさめる ru N2 comfort
殴る なぐる u N3 strike
嘆く なげく u N1 grieve
投げ出す なげだす u N1 throw out, give up
投げる なげる ru N4 pitch
なさる なさる honor N4 do (honorific)
詰る なじる u N1 rebuke
為す なす u N2 do, accomplish
懐く なつく u N1 become attached
名付ける なづける ru N1 name
撫でる なでる ru N2 stroke
怠ける なまける ru N3 be idle
嘗める なめる ru N1 lick
悩ます なやます u N1 trouble
悩む なやむ u N3 agonize
倣う ならう u N2 imitate
習う ならう u N5 learn
慣らす ならす u N3 accustom
馴らす ならす u N3 tame
鳴らす ならす u N3 ring
並ぶ ならぶ u N5 line up
並べる ならべる ru N5 line up (things)
成り立つ なりたつ u N1 consist of
なる なる u N5 become
生る なる u N3 bear (fruit)
鳴る なる u N4 ring, sound
慣れる なれる ru N4 get used to
似合う にあう u N3 suit
煮える にえる ru N3 be cooked
匂う におう u N2 smell
似通う にかよう u N1 be similar
逃がす にがす u N2 let go
握る にぎる u N3 grasp
賑わう にぎわう u N1 be lively
憎む にくむ u N2 hate
逃げ出す にげだす u N1 run away
逃げる にげる ru N4 escape
濁る にごる u N2 become cloudy
滲む にじむ u N1 blur, ooze
担う になう u N1 bear
鈍る にぶる u N1 get rusty
入院する にゅういんする suru N4 be hospitalised
入学する にゅうがくする suru N4 enter a school
睨む にらむ u N2 glare at
似る にる ru N4 resemble
煮る にる ru N3 boil, simmer
縫う ぬう u N2 sew
抜かす ぬかす u N1 skip
抜く ぬく u N3 extract
脱ぐ ぬぐ u N5 take off
抜け出す ぬけだす u N1 slip out
抜ける ぬける ru N3 come out, fall out
盗む ぬすむ u N4 steal
濡らす ぬらす u N3 wet
塗る ぬる u N4 paint, spread
濡れる ぬれる ru N4 get wet
寝かせる ねかせる ru N1 put to bed
願う ねがう u N3 desire
捩る ねじる u N2 twist
妬む ねたむ u N1 be jealous of
ねだる ねだる u N1 pester
熱する ねっする suru N2 heat
粘る ねばる u N1 persist
眠る ねむる u N4 sleep
狙う ねらう u N2 aim at
寝る ねる ru N5 sleep, go to bed
練る ねる u N1 knead, polish (a plan)
逃す のがす u N1 miss
逃れる のがれる ru N1 escape
残す のこす u N3 leave behind
残る のこる u N4 remain
乗せる のせる ru N3 give (someone) a ride
載せる のせる ru N3 put on, publish
覗く のぞく u N3 peek in
除く のぞく u N3 remove
望む のぞむ u N3 desire
臨む のぞむ u N3 face, attend
乗っ取る のっとる u N1 take over
罵る ののしる u N1 curse, abuse
伸ばす のばす u N3 extend
延ばす のばす u N3 extend
伸びる のびる ru N3 grow, stretch
延びる のびる ru N3 be extended
述べる のべる ru N3 state
上る のぼる u N3 go up
昇る のぼる u N3 rise (the sun)
登る のぼる u N5 climb
飲み込む のみこむ u N1 swallow
飲む のむ u N5 drink
乗り換える のりかえる ru N4 transfer
乗り込む のりこむ u N1 get in
乗る のる u N5 ride, get on
載る のる u N3 be on, appear (in print)
拝見する はいけんする suru N4 see (humble)
入る はいる u N5 enter
這う はう u N2 crawl
映える はえる ru N3 look good
生える はえる ru N3 grow (hair, plants)
捗る はかどる u N1 make progress
図る はかる u N3 plan, attempt
測る はかる u N3 measure (length)
計る はかる u N3 measure (time)
諮る はかる u N3 consult
量る はかる u N3 weigh
剥がす はがす u N2 peel off
はく はく u N5 put on (shoes, trousers)
吐く はく u N3 vomit, breathe out
掃く はく u N3 sweep
剥ぐ はぐ u N1 strip off
励ます はげます u N1 encourage
励む はげむ u N1 strive
剥げる はげる ru N1 peel off
運ぶ はこぶ u N4 carry
挟まる はさまる u N2 get caught between
挟む はさむ u N2 put between
走る はしる u N5 run
始める はじめる ru N4 start
恥じらう はじらう u N1 be shy
恥じる はじる ru N1 be ashamed
外す はずす u N3 unfasten
弾む はずむ u N1 bounce
外れる はずれる ru N3 come off, miss
果たす はたす u N1 fulfil
働く はたらく u N5 work
発見する はっけんする suru N3 discover
発展する はってんする suru N3 develop
発表する はっぴょうする suru N3 announce, present
果てる はてる ru N1 end, die
話し合う はなしあう u N3 discuss
話し掛ける はなしかける ru N2 speak to
放す はなす u N3 let go, release
話す はなす u N5 speak
離す はなす u N3 separate, let go
離れる はなれる ru N3 leave, be apart
跳ねる はねる ru N2 jump, splash
阻む はばむ u N1 block
省く はぶく u N3 omit
はまる はまる u N1 fit, get hooked
はめる はめる ru N2 put on, fit
生やす はやす u N3 grow (a beard)
早める はやめる ru N1 bring forward
流行る はやる u N3 be in fashion
払い込む はらいこむ u N2 pay in
払い戻す はらいもどす u N2 refund
払う はらう u N4 pay
張り切る はりきる u N2 be eager
貼る はる u N5 stick (on)
晴れる はれる ru N5 clear up
腫れる はれる ru N1 swell
反する はんする suru N1 go against
反対する はんたいする suru N4 oppose
判断する はんだんする suru N3 judge
化ける ばける ru N1 turn into
罰する ばっする suru N3 punish
ばてる ばてる ru N1 be exhausted
ばらまく ばらまく u N1 scatter
冷える ひえる ru N4 get cold
控える ひかえる ru N1 hold back, note down
比較する ひかくする suru N3 compare
光る ひかる u N4 shine
引き上げる ひきあげる ru N1 raise, pull out
率いる ひきいる ru N1 lead
引き受ける ひきうける ru N2 take on
引き起こす ひきおこす u N1 cause
引き返す ひきかえす u N2 turn back
引き下げる ひきさげる ru N1 lower
引きずる ひきずる u N1 drag
引き出す ひきだす u N2 pull out, withdraw
引き止める ひきとめる ru N2 hold back
引き取る ひきとる u N1 take over, leave
引く ひく u N5 pull
弾く ひく u N5 play (an instrument)
浸す ひたす u N1 soak
引っ掛かる ひっかかる u N2 get caught
引っ掻く ひっかく u N1 scratch
引っ繰り返す ひっくりかえす u N2 turn over
引っ繰り返る ひっくりかえる u N2 be overturned
引っ越す ひっこす u N4 move (house)
引っ込む ひっこむ u N2 draw back
引っ張る ひっぱる u N3 pull
捻る ひねる u N2 twist
響く ひびく u N2 echo
冷やかす ひやかす u N1 tease
冷やす ひやす u N3 chill
表現する ひょうげんする suru N3 express
開く ひらく u N4 open
拾う ひろう u N4 pick up
広がる ひろがる u N3 spread
広げる ひろげる ru N3 spread
広まる ひろまる u N3 spread
広める ひろめる ru N3 broaden
びっくりする びっくりする suru N4 be surprised
増える ふえる ru N4 increase
深まる ふかまる u N3 deepen
深める ふかめる ru N3 deepen
吹く ふく u N5 blow
拭く ふく u N3 wipe
復習する ふくしゅうする suru N4 review (lessons)
含む ふくむ u N3 contain
含める ふくめる ru N3 include
膨らます ふくらます u N2 inflate
膨らむ ふくらむ u N2 swell
膨れる ふくれる ru N1 swell, sulk
更ける ふける ru N2 grow late
老ける ふける ru N1 age
耽る ふける u N1 be absorbed in
塞がる ふさがる u N2 be blocked
塞ぐ ふさぐ u N2 block
ふざける ふざける ru N2 fool around
防ぐ ふせぐ u N3 defend
太る ふとる u N4 gain weight
踏まえる ふまえる ru N1 be based on
踏み込む ふみこむ u N1 step into
踏む ふむ u N4 step on
増やす ふやす u N3 increase
振り返る ふりかえる u N1 look back
振り向く ふりむく u N2 look back
振る ふる u N3 wave
降る ふる u N5 fall (rain, snow)
震える ふるえる ru N3 shiver
振る舞う ふるまう u N2 behave
震わせる ふるわせる ru N1 make tremble
触れる ふれる ru N3 touch
ぶつかる ぶつかる u N3 strike
ぶつける ぶつける ru N3 bump, hit
ぶらさげる ぶらさげる ru N2 dangle
凹む へこむ u N2 be dented
隔たる へだたる u N1 be distant
隔てる へだてる ru N2 separate
減らす へらす u N3 decrease
へりくだる へりくだる u N1 be humble
減る へる u N3 decrease
経る へる ru N3 pass through
変化する へんかする suru N3 change
返事する へんじする suru N4 reply
勉強する べんきょうする suru N5 study
報告する ほうこくする suru N3 report
報じる ほうじる ru N1 report
葬る ほうむる u N1 bury
放り込む ほうりこむ u N1 throw into
放り出す ほうりだす u N1 throw out
放る ほうる u N2 throw
吠える ほえる ru N3 bark
誇る ほこる u N1 be proud of
綻びる ほころびる ru N1 come apart
干す ほす u N2 dry, air
施す ほどこす u N1 give, carry out
微笑む ほほえむ u N3 smile
褒める ほめる ru N4 praise
彫る ほる u N2 carve
掘る ほる u N2 dig
滅びる ほろびる ru N1 perish
滅ぼす ほろぼす u N1 destroy
翻訳する ほんやくする suru N4 translate
惚ける ぼける ru N1 go senile
ぼやく ぼやく u N1 grumble
ぼやける ぼやける ru N1 become dim
参る まいる u N4 go, come (humble)
舞う まう u N1 dance, flutter
任す まかす u N1 entrust
負かす まかす u N1 defeat
任せる まかせる ru N3 entrust
賄う まかなう u N1 cover (costs)
曲がる まがる u N5 turn
紛れる まぎれる ru N1 be lost in
巻く まく u N3 wind, roll
撒く まく u N3 sprinkle
蒔く まく u N3 sow
負ける まける ru N4 lose
曲げる まげる ru N2 bend
まごつく まごつく u N1 be confused
勝る まさる u N1 surpass
混ざる まざる u N3 be mixed
交える まじえる ru N1 mix, exchange
混じる まじる u N3 be mixed
交わる まじわる u N1 intersect, mix with
増す ます u N3 increase
混ぜる まぜる ru N3 mix
跨ぐ またぐ u N2 step over
待ち合わせる まちあわせる ru N2 meet up
間違える まちがえる ru N4 make a mistake
待ち望む まちのぞむ u N1 look forward to
待つ まつ u N5 wait
祭る まつる u N2 enshrine
まとまる まとまる u N3 come together
まとめる まとめる ru N3 put together, sum up
学ぶ まなぶ u N3 learn
間に合う まにあう u N4 be in time
免れる まぬがれる ru N1 escape
招く まねく u N3 invite
真似る まねる ru N2 imitate
守る まもる u N3 protect
迷う まよう u N3 be puzzled
丸める まるめる ru N1 roll up
回す まわす u N4 turn (something)
回る まわる u N4 go around, turn
見上げる みあげる ru N2 look up at
見合わせる みあわせる ru N1 postpone
見える みえる ru N4 be visible
見送る みおくる u N2 see off
見落とす みおとす u N1 overlook
見下ろす みおろす u N2 look down on
磨く みがく u N5 brush, polish
見せびらかす みせびらかす u N1 show off
見せる みせる ru N5 show
満たす みたす u N1 fill, satisfy
乱す みだす u N1 disturb
乱れる みだれる ru N1 be in disorder
導く みちびく u N1 guide
満ちる みちる ru N3 be full
見つかる みつかる u N4 be found
見つける みつける ru N4 discover
見詰める みつめる ru N2 stare at
認める みとめる ru N3 recognize
見直す みなおす u N2 look at again
見なす みなす u N1 regard as
見習う みならう u N1 learn from
見慣れる みなれる ru N2 get used to seeing
見逃す みのがす u N1 miss, let pass
実る みのる u N2 bear fruit
見計らう みはからう u N1 choose (the right moment)
見舞う みまう u N2 visit (a sick person)
見る みる ru N5 see, watch
診る みる ru N3 examine (a patient)
見渡す みわたす u N1 look out over
向かう むかう u N4 head for
迎える むかえる ru N4 welcome
剥く むく u N3 peel
向く むく u N3 face, turn
向ける むける ru N3 turn (towards)
むしる むしる u N1 pluck
蒸す むす u N3 steam
結び付く むすびつく u N1 be linked
結び付ける むすびつける ru N1 tie together
結ぶ むすぶ u N3 tie
群がる むらがる u N1 swarm
命じる めいじる ru N3 order
捲る めくる u N3 turn over (pages)
恵まれる めぐまれる ru N2 be blessed with
恵む めぐむ u N1 give (in charity)
巡る めぐる u N2 go around
目指す めざす u N2 aim for
目覚める めざめる ru N1 wake up
召し上がる めしあがる u N4 eat, drink (honorific)
召す めす u N1 call, wear (honorific)
目立つ めだつ u N2 stand out
面する めんする suru N1 face
儲かる もうかる u N2 be profitable
儲ける もうける ru N2 make a profit
設ける もうける ru N1 set up
申し上げる もうしあげる ru N4 say (humble)
申し入れる もうしいれる ru N1 propose
申し込む もうしこむ u N3 apply for
申し出る もうしでる ru N1 offer, propose
申す もうす u N4 say (humble)
燃える もえる ru N3 burn
もがく もがく u N1 struggle
潜る もぐる u N2 dive
もたらす もたらす u N1 bring about
もたれる もたれる ru N2 lean on
持ち上げる もちあげる ru N3 raise
用いる もちいる ru N3 use
持つ もつ u N5 hold, have
もてなす もてなす u N1 entertain
もてる もてる ru N1 be popular
基づく もとづく u N3 be based on
求める もとめる ru N3 request
戻す もどす u N3 put back
戻る もどる u N4 go back
物語る ものがたる u N2 tell, show
揉む もむ u N2 massage
もめる もめる ru N1 quarrel
燃やす もやす u N3 burn
催す もよおす u N1 hold (an event)
もらう もらう u N4 receive
漏らす もらす u N1 let leak
盛り上がる もりあがる u N1 liven up
漏る もる u N1 leak
盛る もる u N2 heap up, serve
漏れる もれる ru N1 leak
焼く やく u N4 bake, grill
訳す やくす u N3 translate
約束する やくそくする suru N4 promise
役に立つ やくにたつ u N4 be useful
焼ける やける ru N4 be burned, be grilled
養う やしなう u N1 raise, support
休む やすむ u N5 rest, take a day off
休める やすめる ru N1 rest
痩せる やせる ru N4 lose weight
やっつける やっつける ru N2 beat
雇う やとう u N3 employ
破く やぶく u N2 tear
破る やぶる u N3 tear
破れる やぶれる ru N3 get torn
止む やむ u N4 stop (rain)
病む やむ u N1 fall ill
止める やめる ru N4 stop, quit
辞める やめる ru N3 quit, retire
やりとおす やりとおす u N1 carry through
やりとげる やりとげる ru N1 accomplish
やる やる u N5 do, give
和らげる やわらげる ru N1 soften
有する ゆうする suru N1 own
歪む ゆがむ u N1 warp
揺さぶる ゆさぶる u N1 shake
輸出する ゆしゅつする suru N4 export
濯ぐ ゆすぐ u N1 rinse
譲る ゆずる u N3 hand over, give up (a seat)
茹でる ゆでる ru N3 boil
輸入する ゆにゅうする suru N4 import
指差す ゆびさす u N1 point at
揺らぐ ゆらぐ u N1 waver
許す ゆるす u N3 permit
緩む ゆるむ u N1 loosen
緩める ゆるめる ru N1 loosen
揺れる ゆれる ru N4 shake
酔う よう u N3 get drunk
用意する よういする suru N4 get ready
要する ようする suru N1 require
横切る よこぎる u N3 cross
よこす よこす u N2 send
汚す よごす u N3 pollute
汚れる よごれる ru N4 become dirty
予習する よしゅうする suru N4 prepare (lessons)
止す よす u N3 stop, quit
寄せる よせる ru N3 bring near
呼び掛ける よびかける ru N2 call out to
呼び出す よびだす u N2 call out, summon
呼び止める よびとめる ru N1 call to (someone) to stop
呼ぶ よぶ u N5 call
読み上げる よみあげる ru N1 read out
蘇る よみがえる u N2 come back to life
読む よむ u N5 read
予約する よやくする suru N4 reserve, book
寄り掛かる よりかかる u N1 lean against
因る よる u N3 be due to
寄る よる u N4 drop by
喜ぶ よろこぶ u N4 rejoice
弱まる よわまる u N3 weaken
弱める よわめる ru N3 weaken
弱る よわる u N1 weaken, be at a loss
理解する りかいする suru N3 understand
略す りゃくす u N2 abbreviate
留学する りゅうがくする suru N4 study abroad
料理する りょうりする suru N5 cook
旅行する りょこうする suru N5 travel
利用する りようする suru N4 use
練習する れんしゅうする suru N5 practise
連絡する れんらくする suru N4 contact
論じる ろんじる ru N3 argue
沸かす わかす u N4 boil (water)
分かる わかる u N5 understand
分かれる わかれる ru N3 branch off
別れる わかれる ru N4 part from
沸く わく u N4 boil (water)
湧く わく u N3 well up
分ける わける ru N3 divide
忘れる わすれる ru N5 forget
渡す わたす u N5 hand over
渡る わたる u N5 cross
詫びる わびる ru N2 apologize
笑う わらう u N4 laugh
割り込む わりこむ u N1 cut in
割る わる u N3 divide
割れる われる ru N4 break, crack
コピーする コピーする suru N5 copy
サボる サボる u N1 skip (class, work)
"""
