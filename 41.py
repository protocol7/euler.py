#!/usr/bin/env python3

from shared import is_prime
from itertools import permutations

def concat(l):
    return int("".join(map(str, l)))

def pans(n):
    return map(concat, permutations(range(n, 0, -1)))

def find():
    for i in range(9, 0, -1):
        ps = pans(i)

        for p in ps:
            if is_prime(p):
                return p

assert 7652413 == find()
