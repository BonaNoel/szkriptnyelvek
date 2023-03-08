#!/usr/bin/env python3


def main():
    H = int(input("Add meg a gyémánt magasságát: "))

    if H % 2 == 0:
        print("Hiba! Páratlan számot adj meg!")
        exit(1)

    text = "*"
    j = 1

    for i in range(int(H/2)+1):

        print((text*j).center(H, " "))
        j += 2

    j -= 4
    for i in range(int(H/2)):
        print((text*j).center(H, " "))
        j -= 2


if __name__ == "__main__":
    main()
