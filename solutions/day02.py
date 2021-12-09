from tools.general import load_input

commands = [(d, int(m)) for d, m in (line.split() for line in load_input('day02.txt').split('\n'))]

# Part 1
hpos, vpos = 0, 0
for d, m in commands:
    if d == 'forward':
        hpos += m
    elif d == 'down':
        vpos += m
    else: # d == 'up'
        vpos -= m

print(f'Part 1 => {hpos * vpos}')

# Part 2
aim, hpos, vpos = 0, 0, 0
for d, m in commands:
    if d == 'forward':
        hpos += m
        vpos += aim * m
    elif d == 'down':
        aim += m
    else: # d == 'up'
        aim -= m

print(f'Part 2 => {hpos * vpos}')