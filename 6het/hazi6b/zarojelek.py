#!/usr/bin/env python3
NYITO = ["(", "[", "{"]
ZARO = [")", "]", "}"]


def test(s):
    zarojel = ["()", "{}", "[]"]
    tiszta_s = []
    for c in s:
        if c in NYITO or c in ZARO:
            tiszta_s.append(c)

    tiszta_s = "".join(tiszta_s)

    while any(x in tiszta_s for x in zarojel):
        for zr in zarojel:
            tiszta_s = tiszta_s.replace(zr, '')
    return not tiszta_s


def main():
    b = test("((5+3)*2+1)")  # == True
    print("((5+3)*2+1) - " + str(b))
    b = test("{[(3+1)+2]+}")  # == True
    print("{[(3+1)+2]+} - " + str(b))
    b = test("(3+{1-1)}")  # == False
    print("(3+{1-1)} - " + str(b))
    b = test("[1+1]+(2*2)-{3/3}")  # == True
    print("[1+1]+(2*2)-{3/3} - " + str(b))
    b = test("(({[(((1)-2)+3)-3]/3}-3)")  # == False
    print("(({[(((1)-2)+3)-3]/3}-3) - " + str(b))


if __name__ == "__main__":
    main()
