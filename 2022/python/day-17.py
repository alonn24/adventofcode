FREE = '.'
FIXED = '#'
MOVING = '@'
stones = [
    [[FREE, FREE, MOVING, MOVING, MOVING, MOVING, FREE]],
    [[FREE, FREE, FREE, MOVING, FREE, FREE, FREE],
     [FREE, FREE, MOVING, MOVING, MOVING, FREE, FREE],
     [FREE, FREE, FREE, MOVING, FREE, FREE, FREE]],
    [[FREE, FREE, FREE, FREE, MOVING, FREE, FREE],
     [FREE, FREE, FREE, FREE, MOVING, FREE, FREE], [FREE, FREE, MOVING, MOVING, MOVING, FREE, FREE]],
    [[FREE, FREE, MOVING, FREE, FREE, FREE, FREE]
        for _ in range(4)],
    [[FREE, FREE, MOVING, MOVING, FREE, FREE, FREE]
        for _ in range(2)]
]

# 1 for > and -1 for <
input = [v for v in open("2022/input/day-17.input.txt", "r").read()]

# helper to print a board


def pretty_print(board): print(
    '\n'.join([' '.join(row) for row in board]) + '\n')


def is_in_bounds(row, i): return i >= 0 and i < len(row)

# Add a stone 3 rows above the last one (0 is the top one)


def add_stone(board, stone):
    vertical_gap = [[FREE for _ in range(7)] for _ in range(3)]
    return stone + vertical_gap + board


def move_horizontally(board, rows_indices_to_move, direction):
    # Check if all next to MOVING are not FIXED and not out of bounds
    def can_move_row_horizontally(row, dd):
        cant_move = [False for i, v in enumerate(row) if v == MOVING and (
            not is_in_bounds(row, i+dd) or row[i+dd] == FIXED)]
        return len(cant_move) == 0

    # Move MOVING to the next position
    def move_row_horizontally(row, d):
        # run by index
        indices = [i for i in range(
            len(row)) if row[i] == MOVING and is_in_bounds(row, i+d)]
        # reverse if moving right so we run from end to start
        if (d == 1):
            indices.reverse()
        for i in indices:
            row[i], row[i+d] = FREE, MOVING
        return row
    # get delta
    d = 1 if direction == '>' else -1
    can_move_horizontally = len([False for i in rows_indices_to_move if not can_move_row_horizontally(board[i], d)]) == 0
    print(f'move {direction} can move: {can_move_horizontally}')
    if can_move_horizontally:
        for i in rows_indices_to_move:
            board[i] = move_row_horizontally(board[i], d)


def move_down(board, rows_indices_to_move):
    last_row = max(rows_indices_to_move)
    # reach to bottom
    if last_row >= len(board) - 1:
        return False
    can_push_row = all(board[last_row+1][i] == FREE for i,
                       v in enumerate(board[last_row]) if v == MOVING)
    if not can_push_row:
        return False

    # run from bottom to top
    for row in reversed(rows_indices_to_move):
        board[row], board[row+1] = board[row+1], board[row]
    return True


def move_stone(board, direction):
    rows_indices_to_move = [i for i, x in enumerate(board) if MOVING in x]
    move_horizontally(board, rows_indices_to_move, direction)
    return move_down(board, rows_indices_to_move)


def fixed_rows(board):
    def fix_row(row):
         return [FIXED if v == MOVING else v for v in row]
    return [fix_row(row) for row in board]


def play():
    stones_n = 0
    movement_i = 0
    board = []
    while (stones_n < 2):
        # Add a new stone
        print(f'add stone {stones_n}')
        board = add_stone(board, stones[stones_n % len(stones)])
        pretty_print(board)
        # Move store as much as possible
        while (move_stone(board, input[movement_i])):
            pretty_print(board)
            movement_i = (movement_i + 1) % len(input)
        # When can't move anymore, fix the rows so we wont move them further
        board = fixed_rows(board)
        print(f'end stone {stones_n}')
        pretty_print(board)
        stones_n += 1


play()
