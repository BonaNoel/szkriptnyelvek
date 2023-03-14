#!/usr/bin/env python3


def get_movie_info():
    return ("Total recall", 1990, 7.7)


def main():
    title, year, score = get_movie_info()
    print(title, year, score)

#############################################################################


if __name__ == "__main__":
    main()
