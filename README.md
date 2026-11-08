# bk1cpp-translation

Text of the game 僕らの大冒険 (bk1), one folder per language:

| Folder | Language |
| --- | --- |
| `ja/` | Japanese (source text) |
| `en/` | English |
| `es/` | Español |

Each folder holds the same JSON files with the same keys: `"key": "text"` or
`"key": ["line", "line", ...]`. Translate the values, never the keys, and keep every
`{placeholder}`.

- New language: [docs/adding_a_language.md](docs/adding_a_language.md)
- Style guide and glossary: [docs/glossary.md](docs/glossary.md) (English),
  [docs/glossary_es.md](docs/glossary_es.md) (Español)
- Check before opening a pull request (Python 3, no packages needed):

  ```
  py tools/check_translation.py          # every language
  py tools/check_translation.py es -v    # one language; -v also notes key order differences
  ```

  The same check runs on every pull request.

To try a translation, copy its folder into `data/lang/` of the latest game build:
https://github.com/yncat/bk1cpp/releases/tag/latest
