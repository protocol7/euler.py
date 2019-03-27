#!/usr/bin/env python3

from itertools import count, islice
from math import sqrt

def triangle():
    s = 0
    for i in count(1):
        s += i
        yield s

assert [1, 3, 6, 10, 15, 21, 28, 36, 45, 55] == list(islice(triangle(), 10))

def factors(n):
    if n == 1:
        return 1

    c = 2
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            c += 2
    return c

assert 1 == factors(1)
assert 2 == factors(3)
assert 4 == factors(6)
assert 6 == factors(28)

def problem12():
    for t in triangle():
        if factors(t) > 500:
            return t

assert 76576500 == problem12()
