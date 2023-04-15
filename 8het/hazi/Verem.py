#!/usr/bin/env python3

from typing import Any


class Verem:
    def __init__(self) -> None:
        self.v: list[int] = []

    def ures(self) -> bool:
        if len(self.v) == 0:
            return True
        else:
            return False

    def betesz(self, n: int) -> None:
        self.v.append(n)

    def meret(self) -> int:
        return len(self.v)

    def kivesz(self) -> Any:
        if self.ures():
            return "None"
        else:
            return self.v.pop(-1)

    def __str__(self) -> str:
        if self.ures():
            return "["
        else:
            return "".join(str(self.v)).replace("]", "").replace(",", "")


def main() -> None:
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
