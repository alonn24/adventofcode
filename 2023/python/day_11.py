import numpy as np
from typing import Any


def get_points(grid: np.ndarray[Any, Any], expand: int = 2) -> np.ndarray[Any, Any]:
    # Get the points indices as tuples
    points = np.transpose(np.where(grid == '#'))

    # Find Expand the points indices by the number of empty rows and columns
    all_dot_rows = np.where(np.all(grid == '.', axis=1))[0]
    all_dot_columns = np.where(np.all(grid == '.', axis=0))[0]

    # Update the points indices by empty rows and columns
    for p in points:
        p[0] += len(all_dot_rows[all_dot_rows < p[0]])*(expand-1)
        p[1] += len(all_dot_columns[all_dot_columns < p[1]])*(expand-1)
    return points


def get_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part1(case: str) -> int:
    """
    --- Day 11 Part 1: Cosmic Expansion ---
    Find the closest distance between two points in a grid.
    """
    grid = np.array([list(line.strip()) for line in case.splitlines()])

    # Get the points indices as tuples
    points = get_points(grid)

    # Create a matrix with each node and its distance to all other nodes
    rows, cols = len(points), len(points)
    distances = np.fromfunction(np.vectorize(lambda row, col: get_distance(
        points[row], points[col])), (rows, cols), dtype=int)

    # Divide by 2 so for distict pairs
    return np.sum(distances) / 2


def part2(case: str, expand: int) -> int:
    """
    Part 2 - expand by a factor
    """
    grid = np.array([list(line.strip()) for line in case.splitlines()])

    # Get the points indices as tuples
    points = get_points(grid, expand)

    # Create a matrix with each node and its distance to all other nodes
    rows, cols = len(points), len(points)
    distances = np.fromfunction(np.vectorize(lambda row, col: get_distance(
        points[row], points[col])), (rows, cols), dtype=int)

    # Divide by 2 so for distict pairs
    return np.sum(distances) / 2
