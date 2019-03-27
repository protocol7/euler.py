#!/usr/bin/env python3

from functools import reduce
from operator import mul

def product(l):
    return reduce(mul, l)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return product(range(1, n + 1))

assert 24 == factorial(4)

def digits(n):
    return [int(i) for i in str(n)]

assert [1, 4 ,5] == digits(145)

s = 0
for i in range(3, 100000):
    if sum(map(factorial, digits(i))) == i:
        s += i

assert 40730 == s
