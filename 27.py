#!/usr/bin/env python3

from itertools import count, takewhile
from shared import primes

def quadratics(a, b):
    for n in count():
        yield n*n + a*n + b

ps = set(primes())
bs = list(primes(1000))

def streak(a, b):
    return len(list(takewhile(lambda x: x in ps, quadratics(a, b))))

assert 80 == streak(-79, 1601)

a, b = max([(a, b) for b in bs for a in range(-999, 1000)], key=lambda x: streak(x[0], x[1]))

print(a * b)
