#!/usr/bin/env python3

class Pisi:
    counter = 0

    def __init__(self):
        Pisi.counter = Pisi.counter + 1


def main():
    a = Pisi()
    b = Pisi()

    print(Pisi.counter)


if __name__ == "__main__":
    main()
