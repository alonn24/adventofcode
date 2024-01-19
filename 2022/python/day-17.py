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


# Add a stone 3 rows above the last one (0 is the top one)
def add_stone(board, stone):
    vertical_gap = [[FREE for _ in range(7)] for _ in range(3)]
    return stone + vertical_gap + board


def can_move_row_horizontally(row, d):
    cant_move = [False for i, v in enumerate(row) if v == MOVING and (
        i+d < 0 or i+d >= len(row) or row[i+d] == FIXED)]
    return len(cant_move) == 0


def move_row_horizontally(row, d):
    # run by index, reverse if move left to not override values
    indices = [i for i in range(len(row))]
    if (d == 1):
        indices.reverse()
    for i in indices:
        if row[i] == MOVING and i+d >= 0 and i+d < len(row) and row[i] == MOVING:
            row[i], row[i+d] = FREE, MOVING
    return row


def move_horizontally(board, rows_indices_to_move, direction):
    d = 1 if direction == '>' else -1
    can_move_horizontally = [can_move_row_horizontally(board[i], i+d)
                             for i in rows_indices_to_move]
    if (can_move_horizontally):
        for i in rows_indices_to_move:
            board[i] = move_row_horizontally(board[i], d)


def move_stone(board, direction):
    rows_indices_to_move = [i for i, x in enumerate(board) if MOVING in x]
    move_horizontally(board, rows_indices_to_move, direction)
    return False


def fixed_rows(board):
    return board


def play():
    stones_n = 0
    movement_i = 0
    board = []
    while (stones_n < 1):
        # Add a new stone
        board = add_stone(board, stones[stones_n])
        stones_n += 1
        # Move store as much as possible
        while (move_stone(board, input[movement_i])):
            movement_i = (movement_i + 1) % len(input)
        # When can't move anymore, fix the rows so we wont move them further
        fixed_rows(board)
    pretty_print(board)


play()
