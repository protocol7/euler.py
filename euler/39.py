#!/usr/bin/env python3

def combos(n):
    cs = 0
    for c in range(n // 2):
        for b in range(n // 2 ):
            a = n - c - b
            if a*a + b*b == c*c:
                cs += 1

    return cs // 2

840 == max(range(2, 1000), key=combos)
