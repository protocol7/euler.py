#!/usr/bin/env python3

def is_palindrom(s):
    return str(s) == str(s)[::-1]

assert is_palindrom("aba")

def is_db_palindrome(n):
    b = bin(n)[2:]
    return is_palindrom(n) and is_palindrom(b)

s = 0
for i in range(1000000):
    if is_db_palindrome(i):
        s += i

assert 872187 == s
