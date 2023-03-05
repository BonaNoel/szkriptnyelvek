#!/usr/bin/env python3


def multiply(li):
    result = 1
    if len(li) == 0:
        return result
    else:
        for e in li:
            result *= e

        return result


def main():
    li = [1, 5, 2, 4]
    null_li = []

    print(multiply(li))
    print(multiply(null_li))


if __name__ == "__main__":
    main()
