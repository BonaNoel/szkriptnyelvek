#!/usr/bin/env python3


def is_palindrome(s):
    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


def main():
    s = "gorog"
    print(f"Az {s} szó palindrome: {is_palindrome(s)}")
    s = "alma"
    print(f"Az {s} szó palindrome: {is_palindrome(s)}")
    s = "abcba"
    print(f"Az {s} szó palindrome: {is_palindrome(s)}")
    s = "xyz"
    print(f"Az {s} szó palindrome: {is_palindrome(s)}")


if __name__ == "__main__":
    main()
