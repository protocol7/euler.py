#!/usr/bin/env python3

def pandigital(a, b, c):
    s = str(a) + str(b) + str(c)
    return len(s) == 9 and "0" not in s and len(s) == len(set(s))

def factors(n):
    factors = set()

    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.add((i, n // i))
        i += 1
    return factors

assert (39, 186) in factors(7254)

xs = set()
for i in range(1000, 10000):
    for a, b in factors(i):
        if pandigital(a, b, i):
            xs.add(i)

assert 45228 == sum(xs)
