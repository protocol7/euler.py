#!/usr/bin/env python3
from itertools import count

def problem5():
    def is_divisble(i):
        for d in range(11, 20):
            if i % d:
                return False
        return True

    r = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2

    return next(filter(is_divisble, count(r, 20)), 1)

assert 232792560 == problem5()
