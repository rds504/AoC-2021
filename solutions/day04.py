from tools.general import load_input

bingo_input = load_input('day04.txt')
called = [int(i) for i in bingo_input.split('\n')[0].split(',')]
boards = [[[int(j) for j in i.split(' ') if j != ''] for i in l.split('\n')] for l in bingo_input.split('\n\n')[1:]]

def mark_number(board, num):

    for r in board:
        for c, v in enumerate(r):
            if v == num:
                r[c] = 0

def has_won(board):

    # Rows
    for r in board:
        if r.count(0) == len(r):
            return True

    # Columns
    for c in range(len(board[0])):
        col = [r[c] for r in board]
        if col.count(0) == len(col):
            return True

    return False

def score(board, last_call):
    return last_call * sum(sum(r) for r in board)

# Part 1
playing = boards.copy()
win  = False

for i in called:

    for board in playing:

        mark_number(board, i)

        if has_won(board):
            # First board to win
            print(f'part 1 => {score(board, i)}')
            win = True
            break

    if win:
        break

# Part 2
playing = boards.copy()

for i in called:

    still_playing = []

    for board in playing:

        mark_number(board, i)

        if not has_won(board):
            still_playing.append(board)
        elif len(playing) == 1:
            # Last board to win
            print(f'part 2 => {score(board, i)}')
            break

    if len(still_playing) == 0:
        break

    playing = still_playing