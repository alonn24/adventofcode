import numpy as np


def get_antinode(pos1: tuple[int, int], pos2: tuple[int, int]) -> list[tuple[int, int]]:
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    if dx == 0:
        miny = min(pos1[1], pos2[1])
        maxy = max(pos1[1], pos2[1])
        return [(pos1[0], miny-dy), (pos1[0], maxy+dy)]
    m = dy / dx
    intercept = pos1[1] - m * pos1[0]
    def get_y(x: int) -> int: return int(m * x + intercept)
    x1 = min(pos1[0], pos2[0]) - dx
    x2 = max(pos1[0], pos2[0]) + dx
    return [(x1, get_y(x1)), (x2, get_y(x2))]


def part1(testcase: str):
    grid = np.array([list(row) for row in testcase.splitlines()])
    # Get uniq locations of the unique chars
    unique_chars = np.unique(grid)
    unique_chars = unique_chars[unique_chars != '.']
    # locations = {char: np.argwhere(grid == char) for char in unique_chars}

    antinode: set[tuple[int, int]] = set()
    # Loop over locations
    for char in unique_chars:
        locations = np.argwhere(grid == char)
        for i in range(len(locations)):
            loc1 = locations[i]
            for j in range(i + 1, len(locations)):
                loc2 = locations[j]
                antinode.update(get_antinode(loc1, loc2))
    # Filter only in bounds
    in_bound_antinode = [loc for loc in antinode if 0 <= loc[0] < grid.shape[0] and 0 <= loc[1] < grid.shape[1]]
    return len(in_bound_antinode)
