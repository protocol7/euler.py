#!/usr/bin/env python3

from itertools import permutations, count

pans = map(lambda l: "".join(l), permutations("9876543210"))

def match(s):
    for i, p in zip(range(1, 8), [2, 3, 5, 7, 11, 13, 17]):
        n = int(s[i:i+3])
        if n % p != 0:
            return False
    return True

assert match("1406357289")

assert 16695334890 == sum(map(int, filter(match, pans)))
