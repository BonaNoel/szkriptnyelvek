#!/usr/bin/env python3


def is_palindrome(s):
    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


def main():
    print(is_palindrome("gorog"))
    print(is_palindrome("alma"))
    print(is_palindrome("abcba"))
    print(is_palindrome("xyz"))


if __name__ == "__main__":
    main()
