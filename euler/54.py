#!/usr/bin/env python3

from collections import Counter

def high_card(h):
    return h[-1][0]

def flush(h):
    suits = [s for _, s in h]
    if len(set(suits)) == 1:
        return high_card(h)

assert not flush([(5, "H"), (5, "C"), (6, "S"), (7, "S"), (13, "D")])
assert flush([(5, "H"), (5, "H"), (6, "H"), (7, "H"), (13, "H")])

def straight(h):
    ns = [n for n, _ in h]
    for n1, n2 in zip(ns, ns[1:]):
        if n2 - n1 != 1:
            return False
    return ns[-1]

assert straight([(5, "H"), (6, "H"), (7, "H"), (8, "H"), (9, "H")])
assert not straight([(5, "H"), (6, "H"), (7, "H"), (8, "H"), (10, "H")])

def straight_flush(h):
    return flush(h) and straight(h)

def royal_straight_flush(h):
    return straight_flush(h) and 14 == high_card(h)

def same_kind(h):
    return Counter([n for n, _ in h]).most_common()

def four_of_a_kind(h):
    n, c = same_kind(h)[0]
    if c == 4:
        return n

assert four_of_a_kind([(5, "H"), (5, "S"), (5, "C"), (5, "D"), (9, "H")])

def full_house(h):
    c = same_kind(h)
    if len(c) > 1:
        if c[0][1] == 3 and c[1][1] == 2:
            return c[0][0], c[1][0]

def three_of_a_kind(h):
    n, c = same_kind(h)[0]
    if c == 3:
        return n

def two_pairs(h):
    c = same_kind(h)
    if len(c) > 1:
        if c[0][1] == 2 and c[1][1] == 2:
            return c[0][0], c[1][0]

def one_pair(h):
    n, c = same_kind(h)[0]
    if c == 2:
        return n

def classify(h):
    four = four_of_a_kind(h)
    fh = full_house(h)
    fl = flush(h)
    st = straight(h)
    three = three_of_a_kind(h)
    tp = two_pairs(h)
    op = one_pair(h)

    if royal_straight_flush(h):
        return 10, 14
    elif straight_flush(h):
        return 9, high_card(h)
    elif four:
        return 8, four
    elif fh:
        return 7, fh[::-1]
    elif fl:
        return 6, fl
    elif st:
        return 5, st
    elif three:
        return 4, three
    elif tp:
        return 3, tp[::-1]
    elif op:
        return 2, op
    else:
        return 1, high_card(h)

numbers = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10}

def parse_card(s):
    n, c = s
    nn = numbers.get(n)
    if not nn:
        nn = int(n)
    return nn, c

assert (5, "C") == parse_card("5C")
assert (13, "C") == parse_card("KC")

def parse(line):
    xs = line.strip().split()
    xs = list(map(parse_card, xs))
    h1, h2 = sorted(xs[:5]), sorted(xs[5:])
    return h1, h2

assert ([(5, "C"), (5, "H"), (6, "S"), (7, "S"), (13, "D")], [(2, "C"), (3, "S"), (8, "D"), (8, "S"), (10, "D")]) == parse("5H 5C 6S 7S KD 2C 3S 8S 8D TD")

def first_wins(h1, h2):
    c1, n1 = h1
    c2, n2 = h2

    if c1 > c2:
        return True
    elif c2 > c1:
        return False
    else:
        return n1 > n2

def find():
    with open("p054_poker.txt") as f:
        winner1 = 0
        for line in f:
            h1, h2 = parse(line)
            c1, c2 = classify(h1), classify(h2)
            if first_wins(c1, c2):
                winner1 += 1
        return winner1

assert 376 == find()
