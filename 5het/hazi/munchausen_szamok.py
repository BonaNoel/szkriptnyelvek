#!/usr/bin/env python3

import sys


def main():

    i = 0
    while i < 440000000:

        li_i = (list(str(i)))
        result = 0

        for n in li_i:
            if int(n) == 0:
                pw = 0
            else:
                pw = pow(int(n), int(n))

            result = result + pw

        if i == result:
            print(f"{i} egy Münchausen-szám")

        i += 1


if __name__ == "__main__":
    main()
