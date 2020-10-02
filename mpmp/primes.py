# Rearrange the numbers from 1-9, such that all adjacent pairs sum to a prime
# number.
#
# http://www.think-maths.co.uk/primepairs

import sys
from itertools import permutations

primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def fil(xs):
    last = None
    for x in xs:
        if last and not (last+x) in primes:
            return False
        last = x
    return True

perms = permutations(range(1, int(sys.argv[1])+1))
perms = filter(fil, perms)
print(sum([1 for _ in perms]))
