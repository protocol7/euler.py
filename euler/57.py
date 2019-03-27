#!/usr/bin/env python3

from itertools import islice
from shared import ilen

def fit(n, d):
    return len(str(n)) > len(str(d))

def sqrt2():
    pn, pd = 1, 1
    n, d = 3, 2

    yield n, d

    while True:
        n, pn = n*2 + pn, n
        d, pd = d*2 + pd, d

        yield n, d

assert [(3,2), (7,5), (17,12)] == list(islice(sqrt2(), 3))

assert 153 == ilen(filter(lambda x: fit(x[0], x[1]), islice(sqrt2(), 1000)))
