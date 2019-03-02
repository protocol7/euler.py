#!/usr/bin/env python3

from itertools import count
from functools import lru_cache

@lru_cache(maxsize=10)
def factors(n):
    factors = set()

    i = 2
    while i <= n:
        if n % i == 0:
            factors.add(i)
            n //= i
        else:
            i += 1
    return len(factors)

assert 2 == factors(24)
assert 2 == factors(14)
assert 3 == factors(644)

def find():
    for i in count():
        if factors(i) == 4 and factors(i+1) == 4 and factors(i+2) == 4 and factors(i+3) == 4:
            return i

# slow but works
assert 134043 == find()
