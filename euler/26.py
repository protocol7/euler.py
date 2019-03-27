#!/usr/bin/env python3

import re
from decimal import Decimal, getcontext

getcontext().prec = 10000

def cycle(i):
    m = re.search(r"(\d+?)\1\1\1", str(Decimal(1) / Decimal(i))) # 4x is good enough :)

    return len(m.group()) // 4 if m else 0

assert 6 == cycle(7)
assert 1 == cycle(3)
assert 1 == cycle(6)

assert 983 == max(range(1, 1000), key=cycle)
