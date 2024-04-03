from lib import parse_grid
import numpy as np
from typing import Any

FREE = '.'
ROCK = '#'

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def get_directions(grid: np.ndarray[str, Any], p: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = p
    return [(x + dx, y + dy) for dx, dy in directions if grid[(x + dx) % len(grid), (y + dy) % len(grid[0])] == FREE]


def run_steps(start: tuple[int, int], grid: np.ndarray[str, Any], steps: int):
    # Hold the visited places and how many steps it took to get there
    visited = {start: 0}
    places = {start}

    for i in range(steps):
        new_places: set[tuple[int, int]] = set()
        for p in places:
            new_places.update([x for x in get_directions(grid, p) if x not in visited])
        places = new_places

        # Add current round to visited
        visited |= {p: i+1 for p in places}
    return visited


def part1(case: str, steps: int) -> int:
    """
    Day 21: Step Counter
    Part 1 - Count the possible position after n steps
    """
    grid = parse_grid(case)
    # Pad with rocks so we wont get out of bounds
    grid = np.pad(grid, 1, constant_values=ROCK)

    # Find the starting position
    start = np.where(grid == 'S')
    grid[start] = FREE

    visited = run_steps(tuple(np.transpose(start)[0]), grid, steps)
    return len([x for x in visited if visited[x] % 2 == 0])


def f(n: int, a: int, b: int, c: int): return a+n*(b-a+(n-1)*(c-b-b+a)//2)


def part2(case: str, steps: int) -> int:
    grid = parse_grid(case)
    start = np.where(grid == 'S')
    grid[start] = FREE

    # The grid is square
    assert len(grid[0]) == len(grid)
    n = len(grid)

    done: list[int] = []
    todo: set[tuple[int, int]] = {tuple(np.transpose(start)[0])}

    def cmod(x: tuple[int, int]): return (x[0] % n, x[1] % n)

    for s in range(3 * n):
        if s % n == 65:
            done.append(len(todo))

        todo = {(p[0]+d[0], p[1]+d[1]) for d in directions
                for p in todo if grid[cmod((p[0]+d[0], p[1]+d[1]))] == FREE}

    return f(steps // n, *done)
