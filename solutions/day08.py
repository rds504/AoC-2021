from itertools import permutations
from tools.general import load_strings

DISPLAY_MAP = {
    'abcefg'  : 0,
    'cf'      : 1,
    'acdeg'   : 2,
    'acdfg'   : 3,
    'bcdf'    : 4,
    'abdfg'   : 5,
    'abdefg'  : 6,
    'acf'     : 7,
    'abcdefg' : 8,
    'abcdfg'  : 9
}

UNIQUE_LENGTHS = (2, 3, 4, 7)

displays = load_strings('day08.txt')

# Part 1
unique_count = 0
for dis in displays:
    unique_count += sum((len(seg) in UNIQUE_LENGTHS) for seg in dis.split(' | ')[1].split(' '))

print(f'Part 1 => {unique_count}')

# Part 2
solved_outputs = []

for dis in displays:

    signals, output = dis.split(' | ')

    # 7! = 5040, small enough for a brute force approach (even though it makes me sad)
    for p in permutations('abcdefg'):

        guess = dict(zip(p, 'abcdefg'))
        valid = True

        for signal in signals.split(' '):
            if ''.join(sorted(guess[c] for c in signal)) not in DISPLAY_MAP:
                # This mapping gives an invalid display value, it can't be the one we're looking for
                valid = False
                break

        if valid:
            # Valid mapping, assume only one possible
            solved = 0

            for seg in output.split(' '):
                solved *= 10
                solved += DISPLAY_MAP[''.join(sorted(guess[c] for c in seg))]

            solved_outputs.append(solved)
            break

print(f'Part 2 => {sum(solved_outputs)}')