#!/usr/bin/env python3

import sys


def main():
    f = open("asd.txt", "r")
    to = open("out.txt", "w")

    for line in f:
        to.write(line)

    f.close()
    to.close()

    # for line in f:
    #     line = line.rsplit('\n')
    #     print(line, )

    # sorok = f.readlines()
    # print(sorok)

    # content = f.read()
    # sorok = content.splitlines()
    # print(content)

    # f.close()

    # f = open("out.txt", "w")

    # print("Hello", file=f)
    # print("World", file=f)

    # f.write("aa")
    # f.write("bb")

    # f.close()


if __name__ == "__main__":
    main()
