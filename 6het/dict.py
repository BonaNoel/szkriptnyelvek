#!/usr/bin/env python3


def main():
    d = {}
    d["a"] = "ALPHA"
    d["b"] = "BETA"
    d["g"] = "GAMMA"
    d["o"] = "OMEGA"

    for k in d.keys():
        print(k, "->", d[k])

    print(f"\n\n")

    for k, v in d.items():
        print(k, "->", v)

    print(f"\n\n")

    d["d"] = "DELTA"

    for k, v in sorted(d.items()):
        print(k, "->", v)

    del d["a"]


if __name__ == "__main__":
    main()
