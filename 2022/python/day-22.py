import re

VOID = ' '
FREE = '.'
WALL = '#'

RIGHT = [0, 1]
DOWN = [1, 0]
LEFT = [0, -1]
UP = [-1, 0]


def rotate(direction, instruction):
    if instruction == 'L':
        return directions[(directions.index(direction) - 1) % 4]
    elif instruction == 'R':
        return directions[(directions.index(direction) + 1) % 4]
    else:
        return direction


def opposite_direction(direction):
    return directions[(directions.index(direction) + 2) % 4]


directions = [RIGHT, DOWN, LEFT, UP]

input = open('2022/input/day-22.input.txt').read()
[str_board, str_instructions] = input.split('\n\n')
max_row = max([len(x) for x in str_board.splitlines()])
board = [row.ljust(max_row, VOID) for row in str_board.splitlines()]
instructions = re.findall(r'\d+|L|R', str_instructions)


def part_1():
    def is_in_bound(point):
        [x, y] = point
        return x >= 0 and y >= 0 and x < len(board) and y < len(board[0])

    def fly_back(point, direction):
        [x, y] = point
        opposite = opposite_direction(direction)
        while is_in_bound([x, y]) and board[x][y] != VOID:
            x += opposite[0]
            y += opposite[1]
        return [x - opposite[0], y - opposite[1]]

    def step_to(point, direction, steps):
        [x, y] = point
        for _ in range(steps):
            x += direction[0]
            y += direction[1]
            if not is_in_bound([x, y]) or board[x][y] == VOID:
                [x, y] = fly_back(
                    [x - direction[0], y - direction[1]], direction)
            elif board[x][y] == WALL:
                return [x - direction[0], y - direction[1]]
        return [x, y]

    def get_scope(point, direction):
        # sum of 1000 times the row, 4 times the column, and the facing
        return (1000 * (point[0]+1)) + (4 * (point[1]+1)) + directions.index(direction)

    # You begin the path in the leftmost open tile of the top row of tiles
    point = [0, [i for i, x in enumerate(board[0]) if x == FREE][0]]
    # Initially, you are facing to the right
    direction = RIGHT

    for instruction in instructions:
        if instruction.isdigit():
            point = step_to(point, direction, int(instruction))
        else:
            direction = rotate(direction, instruction)
    return get_scope(point, direction)

# 128350 too low
print(f'Part 1: {part_1()}')
