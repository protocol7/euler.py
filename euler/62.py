#!/usr/bin/env python3

from itertools import count

def key(n):
    return "".join(sorted(str(n)))

assert "0234" == key(2034)

def find(n):
    combos = {}
    for i in count(1):
        c = i**3
        k = key(c)
        smallest, cnt = combos.get(k, (c, 0))
        if cnt == n-1:
            return smallest
        combos[k] = (smallest, cnt + 1)

assert 127035954683 == find(5)
