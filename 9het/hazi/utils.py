def is_palindrome_dec_bin(number: int, b_string: str) -> bool:
    '''
    Decides if both the decimal number and it's binary counterpart are palindrome
    '''

    n_palindrome = False
    b_palindrome = False

    n_string = str(number)

    if n_string[0] == 0 or b_string[2] == 0:
        return False

    if n_string[:] == n_string[::-1]:
        n_palindrome = True
    else:
        n_palindrome = False

    if b_string[2:] == b_string[:-len(b_string)+1:-1]:
        b_palindrome = True
    else:
        b_palindrome = False

    if n_palindrome == True and b_palindrome == True:
        return True
    else:
        return False


def is_palindrome_dec(n: int) -> bool:
    '''
    Decides if a deciaml values is a bool
    '''
    n_string = str(n)
    if n_string[:] == n_string[::-1]:
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    Source: http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
    """
    import random

    _mrpt_num_trials = 5    # number of bases to test

    if n < 2:
        return False
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a: int) -> bool:
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  # n is definitely composite

    for _ in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite


def prim_palindrome(n: int) -> int:
    while 1:
        if is_palindrome_dec(n) == True and is_prime(n) == True:
            return n
        else:
            n += 1
