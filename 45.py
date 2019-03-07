#!/usr/bin/env python3

from itertools import islice
from shared import pentagonal, triangle, hexagonal

p = list(islice(pentagonal(), 100000))
t = list(islice(triangle(), 100000))
h = list(islice(hexagonal(), 100000))

assert t[284] == p[164] == h[142] == 40755

t = set(t)
h = set(h)

def find():
    for n in p[284:]:
        if n in t and n in h:
            return n

assert 1533776805 == find()
