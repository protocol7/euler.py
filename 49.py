#!/usr/bin/env python3

from shared import primes
from itertools import permutations, combinations
from collections import Counter

ps = set(filter(lambda x: x > 1000, primes(10000)))

def perms(p):
    out = []
    for i in [int("".join(x)) for x in permutations(str(p))]:
        if i in ps:
            out.append(i)
    return sorted(out)


def f(l):
    for a, b, c in combinations(l, 3):
        if c - b == b - a and a != b:
            return (a, b, c)

# find all permutations at least 3 long
pps = set(map(tuple, filter(lambda l: len(l) >= 3, [perms(p) for p in ps])))

# find those with a shared delta
res = list(filter(lambda x: x, map(f, pps)))

# remove the known one
res.remove(((1487, 4817, 8147)))

assert "296962999629" == "".join(map(str, res[0]))
