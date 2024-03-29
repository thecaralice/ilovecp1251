# бНОПНЯ

[![Использовать в Telegram](https://img.shields.io/static/v1?logo=telegram&label=Использовать%20в&message=Telegram&color=success)][apply]
[![Telegram чат](https://img.shields.io/static/v1?logo=telegram&label=Telegram&message=чат&color=blue)](https://t.me/setlanguage/translation_ilovecp1251)
[![Помочь с переводом](https://img.shields.io/static/v1?logo=telegram&label=Помочь&message=с%20переводом&color=important)](https://translations.telegram.org/ilovecp1251/)
[![build](https://img.shields.io/github/actions/workflow/status/thecaralice/ilovecp1251/translate.yml?branch=mistress&logo=github)][download]
[![Лицензия](https://img.shields.io/github/license/thecaralice/ilovecp1251?logo=github)](https://github.com/thecaralice/ilovecp1251/blob/mistress/LICENSE)

Как выглядел бы русский перевод Telegtam, если бы он был в Windows-1251 и прочитан как KOI8-R

## Название

"бНОПНЯ" - то, как пользователи KOI8-R видят слово "Вопрос" в кодировке Windows-1251. Про это можно прочитать на [Lurkmore][lurkmore].

## Зачем?

А почему бы и нет?

## Почему не на Rust?

Я не смогла найти простого способа закодировать и декодеровать текст, игнорируя неизвестные символы, используя [encoding_rs](https://github.com/hsivonen/encoding_rs) и решила, что использование Rust для столь простого скрипта - ненужное усложнение.

## Как это использовать?

Нажмите "Использовать Telegram" кнопку в начале этого файла или просто кликните [сюда][apply].

## Но... я имею в виду... как вообще читать *это*??

Не знаю, быть может, вы достаточно опытный пользователь IRC, умеющий читать текст с неправильной кодировке? В любом случае, для кого-то неподготовленного вы слишко заинтересованы :)

## Удали это

нет

## Файловая структура

- `main.py*` - конвертирующий скрипт \
    Его интерфейс подобен [cat (1)][man-cat-1] - он построчно читает стандартный ввод и построчно пишет перевод в стандартный вывод. \
    Кстати, у него есть подкоманда `test`, проверяющая работу конвертации на печально известном Вопрос-бНОПНЯ и изменённых примерах с [Lurkmore][lurkmore].
- `translate.sh*` - вспомогательный сценарий, запускающий `main.py` на каждом файле из исходной директории и помещающий результат в целевую директорию \
  Пример использования: `./translate.sh source/ dest/`
- `download.sh*` - вспомогательный сценарий, скачивающий файлы переводов для указанного языка \
  Пример использования: `./download.sh ru source/`
- `README.md` - это нужно объяснять?
- `README.en.md` - английский перевод README
- `README.ru.md` - русский перевод README (вы его читаете)
- `source/` - исходные файлы перевода (официальный русский перевод Telegram)
- `dest/` - директория, в которую должны попадать готовые файлы перевода \
  Собранную с помощью Github Actions версию можно скачать [тут][download].

## Благодарности

- [Zetroks](https://t.me/Zetroks) за его перевод [KOI-7 H1](https://t.me/rulangs/211), вдохновивший меня на это.

[apply]: (https://t.me/setlanguage/ilovecp1251)
[lurkmore]: https://lurkmore.to/БНОПНЯ
[man-cat-1]: https://linux.die.net/man/1/cat
[download]: https://nightly.link/thecaralice/ilovecp1251/workflows/translate/mistress/translation.zip
