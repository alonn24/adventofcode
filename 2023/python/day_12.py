import numpy as np
from itertools import product
from scipy.ndimage import label
from typing import Any


def get_row_count(row: np.ndarray[str, Any]) -> np.ndarray[int, Any]:
    binary_arr = (row == '#').astype(int)
    labeled_arr, _ = label(binary_arr)
    counts = np.bincount(labeled_arr[labeled_arr > 0])
    return np.pad(counts[1:], (len(row) - len(counts[1:]), 0))


PLACEHOLDER = '?'
SPRING = '#'
FREE = '.'


def get_patter_combinations(pattern: np.ndarray[str, Any], groups: np.ndarray[int, Any]) -> int:
    placeholders = np.count_nonzero(pattern == PLACEHOLDER)

    combinations = np.array([*product([SPRING, FREE], repeat=placeholders)])

    matrices = np.tile(pattern, (len(combinations), 1))
    matrices[:, pattern == '?'] = combinations
    matrices_groups = np.apply_along_axis(get_row_count, 1, matrices)
    padded_groups = np.pad(groups, (len(pattern) - len(groups), 0))
    return np.sum(np.all(matrices_groups == padded_groups, axis=1))


def cal_for_row(row: str) -> int:
    """
    Calculate the number of valid combinations in a row.
    """
    [pattern, groups] = row.strip().split(" ")
    groups = np.array(groups.split(","), dtype=np.int64)
    pattern = np.array([*pattern])
    return get_patter_combinations(pattern, groups)


def part1(case: str) -> int:
    rows = np.array(case.splitlines())
    result = np.vectorize(cal_for_row)(rows)
    return np.sum(result)
