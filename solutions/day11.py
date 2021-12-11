from tools.general import load_strings

def neighbours(pt, grid):

    x0, y0 = pt
    xmax, ymax = len(grid[0]) - 1, len(grid) - 1
    nbrs = []

    for x in range(max(x0 - 1, 0), min(x0 + 1, xmax) + 1):
        for y in range(max(y0 - 1, 0), min(y0 + 1, ymax) + 1):
            if (x, y) != (x0, y0):
                nbrs.append((x, y))

    return nbrs

octopuses = [[int(i) for i in l] for l in load_strings('day11.txt')]
xrange, yrange = len(octopuses[0]), len(octopuses)
cumulative_flashes = 0
iterations = 0

while True:

    flashed, to_flash = set(), set()

    for x in range(xrange):
        for y in range(yrange):
            octopuses[y][x] += 1
            if octopuses[y][x] > 9:
                to_flash.add((x, y))

    while len(to_flash) > 0:
        flashing = to_flash.pop()
        for x, y in neighbours(flashing, octopuses):
            octopuses[y][x] += 1
            if octopuses[y][x] > 9 and (x, y) not in flashed:
                to_flash.add((x, y))
        flashed.add(flashing)

    for x, y in flashed:
        octopuses[y][x] = 0

    cumulative_flashes += len(flashed)
    iterations += 1

    if iterations == 100:
        print(f'Part 1 => {cumulative_flashes}')

    if len(flashed) == xrange * yrange:
        # All octopuses flashed this iteration
        print(f'Part 2 => {iterations}')
        break