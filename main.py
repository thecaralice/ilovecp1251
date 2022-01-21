#!/usr/bin/env python3
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

    # Changed a bit because the original one seems to be invalid
    # TODO: Send a patch to https://lurkmore.to/БНОПНЯ
    LURK_TABLE: Final = """\
Привет	оПХБЕР
всем хай	БЯЕЛ УЮИ
Что такое?	вРН РЮЙНЕ?
Сергеев	яЕПЦЕЕБ
С уважением	я СБЮФЕМХЕЛ
Вопрос читал?	бНОПНЯ ВХРЮК?
Пиздец	оХГДЕЖ
Беспредел	аЕЯОПЕДЕК
КПРФ	йопт
Единая Россия	еДХМЮЪ пНЯЯХЪ
Ку	йС
Как переключить кодировку?	йЮЙ ОЕПЕЙКЧВХРЭ ЙНДХПНБЙС?"""
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
