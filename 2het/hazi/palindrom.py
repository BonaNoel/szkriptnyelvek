#!/usr/bin/env python3


def palindrome(s):
    if s[:] == s[::-1]:
        return True
    else:
        return False

def main():
    s = "gorog"
    if(palindrome(s)):
        print(f"A {s} palindróm")
    else:
        print(f"A {s} NEM palindróm")

    s = "alma"
    if(palindrome(s)):
        print(f"A {s} palindróm")
    else:
        print(f"A {s} NEM palindróm")


if __name__ == "__main__":
    main()
