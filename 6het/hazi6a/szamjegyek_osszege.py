#!/usr/bin/env python3


def main():
    number = 2**1000
    digits = [int(n)for n in str(number)]

    sum = 0

    for n in digits:
        sum += n

    print("2**1000 számjegyeienk az összege: " + str(sum))


if __name__ == "__main__":
    main()
