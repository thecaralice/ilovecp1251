#!/usr/bin/env python3
"""
MIT License

Copyright (c) 2022 Alice Carroll

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from sys import argv, stdin, stdout
from typing import Callable, Final, Optional

# translation dictionary is used instead of the simpler encode-decode because
# some characters are not in either encoding and thus are to be skipped
TRANS: Final = str.maketrans(
    {
        bytes((i,)).decode("cp1251"): bytes((i,)).decode("koi8-r")
        for i in range(0x100)
        if i != 0x98  # \x98 is invalid in cp1251
    }
)


def test():
    assert "Вопрос".translate(TRANS) == "бНОПНЯ"

    # From https://lurkmore.to/БНОПНЯ
    LURK_TABLE: Final = """\
Привет	оПХБЕР
всем хай	БЯЕЛ УЮИ
Что такое?	вРН РЮЙНЕ?
Муси-Пуси	лСЯХ-оСЯХ
нХУЙ-рХУЙ	Муси-Пуси
Сергеев	яЕПЦЕЕБ
С уважением	я СБЮФЕМХЕЛ
Вопрос читал?	бНОПНЯ ВХРЮК?
Пиздец	оХГДЕЖ
Беспредел	аЕЯОПЕДЕК
нБУФЕТ	Мастер
КПРФ	йопт
Единая Россия	еДХМЮЪ пНЯЯХЪ
Ку	йС
хъй	УЗИ
Как переключать кодировку?	йЮЙ ОЕПЕЙКЧВЮРЭ ЙНДХПНБЙС?"""
    for line in LURK_TABLE.splitlines():
        test, ref = line.split("\t")
        res = test.translate(TRANS)
        assert res == ref, f"{res!r} != {ref!r}"


def main():
    for line in stdin:
        stdout.write(line.translate(TRANS))


if __name__ == "__main__":
    ACTIONS: Final[dict[Optional[str], Callable[[], None]]] = {
        "test": test,
        None: main,
    }
    action = NotImplemented
    try:
        action = argv[1]
    except IndexError:
        action = None
    finally:
        ACTIONS[action]()
