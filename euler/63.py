#!/usr/bin/env python3

from itertools import count

def nlen(n):
    return len(str(n))

found = set()
for a in range(1, 100):
    for b in range(1, 100):
        n = a**b
        if nlen(n) == b:
            found.add(n)

assert 49 == len(found)
