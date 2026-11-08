# Traducción al español: guía de estilo y glosario

El texto en español está en `es/*.json`, un archivo por cada archivo de `ja/`,
con exactamente las mismas claves, tipos de valor y longitudes de array. Se traduce desde el
japonés original; el inglés (`en/`) sirve de referencia para el sentido y para ver cómo
se han resuelto los marcadores. Los marcadores (`{player}`, `{enemy}`, `{value}`...) se conservan
tal cual y pueden cambiar de posición en la frase. Comprobación: `py tools/check_translation.py es`.

## Estilo

- Español de España, nivel profesional: ortografía y puntuación correctas (¡! ¿?, tildes,
  comillas «»), pero con el tono del original. No es un texto formal: lo escribió un niño y es
  desenfadado, con bromas, gritos exagerados, el autor hablando con el jugador y rompiendo la
  cuarta pared. Mantén esa voz con un español natural, ni rígido ni calcado del japonés.
- Se juega de oído: cada cadena la lee un lector de pantalla. Frases claras, nada que dependa de
  lo visual, sin emojis ni arte ASCII. Evita abreviaturas ambiguas.
- Al jugador se le trata de tú. Los personajes se tratan según su relación (el policía puede
  tratar de tú al protagonista; un niño al policía, de usted, etc.).
- El protagonista ({player}, «僕») es un chico: concordancia en masculino.
- Alargamientos (うわぁぁぁぁ, ひえええ): equivalentes españoles cortos («¡Aaaah!», «¡Uaaah!»,
  «¡Iiiih!»). No más de 4-5 letras repetidas: el lector de pantalla las deletrea.
- (笑) / (笑い) -> «(jaja)»; (爆) -> «(JAJAJA)»; (待て) -> «(¿pero qué?)».
- Juegos de palabras intraducibles: sustitúyelos por una broma española del mismo espíritu o
  tradúcelos con naturalidad. Nunca dejes texto japonés.
- Menús en minúscula inicial de frase: «Ver estado», «Cerrar menú».
- Los contadores japoneses (個, 本, 枚...) desaparecen: «3 bolas de arroz».
- Dinero: 円 -> «yenes» («120 yenes»; «1 yen»).
- Etiquetas de hablante: «Nombre: texto», igual que en el japonés («闇人:...» -> «Yamijin: ...»).
- Antes de decidir artículos o géneros en cadenas que el código une con otras (nombres de
  objetos, enemigos, unidades), mira en `src/` cómo se montan.

## Nombres

| Japonés | Español |
|---|---|
| 僕らの大冒険〜闇の中の野望〜 | Nuestra gran aventura: Ambición en la oscuridad |
| 闇人 / 闇人さま | Yamijin / el señor Yamijin |
| la muletilla にゃ de 闇人 | «nya» |
| ヨコタンク / ヨコタンクの砦 | Yokotank / la Fortaleza de Yokotank |
| クリスタルシティー | Ciudad Cristal |
| アークハイアシティー | Ciudad Arkhaia |
| アークハイアデパート | Grandes Almacenes Arkhaia |
| フレイムタウン / フレイムマウンテン | Pueblo Llama / Monte Llama |
| 仲良し公園 | Parque de la Amistad |
| 邪悪なる館 | la Mansión del Mal |
| なぞの建物 / なぞの家 | el Edificio Misterioso / la Casa Misteriosa |
| 未知の地 | la Tierra Desconocida |
| 民家 | una casa (la casa de alguien) |
| 秘密倉庫 | el almacén secreto |
| 〜を出たところ (nombres de lugar) | A la salida de... |
| Normal mode / Hell mode / No future mode (ヘルモード...; modos de dificultad) | modo normal / modo infierno / modo sin futuro (todo en minúscula) |

## Personajes y etiquetas

| Japonés | Español |
|---|---|
| 仲間 1/3 / 仲間 2 / 仲間たち | Amigo 1 / Amigo 3 / Amiga 2 (es una chica) / los amigos |
| 子供 / こども | Niño (Niña si es una chica) |
| 家の人 | Vecino (Vecina si es una mujer) |
| 宿の人 | Recepcionista |
| 商人 | Mercader |
| ??? / ？？？ | Alguien (el lector leería «interrogación» tres veces) |
| 作者 | Autor |
| 警察官 | Policía |
| 旅人 / 旅人 2 | Viajero / Viajera 2 (es una mujer) |
| ジェイド (el perro del viajero) | Jade |

## Enemigos

| Japonés | Español |
|---|---|
| ガキ少年 / ガキ | Mocoso |
| パワフルガキ少年 / スーパーガキ少年 / ウルトラガキ少年 | Mocoso Fortachón / Supermocoso / Ultramocoso |
| スパルタガキ少年 / マスターガキ少年 | Mocoso Espartano / Mocoso Maestro |
| チビスライム / ビッグスライム / パワースライム / ファストスライム | Minislime / Slime Grande / Slime Fuerte / Slime Veloz |
| ドラゴンs / ドラゴンM | Dragón S / Dragón M |
| コーモリ | Murciélago |
| グランドクルーザー / グランドクルーザー Ⅱ | Gran Crucero / Gran Crucero II |
| 小悪魔 / 小悪魔メカ | Diablillo / Diablillo Mecánico |
| メガザウルス | Megasaurio |
| デスロボット | Robot de la Muerte |
| ビームマシーン | Máquina de Rayos |
| kissenon / クロロ | kissenon / Kuroro |

## Armas, protecciones y estadísticas

| Japonés | Español |
|---|---|
| ハンマー / パチンコ / パチンコの玉 | Martillo / Tirachinas / bola de tirachinas |
| ショートソード / ロングソード | Espada Corta / Espada Larga |
| 鞭 / ブロンズナイフ / バスターブレード | Látigo / Cuchillo de Bronce / Espada Destructora |
| アローショット / ナックル | Lanzaflechas / Nudilleras |
| たらい / 大きいたらい / ガラス盤 / アルミ板 / 鋼鉄 / レーザーシールド | Barreño / Barreño Grande / Placa de Cristal / Plancha de Aluminio / Acero / Escudo Láser |
| HP / スタミナ | PV / Aguante |
| 攻撃力 / 防御力 / 素早さ / 体力 | Ataque / Defensa / Velocidad / Vitalidad |
| 経験値 / レベル / 所持金 | Experiencia / Nivel / Dinero |

## Objetos

Los nombres de `items.json` llevan mayúscula inicial en cada palabra significativa porque se leen
como nombres en listas, tiendas y botines; en el texto corrido, minúscula («he encontrado un
bollo»).

| Japonés | Español |
|---|---|
| おにぎり / おむすび / 巨大おにぎり | Bola de Arroz / Bola de Arroz Gigante |
| まつたけ / マツタケ | Seta Matsutake |
| 光のかけら / 光の欠片 | Fragmento de Luz |
| 赤い/青い/黄色い欠片 (Edificio Misterioso) | fragmento rojo / azul / amarillo |
| 菓子パン / つぶれた菓子パン | Bollo / Bollo Aplastado |
| サボンの実 / サボンの木 | Fruto de Sabón / árbol de sabón |
| トンカツ弁当 | Bento de Tonkatsu |
| タマゴサンド / ハムサンド | Sándwich de Huevo / Sándwich de Jamón |
| スポーツドリンク / スタミナドリンク / スーパードリンク / メガスタミナドリンク | Bebida Isotónica / Bebida Energética / Superbebida / Megabebida Energética |
| フレッシュボトル / フレッシュスター | Botella Fresca / Estrella Fresca |
| 回復薬 / 命の草 / 不思議なお香 | Poción / Hierba Vital / Incienso Misterioso |
| 命の欠片 / 命の結晶 / 伝説の秘薬 | Fragmento Vital / Cristal Vital / Elixir Legendario |
| やさしい木漏れ日 | Luz entre las Hojas |
| 鉄球 / ワープパネル | Bola de Hierro / Panel de Teletransporte |
| 赤い/青い/黄色い/緑の/七色のマーカー (se colocan en el suelo como señal) | Marcador Rojo / Azul / Amarillo / Verde / Arcoíris |

Las entradas de objetos se leen como «{name}, {count}{unit}. {desc}». Las unidades en español son
"" salvo " kg", " puntos" y equivalentes: escribe la unidad con su espacio inicial.

## Añadidos durante la primera traducción

| Japonés | Español |
|---|---|
| 人 N / 人 | Persona N / Persona (Cliente en las tiendas) |
| 店員 | Dependiente (Camarero en el restaurante) |
| 兵士 / お嬢様 / 少女 | Soldado / Señorita / Chica |
| タバコを吸っている男 | Hombre fumando |
| 雄介 | Yusuke |
| 設定 | Ajustes |
| 防具 / 防具の変更 | protección / Cambiar protección |
| ひるむ (estado en combate) | aturdido / aturdimiento |
| 中ボス | minijefe |
| 記憶の道 | el Camino de los Recuerdos |
| お仕置部屋 | el cuarto de castigo |
| マンホール | alcantarilla |
| ダークルームキー | Llave de la Sala Oscura |
| アイアンアロー | Flechas de Hierro |
| 食料略奪計画 | Plan de saqueo de comida |
| ゲーセン / UFOキャッチャー / プリクラ / ジュークボックス | los recreativos / máquina de gancho / fotomatón / gramola |
| 1階, 2階... (Grandes Almacenes) | planta baja, primera planta... |
| 1u4l2u7r... (código de la roca del almacén) | se deja igual (u/l/r/d = arriba/izquierda/derecha/abajo) |

Los nombres de enemigos se insertan sin artículo (`{enemy}`): redacta esas frases para que el
nombre funcione solo («Enemigo derrotado: {enemy}.», «Botín de {enemy}: {item}.»).

El documento cifrado de `omake3.docs[0]` (story_end.json) es `cheat.code.author_on` de menu.json
al revés, con «/» en lugar de espacios: si cambia el truco, hay que regenerarlo.

Quien introduzca un nombre recurrente nuevo lo añade a estas tablas.
