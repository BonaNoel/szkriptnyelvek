#!/usr/bin/env python3


def reverse(number):
    return int(str(number)[::-1])


def main():
    print(reverse(1977))
    print(reverse(123))


if __name__ == "__main__":
    main()
