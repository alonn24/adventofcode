"""Geometric utility functions for Advent of Code."""

from typing import TypeAlias

Point: TypeAlias = tuple[int, int]


def add_tuples(a: Point, b: Point) -> Point:
    """Add two point tuples component-wise."""
    return a[0] + b[0], a[1] + b[1]


def manhattan_distance(a: Point, b: Point) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def is_in_bounds(shape: tuple[int, int], pos: Point) -> bool:
    """Check if a position is within bounds of a grid with given shape.

    Args:
        shape: Tuple of (height, width) representing grid dimensions
        pos: Position tuple (row, col) to check

    Returns:
        True if position is within bounds, False otherwise
    """
    return 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]
