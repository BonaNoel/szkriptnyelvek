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


class MyQueue:

    def __init__(self) -> None:
        self.inp = Verem()
        self.out = Verem()

    def append(self, n: int) -> None:
        self.inp.betesz(n)

    def popleft(self) -> Any:
        if self.out.ures():
            while not self.inp.ures():
                self.out.betesz(self.inp.kivesz())
        return self.out.kivesz()

    def is_empty(self) -> bool:
        if self.inp.ures() and self.inp.ures():
            return True
        else:
            return False

    def size(self) -> int:
        return self.inp.meret() + self.out.meret()

    def __str__(self) -> Any:
        if self.is_empty():
            return "[]"
        else:
            revers_inp = str(self.inp)[::-1]
            return "[ " + str(revers_inp).replace("[", "") + " " + str(self.out).replace("[", "") + "]"


def main() -> None:
    q = MyQueue()      # üres verem létrehozása
    print(q)         # []
    print(q.is_empty())  # True
    q.append(1)
    q.append(4)
    q.append(5)
    print(q)         # [5 4 1]
    print(q.size())  # 3
    print(q.is_empty())  # False
    x = q.popleft()
    print(x)         # 1
    q.append(9)
    print(q)         # [9 5 4]
    q.popleft()
    q.popleft()
    x = q.popleft()
    print(x)  # 9
    x = q.popleft()  # most már üres
    print(x)  # None


if __name__ == "__main__":
    main()
