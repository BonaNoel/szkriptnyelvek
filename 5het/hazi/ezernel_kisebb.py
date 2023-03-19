#!/usr/bin/env python3


def main():
    result = sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0])
    print(
        f"1000-nél kisebb számok összege, melyek 3-nak vagy 5-nek a többszörösei:  {result}")


if __name__ == "__main__":
    main()
