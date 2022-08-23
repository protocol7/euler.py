from heapq import heappush, heappop

# https://erkal.github.io/elm-3d-playground-exploration/red-faced-cube/

# (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (1, 2),
# (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
# (1, 7), (1, 6), (2, 6), (2, 7), (3, 7), (3, 6), (3, 5), (2, 5),
# (1, 5), (1, 4), (1, 3), (2, 3), (2, 4), (3, 4), (3, 3), (3, 2),
# (4, 2), (4, 3), (4, 4), (5, 4), (5, 3), (6, 3), (6, 4), (6, 5),
# (5, 5), (4, 5), (4, 6), (4, 7), (5, 7), (5, 6), (6, 6), (6, 7),
# (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (7, 1), (6, 1),
# (6, 2), (5, 2), (5, 1), (4, 1), (4, 0), (5, 0), (6, 0), (7, 0)])

# the cube is described as having one of the states:
# R: red side up
# Y: yellow side up
# YR: yellow left side, red right side
# RY: red left side, yellow right side
# yr: yellow top side, red bottom side
# re: red top side, yellow bottom side


def turn(state, dx, dy):
    if state == "R":
        if dx == -1:
            return "RY"
        elif dx == 1:
            return "YR"
        elif dy == -1:
            return "ry"
        elif dy == 1:
            return "yr"
    elif state == "Y":
        if dx == -1:
            return "YR"
        elif dx == 1:
            return "RY"
        elif dy == -1:
            return "yr"
        elif dy == 1:
            return "ry"
    elif state == "YR":
        if dx == 0: # up or down
            return "YR"
        elif dx == -1:
            return "R"
        elif dx == 1:
            return "Y"
    elif state == "RY":
        if dx == 0:
            return "RY"
        elif dx == -1:
            return "Y"
        elif dx == 1:
            return "R"
    elif state == "yr":
        if dy == 0:
            return "yr"
        elif dy == -1:
            return "R"
        elif dy == 1:
            return "Y"
    elif state == "ry":
        if dy == 0:
            return "ry"
        elif dy == -1:
            return "Y"
        elif dy == 1:
            return "R"


def run(w, h):
    paths = []
    heappush(paths, (-1, [(0, 0)], "R"))

    ml = 0  # longest path seen, for printing progress

    while paths:
        l, path, state = heappop(paths)

        if l <= ml:
            #print(l, path, state)
            ml = l

        x, y = path[-1]

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ns = turn(state, dx, dy)
            nx = x + dx
            ny = y + dy
            nxy = (nx, ny)

            if nx < 0 or ny < 0 or nx >= w or ny >= h or nxy in path:
                continue

            np = path + [nxy]

            if nx == w-1 and ny == 0 and len(path) == (w*h)-1 and ns == "R":
                return np
            elif ns == "R" or (nx == w-1 and ny == 0):
                continue

            heappush(paths, (l-1, np, ns))

for w in range(2, 9):
    for h in range(2, 9):
        print(w, h, run(w, h))