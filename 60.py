#!/usr/bin/env python3

from shared import primes

ps = list(primes(100000000))
ps_set = set(ps)
ps = ps[:2000]

def combine(x, y):
    return int(str(x) + str(y))

def fit(x, y):
    if x == y:
        return False

    return combine(x, y) in ps_set and combine(y, x) in ps_set

assert fit(13, 5197)
assert fit(13, 5701)
assert fit(13, 6733)
assert fit(13, 8389)
assert fit(5197, 5701)
assert fit(5197, 6733)

def find():
    for ia, a in enumerate(ps):
        for ib, b in enumerate(ps[ia+1:]):
            if fit(a, b):
                for ic, c in enumerate(ps[ib+1:]):
                    if fit(a, c) and fit(b, c):
                        for id, d in enumerate(ps[ic+1:]):
                            if fit(a, d) and fit(b, d) and fit(c, d):
                                for e in ps[id+1:]:
                                    if fit(a, e) and fit(b, e) and fit(c, e) and fit(d, e):
                                        return a, b, c, d, e

assert 26033 == sum(find())
