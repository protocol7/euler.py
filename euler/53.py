#!/usr/bin/env python3

from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

assert 24 == factorial(4)

def combos(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

assert 1144066 == combos(23, 10)

def find():
    c = 0
    for n in range(1, 101):
        for r in range(1, n):
            if combos(n, r) > 1000000:
                c += 1
    return c

assert 4075 == find()
