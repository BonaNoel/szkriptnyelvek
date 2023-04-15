#!/usr/bin/env python3

from enum import Enum

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


class Maganhangzok(Enum):
    MAGAS = 1
    MELY = 2
    VEGYES = 3
    SEMMILYEN = 4


def hangrend(word: str) -> Maganhangzok:
    mely = False
    magas = False

    if word == "mély":
        return Maganhangzok.MAGAS
    elif word == "magas":
        return Maganhangzok.MELY

    for e in list(word):

        for me in list(MELY_MGHK):
            if e == me:
                mely = True

        for ma in list(MAGAS_MGHK):
            if e == ma:
                magas = True

    if mely and magas:
        return Maganhangzok.VEGYES
    elif mely == True and magas == False:
        return Maganhangzok.MELY
    elif mely == False and magas == True:
        return Maganhangzok.MAGAS
    else:
        return Maganhangzok.SEMMILYEN


def main() -> None:
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for e in words:
        print(f"{e}: " + str(hangrend(e).name))


if __name__ == "__main__":
    main()
