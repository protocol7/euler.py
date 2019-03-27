#!/usr/bin/env python3

import sys
from itertools import count, islice

def pentagonal():
    for n in count(1):
        yield n * (3 * n - 1) // 2

assert [1, 5, 12, 22, 35, 51] == list(islice(pentagonal(), 6))

pentas = list(islice(pentagonal(), 10000))
penta_set = set(pentas)

d = sys.maxsize
for pj in pentas:
    for pk in pentas:
        diff = pk - pj
        if diff <= 0:
            continue
        if diff in penta_set and (pj + pk) in penta_set:
            if diff < d:
                d = diff
            break

assert d == 5482660
