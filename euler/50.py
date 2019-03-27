#!/usr/bin/env python3

from shared import primes

ps = list(primes(1000000))
ps_set = set(ps)

ms = ps[-1]

mp = 0
mc = 0
for i in range(len(ps)):
    s = 0
    c = 0
    for p in ps[i:]:
        s += p
        if s > ms:
            break
        c += 1
        if s in ps_set and c > mc:
            mp = s
            mc = c

assert 997651 == mp
