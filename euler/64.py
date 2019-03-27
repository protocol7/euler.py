#!/usr/bin/env python3

from itertools import islice
from math import sqrt
from shared import ilen

def is_sqrt(n):
    return int(round(n**(1/2)))**2 == n

def sq(s):
    # as per
    # https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
    seen = set()
    m = 0
    d = 1
    a0 = int(sqrt(s))
    a = a0
    while True:
        k = (m, d, a)
        if k in seen:
            break
        seen.add(k)

        yield a

        m = d * a - m
        d = (s - m*m) // d
        a = int((a0 + m) / d)

assert [1, 2] == list(islice(sq(2), 10))
assert [1, 1, 2] == list(islice(sq(3), 10))

def find(n):
    odd = 0
    for i in range(1, n + 1):
        if is_sqrt(i):
            continue
        f = ilen(sq(i))
        # has a single digit lead, so check if even
        if f % 2 == 0:
            odd += 1
    return odd

assert 4 == find(13)

assert 1322 == find(10000)
