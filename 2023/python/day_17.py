import numpy as np
import heapq
from typing import Any

Pos = tuple[int, int]
Dir = tuple[int, int]

# Movement directions
LEFT: Dir = (0, -1)
RIGHT: Dir = (0, 1)
UP: Dir = (-1, 0)
DOWN: Dir = (1, 0)

# Vertical directions
VERTICALS: dict[Dir | None, list[Dir]] = {
    UP: [LEFT, RIGHT],
    DOWN: [RIGHT, LEFT],
    LEFT: [UP, DOWN],
    RIGHT: [DOWN, UP],
    None: [UP, DOWN, LEFT, RIGHT],
}


def is_in_bounds(grid: np.ndarray[Any, Any], pos: Pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0]+b[0], a[1]+b[1])


EntryKey = tuple[Pos, Dir, int]


def find_heat_loss(case: str, min_same_dir: int = 0, max_same_dir: int = 3):
    """
    Day 17: Clumsy Crucible
        Calculate the minimum heat loss moving thought lava
    """
    grid = np.array([list(row) for row in case.splitlines()], dtype=np.int64)
    start = (0, 0)
    destination = (len(grid)-1, len(grid[0])-1)

    # The key to the visited array is (position, direction, steps_in_same_direction)
    # Because we are working with priority queue, if we get here again, it must be a longer part
    visited: set[EntryKey] = set()

    # Create a priority queue so we can always continue from the shortest path
    # We add entries for down and right so we can continue in 2 directions,
    # 	The dir count is 0 so it doesn't count
    pq: list[tuple[int, EntryKey]] = [(0, (start, DOWN, 0)), (0, (start, RIGHT, 0))]

    while pq:
        score, current_pos = heapq.heappop(pq)
        (current, dir, dir_steps) = current_pos
        # Got to destination
        if current == destination:
            return score
        # Already visited
        if (current_pos in visited):
            continue
        visited.add(current_pos)

        next_pos: list[EntryKey] = []
        # Can turn after min same dir steps
        if dir_steps >= min_same_dir:
            next_pos: list[EntryKey] = [(add(current, d), d, 1) for d in VERTICALS[dir]]

        # Can continue in the same direction
        if dir_steps < max_same_dir:
            next_pos.append((add(current, dir), dir, dir_steps+1))

        # Filter visited and position
        next_pos = [pos for pos in next_pos if is_in_bounds(grid, pos[0]) and pos not in visited]

        # Add to the next loop
        for pos in next_pos:
            new_score = score + grid[pos[0][0]][pos[0][1]]
            heapq.heappush(pq, (new_score, pos))
    raise ValueError("No path found")
