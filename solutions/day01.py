from tools.general import load_ints

def count_increases(sequence):
    return sum((sequence[i - 1] < sequence[i]) for i in range(1, len(sequence)))

depths = load_ints('day01.txt', delim='\n')
print(f'Part 1 => {count_increases(depths)}')

threes = [sum(depths[i - 2:i + 1]) for i in range(2, len(depths))]
print(f'Part 2 => {count_increases(threes)}')