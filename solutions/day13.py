import re
from tools.general import load_input

def process_input():

    dot_list, fold_list = load_input('day13.txt').split('\n\n')

    dots = set()
    for dot in dot_list.split('\n'):
        x, y = dot.split(',')
        dots.add((int(x), int(y)))

    folds = []
    for fld in fold_list.split('\n'):
        match = re.match(r'fold along ([xy])=([0-9]+)', fld)
        if match:
            folds.append((match.group(1), int(match.group(2))))

    return (dots, folds)

def do_fold(dot_set, axis):

    new_dot_set = set()
    param, val = axis

    for x, y in dot_set:
        if param == 'x':
            # Fold along x=val
            if x > val:
                x = 2 * val - x
        else:
            # Fold along y=val
            if y > val:
                y = 2 * val - y
        new_dot_set.add((x, y))

    return new_dot_set

def print_dots(dot_set):

    xmax = max(x for x, y in dot_set)
    ymax = max(y for x, y in dot_set)

    for y in range(ymax + 1):
        row = ''
        for x in range(xmax + 1):
            row += '#' if (x, y) in dot_set else ' '
        print(row)

dots, folds = process_input()

print(f'Part 1 => {len(do_fold(dots, folds[0]))}')

for fld in folds:
    dots = do_fold(dots, fld)

print('Part 2 =>')
print_dots(dots)