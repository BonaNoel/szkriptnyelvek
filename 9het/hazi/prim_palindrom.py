#!/usr/bin/env python3

from utils import prim_palindrome


def main() -> None:
    print(f"31 --> {prim_palindrome(31)}")
    print(f"130 --> {prim_palindrome(130)}")
    print(f"131 --> {prim_palindrome(131)}")
    print(f"1977 --> {prim_palindrome(1977)}")


if __name__ == "__main__":
    main()
