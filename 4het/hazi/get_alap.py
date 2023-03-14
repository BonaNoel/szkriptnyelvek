#!/usr/bin/env python3

import shutil
import os.path
from pathlib import Path

SOURCE_PY = "/home/noel/szkriptnyelvek/alap.py"
SOURCE_C = "/home/noel/szkriptnyelvek/alap.c"


def make_py():

    if (os.path.isfile(str(os.path.dirname(__file__)) + "/alap.py")):
        print("Hiba! A fálj már létezik")
        exit(1)
    else:
        shutil.copy(SOURCE_PY, str(os.path.dirname(__file__)) + "/alap.py")

    return 0


def make_c():

    if (os.path.isfile(str(os.path.dirname(__file__)) + "/alap.c")):
        print("Hiba! A fálj már létezik")
        exit(1)
    else:
        shutil.copy(SOURCE_C, str(os.path.dirname(__file__))+"/alap.c")

    return 0


def main():

    inp = input(
        "---------------------------\r\nCreate an empty source file\r\n---------------------------\r\n1) Python [py]\r\n2) C      [c]\r\nq) quit\r\n> ")

    if inp == "q":
        exit(0)
    elif int(inp) == 1:
        make_py()
    elif int(inp) == 2:
        make_c()


if __name__ == "__main__":
    main()
