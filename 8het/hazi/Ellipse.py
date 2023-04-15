#!/usr/bin/env python3

class Ellipse:

    def __init__(self, lenght, widht):
        self.lenght = lenght
        self.widht = widht

    def area(self):
        return self.lenght * self.widht * 3.14

    def perimeter(self):
        return 2 * 3.14 * (self.lenght + self.widht)

    def __str__(self):
        return f"Ellipse: lenght = {self.lenght}, widht = {self.widht}"


def main():
    e = Ellipse(5, 10)
    print(e)
    print(f"Area: {e.area()}")
    print(f"Perimeter: {e.perimeter()}")


if __name__ == "__main__":
    main()
