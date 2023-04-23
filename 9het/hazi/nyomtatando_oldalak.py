#!/usr/bin/env python3


def main() -> None:
    s = input("Add meg az oldalakat pl(1,3-5,6):  ")

    li = s.split(",")

    pages_li = []

    for n in li:
        if n.find("-") == -1:
            pages_li.append(int(n))
        else:
            start = int(n[:n.find("-")])
            end = int(n[n.find("-")+1:]) + 1
            for i in range(start, end):
                pages_li.append(i)

    print(pages_li)


if __name__ == "__main__":
    main()
