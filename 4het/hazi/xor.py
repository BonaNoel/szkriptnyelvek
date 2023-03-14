#!/usr/bin/env python3

def xor(v1, v2):
    if bool(v1) == bool(v2):
        return False
    else:
        return True


def main():
    str1 = "python"
    str2 = None
    print("bool('python'): " + str(bool(str1)))
    print("bool(None): " + str(bool(str2)))

    print("xor('python',None): " + str(xor(str1, str2)))


if __name__ == "__main__":
    main()
