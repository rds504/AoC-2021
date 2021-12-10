from math import inf
from tools.general import load_ints

initial_crabs = load_ints('day07.txt')

def minimal_crab_movement(crabs, cost_func):

    min_cost = inf

    for pos in range(max(crabs)):
        cost = sum(cost_func(c, pos) for c in crabs)
        if cost < min_cost:
            min_cost = cost

    return min_cost

def triang_num(n):
    # Maths: 1 + 2 + ... + n = T(n) = n(n + 1)/2
    return int(n * (n + 1) / 2)

print(f'part 1 => {minimal_crab_movement(initial_crabs, (lambda x, y : abs(x - y)))}')
print(f'part 2 => {minimal_crab_movement(initial_crabs, (lambda x, y : triang_num(abs(x - y))))}')