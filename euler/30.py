#!/usr/bin/env python3

def fifth(n):
    return sum([int(i)**5 for i in str(n)])

ss = 0
for n in range(10, 1000000):
    if n == fifth(n):
        ss += n

print(ss)
