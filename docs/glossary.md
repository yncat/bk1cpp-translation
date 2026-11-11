# English translation: style guide and glossary

The English text lives in `en/*.json`, one file per Japanese file in `ja/`,
with exactly the same keys (a test enforces this). Placeholders such as `{player}`, `{enemy}`,
`{value}` must be kept unchanged; they may move within the sentence.

## Style

- The game is played by ear: every string is read aloud by a screen reader. Write for the ear.
  Short sentences, no visual-only jokes, no ASCII art, no emoji. Avoid ambiguous abbreviations.
- The original was written by a child. Keep its voice: casual, cheeky, silly, fourth-wall
  jokes, the author talking to the player ("the author got lazy"), exaggerated screams.
  Do not make it formal or polished, but do write correct, natural English.
- Elongations (うわぁぁぁぁ, ひえええええ) become English equivalents ("Waaaaah!", "Eeeeek!").
  Keep them reasonably short so they are not tedious to hear (a screen reader spells out long runs).
- Japanese laughter markers: (笑) / (笑い) -> "(lol)"; (爆) -> "(lmao)"; (待て) -> "(wait, what?)".
- Puns that cannot survive: replace with an English joke of the same spirit, or translate plainly.
  Never leave Japanese text in an English string.
- Menu items: Title Case is not needed; use sentence case ("Check status", "Close menu").
- Units/counters (個, 本, 枚...) usually disappear in English: "3 rice balls" not "3 pieces of rice ball".
  If an item table has a separate unit field, use "" or a natural English unit ("kg", "points").
- Money: 円 -> "yen" ("120 yen").
- Item names used as "a/an X" by code? Check how the string is assembled before choosing articles.

## Names

| Japanese | English |
|---|---|
| 僕らの大冒険〜闇の中の野望〜 | Our Great Adventure: Ambition in the Dark |
| 闇人 | Yamijin |
| ヨコタンク | Yokotank |
| ヨコタンクの砦 | Yokotank's Fortress |
| クリスタルシティー | Crystal City |
| アークハイアシティー | Arkhaia City |
| アークハイアデパート | Arkhaia Department Store |
| フレイムタウン / フレイムマウンテン | Flame Town / Flame Mountain |
| 仲良し公園 | Nakayoshi Park |
| 邪悪なる館 | the Evil Mansion |
| なぞの建物 / なぞの家 | the Mystery Building / the Mystery House |
| 未知の地 | the Unknown Land |
| 民家 | a house (someone's house) |
| 秘密倉庫 | secret warehouse |

## Enemies

| Japanese | English |
|---|---|
| ガキ少年 / ガキ (the enemy kind) | Gakishonen |
| パワフルガキ少年 | Powerful Gakishonen |
| スーパーガキ少年 | Super Gakishonen |
| ウルトラガキ少年 | Ultra Gakishonen |
| スパルタガキ少年 | Spartan Gakishonen |
| マスターガキ少年 | Master Gakishonen |
| チビスライム | Tiny Slime |
| ビッグスライム | Big Slime |
| パワースライム | Power Slime |
| ファストスライム | Fast Slime |
| ドラゴンs / ドラゴンM | Dragon S / Dragon M |
| コーモリ | Bat |
| グランドクルーザー / グランドクルーザー Ⅱ | Grand Cruiser / Grand Cruiser II |
| 小悪魔 / 小悪魔メカ | Imp / Mecha Imp |
| メガザウルス | Megasaurus |
| デスロボット | Death Robot |
| ビームマシーン | Beam Machine |
| kissenon | kissenon |
| クロロ | Kuroro |

## Weapons and stats

| Japanese | English |
|---|---|
| ハンマー / パチンコ / ショートソード / ロングソード | Hammer / Slingshot / Short Sword / Long Sword |
| 鞭 / ブロンズナイフ / バスターブレード / アローショット / ナックル | Whip / Bronze Knife / Buster Blade / Arrow Shot / Knuckles |
| HP / スタミナ | HP / Stamina |
| 攻撃力 / 防御力 / 素早さ / 体力 | Attack / Defense / Speed / Vitality |
| 経験値 / レベル / 所持金 | EXP / Level / Money |
| ワープパネル | Warp Panel |
| マーカー (赤い/青い/黄色い/緑の/七色の) | Red / Blue / Yellow / Green / Rainbow Marker |

Translators add new recurring names to this table (in their own branch) when they introduce them.

## Characters, speaker labels and items (added with the first translations)

Speaker labels are written "Name: text".

| Japanese | English |
|---|---|
| 闇人 (one character, no article) / 闇人さま | Yamijin / Lord Yamijin |
| 闇人's にゃ tic | "nya" |
| 仲間 1/2/3 / 仲間たち | Friend 1/2/3 / Friends |
| 子供 / こども | Kid |
| 家の人 | Resident |
| 宿の人 | Hotel staff |
| 商人 | Merchant |
| ??? / ？？？ (unknown speaker) | Someone (a screen reader would read "question mark" three times) |
| 作者 | Author |
| 警察官 | Police officer |
| 旅人 | Traveler |
| ジェイド (the traveler's dog) | Jade |
| おにぎり / おむすび | Rice Ball (item name; "rice balls" in running text) |
| マツタケ | Matsutake Mushroom |
| 光のかけら / 光の欠片 | Light Shard |
| 赤い/青い/黄色い欠片 (mystery building) | red / blue / yellow fragment |
| 菓子パン / つぶれた菓子パン | Sweet Bun / Squashed Sweet Bun |
| サボンの実 / サボンの木 | Sabon Fruit / Sabon tree |
| パチンコの玉 | slingshot pellet |
| スポーツドリンク | Sports Drink |
| 〜を出たところ (location names) | Outside ... |
| 民家 (location name) | A house / Someone's house |
| Normal mode / Hell mode / No future mode | unchanged |

Item names in `items.json` are in Title Case (they are spoken as names in lists, shops and drops):
Rice Ball, Giant Rice Ball, Pork Cutlet Bento, Egg Sandwich, Ham Sandwich, Stamina Drink, Super Drink,
Mega Stamina Drink, Fresh Bottle, Recovery Potion (回復薬), Life Herb (命の草), Mysterious Incense,
Life Shard (命の欠片), Life Crystal (命の結晶), Legendary Elixir, Fresh Star, Gentle Sunbeam
(やさしい木漏れ日), Iron Ball, Warp Panel. Shields: Washtub, Glass Plate, Aluminum Plate, Big Washtub,
Steel, Laser Shield. In running text lower case is fine ("I found a sweet bun").

Item list entries are spoken as "{name}, {count}{unit}. {desc}". English units are "" except
" kg", " points" and " (1000 rounds per box)": write the unit with its leading space.
