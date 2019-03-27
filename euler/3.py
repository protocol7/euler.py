#!/usr/bin/env python3

def factors(n):
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n /= i
        i += 1
    return factors

assert [2, 3] == factors(12)
assert [13] == factors(13)
assert [2, 3, 4] == factors(24)

def problem3():
    return max(factors(600851475143))

assert 6857 == problem3()
