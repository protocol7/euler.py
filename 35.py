#!/usr/bin/env python3

from shared import primes

def rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

assert [197, 971, 719] == rotations(197)
assert [1] == rotations(1)
assert [79, 97] == rotations(79)

ps = set(primes(1000000))

def is_circular(n):
    return all(map(lambda i: i in ps, rotations(n)))

assert 55 == len(list(filter(is_circular, ps)))
