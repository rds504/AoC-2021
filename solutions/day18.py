from copy import deepcopy
from functools import reduce
from itertools import permutations
from tools.general import load_strings

def parse_sailfish_num(num_str):
    # Snailfish numbers use a Python-style notation, so we can just avert our eyes and...
    return eval(num_str)

def try_explode(number, ancestors=None):

    if ancestors is None:
        ancestors = []

    if isinstance(number, int):
        return False

    if len(ancestors) < 4:
        return any(try_explode(number[i], ancestors + [(number, i)]) for i in range(2))

    # Add to left
    for (anc, i) in reversed(ancestors):

        if i == 1:

            if isinstance(anc[0], int):
                anc[0] += number[0]
                break

            anc = anc[0]
            while not isinstance(anc[1], int):
                anc = anc[1]

            anc[1] += number[0]
            break

    # Add to right
    for (anc, i) in reversed(ancestors):

        if i == 0:

            if isinstance(anc[1], int):
                anc[1] += number[1]
                break

            anc = anc[1]
            while not isinstance(anc[0], int):
                anc = anc[0]

            anc[0] += number[1]
            break

    anc, i = ancestors[-1]
    anc[i] = 0

    return True

def try_split(number, ancestors = None):

    if ancestors is None:
        ancestors = []

    if isinstance(number, list):
        return any(try_split(number[i], ancestors + [(number, i)]) for i in range(2))

    if number < 10:
        return False

    anc, i = ancestors[-1]
    anc[i] = [int(number / 2), int((number + 1) / 2)]

    return True

def try_reduce(number):
    return try_explode(number) or try_split(number)

def magnitude(number):

    if isinstance(number, int):
        return number

    return 3 * magnitude(number[0]) + 2 * magnitude(number[1])

def pairwise_sum(sequence):

    result = deepcopy(sequence[0])

    for num in sequence[1:]:
        result = [result, deepcopy(num)]
        while try_reduce(result):
            pass

    return magnitude(result)

numbers = [parse_sailfish_num(line) for line in load_strings('day18.txt')]

print(f'part 1 => {pairwise_sum(numbers)}')
print(f'part 2 => {reduce(max, (pairwise_sum(prm) for prm in permutations(numbers, 2)))}')