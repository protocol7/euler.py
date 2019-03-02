#!/usr/bin/env python3

s = 0
for i in range(1, 1001):
    s += i**i

assert "9110846700" == str(s)[-10:]
