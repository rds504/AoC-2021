from tools.general import load_ints

def grow_fish(initial, days):

    # Count of fish with N days until spawn
    fish = [0] * 9
    for i in initial:
        fish[i] += 1

    for _ in range(days):
        fish = fish[1:] + [fish[0]]
        fish[6] += fish[-1]

    return sum(fish)

initial_fish = load_ints('day06.txt')

print(f'Part 1 => {grow_fish(initial_fish, 80)}')
print(f'Part 2 => {grow_fish(initial_fish, 256)}')