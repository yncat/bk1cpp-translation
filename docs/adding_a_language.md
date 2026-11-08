# Adding a language

Each folder `<code>/` of this repository is one language. The game offers every such folder it
finds in its `data/lang/` at startup. No code change or rebuild is needed: a translation can even
be dropped into `data/lang/` next to an installed `bk1.exe`.

1. Copy `en/` (or `ja/`) to `<code>/`. The code is the folder name: 2-3 lowercase letters,
   optionally `-` and 2-8 letters or digits (`de`, `pt-br`, `zh-hant`).
2. Translate the values, never the keys. Keep every `{placeholder}`; it may move in the sentence.
   Arrays must keep their length (each entry is one spoken line or one menu item).
3. Set `"language.name"` in `story.json` to the language's own name ("Deutsch", "Español").
   The language menu speaks it, so players can find their language without understanding the
   current one. A folder without this key is not offered.
4. Keep `settings.entry` and `settings.language` readable for someone who doesn't know your
   language, e.g. "Einstellungen / Settings / 設定" and "Sprache / Language / 言語".
5. Check it: `py tools/check_translation.py <code>` (same keys, value kinds, array lengths and
   placeholders as Japanese; no kana left). The same check runs on every pull request.
6. Try it in the game: copy the folder into `data/lang/` of the latest release
   (https://github.com/yncat/bk1cpp/releases/tag/latest), then start `bk1.exe --lang <code>` or
   choose it in Settings > Language.

At run time a key missing from a translation is read from Japanese, so a partial translation
still runs. In this repository the check requires every language folder to be complete.

The language picked at first start follows the Windows display language when a folder with
that code exists (`de` for German Windows), otherwise English, otherwise Japanese.

`ja/` is the source text and its keys are defined by the game's code, so keys are added or
removed only together with a change of the game. Fixes to the Japanese wording are welcome.

Style and names: see [glossary.md](glossary.md) (written for English; follow its spirit).
