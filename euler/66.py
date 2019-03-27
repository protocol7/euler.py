#!/usr/bin/env python3

from itertools import count
from math import sqrt

def is_square(n):
    return int(round(n**(1/2))) ** 2 == n

def solve(d):
    print(d)
    for x in count(1):
        y = int(round(sqrt((x*x - 1) / d)))
        if y > 0 and x*x - d * y*y == 1:
            print(x, y)
            return x

print(solve(5))
assert 9 == solve(5)

mx = 0
for d in range(1001):
    if is_square(d):
        continue

    x = solve(d)
    mx = max(mx, x)

print(mx)
