#!/usr/bin/env python3

def ciklus(value, debug=False):
    if debug:
        print("#ciklus kezdete")

    for i in range(value):
        print(i, end=", ")
    print(value)

    if debug:
        print("#ciklus vége")


def main():
    ciklus(5)
    ciklus(5, True)


if __name__ == "__main__":
    main()
