#!/usr/bin/env python3

from shared import primes

def problem10():
    return sum(primes(2000000))

assert 142913828922 == problem10()
