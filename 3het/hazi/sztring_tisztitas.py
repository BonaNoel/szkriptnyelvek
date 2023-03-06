#!/usr/bin/env python3

def tisztit(s):
    return s.replace(" ","").replace("\t","").replace("\n","")

def main():
    s1 = f"192.20.246.138:\n 6666"
    s2 = f"2\t06.   13 0.9 9.8  \n2:\n80\t80"
    print("Előtte:  " + s2)
    print("Utánna: " + tisztit(s2))

    


if __name__ == "__main__":
    main()