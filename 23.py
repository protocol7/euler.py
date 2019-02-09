#!/usr/bin/env python3

from itertools import count, takewhile

def factors(n):
    factors = set([1])

    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1
    return factors

assert [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110] == sorted(factors(220))
assert [1, 2] == sorted(factors(4))

def sum_of_factors(n):
    return sum(factors(n))

def is_abundant(n):
    return sum_of_factors(n) > n

assert not is_abundant(4)
assert is_abundant(12)

def abundants():
    for i in count(1):
        if is_abundant(i):
            yield i

abus = set(takewhile(lambda x: x < 28123, abundants()))

def cant_be_sum(n):
    for a in abus:
        if (n - a) in abus:
            return False
    return True

assert 4179871 == sum(filter(cant_be_sum, range(1, 28124)))
