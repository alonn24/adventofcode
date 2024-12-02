import numpy as np
import re
from typing import Any


def is_line_valid(line: np.ndarray[Any, Any]) -> bool:
    # Get distances between each pair of adjacent levels.
    distances = line[:-1] - line[1:]

    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    is_same_direction = np.all(distances > 0)
    is_same_direction = is_same_direction or np.all(distances < 0)
    is_same_direction = is_same_direction and np.all(np.abs(distances) <= 3)
    return bool(is_same_direction)


def part1(testcase: str):
    lines = [np.array(list(map(int, re.findall(r'\d+', line)))) for line in testcase.splitlines()]
    valid_lines = [line for line in lines if is_line_valid(line)]
    return len(valid_lines)


def part2(testcase: str):
    lines = [np.array(list(map(int, re.findall(r'\d+', line)))) for line in testcase.splitlines()]
    count = 0
    for line in lines:
        is_ok = False
        for i, _ in enumerate(line):
            # check valid without the column
            if is_line_valid(np.delete(line, i)):
                is_ok = True
        if is_ok:
            count += 1
    return count
