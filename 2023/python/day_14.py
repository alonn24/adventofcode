import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Rectangle
from typing import Any
import numpy as np

ROLLING = 'O'
STONE = '#'
FREE = '.'


def run_round(grid: np.ndarray[str, Any]):
    result = grid.copy()
    rolled_stones = (result[1:] == ROLLING) & (result[:-1] == FREE)
    result[:-1][rolled_stones] = ROLLING
    result[1:][rolled_stones] = FREE
    return result


def part1(case: str):
    grid = np.array([list(row) for row in case.split('\n') if row])
    updated = run_round(grid)
    while np.any(updated != grid):
        grid = updated
        updated = run_round(grid)
    rolling = np.transpose(np.where(updated == ROLLING))
    rolling[:, 0] = len(grid) - rolling[:, 0]
    return np.sum(rolling[:, 0])


def play():
    fig, ax = plt.subplots()
    matrix = np.array([list(row) for row in open('2023/input/day-14.test.txt', 'r').read().splitlines() if row])

    def draw_grid(frame):
        ax.clear()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i, j] == "#":
                    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor='gray'))
                if matrix[i, j] == "O":
                    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor='red'))
        ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(matrix), 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        plt.xlim([-1, len(matrix[0])])
        plt.ylim([-1, len(matrix)])
        plt.gca().invert_yaxis()

    def on_key(event):
        nonlocal matrix
        matrix = run_round(matrix)

    # draw_grid()
    fig.canvas.mpl_connect('key_press_event', on_key)
    ani = animation.FuncAnimation(fig, draw_grid, frames=100, interval=100, repeat=False)
    ani.resume()
    plt.show()


if __name__ == '__main__':
    play()
