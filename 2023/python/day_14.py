import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from typing import Any
import numpy as np

ROLLING = 'O'
STONE = '#'
FREE = '.'


def roll_once(grid: np.ndarray[str, Any], direction: str = 'up'):
    """
    Roll the stones in the grid in the given direction
    """
    result = grid
    match direction:
        case 'up':
            rolled_stones = (result[1:] == ROLLING) & (result[:-1] == FREE)
            result[:-1] = np.where(rolled_stones, ROLLING, result[:-1])
            result[1:] = np.where(rolled_stones, FREE, result[1:])
        case 'down':
            rolled_stones = (result[:-1] == ROLLING) & (result[1:] == FREE)
            result[1:] = np.where(rolled_stones, ROLLING, result[1:])
            result[:-1] = np.where(rolled_stones, FREE, result[:-1])
        case 'left':
            rolled_stones = (result[:, 1:] == ROLLING) & (result[:, :-1] == FREE)
            result[:, :-1] = np.where(rolled_stones, ROLLING, result[:, :-1])
            result[:, 1:] = np.where(rolled_stones, FREE, result[:, 1:])
        case 'right':
            rolled_stones = (result[:, :-1] == ROLLING) & (result[:, 1:] == FREE)
            result[:, 1:] = np.where(rolled_stones, ROLLING, result[:, 1:])
            result[:, :-1] = np.where(rolled_stones, FREE, result[:, :-1])
        case _:
            raise ValueError(f"Invalid direction: {direction}")
    return rolled_stones.any()


def roll_all_the_way(grid: np.ndarray[str, Any], direction: str = 'up'):
    changed = roll_once(grid, direction)
    while changed:
        changed = roll_once(grid, direction)


def calc_load(grid: np.ndarray[str, Any]):
    rolling = np.transpose(np.nonzero(grid == ROLLING))
    rolling[:, 0] = len(grid) - rolling[:, 0]
    return np.sum(rolling[:, 0])


def part1(case: str):
    """
    Day 14: Parabolic Reflector Dish
    Roll stones over the grid and calculate the load
    """
    grid = np.array([list(row) for row in case.split('\n') if row])
    roll_all_the_way(grid, 'up')
    return calc_load(grid)


PART2_TIMES = 1000000000


def part2(case: str):
    """
    Part 2 - run 4 times to all directions
    find the cycle and skip most of the iterations
    """
    grid = np.array([list(row) for row in case.split('\n') if row])
    # Keep track of visited states to find a loop
    visited = {grid.tobytes(): 0}
    start = 0
    steps = 0
    # Find the cycle
    for i in range(PART2_TIMES):
        roll_all_the_way(grid, 'up')
        roll_all_the_way(grid, 'left')
        roll_all_the_way(grid, 'down')
        roll_all_the_way(grid, 'right')
        if grid.tobytes() in visited:
            start = visited[grid.tobytes()]
            steps = i - visited[grid.tobytes()]
            break
        visited[grid.tobytes()] = i
    # Calculate the effective position skipping the cycles
    # And roll the stones
    effective_position = (PART2_TIMES - start) % steps
    for i in range(effective_position - 1):
        roll_all_the_way(grid, 'up')
        roll_all_the_way(grid, 'left')
        roll_all_the_way(grid, 'down')
        roll_all_the_way(grid, 'right')
    return calc_load(grid)


def play():
    fig, ax = plt.subplots()
    matrix = np.array([list(row) for row in open('2023/input/day-14.test.txt', 'r').read().splitlines() if row])

    def draw_grid():
        ax.clear()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i, j] == "#":
                    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor='gray'))
                if matrix[i, j] == "O":
                    ax.add_patch(Circle((j, i), 0.5, color='red'))
        ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(matrix), 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        plt.xlim([-1, len(matrix[0])])
        plt.ylim([-1, len(matrix)])
        plt.gca().invert_yaxis()

    def on_key(event):
        nonlocal matrix
        roll_once(matrix, event.key)
        draw_grid()
        plt.pause(0.1)

    draw_grid()
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()


if __name__ == '__main__':
    play()
