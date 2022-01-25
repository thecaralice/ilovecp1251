# бНОПНЯ

[![Use in Telegram](https://img.shields.io/static/v1?logo=telegram&label=Use%20in&message=Telegram&color=success)][apply]
[![Telegram chat](https://img.shields.io/static/v1?logo=telegram&label=Telegram&message=chat&color=blue)](https://t.me/setlanguage/translation_ilovecp1251)
[![Help translating](https://img.shields.io/static/v1?logo=telegram&label=Help&message=translating&color=important)](https://translations.telegram.org/ilovecp1251/)

What Russian Telegram translation would look like if it was in Windows-1251 and you read it in KOI8-R

## Naming

The name is how KOI8-R users see "Вопрос" (Russian for "Question") in Windows-1251. You can read more on [Lurkmore][lurkmore].

## Why?

Why not?

## Why not in Rust?

I was unable to find an easy way to run encode-decode ignoring unknown characters via [encoding_rs](https://github.com/hsivonen/encoding_rs) and found using Rust for such a simple script an unnecesary overcomplication.

## How do I use this?

Press the "Use in Telegram" button on the top of this document or click [here][apply].

## No- I mean, how am I supposed to read *that*??

I dunno, maybe you're an experienced enough IRC user with ability to read any text in a wrong encoding? Anyway, you are too interested in this for someone unprepared :)

## Please delete this

no

## File structure

- `main.py*` - script that does the convertation \
    Its interface is similar to [cat (1)][man-cat-1] - it reads stdin line-by-line and writes the translation to stdout line-by-line. \
    It also has a `test` subcommand to check the convertation on the infamous Вопрос-бНОПНЯ and patched examples from [Lurkmore][lurkmore]
- `translate.sh*` - helper script that runs `main.py` for every translation file in the source directory and places the result in the destination directory \
  Usage example: `./translate.sh source/ dest/`
- `download.sh*` - helper script that downloads translation files for a specified language \
  Usage example: `./download.sh ru source/`
- `README.md` - do I have to explain it?
- `README.en.md` - English README translation (you are reading this)
- `README.ru.md` - Russian README translation
- `source/` - the source translation files (official Russian Telegram translation)
  - `.gitkeep`
- `dest/` - where the generated translation files are supposed to be placed
  - `android.xml`
  - `android_x.xml`
  - `ios.strings`
  - `macos.strings`
  - `tdesktop.strings`

## Credits

- [Zetroks](https://t.me/Zetroks) for their [KOI-7 H1](https://t.me/rulangs/211) translation which inspired me on this.

[apply]: (https://t.me/setlanguage/ilovecp1251)
[lurkmore]: https://lurkmore.to/БНОПНЯ
[man-cat-1]: https://linux.die.net/man/1/cat
