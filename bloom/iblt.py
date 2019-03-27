from mmh3 import hash
from collections import deque

def create(m, k):
    return k, m * [(0, 0)]

def add(f, v):
    k, b = f
    for i in range(k):
        x = hash(str(v), i) % len(b)
        b[x] = (b[x][0] ^ v, b[x][1] + 1)

def remove(f, v):
    k, b = f
    for i in range(k):
        x = hash(str(v), i) % len(b)
        b[x] = (b[x][0] ^ v, b[x][1] - 1)

def inverse(f):
    k, b = f
    b = b[:]
    q = deque()

    for s, c in b:
        if c == 1 and s not in q:
            q.append(s)

    values = set()
    while (q):
        v = q.popleft()
        if v in values:
            continue
        values.add(v)
        for i in range(k):
            x = hash(str(v), i) % len(b)
            b[x] = nv, nc = b[x][0] ^ v, b[x][1] - 1
            if nc == 1:
                q.append(nv)

    if any(filter(lambda x: x[1] != 0, b)):
        return None

    return values

def subtract(f1, f2):
    # assume f1 is a strict superset of f2
    k1, b1 = f1
    k2, b2 = f2
    assert k1 == k2
    assert len(b1) == len(b2)

    return k1, [(s1 ^ s2, c1 - c2) for (s1, c1), (s2, c2) in zip(b1, b2)]

f = create(1000, 6)
f2 = create(1000, 6)

a = set(range(500))

for x in a:
    add(f, x)
    add(f2, x)

b = set(range(50))
for x in b:
    remove(f, x)

assert a - b == inverse(f)

d = subtract(f2, f)

assert b == inverse(d)
