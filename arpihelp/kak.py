#!/usr/bin/env python3


def main():
    di = {}

    with open("hibas_bevasarlo_lista.txt", "r") as ffrom:

        for line in ffrom:

            line = line.replace("\n", "").split(" - ")
            if line[0] in di:
                di[line[0]] = int(di[line[0]]) + int(line[1])
            else:
                di[line[0]] = int(line[1])

    with open("bevasarlo_lista.txt", "w") as fto:
        for k, v in di.items():
            print(f"{k} -{v}\n", end="", file=fto)


if __name__ == "__main__":
    main()
