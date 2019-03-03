#!/usr/bin/env python3

from string import ascii_lowercase
from itertools import permutations, cycle

def read_cipher():
    with open("p059_cipher.txt") as f:
        s = f.read().strip()
        return [int(i) for i in s.split(",")]

c = read_cipher()

def to_string(l):
    return "".join([chr(x) for x in l])

def find():
    for key in permutations(ascii_lowercase, 3):
        key = cycle([ord(x) for x in key])

        pt = list(map(lambda x: x[0] ^ x[1], zip(c, key)))

        if " the " in to_string(pt):
            return sum(pt)

assert 129448 == find()
