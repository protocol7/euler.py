from bitarray import bitarray
from mmh3 import hash

def create(m, k):
    return k, m * bitarray('0')

def add(f, v):
    k, b = f
    for i in range(k):
        b[hash(v, i) % len(b)] = True

def contains(f, v):
    k, b = f
    for i in range(k):
        if not b[hash(v, i) % len(b)]:
            return False
    return True

f = create(500, 3)

for i in range(50):
    add(f, "foo%s" % i)

for i in range(50):
    assert contains(f, "foo%s" % i)
    assert not contains(f, "bar%s" % i)
