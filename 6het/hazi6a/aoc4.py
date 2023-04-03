#!/usr/bin/env python3


def main():
    result = 0

    with open("aoc.txt", "r") as f:
        for line in f:

            li = line.replace("\n", "").split(" ")

            if (len(set(li)) == len(li)):
                result += 1

    print(result)


if __name__ == "__main__":
    main()
