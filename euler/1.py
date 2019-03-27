#!/usr/bin/env python3

assert 233168 == sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1, 1000)))
