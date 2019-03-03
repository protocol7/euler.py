#!/usr/bin/env python3

from itertools import count

def digits(n):
    return sorted(n)

def same_digits(ns):
    sns = list(map(str, ns))
    ds = digits(sns[0])
    for n in sns[1:]:
        if ds != digits(n):
            return False
    return True

assert same_digits([125874, 251748])

def times(n):
    return same_digits([n * x for x in range(1, 7)])

def find():
    for c in count(1):
        if times(c):
            return c

assert 142857 == find()
