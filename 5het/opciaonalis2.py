#!/usr/bin/env python3

def hello(name, repeat=1, postfix=""):
    for i in range(repeat):
        print(name+postfix)


def main():
    hello("Laci")
    print("------")
    hello("Lackó", repeat=3)
    print("------")
    hello("László", 2, "!")


if __name__ == "__main__":
    main()
