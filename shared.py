#!/usr/bin/env python3
from itertools import islice

def is_prime(n):
    if n == 1 or n == 2:
        return True

    if not n & 1:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

assert is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(7)

def primes(limit=1000000):
    yield 2
    sieve = [False, False] + [True] * (limit - 2)
    for i in range(3, limit, 2):
        if sieve[i]:
            yield i
            for j in range(i*i, limit, i * 2):
                sieve[j] = False

assert [2, 3, 5, 7, 11, 13] == list(islice(primes(), 6))

def ilen(it):
    return sum([1 for _ in it])
