#!/usr/bin/env python3

def test(li_vals):
    '''Returns the median value of a list'''
    li_vals = sorted(li_vals)
    median = 0
    if len(li_vals) % 2 == 1:
        median = li_vals[len(li_vals) // 2]
    else:
        median = (li_vals[len(li_vals) // 2-1] +
                  li_vals[(len(li_vals) // 2)]) / 2

    return median


def main():
    print("A [1, 2, 3, 4, 5] medián értéle: " +
          str(test([1, 2, 3, 4, 5])))  # == 3
    print("A [3, 1, 2, 5, 3] medián értéle: " +
          str(test([3, 1, 2, 5, 3])))  # == 3
    print("A [1, 300, 2, 200, 1] medián értéle: " +
          str(test([1, 300, 2, 200, 1])))  # == 2
    print("A [3, 6, 20, 99, 10, 15] medián értéle: " +
          str(test([3, 6, 20, 99, 10, 15])))  # == 12.5


if __name__ == "__main__":
    main()
