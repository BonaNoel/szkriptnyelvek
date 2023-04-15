#!/usr/bin/env python3

class Verem:
    def __init__(self):
        self.v = []

    def ures(self):
        if len(self.v) == 0:
            return True
        else:
            return False

    def betesz(self, n):
        self.v.append(n)

    def meret(self):
        return len(self.v)

    def kivesz(self):
        if self.ures():
            return "None"
        else:
            return self.v.pop(-1)

    def __str__(self):
        if self.ures():
            return "["
        else:
            return "".join(str(self.v)).replace("]", "").replace(",", "")


def main():
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
