#!/usr/bin/env python3

def collatz(n):
    c = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        c += 1
    return c

assert 10 == collatz(13)

assert 837799 == max([n for n in range(1, 1000000)], key=collatz)
