#!/usr/bin/env python3

import pygyak as pgy


def main():
    a = [n for n in range(100) if pgy.is_prime(n) == True]

    print(a)


if __name__ == "__main__":
    main()
