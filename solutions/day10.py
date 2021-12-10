from statistics import median
from tools.general import load_strings

CLOSING_DELIM = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }
ERROR_POINTS = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }
COMPLETE_POINTS = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }

err_score = 0
com_score = []

for line in load_strings('day10.txt'):

    corrupt = False
    stack = []

    for char in line:

        if char in CLOSING_DELIM:
            stack.append(char)
        elif char == CLOSING_DELIM[stack[-1]]:
            stack.pop()
        else:
            corrupt = True
            err_score += ERROR_POINTS[char]
            break

    if not corrupt:
        cs = 0
        for char in stack[::-1]:
            cs *= 5
            cs += COMPLETE_POINTS[CLOSING_DELIM[char]]
        com_score.append(cs)

print(f'Part 1 => {err_score}')
print(f'Part 2 => {median(com_score)}')