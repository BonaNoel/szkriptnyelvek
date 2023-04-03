#!/usr/bin/env python3

def normalize(s):
    '''Returns the string in normalized form (lowercase nad no whitespace)'''
    return s.lower().replace(" ", "")


def is_anagramm1(s1, s2):
    '''Decides if the 2 strings are anagrams of each other version1'''
    s1 = normalize(s1)
    s2 = normalize(s2)

    d1 = dict()
    d2 = dict()

    for c in list(s1):
        d1[c] = d1.get(c, 0) + 1

    for c in list(s2):
        d2[c] = d2.get(c, 0) + 1

    if d1 == d2:
        return True
    else:
        return False


def is_anagramm2(s1, s2):
    '''Decides if the 2 strings are anagrams of each other version2(trivial)'''
    s1 = normalize(s1)
    s2 = normalize(s2)

    if (sorted(s1) == sorted(s2)):
        return True
    else:
        return False


def main():

    print("version 1")
    s1 = "listen"
    s2 = "silent"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm1(s1,s2)}")

    s1 = "Clint Eastwood"
    s2 = "Old west action"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm1(s1,s2)}")

    s1 = "Apple"
    s2 = "Pear"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm1(s1,s2)}")

    print("version 2")
    s1 = "listen"
    s2 = "silent"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm2(s1,s2)}")

    s1 = "Clint Eastwood"
    s2 = "Old west action"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm2(s1,s2)}")

    s1 = "Apple"
    s2 = "Pear"

    print(f"'{s1}' and '{s2}' is anagramm of eachother: {is_anagramm2(s1,s2)}")


if __name__ == "__main__":
    main()
