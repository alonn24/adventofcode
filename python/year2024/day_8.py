import numpy as np
from python.common.geometry import Point, is_in_bounds, add_tuples
from python.common.grid import parse_grid


def get_antinode(pos1: Point, pos2: Point) -> list[Point]:
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    if dx == 0:
        miny = min(pos1[1], pos2[1])
        maxy = max(pos1[1], pos2[1])
        return [(pos1[0], miny - dy), (pos1[0], maxy + dy)]
    m = dy / dx
    intercept = pos1[1] - m * pos1[0]
    def get_y(x: int) -> int: return int(m * x + intercept)
    x1 = min(pos1[0], pos2[0]) - dx
    x2 = max(pos1[0], pos2[0]) + dx
    return [(x1, get_y(x1)), (x2, get_y(x2))]


def part1(testcase: str):
    grid = parse_grid(testcase)
    # Get uniq locations of the unique chars
    unique_chars = np.unique(grid)
    unique_chars = unique_chars[unique_chars != '.']
    # locations = {char: np.argwhere(grid == char) for char in unique_chars}

    antinode: set[Point] = set()
    # Loop over locations
    for char in unique_chars:
        locations = np.argwhere(grid == char)
        for i in range(len(locations)):
            loc1 = locations[i]
            for j in range(i + 1, len(locations)):
                loc2 = locations[j]
                antinode.update(get_antinode(loc1, loc2))
    # Filter only in bounds
    in_bound_antinode = [
        loc for loc in antinode if is_in_bounds(
            grid.shape, loc)]
    return len(in_bound_antinode)


def get_antinode_on_line(
        shape: tuple[int, int], pos1: Point, pos2: Point) -> list[Point]:
    result: set[Point] = set()
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]

    cur = (pos2[0], pos2[1])
    while is_in_bounds(shape, cur):
        result.add(cur)
        cur = add_tuples(cur, (dx, dy))
    cur = (pos1[0], pos1[1])
    while is_in_bounds(shape, cur):
        result.add(cur)
        cur = add_tuples(cur, (-dx, -dy))
    return list(result)


def part2(testcase: str):
    grid = parse_grid(testcase)
    # Get uniq locations of the unique chars
    unique_chars = np.unique(grid)
    unique_chars = unique_chars[unique_chars != '.']
    # locations = {char: np.argwhere(grid == char) for char in unique_chars}

    antinode: set[Point] = set()
    # Loop over locations
    for char in unique_chars:
        locations = np.argwhere(grid == char)
        for i in range(len(locations)):
            loc1 = locations[i]
            for j in range(i + 1, len(locations)):
                loc2 = locations[j]
                antinode.update(get_antinode_on_line(grid.shape, loc1, loc2))
    # Filter only in bounds
    in_bound_antinode = [
        loc for loc in antinode if is_in_bounds(
            grid.shape, loc)]
    return len(in_bound_antinode)
