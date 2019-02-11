#!/usr/bin/env python3

size = 1001
layers = (size - 1) // 2

ss = 1
value = 1
for layer in range(1, layers + 1):
    for c in range(4):
        value += layer * 2
        ss += value

assert 669171001 == ss
