#!/usr/bin/env python3

from shared import primes

def ltrunc(n):
    s = str(n)
    return [int(s[i:]) for i in range(len(s))]

assert [3797, 797, 97, 7] == ltrunc(3797)

def rtrunc(n):
    s = str(n)
    return [int(s[:i]) for i in range(len(s), 0, -1)]

assert [3797, 379, 37, 3] == rtrunc(3797)

ps = set(primes())

def truncatable(n):
    for t in ltrunc(n) + rtrunc(n):
        if t not in ps:
            return False
    return True

assert truncatable(3797)

assert 748317 == sum(filter(lambda p: p > 10 and truncatable(p), ps))
