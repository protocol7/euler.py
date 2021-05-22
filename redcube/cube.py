import sys

# https://erkal.github.io/elm-3d-playground-exploration/red-faced-cube/

# (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (1, 2),
# (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
# (1, 7), (1, 6), (2, 6), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5),
# (1, 5), (1, 4), (1, 3), (2, 3), (2, 4), (3, 4), (3, 3), (3, 2),
# (4, 2), (4, 3), (4, 4), (5, 4), (5, 3), (6, 3), (6, 4), (6, 5),
# (5, 5), (4, 5), (4, 6), (4, 7), (5, 7), (5, 6), (6, 6), (6, 7),
# (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1),
# (6, 2), (5, 2), (5, 1), (4, 1), (4, 0), (5, 0), (6, 0), (7, 0)])

states = ["R", "Y", "YR", "RY", "yr", "ry"]
dirs = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
    }


def turn(state, dir):
    if state == "R":
        if dir == "L":
            return "RY"
        elif dir == "R":
            return "YR"
        elif dir == "U":
            return "ry"
        elif dir == "D":
            return "yr"
    elif state == "Y":
        if dir == "L":
            return "YR"
        elif dir == "R":
            return "RY"
        elif dir == "U":
            return "yr"
        elif dir == "D":
            return "ry"
    elif state == "YR":
        if dir == "U" or dir == "D":
            return "YR"
        elif dir == "L":
            return "R"
        elif dir == "R":
            return "Y"
    elif state == "RY":
        if dir == "U" or dir == "D":
            return "RY"
        elif dir == "L":
            return "Y"
        elif dir == "R":
            return "R"
    elif state == "yr":
        if dir == "L" or dir == "R":
            return "yr"
        elif dir == "U":
            return "R"
        elif dir == "D":
            return "Y"
    elif state == "ry":
        if dir == "L" or dir == "R":
            return "ry"
        elif dir == "U":
            return "Y"
        elif dir == "D":
            return "R"
    else:
        assert False

start = (-1, [(0, 0)], "R")
from heapq import heappush, heappop

paths = []
heappush(paths, start)

ml = 0

while paths:
    l, path, state = heappop(paths)

    #if l * -1 != len(path):
    #if l < -63:
    #    assert False

    if l <= ml:
        print(l, path, state)
        ml = l

    #print(l)
    #print(path, state)

    x, y = path[-1]

    for dir, (dx, dy) in dirs.items():
        ns = turn(state, dir)
        nx = x + dx
        ny = y + dy

        if nx < 0 or ny < 0 or nx > 7 or ny > 7:
            continue

        nxy = (nx, ny)

        if nxy in path:
            continue

        if ns == "R" or (nx == 7 and ny == 0):
            if len(path) == 63:
                print(ns, nx, ny, path)
            if nx == 7 and ny == 0 and len(path) == 63 and ns == "R":
                print("done ")
                print(path)
                sys.exit()
            else:
                continue

        np = path + [nxy]

        heappush(paths, (l-1, np, ns))
