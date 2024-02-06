FREE = '.'
WALL = '#'

input = open('2022/input/day-24.input.txt').read().splitlines()
# We discard the walls
entry = [(0, y)
         for y, _ in enumerate(input[0]) if input[0][y] == FREE][0]
exit = [(len(input)-1, y) for y, _ in enumerate(input[len(input)-1])
        if input[len(input)-1][y] == FREE][0]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def has_blizzard_after(map, x, y, t):
    rows = len(map)
    columns = len(map[0])
    # we decrease 1 and add one to avoid walls
    return map[(x-t-1) % (rows-2) + 1][y] == 'v' \
        or map[(x+t-1) % (rows-2) + 1][y] == '^' \
        or map[x][(y-t-1) % (columns-2)+1] == '>' \
        or map[x][(y+t-1) % (columns-2)+1] == '<'


def part_1():
    def is_in_bounds(x: int, y: int):
        return 0 <= x < len(input) and 0 <= y < len(input[0]) and input[x][y] != WALL

    visited = set([entry])
    positions = [(entry, 0)]
    while positions:
        pos, t = positions.pop(0)
        if (pos == exit):
            return t
        x, y = pos
        next_entries = [(x+dx, y+dy)
                        for dx, dy in directions if
                        is_in_bounds(x+dx, y+dy) and
                        (x+dx, y+dy) not in visited and
                        not has_blizzard_after(input, x+dx, y+dy, t+1)]
        visited.update(next_entries)
        if len(next_entries) == 0:
            positions.append((pos, t+1))
        else:
            positions.extend([(pos, t+1) for pos in next_entries])
    raise Exception("No path found")
