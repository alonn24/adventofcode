import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np
from typing import Callable, Tuple, Any

"""
Day 16: The Floor Will Be Lava
Get the energized cells moving in a grid or mirrors ('/', '\') and splitters ('|', '-')
"""

"""
Moving dictionary for the beams according
to the direction of the beams and the cell they are in
"""
light_dir: dict[str, Callable[[int, int], list[Tuple[int, int]]]] = {
    '.': lambda dx, dy: [(dx, dy)],
    '/': lambda dx, dy:
    [(-1, 0)] if (dx, dy) == (0, 1) else  # ->
    [(1, 0)] if (dx, dy) == (0, -1) else  # <-
    [(0, 1)] if (dx, dy) == (-1, 0) else  # ^
    [(0, -1)] if (dx, dy) == (1, 0) else  # v
    [],
    '\\': lambda dx, dy:
    [(1, 0)] if (dx, dy) == (0, 1) else    # ->
    [(-1, 0)] if (dx, dy) == (0, -1) else  # <-
    [(0, -1)] if (dx, dy) == (-1, 0) else  # ^
    [(0, 1)] if (dx, dy) == (1, 0) else    # v
    [],
    '|': lambda dx, dy:
    [(dx, dy)] if (dx, dy) in [(-1, 0), (1, 0)] else         # ^ or v
    [(-1, 0), (1, 0)] if (dx, dy) in [(0, 1), (0, -1)] else  # -> or <-
    [],
    '-': lambda dx, dy:
    [(dx, dy)] if (dx, dy) in [(0, 1), (0, -1)] else         # -> or <-
    [(0, -1), (0, 1)] if (dx, dy) in [(-1, 0), (1, 0)] else  # ^ or v
    []
}

dir_to_sign = {
    (0, 1): '>',
    (0, -1): '<',
    (1, 0): 'v',
    (-1, 0): '^'
}


def play_beams(grid: np.ndarray[int, Any], beams: np.ndarray[int, Any]) -> np.ndarray[int, Any]:
    x, y, _, _ = beams.T
    cells = grid[x, y]

    new_beams = np.array([], dtype=int).reshape(0, 4)
    for i, cell in enumerate(cells):
        beam = beams[i]
        # Get the new beam direction
        new_dirs = light_dir[cell](beam[2], beam[3])
        # Add the new beams to the next array while stepping to the next position
        for new_dir in new_dirs:
            new_beams = np.append(new_beams, [[beam[0] + new_dir[0], beam[1] + new_dir[1], *new_dir]], axis=0)
    # Filter beams out of the grid
    new_beams = new_beams[(0 <= new_beams[:, 0]) & (new_beams[:, 0] < grid.shape[0]) &
                          (0 <= new_beams[:, 1]) & (new_beams[:, 1] < grid.shape[1])]
    return np.unique(new_beams, axis=0)


def get_energized_cells(matrix: np.ndarray[int, Any], entrance_beams: np.ndarray[int, Any]):
    """
    This function simulate the beams moving in the grid
    and result with the number of energized cells

    Args:
    matrix (np.array): the grid of the beams
    entrance_beams (np.array): the entrance beams to the grid
        each item has 4 values: x, y, dx, dy
        [dx, dy] is the direction of the beam

    Returns:
    int: the number of energized cells
    """
    beam_edges = entrance_beams.copy()
    # We will filter out beams with the same spot and direction
    visited_beams = {tuple(row) for row in beam_edges}
    while True:
        # Play a round
        beam_edges = play_beams(matrix, beam_edges)

        # Filter out beams that are already in the visited beams
        exclude_array = np.array(list(visited_beams))
        is_in_exclude_array = np.all(beam_edges[:, None, :] == exclude_array[None, :, :], axis=2)
        beam_edges = beam_edges[~np.any(is_in_exclude_array, axis=1)]
        if (len(beam_edges) == 0):
            break

        # Add the new beams to the visited beams
        visited_beams = visited_beams | {tuple(row) for row in beam_edges}
    positions_visited = np.array(list(visited_beams))[:, :2]
    return len(np.unique(positions_visited, axis=0))


def part1(case: str):
    """
    Day 16: The Floor Will Be Lava
    Get the energized cells moving in a grid or mirrors ('/', '\') and splitters ('|', '-')
    """

    matrix = np.array([[*row] for row in case.split('\n')])
    # Simulate a beam from the top left corner
    return get_energized_cells(matrix, np.array([[0, 0, 0, 1]]))


def part2(case: str):
    """
    Search for the entrance that will make the maximum number of energized cells
    """
    matrix = np.array([[*row] for row in case.split('\n')])
    max_energized_cells = 0

    top_row = [(0, i, 1, 0) for i in range(matrix.shape[1])]
    bottom_row = [(matrix.shape[0] - 1, i, -1, 0) for i in range(matrix.shape[1])]
    left_column = [(i, 0, 0, 1) for i in range(matrix.shape[0])]
    right_column = [(i, matrix.shape[1] - 1, 0, -1) for i in range(matrix.shape[0])]

    all_entrances = top_row + bottom_row + left_column + right_column
    for entrance in all_entrances:
        max_energized_cells = max(max_energized_cells, get_energized_cells(matrix, np.array([entrance])))
    return max_energized_cells


def play():
    fig, ax = plt.subplots()
    matrix = np.array([list(row) for row in open('2023/input/day-16.test.txt', 'r').read().splitlines() if row])
    beam_edges = np.array([[0, 0, 0, 1]])
    beam_positions = beam_edges[:, :2]

    def draw_grid():
        ax.clear()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i, j] != ".":
                    ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=1, edgecolor='black', facecolor='gray'))
                    plt.text(j, i, matrix[i, j], ha="center", va="center", color="black", fontsize=14)
        for beam in beam_edges:
            sign = dir_to_sign[(beam[2], beam[3])]
            plt.text(beam[1], beam[0], sign, ha="center", va="center", color="black", fontsize=14)
            ax.add_patch(Circle((beam[1], beam[0]), 0.5, color='blue'))
        for beam in beam_positions:
            ax.add_patch(Circle((beam[1], beam[0]), 0.5, color='blue'))
        ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1), minor=True)
        ax.set_yticks(np.arange(-0.5, len(matrix), 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        plt.xlim([-1, len(matrix[0])])
        plt.ylim([-1, len(matrix)])
        plt.gca().invert_yaxis()

    def on_key(event):
        nonlocal matrix
        nonlocal beam_edges
        nonlocal beam_positions
        beam_edges = play_beams(matrix, beam_edges)
        beam_positions = np.unique(np.append(beam_positions, beam_edges[:, :2], axis=0), axis=0)
        draw_grid()
        plt.pause(0.1)

    draw_grid()
    fig.canvas.mpl_connect('key_press_event', on_key)
    plt.show()


if __name__ == '__main__':
    play()
