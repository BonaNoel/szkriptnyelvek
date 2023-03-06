#!/usr/bin/env python3


def is_palindrome(s):
    i = 0
    while i < len(s):
        if s[i] != s[-(i + 1)]:
            return False

        i += 1

    return True


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
