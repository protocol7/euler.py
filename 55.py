#!/usr/bin/env python3

def is_palindrom(s):
    return str(s) == str(s)[::-1]

def rev(n):
    return int(str(n)[::-1])

assert 321 == rev(123)

def is_lychrel(n):
    for r in range(50):
        n = n + rev(n)
        if is_palindrom(n):
            return False
    return True

assert is_lychrel(4994)
assert not is_lychrel(47)
assert is_lychrel(10677)

c = 0
for i in range(1, 10000):
    if is_lychrel(i):
        c += 1

assert 249 == c
