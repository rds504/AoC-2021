from tools.general import load_input

vent_lines = []
for l in load_input('day05.txt').split('\n'):
    x0, y0 = l.split(' -> ')[0].split(',')
    x1, y1 = l.split(' -> ')[1].split(',')
    vent_lines.append(((int(x0), int(y0)), (int(x1), int(y1))))

def generate_points(start_point, end_point, include_diagonal=False):

    all_points = []
    x0, y0 = start_point
    x1, y1 = end_point

    # Vertical
    if x0 == x1:
        if y0 > y1:
            # Reverse direction
            y0, y1 = y1, y0
        for y in range(y0, y1 + 1):
            all_points.append((x0, y))

    # Horizontal
    elif y0 == y1:
        if x0 > x1:
            # Reverse direction
            x0, x1 = x1, x0
        for x in range(x0, x1 + 1):
            all_points.append((x, y0))

    # Diagonal (we may assume gradient of 1)
    elif include_diagonal:

        # Order such that x increases
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        # y may be increasing or decreasing (but only by equal magnitude to x)
        y_incr = 1 if y0 < y1 else -1
        y = y0

        for x in range(x0, x1 + 1):
            all_points.append((x, y))
            y += y_incr

    return all_points

# Part 1
points = {}

for vl in vent_lines:

    for pt in generate_points(vl[0], vl[1]):
        if pt in points:
            points[pt] += 1
        else:
            points[pt] = 1

print(f'Part 1 => {sum(1 for p in points if points[p] > 1)}')

# Part 2
points = {}

for vl in vent_lines:

    for pt in generate_points(vl[0], vl[1], include_diagonal=True):
        if pt in points:
            points[pt] += 1
        else:
            points[pt] = 1

print(f'Part 2 => {sum(1 for p in points if points[p] > 1)}')