#!/usr/bin/env python3
PI = 3.14159


def hello(name, color, what):
    # v1
    # print("{0}, {1} az {2}! Ki? {0}".format(name,color,what))
    # v2
    # print("{}, {} az {}!".format(name,color,what))
    # v3
    # print("{name}, {c} az {w}!".format(name=name,c=color,w=what))
    # v4
    # print(f"1 + 1 = {1+1}")
    print(f"{name.capitalize()}, {color} az {what}!")


def main():
    hello("geza", "kek", "eg")
    print("---" * 10)
    hello("peti", "piros", "auto")

    s = "abcde"
    print((int)(len(s) / 2))


if __name__ == "__main__":
    main()
