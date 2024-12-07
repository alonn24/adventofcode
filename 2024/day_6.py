import numpy as np
from typing import NamedTuple, Any


class Grid:
    def __init__(self, grid: np.ndarray[str, Any]):
        self.grid = grid
        self.limits = [0, grid.shape[0], 0, grid.shape[1]]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def is_in_bounds(self, pos: tuple[int, int]):
        return self.limits[0] <= pos[0] < self.limits[1] and self.limits[2] <= pos[1] < self.limits[3]

    def get_pos(self, pos: tuple[int, int]):
        return self.grid[pos[0], pos[1]]

    def set_pos(self, pos: tuple[int, int], value: Any):
        self.grid[pos[0], pos[1]] = value

    def get_start_pos(self):
        return np.argwhere(self.grid == START_POS)[0]


class Move(NamedTuple):
    direction: tuple[int, int]
    turn: str

    def get_next_pos(self, pos: tuple[int, int]):
        return (pos[0] + self.direction[0], pos[1] + self.direction[1])


START_POS = '^'
WALL = '#'
VISITED = 'X'
moves = {
    '^': Move(direction=(-1, 0), turn='>'),
    '>': Move(direction=(0, 1), turn='v'),
    'v': Move(direction=(1, 0), turn='<'),
    '<': Move(direction=(0, -1), turn='^'),
}


def part1(testcase: str):
    grid = np.array([list(row) for row in testcase.splitlines()])
    grid = Grid(grid)

    pos = grid.get_start_pos()
    while (grid.is_in_bounds(pos)):
        move = moves[grid.get_pos(pos)]
        next_pos = move.get_next_pos(pos)

        # Out of bounds
        if not grid.is_in_bounds(next_pos):
            grid.set_pos(pos, VISITED)
            pos = next_pos
        elif grid.get_pos(next_pos) == WALL:
            # Next position is a wall - rotate
            grid.set_pos(pos, move.turn)
        else:
            # Next position is free - move
            grid.set_pos(next_pos, grid.get_pos(pos))
            grid.set_pos(pos, VISITED)
            pos = next_pos
    # return all visited positions
    return np.count_nonzero(grid.grid == VISITED)
