"""Grid parsing utilities for Advent of Code."""

import numpy as np
from typing import Any


def parse_grid(case: str) -> np.ndarray[Any, Any]:
    """Parse a string representation of a grid into a numpy array.

    Args:
        case: String with lines representing rows of the grid

    Returns:
        2D numpy array where each cell contains a character from the input
    """
    return np.array([list(x) for x in case.strip().splitlines()])
