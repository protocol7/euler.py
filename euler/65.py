#!/usr/bin/env python3

from itertools import islice

def repeats():
    s = 0
    i = 0
    yield 2
    while True:
        if s == 0:
            s = 1
            yield 1
        elif s == 1:
            i += 2
            s = 2
            yield i
        else:
            s = 0
            yield 1

assert [2, 1,2,1,1,4,1,1,6,1] == list(islice(repeats(), 10))

def convergents(x, rs):
    rs = rs[:x]
    t, n = 1, rs[-1]
    for i in reversed(rs[:x-1]):
        t += n * i
        t, n = n, t
    return t, n

def nth(x, rs):
    _, t = convergents(x, rs)
    return sum([int(i) for i in str(t)])


rs = list(islice(repeats(), 1000))

assert 272 == nth(100, rs)
