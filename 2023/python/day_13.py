import numpy as np
from typing import Any


def parse_pattern(pattern: str) -> np.ndarray[str, Any]:
    rows = pattern.strip().split('\n')
    return np.array([list(row) for row in rows])


def compare_with_idx(pattern: np.ndarray[str, Any], idx: int) -> np.ndarray[bool, Any]:
    gap = min(idx, len(pattern[0])-idx)
    left = pattern[:, idx-gap:idx]
    right = pattern[:, idx:idx+gap]
    return left == right[:, ::-1]


def get_vertical_mirror_idx(pattern: np.ndarray[str, Any]) -> int:
    equal_cols_idx = np.where(np.all(pattern[:, :-1] == pattern[:, 1:], axis=0))[0]
    equal_cols_idx += 1
    for col in equal_cols_idx:
        if np.all(compare_with_idx(pattern, col)):
            return col
    return 0


def part1(case: str) -> int:
    """
    Day 13: Point of Incidence
    Part 1 - find mirror index
    """
    print('')
    patterns = [parse_pattern(part) for part in case.split('\n\n')]
    verticals = 0
    horizontals = 0
    for pattern in patterns:
        verticals += get_vertical_mirror_idx(pattern)
        horizontals += get_vertical_mirror_idx(np.rot90(pattern, k=1))
    return horizontals*100+verticals
