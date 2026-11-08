#!/usr/bin/env python3
"""Checks a translation folder <lang>/ against the Japanese source (ja/).

Same checks as the game's C++ tests (bk1cpp: tests/test_game.cpp), runnable without the game:

  py tools/check_translation.py          # checks every language folder except ja
  py tools/check_translation.py de -v    # one language; -v also lists keys whose order differs

For every ja file there must be a translated file with
  * exactly the same keys (same order recommended: reported with -v),
  * the same value kinds (string / array) and the same array lengths,
  * the same set of {placeholders} per value,
  * no kana (Japanese-only script), unless the value is identical to the Japanese one
    (e.g. the bilingual "Language / 言語"); kanji are not checked, so Chinese works.
The catalog must also name its language with the key "language.name" (the game only offers
folders that do); since the key is in ja, the "same keys" check covers it.
When this repository is checked out as data/lang/ of the game (bk1cpp), every literal key used
by tr("...") / trLines("...") in the game's src/ must also exist in the translation.

Exit status 0 if everything passes, 1 otherwise.
"""
import json
import pathlib
import re
import sys

LANG_DIR = pathlib.Path(__file__).resolve().parent.parent
GAME_DIR = LANG_DIR.parent.parent  # the game's repository when mounted as its data/lang/
SRC_DIR = GAME_DIR / "src"

JAPANESE = re.compile("[ぁ-ヿｦ-ﾟ]")  # kana: not used by any other language
PLACEHOLDER = re.compile(r"\{[A-Za-z0-9_]+\}")
TR_CALL = re.compile(r'tr(?:Lines)?\("([A-Za-z0-9_.]+)"')


def load(path):
    with open(path, encoding="utf-8") as f:
        doc = json.load(f)
    if not isinstance(doc, dict):
        raise ValueError("top level is not an object")
    return doc


def placeholders(value):
    texts = value if isinstance(value, list) else [value]
    return {p for t in texts if isinstance(t, str) for p in PLACEHOLDER.findall(t)}


def japanese_ok(tr, ja):
    return not isinstance(tr, str) or not JAPANESE.search(tr) or tr == ja


LANG_CODE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]{2,8})*$")


def main(argv):
    verbose = "-v" in argv
    args = [a for a in argv if not a.startswith("-")]
    if args:
        return check(args[0], verbose)
    langs = sorted(d.name for d in LANG_DIR.iterdir()
                   if d.is_dir() and d.name != "ja" and LANG_CODE.match(d.name))
    return max((check(lang, verbose) for lang in langs), default=0)


def check(lang, verbose):
    errors = []
    tr_dir = LANG_DIR / lang
    catalog = {}
    owner = {}  # key -> ja file name

    for ja_path in sorted((LANG_DIR / "ja").glob("*.json")):
        name = ja_path.name
        ja = load(ja_path)
        for key in ja:
            owner[key] = name
        tr_path = tr_dir / name
        if not tr_path.exists():
            errors.append(f"{lang}/{name}: file missing ({len(ja)} keys)")
            continue
        try:
            tr = load(tr_path)
        except (ValueError, json.JSONDecodeError) as e:
            errors.append(f"{lang}/{name}: invalid JSON: {e}")
            continue
        catalog.update(tr)
        for key, jv in ja.items():
            if key not in tr:
                errors.append(f"{lang}/{name}: missing key {key}")
                continue
            tv = tr[key]
            if isinstance(jv, list) != isinstance(tv, list) or (
                    not isinstance(tv, list) and not isinstance(tv, str)):
                errors.append(f"{lang}/{name}: {key}: different kind (string / array)")
                continue
            if isinstance(jv, list):
                if len(jv) != len(tv):
                    errors.append(f"{lang}/{name}: {key}: {len(tv)} lines, ja has {len(jv)}")
                for i, t in enumerate(tv):
                    if not isinstance(t, str):
                        errors.append(f"{lang}/{name}: {key}[{i}] is not a string")
                    elif not japanese_ok(t, jv[i] if i < len(jv) else None):
                        errors.append(f"{lang}/{name}: {key}[{i}] contains Japanese")
            elif not japanese_ok(tv, jv):
                errors.append(f"{lang}/{name}: {key} contains Japanese")
            if placeholders(jv) != placeholders(tv):
                errors.append(f"{lang}/{name}: {key}: placeholders {sorted(placeholders(tv))}, "
                              f"ja has {sorted(placeholders(jv))}")
        for key in tr:
            if key not in ja:
                errors.append(f"{lang}/{name}: extra key {key}")
        if verbose and [k for k in tr if k in ja] != [k for k in ja if k in tr]:
            print(f"note: {lang}/{name}: key order differs from ja")

    missing_files = {e.split(":")[0] for e in errors if e.endswith("keys)")}
    game_sources = sorted(SRC_DIR.rglob("*.cpp")) if (SRC_DIR / "game").is_dir() else []
    for path in game_sources:
        code = path.read_text(encoding="utf-8")
        for key in sorted(set(TR_CALL.findall(code))):
            if key in catalog:
                continue
            src = owner.get(key)
            if src and f"{lang}/{src}" in missing_files:
                continue  # already reported as a missing file
            where = f" (ja: {src})" if src else " (not in ja either)"
            errors.append(f"{path.relative_to(GAME_DIR)}: key {key} not in {lang}{where}")

    for e in errors:
        print(e)
    print(f"{lang}: {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
