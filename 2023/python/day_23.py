from lib import parse_grid, is_in_bounds, add_tuples, Point
import numpy as np
from typing import Any

PATH = '.'
FOREST = '#'
SLOPES = ['^', '>', 'v', '<']
SLOPES_DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_next_positions(grid: np.ndarray[int, Any],
                       pos: Point) -> list[Point]:
    val = grid[pos]

    # If slope we have to move in that direction
    directions = [SLOPES_DIR[SLOPES.index(val)]] if val in SLOPES else SLOPES_DIR
    next_positions = [add_tuples(pos, x) for x in directions]
    # Filter inbound, free and not in path
    return [x for x in next_positions if
            is_in_bounds(grid, x) and
            grid[x] != FOREST]


def part1(case: str):
    """
    Day 23: A Long Walk
    Part 1 - calculate the longest path from start to end
    """
    grid = parse_grid(case)
    start: Point = (0, np.where(grid[0] == PATH)[0][0])
    end: Point = (len(grid) - 1, np.where(grid[-1] == PATH)[0][0])

    q = [[start]]

    result = 0
    while q:
        path = q.pop(0)
        pos = path[-1]
        # Got to the end
        if pos == end:
            result = max(result, len(path) - 1)

        # Filter not in path
        next_positions = [x for x in get_next_positions(grid, pos) if x not in path]
        q += [path + [x] for x in next_positions]

    return result


def part2(case: str):
    """
    Part 2 - now ignoring the slopes will have to be more efficient
    """
    grid = parse_grid(case)

    # Ignore slopes
    grid[np.where((grid == '>') | (grid == '<') | (grid == '^') | (grid == 'v'))] = PATH

    start: Point = (0, np.where(grid[0] == PATH)[0][0])
    end: Point = (len(grid) - 1, np.where(grid[-1] == PATH)[0][0])

    q = [[start]]
    result = 0
    while q:
        print(result, len(q))
        path = q.pop(0)
        # pos = path[-1]

        # Filter not in path
        next_positions = [x for x in get_next_positions(grid, path[-1]) if x not in path]
        # Go over hallways
        while len(next_positions) == 1:
            path.append(next_positions[0])
            pos = next_positions[0]
            next_positions = [x for x in get_next_positions(grid, pos) if x not in path]

        # Got to the end
        if path[-1] == end:
            result = max(result, len(path) - 1)

        if len(next_positions) == 0:
            continue
        q += [path + [x] for x in next_positions]

    return result
