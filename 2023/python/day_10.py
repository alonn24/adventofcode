import matplotlib.pyplot as plt
import numpy as np
from typing import Any

GridNode = tuple[int, int]
NpStrMatrix = np.ndarray[Any, np.dtype[np.str_]]

START = "S"
PIPES = {
    "S": [(0, 1), (0, -1), (1, 0), (-1, 0)],
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def is_in_bounds(grid: NpStrMatrix, x: int, y: int) -> bool:
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])


def is_connected(grid: NpStrMatrix, x1: int, y1: int, x2: int, y2: int) -> bool:
    if not is_in_bounds(grid, x1, y1) or not is_in_bounds(grid, x2, y2):
        return False
    is_n1_connected = any([(x1 + d[0], y1 + d[1])
                          == (x2, y2) for d in PIPES[grid[x1, y1]]])
    is_n2_connected = any([(x2 + d[0], y2 + d[1])
                          == (x1, y1) for d in PIPES[grid[x2, y2]]])
    return is_n1_connected and is_n2_connected


def get_connected_pipes(grid: NpStrMatrix, x: int, y: int) -> list[GridNode]:
    near_pipes = [(x + direction[0], y + direction[1])
                  for direction in PIPES[grid[x, y]]]
    return [*filter(lambda n: is_connected(grid, x, y, n[0], n[1]), near_pipes)]


def get_steps_matrix(grid: NpStrMatrix, start: GridNode) -> Any:
    visited = (grid == START).astype(np.int64)

    # BFS
    nodes = [start]
    counter = 0
    while True:
        nodes = np.array([get_connected_pipes(grid, d[0], d[1])
                          for d in nodes]).reshape(-1, 2)
        # Get only not visited nodes
        nodes = [*filter(lambda n: visited[n[0], n[1]] == 0, nodes)]
        if len(nodes) == 0:
            break
        counter += 1
        visited[*np.transpose(nodes)] = counter
    return visited


def part1(case: str) -> int:
    """
    --- Day 10 Part 1: Pipe Maze ---
    Find the farthest point from the start point in a maze of pipes.
    """
    grid = np.array([list(row)
                    for row in case.strip().split("\n")], dtype=np.str_)
    # Get starting point and 2 directions to walk
    # We assume:
    #   only 2 are connected to START
    #   there is only only 1 instance of START
    start_point = np.argwhere(grid == START)[0]
    steps = get_steps_matrix(grid, start_point)
    return np.max(steps)


def part2(case: str) -> int:
    """
    Part 2 - find tiles enclosed by the loop in the pipes
    """
    grid = np.array([list(row)
                    for row in case.strip().split("\n")], dtype=np.str_)
    # Create the steps matrix
    start_point = np.argwhere(grid == START)[0]
    steps = get_steps_matrix(grid, start_point)

    # determind to include S or not
    verticals_items = ['|', 'L', 'J']  # S | - L J F 7 .
    is_For7 = (steps[*start_point + (1, 0)] and steps[*start_point + (0, 1)]) \
        or (steps[*start_point + (1, 0)] and steps[*start_point + (0, -1)])
    if not is_For7:
        verticals_items += ['S']

    # Count the vertical elements that are part of the loop
    verticals = (steps > 0) & (np.isin(grid, verticals_items))
    pipes_thought = np.cumsum(verticals, axis=1)
    # Get an indication for when we have odd number of vertical pipes
    odd_matrix = pipes_thought % 2 == 1
    # Ray Casting Algorithm - if the wall numbers are odd, the point is within the loop
    return np.count_nonzero(odd_matrix & (steps == 0))


if __name__ == "__main__":
    with open("2023/input/day-10.input.txt", "r") as f:
        case = f.read()
    grid = np.array([list(row)
                    for row in case.strip().split("\n")], dtype=np.str_)
    # Create the steps matrix
    start_point = np.argwhere(grid == START)[0]
    steps = get_steps_matrix(grid, start_point)
    matrix = steps > 0

    # Define a custom colormap for taken (True) and free (False) spaces
    cmap = plt.get_cmap('coolwarm', 2)
    # Plot the matrix using imshow
    plt.imshow(matrix, cmap=cmap)
    plt.title('The Loop')
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    # Add a color bar for reference
    cbar = plt.colorbar(ticks=[0.25, 0.75])
    cbar.set_ticklabels(['Free', 'Loop'])
    plt.show()
