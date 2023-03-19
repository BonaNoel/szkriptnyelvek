#!/usr/bin/env python3

import os.path


def main():

    li = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
          "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    if os.path.islink(__file__):
        for c in li[::-1]:
            print(c, end="")
        print(" ")
    else:
        for c in li:
            print(c, end="")
        print(" ")


if __name__ == "__main__":
    main()
