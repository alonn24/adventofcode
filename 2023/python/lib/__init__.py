import numpy as np
from typing import Any

Point = tuple[int, int]


def is_in_bounds(grid: np.ndarray[Any, Any], pos: Point):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def add_tuples(a: Point, b: Point):
    return a[0] + b[0], a[1] + b[1]


def manhattan_distance(a: Point, b: Point):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_grid(case: str):
    return np.array([list(x) for x in case.strip().splitlines()])


def polygon_area(points: np.ndarray[int, Any]):
    # Add the first point to the end to close the polygon
    points = points + [points[0]]

    # Calculate the area using the Shoelace formula
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area /= 2

    return abs(area)
