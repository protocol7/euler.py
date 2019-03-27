#!/usr/bin/env python3

def digit_sum(n):
    return sum([int(i) for i in str(n)])

assert 6 == digit_sum(123)

assert 972 == max([digit_sum(a**b) for a in range(1, 100) for b in range(1, 100)])
