#!/usr/bin/env python3

def problem9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a * b * c

assert 31875000 == problem9()
