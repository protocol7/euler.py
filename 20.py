#!/usr/bin/env python3

def factorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

assert 3628800 == factorial(10)

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

assert 27 == sum_of_digits(3628800)

assert 648 == sum_of_digits(factorial(100))
