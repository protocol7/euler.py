#!/usr/bin/env python3

words = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "onehundred",
        1000: "onethousand"
        }

def to_words(n):
    if n in words:
        return words[n]

    if n > 100:
        c = n % 10
        b = n % 100 - c
        a = n // 100

        if b == 10:
            return "%shundredand%s" % (words[a], words[b+c])
        elif b == 0 and c == 0:
            return "%shundred" % (words[a])
        else:
            return "%shundredand%s%s" % (words[a], words[b], words[c])
    else:
        b = n % 10
        a = n - b
        return words[a] + words[b]

assert "five" == to_words(5)
assert "twenty" == to_words(20)
assert "twentyone" == to_words(21)
assert "twohundred" == to_words(200)
assert "twohundredandthirteen" == to_words(213)
assert "twohundredandtwentyone" == to_words(221)
assert 23 == len(to_words(342))
assert 20 == len(to_words(115))

assert 21124 == sum([len(to_words(i)) for i in range(1, 1001)])
