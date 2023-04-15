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


class MyQueue:

    def __init__(self):
        self.inp = Verem()
        self.out = Verem()

    def append(self, n):
        self.inp.betesz(n)

    def popleft(self):
        if self.out.ures():
            if self.inp.ures():
                return "None"
            else:
                while self.inp.ures() != True:
                    tmp = self.inp.kivesz()
                    self.out.betesz(tmp)
                return self.out.kivesz()
        else:
            return self.out.kivesz()

    def is_empty(self):
        if self.inp.ures() and self.inp.ures():
            return True
        else:
            return False

    def size(self):
        return self.inp.meret() + self.out.meret()

    def __str__(self):
        if self.is_empty():
            return "[]"

        return (print(str(self.out), str(self.inp)))


def main():
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
    print(q)         # [5 4]
    q.popleft()
    q.popleft()       # most már üres
    x = q.popleft()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
