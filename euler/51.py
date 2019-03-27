#!/usr/bin/env python3

from shared import primes
from collections import Counter

ps = list(primes(2000000))
ps_set = set(map(str, ps))

# Assume (incorrectly) that we're replacing all the digits of the same digit
def perms(n):
    s = str(n)
    if len(set(s)) == len(s):
        return
    c = Counter(s)
    for digit, count in c.most_common():
        # Assume that we're replacing more than one digit
        if count == 1:
            break
        cc = 0
        for i in range(10):
            ss = s.replace(digit, str(i))
            if ss in ps_set:
                cc += 1
        if cc == 8:
            return True

def find():
    for p in ps:
        if p < 56003:
            continue

        if perms(p):
            return p

assert 121313 == find()
