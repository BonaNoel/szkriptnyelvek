#!/usr/bin/env python3

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * 3.14 * self.radius ** 2

    def volume(self):
        return 4 / 3 * 3.14 * self.radius ** 3

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __str__(self):
        return f"Sphere: radius = {self.radius}"


def main():
    s1 = Sphere(5)
    s2 = Sphere(10)

    print(s1)
    print(f"s1 area: {s1.area()}")
    print(f"s1 volume: {s1.volume()}")

    print(s2)
    print(f"s2 area: {s2.area()}")
    print(f"s2 volume: {s2.volume()}")

    print(s1 < s2)
    print(s1 <= s2)
    print(s1 > s2)
    print(s1 >= s2)


if __name__ == "__main__":
    main()
