from heapq import heappop, heappush
from tools.general import load_input

RISK_MAP = [[int(j) for j in i] for i in load_input('day15.txt').split('\n')]

def safest_path(map_size):

    xmod, ymod = len(RISK_MAP[0]), len(RISK_MAP)
    xmax, ymax = map_size * xmod - 1, map_size * ymod - 1

    to_visit = [(0, 0, 0)]
    visited = {(0, 0)}

    while len(to_visit) > 0:

        risk, x, y = heappop(to_visit)

        if (x, y) == (xmax, ymax):
            return risk

        for x1, y1 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):

            if x1 < 0 or y1 < 0 or x1 > xmax or y1 > ymax or (x1, y1) in visited:
                continue

            xq, xr = divmod(x1, xmod)
            yq, yr = divmod(y1, ymod)

            # Value wraps from 9 to 1 (not 0)
            nrisk = ((RISK_MAP[yr][xr] + xq + yq) - 1) % 9 + 1

            visited.add((x1, y1))
            heappush(to_visit, (risk + nrisk, x1, y1))

print(f'Part 1 => {safest_path(1)}')
print(f'Part 2 => {safest_path(5)}')