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


def build_graph(grid: np.ndarray[int, Any], start: Point, end: Point) -> dict[Point, dict[Point, int]]:
    """
    Build a weighted graph from the grid
    """

    # Weighted graph
    g: dict[Point, dict[Point, int]] = {start: {}}

    # q of list of paths
    q: list[list[Point]] = [[start]]
    while q:
        path = q.pop()
        parent = path[0]
        pos = path[-1]

        # Add the end to the graph
        if pos == end:
            g[parent] = {} if parent not in g else g[parent]
            g[parent].update({pos: len(path) - 1})
            continue

        neighbors = get_next_positions(grid, pos)

        # pos is a split. connect it the parent
        is_split = len(neighbors) > 2 and len(path) > 1
        if is_split:
            g[parent] = {} if parent not in g else g[parent]
            g[parent].update({pos: len(path) - 1})
            if pos not in g:
                q.append([pos])
        else:
            q += [(path + [x]) for x in neighbors if x not in path]
    return g


def part2(case: str):
    print('')
    """
    Part 2 - now ignoring the slopes will have to be more efficient
    """
    grid = parse_grid(case)
    # Ignore slopes
    grid[np.where((grid == '>') | (grid == '<') | (grid == '^') | (grid == 'v'))] = PATH

    start: Point = (0, np.where(grid[0] == PATH)[0][0])
    end: Point = (len(grid) - 1, np.where(grid[-1] == PATH)[0][0])

    g = build_graph(grid, start, end)

    q: list[tuple[list[Point], int]] = [([start], 0)]
    result = 0
    while q:
        path, steps = q.pop()
        pos = path[-1]

        if pos == end:
            result = max(result, steps)
            continue
        next_positions = [k for k in g[pos] if k not in path]
        q += [(path + [x], steps + g[pos][x]) for x in next_positions]

    return result
