#!/usr/bin/env python3

from itertools import count, islice
from string import ascii_uppercase

def triangle():
    for n in count(1):
        yield n * (n+1) // 2

assert [1, 3, 6, 10, 15, 21, 28] == list(islice(triangle(), 7))

triangles = set(islice(triangle(), 1000))

def char_value(c):
    return ascii_uppercase.index(c) + 1

assert char_value("S") == 19

def word_value(word):
    return sum([char_value(c) for c in word])

assert 55 == word_value("SKY")

cc = 0
with open("p042_words.txt") as f:
    for word in f.read().split(","):
        word = word.strip('"')
        value = word_value(word)
        if value in triangles:
            cc += 1

assert 162 == cc


