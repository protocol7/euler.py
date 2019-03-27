#!/usr/bin/env python3

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

def sum_of_factors(n):
    return sum(factors(n))

assert 284 == sum_of_factors(220)

ss = 0
for i in range(1, 10001):
    s = sum_of_factors(i)
    if s != i and sum_of_factors(s) == i:
        ss += i

assert 31626 == ss
