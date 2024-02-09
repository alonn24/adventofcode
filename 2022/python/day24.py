FREE = '.'
WALL = '#'

input = open('2022/input/day-24.input.txt').read().splitlines()
# We discard the walls
entry = [(0, y)
         for y, _ in enumerate(input[0]) if input[0][y] == FREE][0]
exit = [(len(input)-1, y) for y, _ in enumerate(input[len(input)-1])
        if input[len(input)-1][y] == FREE][0]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]


def has_blizzard_after(map, x, y, t):
    rows = len(map)
    columns = len(map[0])
    # we decrease 1 and add one to avoid walls
    return map[(x-t-1) % (rows-2) + 1][y] == 'v' \
        or map[(x+t-1) % (rows-2) + 1][y] == '^' \
        or map[x][(y-t-1) % (columns-2)+1] == '>' \
        or map[x][(y+t-1) % (columns-2)+1] == '<'


def part_1():
    def is_in_bounds(x, y):
        return 0 <= x < len(input) and 0 <= y < len(input[0]) and input[x][y] != WALL

    positions = set([entry])
    t = 0
    while exit not in positions:
        positions = set([(x+dx, y+dy) for x, y in positions for dx,
                        dy in directions if is_in_bounds(x+dx, y+dy)
                        and not has_blizzard_after(input, x+dx, y+dy, t+1)])
        t += 1
    return t
