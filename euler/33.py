#!/usr/bin/env python3

def shares(a, b):
    if a // 10 == b % 10:
        return a % 10, b // 10
    elif a % 10 == b // 10:
        return a // 10, b % 10
    elif a % 10 == b % 10:
        return a // 10, b // 10
    elif a // 10 == b // 10:
        return a % 10, b % 10

assert (4, 8) == shares(49, 98)
assert (4, 8) == shares(94, 89)
assert (4, 8) == shares(94, 98)
assert (4, 8) == shares(49, 89)

ns, ds = 1, 1
for a in range(11, 100):
    for b in range(11, 100):
        if a >= b:
            continue

        if a % 10 == 0 or b % 10 == 0:
            continue

        sh = shares(a, b)
        if sh:
            ar, br = sh
            if a / b == ar / br:
                ns *= a
                ds *= b

assert 100 == ds // ns
