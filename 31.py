#!/usr/bin/env python3

def f(v, coins):
    s = sum(v)
    if s == 200:
        return 1
    elif s > 200:
        return 0

    cs = 0
    for i, coin in enumerate(coins):
        cs += f(v + [coin], coins[i:])
    return cs

assert 73682 == f([], [1, 2, 5, 10, 20, 50, 100, 200])
