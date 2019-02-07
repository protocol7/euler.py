#!/usr/bin/env python3
from itertools import permutations, starmap

def is_palindrome(i):
    return str(i) == str(i)[::-1]

def problem4():
    return max(
            filter(is_palindrome,
                starmap(lambda a, b: a * b,
                    permutations(range(100, 1000), 2))))

assert 906609 == problem4()
