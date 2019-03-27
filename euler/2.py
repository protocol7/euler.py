#!/usr/bin/env python3
from itertools import islice, takewhile

def fib(a, b):
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

assert [1, 2, 3, 5, 8, 13] == list(islice(fib(1,2), 6))

def problem2():
    return sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x < 4000001, fib(1, 2))))

assert 4613732 == problem2()
