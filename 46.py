#!/usr/bin/env python3

from shared import primes
from itertools import count
from math import sqrt

ps = list(primes())
ps_set = set(ps)

def goldbach(n):
    for p in ps:
        if p > n:
            return False
        i = int(sqrt((n - p) // 2))
        if p + 2 * i * i == n:
            return True

assert goldbach(9)

def match(n):
    return n not in ps_set and not goldbach(n)

assert 5777 == next(filter(match, count(9, 2)))
