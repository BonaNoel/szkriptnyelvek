#!/usr/bin/env python3


def main():

    result1 = 0
    for i in range(101):
        result1 += i
    print("1-100-ig a számok összege: " + str(result1))

    result2 = 0
    for i in range(101):
        tmp = list(str(i))
        for e in tmp:
            result2 += int(e)

    print("1-100-ig a számjegyek összege: " + str(result2))


if __name__ == "__main__":
    main()
