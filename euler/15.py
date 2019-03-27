#!/usr/bin/env python3

x, y = 0, 0

tx, ty = 20, 20

paths = 0
def move(x, y):
    global paths
    if x == tx and y == ty:
        paths += 1
        print(paths)
        return

    # move down
    if y < ty:
        move(x, y+1)
    # move right
    if x < tx:
        move(x+1, y)

# slooooow with large tx, ty
#move(x, y)
#print(paths)

# based on http://code.jasonbhill.com/python/project-euler-problem-15/
def dynamic(size):
    l = [1] * size
    for i in range(size):
        for j in range(i):
            l[j] = l[j] + l[j - 1]
        l[i] = 2 * l[i - 1]
    return l[-1]

assert 137846528820 == dynamic(20)
