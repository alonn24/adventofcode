from lib import parse_grid, is_in_bounds, add_tuples
import numpy as np

PATH = '.'
FOREST = '#'
SLOPES = ['^', '>', 'v', '<']
SLOPES_DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1(case: str):
    """
    Day 23: A Long Walk
    Part 1 - calculate the longest path from start to end
    """
    grid = parse_grid(case)
    start: tuple[int, int] = (0, np.where(grid[0] == PATH)[0][0])
    end: tuple[int, int] = (len(grid) - 1, np.where(grid[-1] == PATH)[0][0])

    q = [[start]]

    result = 0
    while q:
        path = q.pop(0)
        pos = path[-1]
        # Got to the end
        if pos == end:
            result = max(result, len(path) - 1)

        val = grid[pos]

        # If slope we have to move in that direction
        directions = [SLOPES_DIR[SLOPES.index(val)]] if val in SLOPES \
            else SLOPES_DIR
        next_positions = [add_tuples(pos, x) for x in directions]
        # Filter inbound, free and not in path
        next_positions = [x for x in next_positions if
                          is_in_bounds(grid, x) and
                          grid[x] != FOREST and
                          x not in path]
        q += [path + [x] for x in next_positions]

    return result


def part2(case: str):
    """
    Part 2 - now ignoring the slopes will have to be more efficient
    """
    grid = parse_grid(case)
    start: tuple[int, int] = (0, np.where(grid[0] == PATH)[0][0])
    end: tuple[int, int] = (len(grid) - 1, np.where(grid[-1] == PATH)[0][0])

    q = [[start]]

    result = 0
    while q:
        path = q.pop(0)
        pos = path[-1]
        # Got to the end
        if pos == end:
            result = max(result, len(path) - 1)

        next_positions = [add_tuples(pos, x) for x in SLOPES_DIR]
        # Filter inbound, free and not in path
        next_positions = [x for x in next_positions if
                          is_in_bounds(grid, x) and
                          grid[x] != FOREST and
                          x not in path]
        q += [path + [x] for x in next_positions]

    return result
