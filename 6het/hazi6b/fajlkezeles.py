#!/usr/bin/env python3


def main():
    with open("string1.py", "r") as ffrom:
        with open("string1_clean.py", "w") as fto:

            for line in ffrom:
                if line.startswith("#"):
                    continue
                else:
                    fto.write(line)

    with open("strin2.py", "r") as ffrom:
        with open("strin2_clean.py", "w") as fto:

            for line in ffrom:
                if line.startswith("    #"):
                    continue
                else:
                    fto.write(line)


if __name__ == "__main__":
    main()
