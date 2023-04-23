#!/usr/bin/env python3

from utils import is_palindrome_dec_bin


def main() -> None:
    total = 0
    for n in range(1000000+1):
        if is_palindrome_dec_bin(n, bin(n)):
            total += n

    print(total)


if __name__ == "__main__":
    main()
