#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'


def hangrend(word):
    mely = False
    magas = False

    if word == "mély":
        return "magas :)"
    elif word == "magas":
        return "mély :)"

    for e in list(word):

        for me in list(MELY_MGHK):
            if e == me:
                mely = True

        for ma in list(MAGAS_MGHK):
            if e == ma:
                magas = True

    if mely and magas:
        return "vegyes"
    elif mely == True and magas == False:
        return "mély"
    elif mely == False and magas == True:
        return "magas"
    else:
        return "semmilyen"


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "Pfffffff"]
    for e in words:
        print(f"{e}: " + str(hangrend(e)))


if __name__ == "__main__":
    main()
