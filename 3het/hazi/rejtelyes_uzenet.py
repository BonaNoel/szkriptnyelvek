#!/usr/bin/env python3

TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

# A papír túloldalán csupán ennyi áll: "K → M, O → Q, E → G".

# A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
#             |----->|          |---->|     |---->|   2-vel el van tolva minden


def main():
    result = TEXT[:]
    for i in result:
        if i == "y":
            print("a", end="")
        elif i == "Y":
            print("A", end="")
        elif i.isalpha():
            print(chr(ord(i) + 2), end="")
        else:
            print(i, end="")


if __name__ == "__main__":
    main()
