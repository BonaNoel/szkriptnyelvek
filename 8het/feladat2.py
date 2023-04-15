#!/usr/bin/env python3

from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def main():
    print(Direction.UP)
    print(Direction.UP.value)
    print(Direction.UP.name)


if __name__ == "__main__":
    main()
