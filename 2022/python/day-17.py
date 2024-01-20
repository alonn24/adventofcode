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
    # Add the stone with the gap. duplicate row content
    to_add = [[*i] for i in stone] + [[FREE for _ in range(7)] for _ in range(3)]
    # Get all rows indices with stones
    rows_with_stones = [i for i, row in enumerate(
        board) if not all(v == FREE for v in row)]
    # Add the stone ad cut off the board to only where the stones are
    return to_add + (board if len(rows_with_stones) == 0 else board[rows_with_stones[0]:])


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
    can_move_horizontally = len(
        [False for i in rows_indices_to_move if not can_move_row_horizontally(board[i], d)]) == 0
    if can_move_horizontally:
        for i in rows_indices_to_move:
            board[i] = move_row_horizontally(board[i], d)


def move_down(board, rows_indices_to_move):
    # reach to bottom
    if rows_indices_to_move[-1] >= len(board) - 1:
        return False
    blocked = False
    for i in rows_indices_to_move:
        for j,_ in enumerate(board[i]):
            blocked = blocked or board[i][j] == MOVING and board[i+1][j] == FIXED
    if blocked:
        return False

    # run from bottom to top
    for i in reversed(rows_indices_to_move):
        for j,_ in enumerate(board[i]):
            if board[i][j] == MOVING:
                board[i][j] = FREE
                board[i+1][j] = MOVING
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
    # 0 - 2021 is 2022 stones
    while (stones_n < 2022):
        print(f'stone {stones_n}', end='\r')
        # Add a new stone
        stone_to_add = stones[stones_n % len(stones)]
        board = add_stone(board, stone_to_add)
        # Move store as much as possible
        move = True
        while (move):
            move = move_stone(board, input[movement_i])
            movement_i = (movement_i + 1) % len(input)
        # When can't move anymore, fix the rows so we wont move them further
        board = fixed_rows(board)
        stones_n += 1
    rows_with_stones = [i for i, row in enumerate(
        board) if not all(v == FREE for v in row)]

    print('')
    print(len(rows_with_stones))


play()
