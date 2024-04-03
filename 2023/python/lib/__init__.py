import numpy as np
from typing import Any


def parse_grid(case: str):
    return np.array([list(x) for x in case.splitlines()])


def polygon_area(points: np.ndarray[int, Any]):
    # Add the first point to the end to close the polygon
    points = points + [points[0]]

    # Calculate the area using the Shoelace formula
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area /= 2

    return abs(area)
