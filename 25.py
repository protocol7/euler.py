#!/usr/bin/env python3

from itertools import islice, takewhile

def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

assert [1, 1, 2, 3, 5, 8, 13] == list(islice(fib(), 7))

def digits(n):
    return len(str(n))

iter = takewhile(lambda i: digits(i) < 1000, fib())

print(sum(1 for _ in iter) + 1)
