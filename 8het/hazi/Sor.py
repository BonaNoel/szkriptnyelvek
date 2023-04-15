#!/usr/bin/env python3

from typing import Any


class Sor:
    def __init__(self) -> None:
        self.s: list[int] = []

    def ures(self) -> bool:
        if len(self.s) == 0:
            return True
        else:
            return False

    def betesz(self, n: int) -> None:
        self.s.append(n)

    def meret(self) -> int:
        return len(self.s)

    def kivesz(self) -> Any:
        if self.ures():
            return "None"
        else:
            return self.s.pop(0)

    def __str__(self) -> str:
        if self.ures():
            return "[]"
        else:
            return "".join(str(self.s[::-1])).replace(",", "")


def main() -> None:
    s = Sor()      # üres verem létrehozása
    print(s)         # []
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # [5 4 1]
    print(s.meret())  # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # [5 4]
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
