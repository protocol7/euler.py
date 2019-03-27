#!/usr/bin/env python3

from itertools import islice, permutations

n = 1000000
c = next(islice(permutations(range(10)), n - 1, n))

assert "2783915460" == "".join([str(i) for i in c])
