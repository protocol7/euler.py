#!/usr/bin/env python3

def problem6():
    s = sum(range(1, 101))
    ss = sum([i*i for i in range(1, 101)])
    return s*s - ss

assert 25164150 == problem6()
