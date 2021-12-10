from tools.arith import product
from tools.general import load_strings

HEIGHT_MAP = [[int(j) for j in i] for i in load_strings('day09.txt')]
XMAX, YMAX = len(HEIGHT_MAP[0]) - 1, len(HEIGHT_MAP) - 1

def adjacent(point):

    adj = []
    x, y = point

    if x > 0:
        adj.append((x - 1, y))
    if x < XMAX:
        adj.append((x + 1, y))
    if y > 0:
        adj.append((x, y - 1))
    if y < YMAX:
        adj.append((x, y + 1))

    return adj

# Part 1
minima = {}

for x in range(XMAX + 1):
    for y in range(YMAX + 1):
        height = HEIGHT_MAP[y][x]
        if height < min(HEIGHT_MAP[y1][x1] for x1, y1 in adjacent((x, y))):
            minima[x, y] = height

print(f'Part 1 => {sum(minima.values()) + len(minima)}')

# part 2
basins = []

for m in minima:

    basin = set()
    to_visit = [m]

    while len(to_visit) > 0:

        pt = to_visit.pop()
        basin.add(pt)

        for x, y in adjacent(pt):
            if (x, y) not in basin and HEIGHT_MAP[y][x] != 9:
                to_visit.append((x, y))

    basins.append(len(basin))

print(f'Part 2 => {product(sorted(basins)[-3:])}')