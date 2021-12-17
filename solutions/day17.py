import re
from tools.general import load_input

def get_target_area():

    srch = re.search(
        r'target area: x=([0-9]+)..([0-9]+), y=([\-0-9]+)..([\-0-9]+)',
        load_input('day17.txt')
    )

    if srch:
        return tuple(int(srch.group(i)) for i in range(1, 5))

    return None

def fire_probe(target, initial_velocity):

    txmin, txmax, tymin, tymax = target
    xpos, ypos = 0, 0
    xvel, yvel = initial_velocity
    ymax = 0

    while True:

        xpos += xvel
        ypos += yvel

        if ypos > ymax:
            ymax = ypos

        yvel -= 1
        if xvel != 0:
            xvel -= int(xvel / abs(xvel))

        if xpos >= txmin:
            # Made it at least as far as target
            if xpos > txmax:
                # Overshot target
                break
            if ypos <= tymax:
                if ypos < tymin:
                    # Undershot target
                    break
                # Else hit target
                return (True, ymax)
        elif xvel == 0:
            # Falling short of target
            break

    return (False, ymax)

target_area = get_target_area()
ybound = max(abs(target_area[2]), abs(target_area[3]))

# Parts 1 and 2
max_height, hit_count = 0, 0

for xguess in range(1, target_area[1] + 1):
    for yguess in range(-ybound, ybound + 1):

        hit, height = fire_probe(target_area, (xguess, yguess))

        if hit:
            hit_count += 1
            if height > max_height:
                max_height = height

print(f'Part 1 => {max_height}')
print(f'Part 2 => {hit_count}')