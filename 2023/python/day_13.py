import numpy as np
from typing import Any


def parse_pattern(pattern: str) -> np.ndarray[str, Any]:
    rows = pattern.strip().split('\n')
    return np.array([list(row) for row in rows])


def count_mismatch(pattern: np.ndarray[str, Any], idx: int) -> int:
    gap = min(idx, len(pattern[0])-idx)
    left = pattern[:, idx-gap:idx]
    right = pattern[:, idx:idx+gap]
    return np.count_nonzero(left != right[:, ::-1])


def get_vertical_mirror_idx(pattern: np.ndarray[str, Any]) -> int:
    equal_cols_idx = np.where(np.all(pattern[:, :-1] == pattern[:, 1:], axis=0))[0]
    equal_cols_idx += 1
    for col in equal_cols_idx:
        if not count_mismatch(pattern, col):
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


def find_mirror_idx_with_smug(pattern: np.ndarray[str, Any]) -> int:
    for i in range(len(pattern[0])):
        mismatch = count_mismatch(pattern, i)
        if mismatch == 1:
            return i
    return 0


def part2(case: str) -> int:
    """
    Part 2 - find mirror index with a smug
    """
    print('')
    patterns = [parse_pattern(part) for part in case.split('\n\n')]
    verticals = 0
    horizontals = 0
    for pattern in patterns:
        verticals += find_mirror_idx_with_smug(pattern)
        horizontals += find_mirror_idx_with_smug(np.rot90(pattern, k=1))
    return horizontals*100+verticals
