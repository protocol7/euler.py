#!/usr/bin/env python3

from itertools import count, islice
from shared import pentagonal, triangle, hexagonal

def square():
    for n in count(1):
        yield n * n

def heptagonal():
    for n in count(1):
        yield n * (5 * n - 3) // 2

def octagonal():
    for n in count(1):
        yield n* (3 * n - 2)

def is_4_digit(n):
    return 999 < n < 10000

def gen(fn):
    return list(filter(is_4_digit, islice(fn(), 1000)))

p = gen(pentagonal)
t = gen(triangle)
hx = gen(hexagonal)
hp = gen(heptagonal)
s = gen(square)
o = gen(octagonal)

r = [gen(fn) for fn in [square, pentagonal, hexagonal, heptagonal, octagonal]]

def f(n, xs):
    # find next value in cycle
    ns = n % 100
    return [x for x in xs if x // 100 == ns]

def fc(c, xs):
    if len(c) == 6:
        return [c]

    out = []
    n = c[-1]
    for x in xs:
        xxs = xs[:]
        xxs.remove(x)
        for cand in f(n, x):
            out += fc(c + [cand], xxs)
    return out

def find_cycles(xs, xxs):
    cycles = []
    for x in xs:
        cycles += fc([x], xxs)

    def cyclic(xs):
        return xs[0] // 100 == xs[-1] % 100

    return next(map(tuple, filter(cyclic, cycles)))

assert 28684 == sum(find_cycles(t, r))
