import numpy as np
from typing import NamedTuple, Any
from collections import defaultdict


class Grid:
    def __init__(self, grid: np.ndarray[str, Any]):
        self.grid = grid
        self.limits = [0, grid.shape[0], 0, grid.shape[1]]

    def __str__(self):
        return self.grid.__str__()

    def is_in_bounds(self, pos: tuple[int, int]):
        return self.limits[0] <= pos[0] < self.limits[1] and self.limits[2] <= pos[1] < self.limits[3]

    def get_pos_move(self, pos: tuple[int, int]) -> str:
        return self.grid[pos[0], pos[1]]

    def set_pos_move(self, pos: tuple[int, int], value: str):
        self.grid[pos[0], pos[1]] = value

    def set_pos_visited(self, pos: tuple[int, int]):
        self.grid[pos[0], pos[1]] = VISITED

    def get_start_pos(self):
        return tuple(np.argwhere(self.grid == START_POS)[0].tolist())


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
        pos_mov = grid.get_pos_move(pos)
        move = moves[pos_mov]
        next_pos = move.get_next_pos(pos)

        # Out of bounds
        if not grid.is_in_bounds(next_pos):
            grid.set_pos_visited(pos)
            pos = next_pos
        elif grid.get_pos_move(next_pos) == WALL:
            # Next position is a wall - rotate
            grid.set_pos_move(pos, move.turn)
        else:
            # Next position is free - move
            grid.set_pos_move(next_pos, pos_mov)
            grid.set_pos_visited(pos)
            pos = next_pos
    # return all visited positions
    return np.count_nonzero(grid.grid == VISITED)


def lead_to_loop(initial_pos: tuple[int, int],
                 initial_turn: str,
                 grid: Grid,
                 visited_moves: defaultdict[tuple[int, int], set[str]]) -> bool:
    pos = initial_pos
    turn = initial_turn

    # As long as we are in bound and not blocked by a wall
    while (grid.is_in_bounds(pos)):
        next_pos = moves[turn].get_next_pos(pos)
        if turn in visited_moves[pos]:
            # If already visited this place with the same turn, we are good
            return True
        elif not grid.is_in_bounds(next_pos):
            # Next step is out of bounds
            return False
        elif grid.get_pos_move(next_pos) == WALL:
            # Got to a wall so we need to turn
            turn = moves[turn].turn
        else:
            # Step forward
            pos = next_pos
    return False


def part2(testcase: str):
    grid = np.array([list(row) for row in testcase.splitlines()])
    grid = Grid(grid)

    count = 0

    # Move and mark the visited places
    pos = grid.get_start_pos()
    visited_moves: defaultdict[tuple[int, int], set[str]] = defaultdict(lambda: set())
    while (grid.is_in_bounds(pos)):
        pos_mov = grid.get_pos_move(pos)
        visited_moves[pos].add(pos_mov)

        move = moves[pos_mov]
        next_pos = move.get_next_pos(pos)

        # Out of bounds
        if not grid.is_in_bounds(next_pos):
            grid.set_pos_visited(pos)
            pos = next_pos
        elif grid.get_pos_move(next_pos) == WALL:
            # Next position is a wall - rotate
            grid.set_pos_move(pos, move.turn)
        else:
            # Check if we have visited this position with this move
            # If we do, we can
            if lead_to_loop(pos, move.turn, grid, visited_moves):
                count += 1

            # Next position is free - move
            grid.set_pos_move(next_pos, pos_mov)
            grid.set_pos_visited(pos)
            pos = next_pos

    # return all visited positions
    return count
