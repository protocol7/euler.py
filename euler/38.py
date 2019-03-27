#!/usr/bin/env python3

from itertools import permutations, count

digits = 987654321

pans = set(map(lambda l: int("".join(l)), permutations(str(digits))))

def is_pandigital(n):
    return n in pans

assert is_pandigital(192384576)

def con_prod(i, n):
    s = ""
    for j in range(1, n + 1):
        s += str(i * j)
    return int(s)

assert 192384576 == con_prod(192, 3)

m = 0
for i in count(1):
    for j in count(2):
        cp = con_prod(i, j)
        if is_pandigital(cp):
            if cp > m:
                m = cp
        if cp > int(digits):
            break

    if j == 2:
        break

assert 932718654 == m
