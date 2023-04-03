#!/usr/bin/env python3

def draw(li):
    '''Draws a chessboard with 8 queens on it on given values'''

    row = 9
    collumn = 0
    isQueen = False

    while row > -1:

        if row == 0 or row == 9:
            print("+-----------------+")
            row -= 1
            continue

        collumn = 0
        while collumn < 10:

            isQueen = False

            if collumn == 0:
                print("/ ", end="")
                collumn += 1
                continue
            elif collumn == 9:
                print("/ ")
                collumn += 1
                continue

            for idx, x in enumerate(li):
                if idx+1 == collumn and x == row-1:
                    isQueen = True

            if isQueen:
                print("Q ", end="")
            else:
                print(". ", end="")

            collumn += 1

        row -= 1



def main():
    li = [0, 4, 7, 5, 2, 6, 1, 3]
    print("A lista: " + str(li))

    draw(li)


if __name__ == "__main__":
    main()
