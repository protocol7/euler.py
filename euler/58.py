#!/usr/bin/env python3

from shared import is_prime
from itertools import count

def find():
    ps = 0
    c = 1
    v = 1
    for layer in count(1):
        side = layer * 2
        for corner in range(4):
            v += side
            if is_prime(v):
                ps += 1
            c += 1

            if ps / c < 0.1:
                return side + 1

assert 26241 == find()
