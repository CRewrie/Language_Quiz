"""Content for the Hiragana Dojo: words, sentences, kana notes and FAQ.

Written once, so the dojo needs no AI requests at runtime. tools/gen_kana.py checks every item, works out the
earliest lesson it fits (from the kana it uses), adds romaji and writes static/kana/content.json.

Format: one item per line, "hiragana|English". Sentences put spaces between words (as in children's books)
and keep particles separate, so は / へ / を read as wa / e / o.
"""

WORDS = """
くき|stem
きか|geometry
しそ|shiso (perilla)
さす|to point, to sting
すす|soot
ささ|bamboo grass
たて|vertical
てつ|iron
つち|soil
とち|land
つつ|tube
つた|ivy
なな|seven
ぬの|cloth
ひふ|skin
まま|as it is
やや|slightly
るり|lapis lazuli
わ|ring, circle
けさ|this morning
くせ|habit
こそこそ|sneakily
さくさく|crispy
せかす|to hurry someone
さく|to bloom
こす|to cross over
しき|ceremony; the four seasons
さき|ahead, tip
てき|enemy
たたく|to hit
かたち|shape
こたつ|kotatsu (heated table)
ちくちく|prickly
きつつき|woodpecker
ちかく|nearby
とく|gain, benefit
つく|to arrive, to stick
かつ|to win
たかく|high (adverb)
けち|stingy
かつて|formerly
こと|thing, matter
こねこ|kitten
きぬ|silk
こな|powder
かに|crab
なかなか|quite, not easily
のき|eaves
のこのこ|nonchalantly
ひかく|comparison
ふかく|deeply
はこ|box
みかく|sense of taste
まき|firewood
こま|spinning top
きみ|you (casual)
くむ|to scoop, to assemble
かゆ|rice porridge
ゆく|to go (literary)
くり|chestnut
きり|fog
くろ|black
くるくる|round and round
ころころ|rolling
かれ|he, boyfriend
かり|a loan
きる|to wear
くる|to come
かるく|lightly
わく|frame
さて|well then
すそ|hem
たす|to add
さつ|banknote
すな|sand
ぬし|master, owner
ひさし|eaves, visor
はす|lotus
ほす|to dry (in the sun)
ます|trout
むす|to steam
すり|pickpocket
する|to do
さら|plate
しる|to know
せり|Japanese parsley
そり|sled
すらすら|fluently
さらさら|smoothly, silky
わし|eagle
さわ|mountain stream
たね|seed
つな|rope
ほたて|scallop
はと|pigeon
つま|wife
まと|target
もち|rice cake
やつ|guy, fellow
たる|barrel
つり|fishing
とる|to take
つる|crane (bird)
たりる|to be enough
ちる|to fall (petals)
わた|cotton
わたる|to cross
はね|feather, wing
なみ|wave
まね|imitation
のり|seaweed, glue
なる|to become
ねる|to sleep
にる|to resemble
のる|to ride
なわ|rope
ひま|free time
はま|beach
ふる|to fall (rain), to shake
ほる|to dig
はら|belly, field
ゆみ|bow (weapon)
まゆ|eyebrow
もや|mist
むら|village
まる|circle
みる|to see
まり|ball
まわる|to turn around
ゆり|lily
やる|to do, to give
より|than, more
よろよろ|staggering
わる|to divide, to break
ゆるす|to forgive
ゆるい|loose
よわい|weak
やわらかい|soft
わかれ|parting
なわとび|skipping rope
ふるさと|hometown
ところ|place
こころ|heart
けむり|smoke
まつり|festival
ひかり|light
からす|crow
ほたる|firefly
すわる|to sit
かわく|to dry
ことわる|to refuse
せんたく|laundry
たんす|chest of drawers
なんか|something like
みんな|everyone
かんたん|easy
にんにく|garlic
さんかく|triangle
しんせつ|kind
てんさい|genius
まんなか|middle
みなと|harbour
みやこ|capital (old)
むすめ|daughter
めかた|weight (old word)
もめん|cotton cloth
やくわり|role
ゆかり|connection
よみせ|night market
らくらく|easily
りかい|understanding
るす|being out
れきし|history
ろうか|corridor
わすれもの|something left behind
あい|love
いえ|house
うえ|above, top
あお|blue
いい|good
おい|nephew
あう|to meet
いう|to say
あおい|blue (adjective)
え|picture
お|tail
うお|fish (old word)
おおい|many
あか|red
あかい|red (adjective)
あき|autumn
いけ|pond
えき|station
かお|face
こい|carp
きく|to listen
かく|to write
いく|to go
こえ|voice
ここ|here
くうき|air
かい|shellfish
かき|persimmon
おおきい|big
こけ|moss
かこ|the past
けいかく|plan
きかい|machine
おく|to put
かう|to buy
きく|chrysanthemum
こうこう|high school
いか|squid
あく|to open
きい|yellow (old word)
くい|stake, post
かかく|price
けいこ|practice, lessons
あさ|morning
すし|sushi
かさ|umbrella
しお|salt
いす|chair
あし|leg, foot
すき|to like
うそ|a lie
そこ|there
せかい|world
おかし|sweets
けしき|scenery
あせ|sweat
うし|cow
すいか|watermelon
せき|seat
さけ|salmon
おいしい|delicious
あそこ|over there
すこし|a little
せいかく|personality
しかく|square
いし|stone
さか|slope
すく|to be empty
さす|to point
けす|to erase
かす|to lend
おす|to push
さそう|to invite
あさい|shallow
しかし|however
うすい|thin, weak
こし|lower back
くさ|grass
きせき|miracle
すいせい|comet
くち|mouth
そと|outside
した|below, tongue
いち|one
きた|north
あつい|hot
たかい|tall, expensive
とけい|clock
たいこ|drum
つくえ|desk
ちかてつ|subway
て|hand
と|door
ち|blood
つき|moon
たき|waterfall
たけ|bamboo
おと|sound
いと|thread
あと|after
ちかい|near
とおい|far
ちいさい|small
たつ|to stand
まつ|to wait
もつ|to hold
きって|stamp
ちち|father
あした|tomorrow
した|did
たすけ|help
たいせつ|important
とうさく|plagiarism
こたえ|answer
ついたち|first day of the month
いつ|when
いくつ|how many
くつ|shoes
うた|song
たこ|octopus
おとうと|younger brother
おとこ|man
とし|year, age
ちしき|knowledge
きた|came
たしか|surely
ねこ|cat
いぬ|dog
なつ|summer
にく|meat
なに|what
あね|older sister
ぬの|cloth
なか|inside
にし|west
さかな|fish
おかね|money
きのこ|mushroom
あなた|you
なく|to cry
しぬ|to die
にほん|Japan
なまえ|name
ねつ|fever
のこす|to leave behind
きのう|yesterday
いなか|countryside
あに|older brother
おにいさん|older brother (polite)
おねえさん|older sister (polite)
かのじょ|she, girlfriend
なし|pear
くに|country
にく|meat
ぬう|to sew
ぬく|to pull out
いのち|life
のち|later
たのしい|fun
すくない|few
あぶない|dangerous
きたない|dirty
ないしょ|secret
なつかしい|nostalgic
にんき|popularity
こないだ|the other day
はな|flower, nose
ひと|person
ふね|boat
ほし|star
へそ|belly button
はし|bridge, chopsticks
ほね|bone
ふた|lid
さいふ|wallet
ひとつ|one thing
ほそい|thin
ひこうき|airplane
はは|mother
ちち|father
ふたつ|two things
ひく|to pull, to play (piano)
はく|to wear (shoes)
ほか|other
へた|bad at
はたけ|field
ふく|clothes
ふくろ|bag
ひかり|light
はいる|to enter
はなす|to speak
ほしい|to want
ひろい|wide
ふかい|deep
へいわ|peace
ほうほう|method
はこ|box
はたち|twenty years old
ひなた|sunny spot
ふとい|thick
はつか|twentieth day
ひふ|skin
ほお|cheek
ふえ|flute
ひつじ|sheep
うみ|sea
あめ|rain
みみ|ear
むし|insect
もも|peach
くま|bear
いま|now
くも|cloud
まめ|bean
あたま|head
むすめ|daughter
さしみ|sashimi
まち|town
みせ|shop
みち|road
むね|chest
め|eye
もの|thing
もり|forest
まど|window
みず|water
むかし|long ago
はじめまして|nice to meet you
あまい|sweet
さむい|cold
ねむい|sleepy
みかん|mandarin orange
みなみ|south
むすこ|son
まいにち|every day
ともだち|friend
こども|child
おもい|heavy
おもしろい|interesting
まえ|front
うしろ|behind
もう|already
まだ|not yet
みる|to see
のむ|to drink
よむ|to read
すむ|to live
やすむ|to rest
たのむ|to ask for
かみ|paper, hair
はさみ|scissors
いみ|meaning
しま|island
くもり|cloudy
あたたかい|warm
つめたい|cold (to touch)
みどり|green
むらさき|purple
やま|mountain
ゆき|snow
ゆめ|dream
へや|room
よこ|side
ふゆ|winter
おゆ|hot water
やさい|vegetable
やすみ|holiday, rest
ゆうひ|sunset
よみかた|way of reading
やさしい|kind
やすい|cheap
ゆび|finger
よる|night
ゆか|floor
やね|roof
やくそく|promise
ゆっくり|slowly
よい|good
よてい|plan, schedule
ゆうめい|famous
ゆうき|courage
やま|mountain
ゆかた|summer kimono
とり|bird
いろ|colour
ひる|noon
これ|this
それ|that
ふろ|bath
はれ|sunny
りす|squirrel
くるま|car
さくら|cherry blossom
しろい|white
きいろ|yellow
くろい|black
あかるい|bright
くらい|dark
るす|not at home
りんご|apple
りょうり|cooking
はる|spring
さる|monkey
てら|temple
そら|sky
まくら|pillow
くすり|medicine
とおり|street
おまつり|festival
まわり|surroundings
かえる|frog, to go home
かえり|the way home
はれる|to clear up
わすれる|to forget
おわり|the end
さいふ|wallet
ほん|book
かわ|river
わたし|I, me
にわ|garden
おんな|woman
わかる|to understand
せんせい|teacher
わに|crocodile
こんにちは|hello
こんばんは|good evening
すいません|excuse me
わるい|bad
かわいい|cute
わらう|to laugh
にわとり|chicken
でんわ|telephone
おんがく|music
しんぶん|newspaper
てんき|weather
げんき|healthy, well
ぎんこう|bank
きんようび|Friday
にんじん|carrot
みんな|everyone
ほんや|bookshop
わしょく|Japanese food
くうこう|airport
がっこう|school
かぞく|family
ごはん|rice, meal
たまご|egg
かばん|bag
ぎゅうにゅう|milk
じかん|time
じてんしゃ|bicycle
でんしゃ|train
どうぶつ|animal
ばしょ|place
びょういん|hospital
ぶんか|culture
べんきょう|study
ぼうし|hat
ぱん|bread
えんぴつ|pencil
さんぽ|walk
しんぱい|worry
てがみ|letter
かぎ|key
ひざ|knee
かぜ|wind, a cold
みぎ|right
ひだり|left
ごご|afternoon
ごぜん|morning (a.m.)
どこ|where
だれ|who
なぜ|why
ぜんぶ|all
ずっと|all the time
ちょっと|a little
いっしょ|together
きょう|today
しゅくだい|homework
りょこう|trip
しゃしん|photo
ちゃいろ|brown
おちゃ|tea
きゅうり|cucumber
じゅうしょ|address
しょくどう|cafeteria
ちゅうごく|China
きょうしつ|classroom
いしゃ|doctor
かいしゃ|company
でぐち|exit
いりぐち|entrance
はなび|fireworks
おまわりさん|police officer
おばあさん|grandmother
おじいさん|grandfather
おかあさん|mother
おとうさん|father
いもうと|younger sister
あさごはん|breakfast
ひるごはん|lunch
ばんごはん|dinner
くだもの|fruit
のみもの|drink
たべもの|food
やきとり|grilled chicken
おにぎり|rice ball
みそしる|miso soup
とうふ|tofu
なっとう|natto
すきやき|sukiyaki
おべんとう|packed lunch
はし|chopsticks
さら|plate
ちゃわん|rice bowl
こおり|ice
さとう|sugar
しょうゆ|soy sauce
からい|spicy
にがい|bitter
すっぱい|sour
あたらしい|new
ふるい|old
いそがしい|busy
ひま|free time
むずかしい|difficult
かんたん|easy
しずか|quiet
にぎやか|lively
きれい|pretty, clean
すてき|lovely
だいじょうぶ|all right
たいへん|tough
べんり|convenient
ふべん|inconvenient
じょうず|good at
へた|bad at
すき|to like
きらい|to dislike
うれしい|happy
かなしい|sad
こわい|scary
はずかしい|embarrassing
さびしい|lonely
ねる|to sleep
おきる|to get up
たべる|to eat
あるく|to walk
はしる|to run
およぐ|to swim
うたう|to sing
おどる|to dance
あそぶ|to play
はたらく|to work
つくる|to make
あける|to open
しめる|to close
まつ|to wait
おしえる|to teach
ならう|to learn
おぼえる|to remember
わすれる|to forget
てつだう|to help
つかう|to use
あらう|to wash
きる|to cut
はじまる|to begin
おわる|to end
でかける|to go out
かえる|to go home
くる|to come
する|to do
ある|to exist (things)
いる|to exist (people)
しる|to know
おもう|to think
いそぐ|to hurry
はやい|early, fast
おそい|late, slow
ながい|long
みじかい|short
たかい|high
ひくい|low
おおきい|big
ちいさい|small
あおぞら|blue sky
にじ|rainbow
かみなり|thunder
たいふう|typhoon
ほし|star
たいよう|sun
つき|moon
うみべ|seaside
すなはま|sandy beach
いわ|rock
みずうみ|lake
しま|island
のはら|field, meadow
はなや|flower shop
さかなや|fish shop
やおや|greengrocer
こうえん|park
としょかん|library
えいがかん|cinema
ゆうびんきょく|post office
どうぶつえん|zoo
すいぞくかん|aquarium
びじゅつかん|art museum
いぬごや|kennel
きつね|fox
たぬき|raccoon dog
うさぎ|rabbit
かめ|turtle
へび|snake
かえる|frog
ぞう|elephant
きりん|giraffe
ねずみ|mouse
うま|horse
ぶた|pig
ひよこ|chick
からす|crow
すずめ|sparrow
はと|pigeon
くじら|whale
いるか|dolphin
かに|crab
えび|shrimp
ほたる|firefly
ちょう|butterfly
はち|bee
あり|ant
せみ|cicada
とんぼ|dragonfly
め|eye
はな|nose
くち|mouth
みみ|ear
かお|face
あたま|head
かみ|hair
て|hand
ゆび|finger
うで|arm
あし|leg
せなか|back
おなか|belly
こころ|heart, mind
からだ|body
いち|one
に|two
さん|three
よん|four
ご|five
ろく|six
なな|seven
はち|eight
きゅう|nine
じゅう|ten
ひゃく|hundred
せん|thousand
まん|ten thousand
ひとつ|one (thing)
ふたつ|two (things)
みっつ|three (things)
よっつ|four (things)
いつつ|five (things)
むっつ|six (things)
ななつ|seven (things)
やっつ|eight (things)
ここのつ|nine (things)
とお|ten (things)
げつようび|Monday
かようび|Tuesday
すいようび|Wednesday
もくようび|Thursday
きんようび|Friday
どようび|Saturday
にちようび|Sunday
はる|spring
なつ|summer
あき|autumn
ふゆ|winter
あさ|morning
ひる|noon
ゆうがた|evening
よる|night
きのう|yesterday
きょう|today
あした|tomorrow
まいあさ|every morning
まいばん|every evening
らいしゅう|next week
せんしゅう|last week
ことし|this year
らいねん|next year
きょねん|last year
いつも|always
ときどき|sometimes
たまに|occasionally
すぐ|immediately
もうすぐ|soon
ありがとう|thank you
おはよう|good morning
おやすみ|good night
さようなら|goodbye
ごめんなさい|I'm sorry
いただきます|let's eat
ごちそうさま|thanks for the meal
おめでとう|congratulations
いってきます|I'm off
ただいま|I'm home
おかえり|welcome home
よろしく|nice to meet you
がんばって|good luck
だいすき|love, really like
ほんとう|true, really
たぶん|probably
もちろん|of course
いいえ|no
はい|yes
そうです|that's right
ちがう|different, wrong
おなじ|same
いろいろ|various
たくさん|a lot
ぜんぜん|not at all
とても|very
あまり|not very
もっと|more
いちばん|number one, most
ふたり|two people
ひとり|one person, alone
なかま|companion
しあわせ|happiness
えがお|smile
なみだ|tears
きもち|feeling
ゆうき|courage
ちから|strength
こえ|voice
ことば|word, language
もじ|letter, character
ひらがな|hiragana
かんじ|kanji
にほんご|Japanese
えいご|English
しつもん|question
こたえ|answer
しけん|exam
じしょ|dictionary
けしごむ|eraser
はさみ|scissors
つくえ|desk
いす|chair
こくばん|blackboard
きょうかしょ|textbook
しゅみ|hobby
えいが|film
おんがく|music
しゃしん|photo
りょうり|cooking
つり|fishing
やきゅう|baseball
すいえい|swimming
さんぽ|walk
どくしょ|reading
ゆかた|summer kimono
きもの|kimono
くつした|socks
てぶくろ|gloves
めがね|glasses
とけい|watch
さいふ|wallet
かさ|umbrella
かばん|bag
ふとん|futon
たたみ|tatami
しょうじ|paper sliding door
おしいれ|closet
だいどころ|kitchen
げんかん|entrance hall
にかい|second floor
かいだん|stairs
まど|window
とびら|door
かべ|wall
やね|roof
にわ|garden
"""

SENTENCES = """
あかい かお。|A red face.
おおきい こえ。|A loud voice.
いい こえ。|A nice voice.
あおい いけ。|A blue pond.
あかい かき。|A red persimmon.
おおきい いか。|A big squid.
いい かお。|A good face.
いく。|I'll go.
かく。|I'll write.
きく。|I'll listen.
ここ か。|Is it here?
かう か。|Will you buy it?
いく か。|Are you going?
いい か。|Is that OK?
あき。 あかい かき。|Autumn. Red persimmons.
すし か すいか か。|Sushi or watermelon?
あさい いけ。|A shallow pond.
うすい かさ。|A thin umbrella.
あおい いす。|A blue chair.
すこし あかい。|It's a little red.
うそ。|No way!
そう、 そう。|Yes, yes.
いい けしき。|Nice scenery.
あそこ か。|Over there?
あかい おかし。|Red sweets.
おおきい うし。|A big cow.
おいしい おかし。|Delicious sweets.
すこし あさい。|It's a little shallow.
すき。|I like it.
あさ、 すこし あつい。|In the morning it's a little hot.
あつい あさ。|A hot morning.
ちいさい いす。|A small chair.
とおい えき。|A faraway station.
たかい とけい。|An expensive clock.
くつ と かさ。|Shoes and an umbrella.
あした いく。|I'll go tomorrow.
あした かう。|I'll buy it tomorrow.
いつ いく。|When are you going?
いくつ かう。|How many will you buy?
おとうと と いく。|I'll go with my little brother.
ちち と いく。|I'll go with my father.
ちいさい たこ。|A small octopus.
あつい あつい。|It's so hot!
たかい たかい。|Up, up high!
うた と おと。|Songs and sounds.
つくえ と いす。|A desk and a chair.
ねこ と いぬ。|A cat and a dog.
ちいさい ねこ。|A small cat.
おおきい いぬ。|A big dog.
なつ に いく。|I'll go in the summer.
いなか に いく。|I'm going to the countryside.
あした いなか に いく。|I'm going to the countryside tomorrow.
ねこ の くち。|The cat's mouth.
あに の くつ。|My older brother's shoes.
あね の かさ。|My older sister's umbrella.
なに か。|What is it?
ねこ に えさ。|Food for the cat.
さかな か にく か。|Fish or meat?
あなた の いす。|Your chair.
いぬ と ねこ と さかな。|A dog, a cat and a fish.
いい におい。|A nice smell.
なつ の あさ。|A summer morning.
あつい なつ。 あおい いけ。|A hot summer. A blue pond.
ねこ は ちいさい。|The cat is small.
いぬ は おおきい。|The dog is big.
なつ は あつい。|Summer is hot.
ふね は おおきい。|The boat is big.
はな は あかい。|The flower is red.
ほし は とおい。|The stars are far away.
そと は あつい。|It's hot outside.
ひと は おおい。|There are a lot of people.
ちち は いかない。|My father isn't going.
へそ は ちいさい。|The belly button is small.
ひとつ ほしい。|I want one.
ふたつ ほしい。|I want two.
はは と はなす。|I talk with my mother.
ひこうき は はやい。|Planes are fast.
ほそい はし。|A narrow bridge.
はなし は たのしい。|The talk is fun.
はこ は ちいさい。|The box is small.
ふく は あかい。|The clothes are red.
いぬ は なかない。|The dog doesn't bark.
うみ は あおい。|The sea is blue.
あめ は つめたい。|The rain is cold.
くま は おおきい。|Bears are big.
いま なにも しない。|I'm not doing anything now.
ねこ も いぬ も すき。|I like both cats and dogs.
みせ は ちかい。|The shop is near.
みち は せまい。|The road is narrow.
あたま は いい。|He's smart.
むすめ は ちいさい。|My daughter is small.
もも は あまい。|Peaches are sweet.
あまい もも。|A sweet peach.
あさ は さむい。|Mornings are cold.
むかし むかし。|Once upon a time.
まち は ちかい。|The town is near.
いま すぐ いく。|I'll go right now.
みみ も はな も ちいさい。|The ears and nose are small too.
さむい あさ。 あたたかい おちゃ。|A cold morning, warm tea.
まめ は ちいさい。|Beans are small.
くも は しろい。|Clouds are white.
やま は たかい。|The mountain is high.
ゆき は つめたい。|Snow is cold.
ふゆ は さむい。|Winter is cold.
やさい は おいしい。|Vegetables are delicious.
へや は せまい。|The room is small.
やすみ は いつ。|When is the holiday?
やさしい ひと。|A kind person.
やすい やさい。|Cheap vegetables.
おゆ は あつい。|The hot water is hot.
やま の うえ。|The top of the mountain.
ゆうひ は あかい。|The sunset is red.
ゆめ の なか。|In a dream.
よこ に すわる。|I sit beside you.
ほん よむ。|I read.
ふゆ の やま。|A mountain in winter.
これ は ねこ。|This is a cat.
それ は いぬ。|That's a dog.
あれ は やま。|That over there is a mountain.
とり は そら に いる。|The bird is in the sky.
よる は くらい。|Nights are dark.
そら は あおい。|The sky is blue.
さくら は きれい。|Cherry blossoms are beautiful.
くるま は はやい。|Cars are fast.
はる は あたたかい。|Spring is warm.
ふろ に はいる。|I get in the bath.
よる に ねる。|I go to bed at night.
あさ おきる。|I get up in the morning.
りす は ちいさい。|Squirrels are small.
これ は いくら。|How much is this?
ひかり は あかるい。|The light is bright.
はれ の ひ。|A sunny day.
わたし は ほん を よむ。|I read a book.
ほん を かう。|I'll buy a book.
わたし の ほん。|My book.
にわ に はな も ある。|There are flowers in the garden too.
かわ は きれい。|The river is clean.
わたし は にほん に いきたい。|I want to go to Japan.
みんな と うたう。|I sing with everyone.
せんせい は やさしい。|The teacher is kind.
おんな の ひと。|A woman.
わかる。|I understand.
わからない。|I don't understand.
てんき は いい。|The weather is good.
わたし も いく。|I'm going too.
おかね を わすれた。|I forgot my money.
みかん を ふたつ かう。|I'll buy two mandarins.
わたし の なまえ は はな。|My name is Hana.
にほん の はる は あたたかい。|Spring in Japan is warm.
せんせい に ほん を かりた。|I borrowed a book from the teacher.
にわとり は あさ なく。|Chickens crow in the morning.
わに は こわい。|Crocodiles are scary.
あかい いえ。|A red house.
おおきい いけ。|A big pond.
あおい かお。|A pale face.
ここ。|Here.
あおい うえ。|The blue above.
おいしい すし。|Delicious sushi.
あかい かさ。|A red umbrella.
おおきい いす。|A big chair.
すこし あつい。|It's a little hot.
おいしい すいか。|A delicious watermelon.
あさ。 さむい。|Morning. It's cold.
ちいさい つくえ。|A small desk.
たかい とけい。|An expensive clock.
あつい おちゃ。|Hot tea.
ちかい えき。|A nearby station.
とおい うち。|A faraway home.
ちいさい ねこ。|A small cat.
おおきい いぬ。|A big dog.
あつい なつ。|A hot summer.
きたない くつ。|Dirty shoes.
ねこ が すき。|I like cats.
これ は ほん です。|This is a book.
それ は はし です。|Those are chopsticks.
はな は きれい です。|The flowers are pretty.
ひと が おおい。|There are a lot of people.
ねこ は ちいさい。|The cat is small.
いぬ は おおきい。|The dog is big.
あの ひと は せんせい です。|That person is a teacher.
わたし は がくせい です。|I'm a student.
ここ は えき です。|This is the station.
あそこ は うみ です。|Over there is the sea.
そこ に いす が あります。|There's a chair there.
あさ は さむい です。|Mornings are cold.
なつ は あつい です。|Summer is hot.
ふゆ は さむい です。|Winter is cold.
はる は あたたかい です。|Spring is warm.
あき は すずしい です。|Autumn is cool.
そら が あおい。|The sky is blue.
うみ が きれい です。|The sea is beautiful.
やま が たかい です。|The mountain is high.
ゆき が ふって います。|It's snowing.
あめ が ふって います。|It's raining.
かぜ が つよい です。|The wind is strong.
きょう は はれ です。|It's sunny today.
あした は くもり です。|It'll be cloudy tomorrow.
つき が きれい です ね。|The moon is beautiful, isn't it?
ほし が たくさん みえる。|You can see lots of stars.
わたし は すし が すき です。|I like sushi.
わたし は ねこ が すき です。|I like cats.
いもうと は いぬ が すき です。|My little sister likes dogs.
あに は さかな が きらい です。|My older brother doesn't like fish.
ちち は おちゃ を のみます。|My father drinks tea.
はは は ほん を よみます。|My mother reads books.
わたし は まいあさ ごはん を たべます。|I eat rice every morning.
まいにち にほんご を べんきょう します。|I study Japanese every day.
ひらがな を かきます。|I write hiragana.
てがみ を かきました。|I wrote a letter.
しんぶん を よみました。|I read the newspaper.
みず を ください。|Water, please.
おちゃ を ください。|Tea, please.
これ を ください。|I'll take this, please.
すみません、 えき は どこ です か。|Excuse me, where is the station?
おてあらい は どこ です か。|Where is the toilet?
いま なんじ です か。|What time is it now?
これ は なん です か。|What is this?
あの ひと は だれ です か。|Who is that person?
なまえ は なん です か。|What's your name?
わたし の なまえ は さくら です。|My name is Sakura.
おなまえ は。|And your name?
はじめまして。 よろしく おねがい します。|Nice to meet you.
おはよう ございます。|Good morning.
こんにちは。 おげんき です か。|Hello. How are you?
はい、 げんき です。|Yes, I'm fine.
ありがとう ございます。|Thank you very much.
どう いたしまして。|You're welcome.
ごめんなさい。|I'm sorry.
いただきます。|Let's eat.
ごちそうさま でした。|Thank you for the meal.
おやすみ なさい。|Good night.
いって きます。|I'm off.
いって らっしゃい。|Have a good day.
ただいま。|I'm home.
おかえり なさい。|Welcome home.
また あした。|See you tomorrow.
きを つけて ね。|Take care.
がんばって ください。|Good luck.
だいじょうぶ です か。|Are you all right?
わかりません。|I don't understand.
もう いちど おねがい します。|Once more, please.
ゆっくり はなして ください。|Please speak slowly.
いっしょに いきましょう。|Let's go together.
すこし まって ください。|Please wait a moment.
ここ に すわって ください。|Please sit here.
まど を あけて ください。|Please open the window.
でんき を けして ください。|Please turn off the light.
てを あらって ください。|Please wash your hands.
くつ を ぬいで ください。|Please take off your shoes.
なまえ を かいて ください。|Please write your name.
しゃしん を とって も いい です か。|May I take a photo?
ここ で たべて も いい です か。|May I eat here?
ねこ が ねて います。|The cat is sleeping.
いぬ が はしって います。|The dog is running.
こども が あそんで います。|The children are playing.
とり が ないて います。|A bird is singing.
はな が さいて います。|The flowers are blooming.
さくら が きれい に さいた。|The cherry blossoms bloomed beautifully.
かわ に さかな が いる。|There are fish in the river.
にわ に き が あります。|There's a tree in the garden.
へや に ねこ が います。|There's a cat in the room.
つくえ の うえ に ほん が ある。|There's a book on the desk.
いす の した に いぬ が いる。|There's a dog under the chair.
はこ の なか に りんご が あります。|There are apples in the box.
えき の まえ に みせ が あります。|There's a shop in front of the station.
がっこう の うしろ に やま が ある。|There's a mountain behind the school.
こうえん は えき の ちかく です。|The park is near the station.
うち から がっこう まで あるきます。|I walk from home to school.
でんしゃ で かいしゃ に いきます。|I go to work by train.
じてんしゃ で こうえん に いった。|I went to the park by bike.
くるま で うみ へ いきました。|We went to the sea by car.
ひこうき で にほん へ いきたい。|I want to go to Japan by plane.
らいねん にほん に いきます。|I'm going to Japan next year.
きのう ともだち に あいました。|I met a friend yesterday.
あした えいが を みます。|I'll see a film tomorrow.
しゅうまつ は なに を します か。|What are you doing at the weekend?
にちようび は やすみ です。|Sunday is my day off.
きょう は いそがしい です。|I'm busy today.
あした は ひま です。|I'm free tomorrow.
すこし つかれました。|I'm a bit tired.
おなか が すきました。|I'm hungry.
のど が かわきました。|I'm thirsty.
あたま が いたい です。|I have a headache.
ねつ が あります。|I have a fever.
かぜ を ひきました。|I've caught a cold.
くすり を のんで ください。|Please take the medicine.
はやく ねて ください。|Please go to bed early.
よく ねむれました か。|Did you sleep well?
あさごはん を たべました か。|Did you have breakfast?
ひるごはん は おにぎり でした。|Lunch was rice balls.
ばんごはん は なに に する。|What shall we have for dinner?
この りんご は あまい です。|This apple is sweet.
この おちゃ は にがい です。|This tea is bitter.
この からし は からい。|This mustard is hot.
みそしる が おいしい です。|The miso soup is delicious.
すし と さしみ が すき です。|I like sushi and sashimi.
たまご を みっつ かいました。|I bought three eggs.
ぱん と ぎゅうにゅう を かった。|I bought bread and milk.
やさい を たくさん たべましょう。|Let's eat lots of vegetables.
くだもの は なに が すき です か。|What fruit do you like?
いちご が いちばん すき です。|I like strawberries best.
この ほん は おもしろい です。|This book is interesting.
にほんご は むずかしい です か。|Is Japanese difficult?
ひらがな は かんたん です。|Hiragana is easy.
かんじ は すこし むずかしい。|Kanji are a little difficult.
まいばん すこし べんきょう します。|I study a little every evening.
ことば を たくさん おぼえたい。|I want to learn lots of words.
この ことば の いみ は なん です か。|What does this word mean?
せんせい に しつもん しました。|I asked the teacher a question.
しけん は あした です。|The exam is tomorrow.
しゅくだい を わすれました。|I forgot my homework.
としょかん で ほん を かりました。|I borrowed a book at the library.
ともだち と えいが を みた。|I watched a film with a friend.
いもうと と こうえん で あそびました。|I played in the park with my little sister.
おとうと は やきゅう が すき です。|My little brother likes baseball.
あね は うた が じょうず です。|My older sister is good at singing.
ちち は りょうり が へた です。|My father is bad at cooking.
はは は やさしい ひと です。|My mother is a kind person.
そふ は ろくじゅう さい です。|My grandfather is sixty.
かぞく は よにん です。|There are four people in my family.
わたし は ひとりっこ です。|I'm an only child.
いぬ を かって います。|I have a dog.
ねこ が にひき います。|I have two cats.
うさぎ は にんじん が すき。|Rabbits like carrots.
ぞう は はな が ながい。|Elephants have long noses.
きりん は くび が ながい です。|Giraffes have long necks.
さる が き に のぼった。|The monkey climbed the tree.
かめ は ゆっくり あるく。|Turtles walk slowly.
うま は はやく はしる。|Horses run fast.
くじら は うみ に すんで いる。|Whales live in the sea.
ほたる が ひかって います。|The fireflies are glowing.
せみ が ないて いる。 もう なつ だ。|The cicadas are singing. It's summer now.
とんぼ が とんで いる。|A dragonfly is flying.
あり は ちいさい けど つよい。|Ants are small but strong.
この みせ は やすくて おいしい。|This shop is cheap and good.
あの みせ は いつも こんで いる。|That shop is always crowded.
この かばん は いくら です か。|How much is this bag?
すこし たかい です ね。|It's a bit expensive, isn't it?
もう すこし やすい の は あります か。|Do you have anything a bit cheaper?
この ふく を きて みて も いい です か。|May I try on these clothes?
あかい の と あおい の、 どちら が いい。|Which is better, the red one or the blue one?
あおい ほう が すき です。|I prefer the blue one.
ぼうし を かぶって でかけた。|I put on a hat and went out.
めがね を なくしました。|I've lost my glasses.
かぎ が みつかりません。|I can't find my key.
さいふ を わすれました。|I forgot my wallet.
でんわ ばんごう を おしえて ください。|Please tell me your phone number.
あとで でんわ します。|I'll call you later.
てがみ を ありがとう。|Thanks for your letter.
たんじょうび おめでとう。|Happy birthday.
あけまして おめでとう ございます。|Happy New Year.
おまつり に いきません か。|Won't you come to the festival?
はなび を みに いこう。|Let's go and see the fireworks.
ゆかた を きて おまつり に いった。|I wore a yukata and went to the festival.
なつやすみ に うみ で およいだ。|I swam in the sea during the summer holidays.
ふゆやすみ に ゆきだるま を つくった。|I made a snowman in the winter holidays.
はる に なったら はなみ を しよう。|Let's go cherry-blossom viewing when spring comes.
あき は もみじ が きれい です。|The autumn leaves are beautiful in autumn.
きょう は とても さむい ね。|It's really cold today, isn't it?
まど の そと は まっしろ だ。|It's all white outside the window.
こども たち が ゆきだるま を つくった。|The children made a snowman.
あめ が やんだら でかけましょう。|Let's go out once the rain stops.
かさ を もって いった ほう が いい。|You'd better take an umbrella.
にじ が でて いる。|There's a rainbow.
かみなり が こわい です。|I'm scared of thunder.
たいふう が きて います。|A typhoon is coming.
あした は はれる と いい ね。|I hope it'll be sunny tomorrow.
まいあさ ろくじ に おきます。|I get up at six every morning.
よる じゅういちじ に ねます。|I go to bed at eleven at night.
しちじ に いえ を でます。|I leave the house at seven.
くじ から ごじ まで はたらきます。|I work from nine to five.
ひるやすみ は いちじかん です。|Lunch break is one hour.
しごと の あと で ともだち に あう。|I'm meeting a friend after work.
いえ に かえって ごはん を つくる。|I go home and cook.
おふろ に はいって から ねます。|I take a bath and then go to bed.
にちようび は ゆっくり やすみたい。|I want to rest on Sunday.
てんき が いい から さんぽ しよう。|The weather's nice, so let's go for a walk.
こうえん に はな が たくさん さいて いる。|Lots of flowers are blooming in the park.
いぬ と いっしょに はしりました。|I ran together with the dog.
やまのぼり は たのしかった。|Mountain climbing was fun.
うみ で かい を ひろいました。|I picked up shells at the beach.
すなはま を あるく の が すき。|I like walking on the sandy beach.
かわ で さかな を つった。|I caught fish in the river.
もり の なか は しずか だった。|It was quiet in the forest.
みずうみ に ふね が うかんで いる。|A boat is floating on the lake.
しま に いく ふね は いっぽん だけ。|There's only one boat to the island.
むかし むかし、 ある ところ に おじいさん と おばあさん が いました。|Once upon a time, in a certain place, there lived an old man and an old woman.
おじいさん は やま へ しばかり に いきました。|The old man went to the mountains to gather firewood.
おばあさん は かわ へ せんたく に いきました。|The old woman went to the river to do the washing.
かわ から おおきな もも が ながれて きました。|A big peach came floating down the river.
もも の なか から あかちゃん が うまれました。|A baby was born from inside the peach.
うさぎ と かめ が かけっこ を しました。|The hare and the tortoise had a race.
うさぎ は とちゅう で ねて しまいました。|The hare fell asleep on the way.
かめ は やすまず に あるきつづけました。|The tortoise kept walking without resting.
さいご に かった の は かめ でした。|In the end, the tortoise won.
きつね が ぶどう を みつけました。|A fox found some grapes.
ぶどう は たかい ところ に ありました。|The grapes were high up.
ねずみ が ちいさな あな に かくれた。|The mouse hid in a little hole.
つる が そら を とんで いきました。|A crane flew away across the sky.
ありがとう、 と つる は いいました。|"Thank you," said the crane.
わたし の ゆめ は せんせい に なる こと です。|My dream is to become a teacher.
いつか にほん に すみたい です。|Someday I want to live in Japan.
にほん の たべもの が だいすき です。|I love Japanese food.
にほんご で てがみ を かきたい。|I want to write a letter in Japanese.
ひらがな が ぜんぶ よめる よう に なった。|I've learned to read all the hiragana.
まいにち すこし ずつ れんしゅう しよう。|Let's practise a little every day.
まちがえて も だいじょうぶ。|It's fine to make mistakes.
ゆっくり で いい から つづけよう。|Slowly is fine — let's keep going.
きょう も よく がんばりました。|You worked hard again today.
あたらしい ことば を みっつ おぼえた。|I learned three new words.
この もじ は かく の が むずかしい。|This character is hard to write.
もう いちど かいて みよう。|Let's try writing it once more.
きれい な じ を かきたい。|I want to write neat characters.
えんぴつ と けしごむ を かして。|Lend me a pencil and an eraser.
かみ に ひらがな を かいた。|I wrote hiragana on paper.
せんせい が ほめて くれました。|The teacher praised me.
ともだち が てつだって くれた。|My friend helped me.
いもうと に ほん を よんで あげた。|I read a book to my little sister.
みんな で しゃしん を とりましょう。|Let's all take a photo together.
また あいましょう。|Let's meet again.
たのしかった です。 また きて ね。|It was fun. Come again.
きを つけて かえって ね。|Get home safely.
あした も がんばろう。|Let's do our best tomorrow too.
"""

# Notes for each kana: (mnemonic, how to write it, lookalikes to watch)
KANA = {
    "あ": ("An Apple with a stalk: a cross, then a big loop like the curve of an apple.", "1 short horizontal line; 2 long vertical line, curving slightly left at the bottom; 3 a big loop that starts top-middle, crosses the vertical and sweeps round to the right.", "お (no cross at the top, the dot sits outside), め (no horizontal line)"),
    "い": ("Two Eels side by side: i-i.", "1 the left stroke, longer, with a small hook up at the end; 2 the right stroke, shorter and slightly lower. Leave a clear gap between them.", "り (the right stroke is much longer), こ (horizontal strokes)"),
    "う": ("A person bending over with an 'Ugh' — a dot of a head and a hooked body.", "1 a short slanted dash at the top; 2 a curve that goes right, then sweeps down and to the left like a hook.", "つ (no dot on top), ら (the dot and a vertical start)"),
    "え": ("An Exotic bird with a feather on top and a zigzag tail.", "1 a short dash on top; 2 one stroke: across, down-left, then a small zigzag ending in a flowing tail to the right.", "ん (no dash on top), る / ろ"),
    "お": ("An Ostrich-like figure: a cross, a loop and a feather (the dot) on the right.", "1 horizontal line; 2 vertical line that loops round to the right and back left at the bottom; 3 a small dot top right.", "あ (loop crosses differently, no outside dot), す"),
    "か": ("A Karate blade with a little 'ka!' shout mark.", "1 a horizontal line that bends down into a hook; 2 a vertical-ish stroke crossing it, slightly slanted left; 3 a short dash to the upper right.", "や (different first stroke), が (with ゛)"),
    "き": ("A Key: two cross bars and a hooked bottom.", "1 and 2 two horizontal bars, the lower one a little longer; 3 a slanted vertical through both; 4 a separate curve at the bottom like the bit of a key. (Some fonts join 3 and 4.)", "さ (only one cross bar), ち (bottom curve opens the other way)"),
    "く": ("A beak going 'Coo-coo': one sharp < angle.", "One stroke: from the top, down-left to the point, then down-right. Keep the angle sharp.", "へ (wider, lies flat), し"),
    "け": ("A Keg next to a tap: a vertical line and a little cross with a hooked leg.", "1 a vertical line on the left with a tiny hook; 2 a short horizontal on the right; 3 a long vertical crossing it, curving down-left at the end.", "は (has a loop), に"),
    "こ": ("Two Koi carp swimming one above the other.", "1 a short upper line ending with a small downward flick; 2 a slightly longer lower line curving up at the end.", "い (vertical), に"),
    "さ": ("A Samurai's sword over a little shield.", "1 a horizontal line; 2 a slanted stroke crossing it from top left down; 3 a separate curve at the bottom opening to the right. (Handwriting often joins 2 and 3.)", "き (two cross bars), ち (bottom curve opens left)"),
    "し": ("A fishing hook — 'Shhh', the fish is biting.", "One stroke: straight down, then curve right and up.", "つ, く, ん"),
    "す": ("A Swing with a loop.", "1 a long horizontal line; 2 a vertical that makes a small loop below the line, then sweeps down-left.", "む (extra dot, loop goes right), お"),
    "せ": ("Say it with a Smile: a cross with a long hooked leg.", "1 a long horizontal; 2 a short vertical on the right ending with a hook; 3 a long vertical on the left that curves right at the bottom.", "さ, も"),
    "そ": ("A zigzag Sewing thread.", "One stroke: a small zigzag at the top, then a long curve down to the left and round. (Often written as two strokes: the dash on top separately.)", "ろ, る"),
    "た": ("A Taco: the letters t and a.", "1 horizontal; 2 slanted vertical crossing it; 3 and 4 two short lines like こ on the right.", "な (a loop at the bottom right), に"),
    "ち": ("A Cheerleader with a curved body.", "1 a horizontal line; 2 a vertical that bends and makes a big curve opening to the left at the bottom.", "さ (curve opens right), ら"),
    "つ": ("A Tsunami wave.", "One stroke: across, then curving down and back to the left.", "う (has a dot on top), し"),
    "て": ("A Tennis racket handle, or 'te' for the shape of a 7.", "One stroke: across, then down in a curve to the left.", "そ, ひ"),
    "と": ("A Toe with a splinter in it.", "1 a short slanted stroke; 2 a curve that starts top left and sweeps down and right.", "こ, そ"),
    "な": ("A Nun praying at a cross, with a knot at the bottom.", "1 horizontal; 2 slanted vertical; 3 a short dash top right; 4 a vertical that ends in a small loop.", "た (no loop), ふ"),
    "に": ("A Knee next to two lines — like 'ni' = こ with a stick.", "1 a vertical with a small hook; 2 and 3 two short horizontals on the right, like こ.", "け, こ, た"),
    "ぬ": ("Noodles with a loop at the end (め has no loop).", "1 a short slanted stroke; 2 a long curve that crosses it and ends in a little loop at the bottom right.", "め (no loop at the end), ね, る"),
    "ね": ("A Nekko (cat) curled up, with its tail looping.", "1 a vertical line; 2 a zigzag that goes right, round, and ends in a loop.", "れ (ends with a kick, not a loop), わ (ends in a big curve), ぬ"),
    "の": ("A 'No' sign: one round swirl.", "One stroke: down a little, then round anticlockwise in a big circle.", "め, ゆ, あ"),
    "は": ("A Ha-ha laugh: a vertical next to a little loop-cross.", "1 vertical on the left; 2 short horizontal; 3 vertical that ends in a loop.", "ほ (two horizontals), け (no loop)"),
    "ひ": ("A big smile: 'Hee hee!'", "One stroke: a short flick, a wide U-shaped smile, then a flick up at the right.", "て, い"),
    "ふ": ("Mount Fuji with clouds: a dot, a curve and two dots.", "1 a small dash on top; 2 a curve in the middle; 3 and 4 two dots, left and right.", "ら, う"),
    "へ": ("A Hill: one gentle ^ shape.", "One stroke: up a little, then a long slope down to the right.", "く (pointed sideways). Written the same in katakana (ヘ)."),
    "ほ": ("A Ho-ho Santa: は with an extra top bar.", "1 vertical left; 2 and 3 two horizontals; 4 vertical with a loop at the bottom.", "は (one horizontal), ま"),
    "ま": ("A Mama with a loop: two cross bars and a loop.", "1 and 2 two horizontals; 3 a vertical that loops at the bottom.", "ほ (has a separate left vertical), よ"),
    "み": ("A Me-21: looks like the number 21 with a swirl.", "1 a zigzag that ends in a loop, then a long line to the right; 2 a short slanted stroke crossing it on the right.", "よ, め"),
    "む": ("A cow saying 'Moo' with a loop and a dot.", "1 horizontal; 2 vertical that loops and sweeps right; 3 a small dot top right.", "す (no dot), お"),
    "め": ("An Eye (me) — like ぬ but with no loop at the end.", "1 a short slanted stroke; 2 a long curve that crosses it and ends without a loop.", "ぬ (loop at the end), あ, の"),
    "も": ("Fishhook with MOre bait: a hook with two bars.", "1 a vertical curve, hooked at the bottom to the right; 2 and 3 two horizontal bars across it.", "し, せ"),
    "や": ("A Yak with horns.", "1 a curve from top left that bends down; 2 a short dash top right; 3 a long slanted vertical through the middle.", "か, ゆ"),
    "ゆ": ("A Unique fish (yu) with a fin through it.", "1 a vertical-ish stroke that loops round to the right; 2 a vertical crossing the loop.", "や, の"),
    "よ": ("A Yo-yo on a string.", "1 a short horizontal on the right; 2 a vertical that ends in a loop.", "ま (two bars), ほ"),
    "ら": ("A Rabbit's ear: a dash and a curl.", "1 a short dash on top; 2 a vertical that curves round to the right and back left at the bottom.", "う, ち, ろ"),
    "り": ("A Reed: two strokes, the right one long.", "1 a short left stroke with a hook; 2 a long right stroke curving down. (Often joined into one stroke.)", "い (strokes the same length)"),
    "る": ("A Route with a loop at the end.", "One stroke: a zigzag that ends in a small loop at the bottom.", "ろ (no loop), ぬ"),
    "れ": ("A Ray kicking out its leg.", "1 vertical line; 2 a zigzag that ends with a kick to the right.", "ね (loop), わ (curve)"),
    "ろ": ("A Road with no loop at the end (る has one).", "One stroke: a zigzag that ends in an open curve.", "る (loop at the end)"),
    "わ": ("A Wasp's wing: a vertical and a big curve.", "1 vertical line; 2 a zigzag that ends in a big rounded curve.", "ね (loop), れ (kick)"),
    "を": ("A wobbly 'Whoa!': a cross and a z.", "1 horizontal; 2 a slanted stroke that zigzags; 3 a curve at the bottom right like a backwards c.", "お, ち. Used almost only as the object particle, read 'o'."),
    "ん": ("A cursive N.", "One stroke: down-left, then up and over in a small hump with a tail.", "そ, し"),
}

# Common questions the tutor used to answer, answered in advance.
FAQ = [
    ("How do I tell ぬ and め apart?", "Both cross a short slanted stroke with a long curve. ぬ ends with a little loop at the bottom right; め does not. Remember: 'noodles' (nu) have a loop, an 'eye' (me) doesn't."),
    ("How do I tell ね, れ and わ apart?", "All three start with a vertical line. ね ends in a loop (like a cat's curled tail), れ ends with a kick to the right, わ ends in a big rounded curve."),
    ("How do I tell る and ろ apart?", "Same zigzag; る finishes with a little loop, ろ stays open."),
    ("How do I tell さ and ち apart?", "Look at the bottom curve: in さ it opens to the right, in ち it opens to the left (like a backwards c)."),
    ("How do I tell は, ほ and ま apart?", "は and ほ have a separate vertical line on the left; ほ has two horizontal bars, は one. ま has no left line — just two bars and a loop."),
    ("Why is は sometimes read 'wa'?", "When は is the topic particle (わたし は …), it's pronounced wa. In normal words like はな (flower) it's ha. In the same way へ as a direction particle is read e, and を is read o."),
    ("What are ゛ and ゜?", "The two ticks ゛ (dakuten) voice a sound: か→が, さ→ざ, た→だ, は→ば. The little circle ゜ (handakuten) only goes on the h-row: は→ぱ. Both are written last, at the top right."),
    ("What does the small っ do?", "A small っ doubles the next consonant — a short pause before it: きって (kitte, stamp), ちょっと (chotto). It's written smaller and lower in the box."),
    ("What are small ゃ, ゅ, ょ?", "They combine with an i-sound kana to make one syllable: き+ゃ = きゃ (kya), し+ょ = しょ (sho), ち+ゅ = ちゅ (chu). Write them about half size, low in the box."),
    ("How are long vowels written in hiragana?", "With an extra vowel: おかあさん (okaasan), おにいさん, くうき, おねえさん. A long o is usually written おう (ありがとう), sometimes おお (おおきい, とおい). The dash ー is only used in katakana."),
    ("Why does stroke order matter?", "Correct order makes characters look balanced, helps you write fast without lifting the pen too often, and makes handwriting readable to others. It also helps you remember the shape."),
    ("Which way should strokes go?", "Generally top to bottom and left to right. Horizontal lines go left→right, vertical lines top→bottom, and loops in のめぬ go anticlockwise."),
    ("How big should a character be?", "Fill most of the box — about 80% — with the centre of the character near the centre of the box. Small kana (っゃゅょ) are about half size, in the lower left."),
    ("What is the difference between hiragana and katakana?", "Both write the same sounds. Hiragana is for Japanese words and grammar endings; katakana (ア, カ, サ …) is mainly for foreign words like コーヒー. Kanji carry the meaning of most words."),
    ("Why is を only used in one place?", "Modern Japanese uses を only as the object particle (ほん を よむ, read a book), pronounced o. The word for 'tail', for example, is お, not を."),
    ("How do I write ん?", "One flowing stroke: down to the left, then up and over in a small hump, ending with a little tail to the right. It never starts a word."),
    ("Is the っ in a word pronounced?", "Not as a sound of its own — it's a tiny stop. Clap it: き・っ・て has three beats, and the middle one is silent."),
    ("How should I practise?", "Little and often: 10 minutes a day beats an hour once a week. Write each new kana a few times while saying it aloud, then use it in words straight away, and come back to old ones from memory."),
    ("Why do some fonts look different from handwriting?", "Printed fonts join or separate some strokes: き, さ, そ, り and ふ often look slightly different in type. When you write by hand, follow the stroke order shown in the dojo."),
    ("What does 'Word path' do?", "It gives you whole words from memory, one kana row at a time. Clear six words without peeking at the guide to unlock the next row."),
]
