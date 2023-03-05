#!/usr/bin/env python3


def is_palindrome(s):
    i = 0
    while i < len(s):
        if s[i] != s[-(i + 1)]:
            return False

        i += 1

    return True


def main():
    print(is_palindrome("gorog"))
    print(is_palindrome("alma"))
    print(is_palindrome("abcba"))
    print(is_palindrome("xyz"))


if __name__ == "__main__":
    main()
