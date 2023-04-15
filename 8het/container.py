#!/usr/bin/env python3

class Bag:
    def __init__(self):
        self.data = []

    def add(self, n):
        self.data.append(n)

    def add_twice(self, n):
        self.add(n)
        self.add(n)

    def __str__(self):
        return "Bag(" + str(self.data) + ")"


def main():
    b = Bag()
    b.add(5)
    print(b)


if __name__ == "__main__":
    main()
