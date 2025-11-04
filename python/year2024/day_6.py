import numpy as np
from typing import NamedTuple


class Grid:
    START_POS = '^'
    WALL = '#'
    VISITED = 'X'

    def __init__(self, grid: list[list[str]]):
        self.grid = np.array(grid)
        self.limits = [0, self.grid.shape[0], 0, self.grid.shape[1]]

    def __str__(self):
        return self.grid.__str__()

    def is_in_bounds(self, pos: tuple[int, int]):
        return self.limits[0] <= pos[0] < self.limits[1] and self.limits[2] <= pos[1] < self.limits[3]

    def get_pos_move(self, pos: tuple[int, int]) -> str:
        return self.grid[pos[0], pos[1]]

    def set_pos_move(self, pos: tuple[int, int], value: str):
        self.grid[pos[0], pos[1]] = value

    def is_wall(self, pos: tuple[int, int]) -> bool:
        return self.grid[pos[0], pos[1]] == self.WALL

    def set_wall(self, pos: tuple[int, int]):
        self.grid[pos[0], pos[1]] = self.WALL

    def get_start_pos(self):
        return (
            self.START_POS, tuple(
                np.argwhere(
                    self.grid == self.START_POS)[0].tolist()))


class Move(NamedTuple):
    direction: tuple[int, int]
    turn: str
    current: str

    def get_next_pos(self, pos: tuple[int, int]):
        return (pos[0] + self.direction[0], pos[1] + self.direction[1])


moves = {
    '^': Move(current='^', direction=(-1, 0), turn='>'),
    '>': Move(current='>', direction=(0, 1), turn='v'),
    'v': Move(current='v', direction=(1, 0), turn='<'),
    '<': Move(current='<', direction=(0, -1), turn='^'),
}


def part1(testcase: str):
    grid = Grid([list(row) for row in testcase.splitlines()])

    visited: set[tuple[int, int]] = set()
    (start_move, pos) = grid.get_start_pos()
    move = moves[start_move]

    while (grid.is_in_bounds(pos)):
        visited.add(pos)
        next_pos = move.get_next_pos(pos)

        if not grid.is_in_bounds(next_pos):
            # game over
            break
        elif grid.is_wall(next_pos):
            # Turn on a wall
            move = moves[move.turn]
        else:
            # Step forward
            pos = next_pos
    return len(visited)


def lead_to_loop(pos: tuple[int, int],
                 move: Move,
                 grid: Grid,
                 visited: set[tuple[tuple[int, int], str]]) -> bool:

    # clone visited so we can track internal loops
    internal_visited = set(visited)

    # As long as we are in bound and not blocked by a wall
    while grid.is_in_bounds(pos):
        state = (pos, move.current)
        if state in internal_visited:
            # If already visited this place with the same turn, we are good
            return True
        internal_visited.add(state)

        next_pos = move.get_next_pos(pos)
        if not grid.is_in_bounds(next_pos):
            # Next step is out of bounds
            break
        elif grid.is_wall(next_pos):
            # Got to a wall so we need to turn
            move = moves[move.turn]
        else:
            # Step forward
            pos = next_pos
    return False


def part2(testcase: str):
    grid = Grid([list(row) for row in testcase.splitlines()])

    visited: set[tuple[tuple[int, int], str]] = set()
    rocks: set[tuple[int, int]] = set()
    rocks_attempts: set[tuple[int, int]] = set()
    # Move and mark the visited places
    (start_move, start_pos) = grid.get_start_pos()

    pos = start_pos
    move = moves[start_move]
    while (grid.is_in_bounds(pos)):
        next_pos = move.get_next_pos(pos)

        visited.add((pos, move.current))

        # Out of bounds
        if not grid.is_in_bounds(next_pos):
            # Game over
            break
        elif grid.is_wall(next_pos):
            # Turn
            move = moves[move.turn]
        else:
            # Check if we have visited this position with this move
            # Edge cases:
            # 1. We have tried to place a rock here already
            # 2. Set the wall in the grid before moving on
            temp = grid.get_pos_move(next_pos)
            grid.set_wall(next_pos)
            if (
                    next_pos not in rocks_attempts and
                    lead_to_loop(pos, moves[move.turn], grid, visited)):
                rocks.add(next_pos)

            # Save all attempts so we dont try putting a rock on a trail
            rocks_attempts.add(next_pos)

            # Roll back
            grid.set_pos_move(next_pos, temp)

            # Move forward
            pos = next_pos

    # return all rocks positions
    if start_pos in rocks:
        rocks.remove(start_pos)
    return len(rocks)
