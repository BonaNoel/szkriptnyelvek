#!/usr/bin/env python3

def greet(name, greetings="Hello"):
    print(f"{greetings} {name}!")


def main():
    greet("Noel")
    greet("Noel", greetings="Hola")


if __name__ == "__main__":
    main()
