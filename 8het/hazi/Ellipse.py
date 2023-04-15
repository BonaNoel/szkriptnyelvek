#!/usr/bin/env python3

class Ellipse:

    def __init__(self, lenght: int, widht: int) -> None:
        self.lenght: int = lenght
        self.widht: int = widht

    def area(self) -> float:
        return self.lenght * self.widht * 3.14

    def perimeter(self) -> float:
        return 2 * 3.14 * (self.lenght + self.widht)

    def __str__(self) -> str:
        return f"Ellipse: lenght = {self.lenght}, widht = {self.widht}"


def main() -> None:
    e = Ellipse(5, 10)
    print(e)
    print(f"Area: {e.area()}")
    print(f"Perimeter: {e.perimeter()}")


if __name__ == "__main__":
    main()
