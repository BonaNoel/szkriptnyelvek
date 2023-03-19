#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    '''This function returns with a string wich only maches with the given chars from the text'''
    result_li = []
    for c in text:
        for v in chars:
            if c == v:
                result_li.append(c)

    return ("".join(result_li))


def main():
    result = valid("Barking!")
    print(f"valid('Barking!') --> {result}")
    result = valid("KL754", "0123456789")
    print(f"valid('KL754', '0123456789') --> {result}")
    result = valid("BEAN", "abcdefghijklmnopqrstuvwxyz")
    print(f"valid('BEAN', 'abcdefghijklmnopqrstuvwxyz') --> {result}")


if __name__ == "__main__":
    main()
