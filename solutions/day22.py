import re
from tools.general import load_strings

def load_steps():

    pattern = r'(on|off) x=([\-0-9]+)..([\-0-9]+),y=([\-0-9]+)..([\-0-9]+),z=([\-0-9]+)..([\-0-9]+)'
    steps = []

    for line in load_strings('day22.txt'):

        match = re.match(pattern, line)
        if match:
            steps.append((match.group(1) == 'on', tuple(int(match.group(i)) for i in range(2, 8))))

    return tuple(steps)

def volume(cuboid):
    xmin, xmax, ymin, ymax, zmin, zmax = cuboid
    return (xmax - xmin + 1) * (ymax - ymin + 1) * (zmax - zmin + 1)

def intersection(lhs, rhs):

    lxmin, lxmax, lymin, lymax, lzmin, lzmax = lhs
    rxmin, rxmax, rymin, rymax, rzmin, rzmax = rhs

    ixmin, ixmax = max(lxmin, rxmin), min(lxmax, rxmax)
    if ixmin <= ixmax:
        iymin, iymax = max(lymin, rymin), min(lymax, rymax)
        if iymin <= iymax:
            izmin, izmax = max(lzmin, rzmin), min(lzmax, rzmax)
            if izmin <= izmax:
                return (ixmin, ixmax, iymin, iymax, izmin, izmax)

    return None

def remainder(lhs, rhs):

    inter = intersection(lhs, rhs)

    if inter is None:
        # Disjoint, therefore remainder is simply the whole starting cuboid
        return [lhs]

    # Break down remainder of cuboid into sub-suboids
    rem_cuboids = []

    lxmin, lxmax, lymin, lymax, lzmin, lzmax = lhs
    ixmin, ixmax, iymin, iymax, izmin, izmax = inter

    if lxmin < ixmin:
        # Remainder to the left, up to bounds of lhs in y and z dimensions
        rem_cuboids.append((lxmin, ixmin - 1, lymin, lymax, lzmin, lzmax))

    if lxmax > ixmax:
        # Remainder to the right, up to bounds of lhs in y and z dimensions
        rem_cuboids.append((ixmax + 1, lxmax, lymin, lymax, lzmin, lzmax))

    if lymin < iymin:
        # Remainder below, up to bounds of lhs in z dimension
        rem_cuboids.append((ixmin, ixmax, lymin, iymin - 1, lzmin, lzmax))

    if lymax > iymax:
        # Remainder above, up to bounds of lhs in z dimension
        rem_cuboids.append((ixmin, ixmax, iymax + 1, lymax, lzmin, lzmax))

    if lzmin < izmin:
        # Remainder in front
        rem_cuboids.append((ixmin, ixmax, iymin, iymax, lzmin, izmin-1))

    if lzmax > izmax:
        # Remainder behind
        rem_cuboids.append((ixmin, ixmax, iymin, iymax, izmax + 1, lzmax))

    return rem_cuboids

def perform_steps(steps, bounds=None):

    # Set of *disjoint* cuboids containing all "on" cubes
    on_cuboids = set()

    for on, cuboid in steps:

        if bounds is not None:

            cuboid = intersection(cuboid, bounds)

            if cuboid is None:
                continue

        if on:

            # Find the subset disjoint from all current on cuboids
            disjoint = [cuboid]

            for on_cbd in on_cuboids:

                new_disj = []

                for djt in disjoint:
                    new_disj += remainder(djt, on_cbd)

                disjoint = new_disj

            on_cuboids.update(disjoint)

        else:

            # Find any current on cuboid that intersects this and remove the intersection
            still_on = set()

            for on_cbd in on_cuboids:
                still_on.update(remainder(on_cbd, cuboid))

            on_cuboids = still_on

    return sum(volume(cbd) for cbd in on_cuboids)

reboot_steps = load_steps()

print(f'part 1 => {perform_steps(reboot_steps, (-50, 50, -50, 50, -50, 50))}')
print(f'part 2 => {perform_steps(reboot_steps)}')