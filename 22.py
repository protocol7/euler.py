#!/usr/bin/env python3

from string import ascii_uppercase

def alpha_score(name):
    return sum([ascii_uppercase.index(c) + 1 for c in name])

assert 53 == alpha_score("COLIN")

with open("p022_names.txt") as f:
    names = sorted([n.strip('"') for n in f.read().split(",")])

    scores = 0
    for i, name in enumerate(names):
        scores += (i + 1) * alpha_score(name)

    assert 871198282 == scores
