from collections import defaultdict
from tools.general import load_strings

def add_and_wrap_to_one(lhs, rhs, mod=10):
    return ((lhs + rhs - 1) % mod) + 1

def play_deterministic(initial_positions):

    position = list(initial_positions)
    score    = [0, 0]
    turn     = 0
    rolls    = 0

    while max(score) < 1000:

        move = 0
        for _ in range(3):
            move += (rolls % 100) + 1
            rolls += 1

        position[turn] = add_and_wrap_to_one(position[turn], move)
        score[turn] += position[turn]

        turn = (turn + 1) % 2

    return min(score) * rolls

def possible_rolls(sides):

    rolls = defaultdict(int)

    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            for k in range(1, sides + 1):
                rolls[i + j + k] += 1

    return rolls

def play_multiverse(initial_positions):

    in_play = { (tuple(initial_positions), (0, 0)) : 1 }
    wins    = [0, 0]
    turn    = 0
    rolls   = possible_rolls(3)

    while len(in_play) > 0:

        still_in_play = defaultdict(int)

        for game in in_play:

            position, score = game

            for roll in rolls:

                new_pos, new_scr = list(position), list(score)
                new_pos[turn] = add_and_wrap_to_one(new_pos[turn], roll)
                new_scr[turn] += new_pos[turn]
                games = in_play[game] * rolls[roll]

                if new_scr[turn] >= 21:
                    wins[turn] += games
                else:
                    still_in_play[tuple(new_pos), tuple(new_scr)] += games

        in_play = still_in_play
        turn = (turn + 1) % 2

    return max(wins)

starting_positions = [int(line.split(': ')[-1]) for line in load_strings('day21.txt')]

print(f'Part 1 => {play_deterministic(starting_positions)}')
print(f'Part 2 => {play_multiverse(starting_positions)}')