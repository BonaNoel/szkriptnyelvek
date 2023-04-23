#!/usr/bin/env python3

# import pygyak as pgy
from pygyak import is_prime


def main():
    a = [n for n in range(200) if is_prime(n) == True]

    print(sum(a))


if __name__ == "__main__":
    main()
