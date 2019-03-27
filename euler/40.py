#!/usr/bin/env python3

from itertools import count, islice

def decimals():
    for i in count():
        for x in str(i):
            yield int(x)

d = list(islice(decimals(), 0, 1000001))

print(d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000])
