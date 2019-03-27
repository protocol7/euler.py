#!/usr/bin/env python3
from itertools import islice
from shared import primes

def problem7():
    return next(islice(primes(), 10000, 10001))

assert 104743 == problem7()
