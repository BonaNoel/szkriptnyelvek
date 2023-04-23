#!/usr/bin/env python3

import random


def shuffled(li):
    new_li = li[::]
    random.shuffle(new_li)
    return new_li


def own_choice(li):
    n = random.randrange(0, len(li))
    return li[n]


def main():
    li = [1, 2, 3]

    n = shuffled(li)[-1]

    print(li)
    print(n)

    print(own_choice(li))


if __name__ == "__main__":
    main()
