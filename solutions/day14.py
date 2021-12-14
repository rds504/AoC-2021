from collections import defaultdict
from tools.general import load_input

def polymerize(starter, rules, iterations):

    pairs = defaultdict(int)
    for i in range(len(starter) - 1):
        pairs[starter[i : i + 2]] += 1

    for _ in range(iterations):
        new_pairs = defaultdict(int)
        for pair in pairs:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs

    counts = defaultdict(int)

    # To avoid double counting, just count the first element of every pair
    for pair in pairs:
        counts[pair[0]] += pairs[pair]

    # And account for the last element
    counts[starter[-1]] += 1

    return max(counts.values()) - min(counts.values())

template, rules = load_input('day14.txt').split('\n\n')
insertion_rules = { line.split(' -> ')[0] : line.split(' -> ')[1] for line in rules.split('\n') }

print(f'Part 1 => {polymerize(template, insertion_rules, 10)}')
print(f'Part 2 => {polymerize(template, insertion_rules, 40)}')