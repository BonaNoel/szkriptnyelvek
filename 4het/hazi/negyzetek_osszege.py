#!/usr/bin/env python3

def negyzetek_osszege(value):
    result = 0

    for i in range(value+1):
        result += i**2

    return result


def osszegek_negyzete(value):
    result = 0

    for i in range(value+1):
        result += i

    return (result ** 2)


def main():
    print("Első 100 szám négyzetének összege: " + str(negyzetek_osszege(100)))
    print("Első 100 szám összegének négyzete: " + str(osszegek_negyzete(100)))

    print("A kettő különbsége: " +
          str(osszegek_negyzete(100)-negyzetek_osszege(100)))


if __name__ == "__main__":
    main()
