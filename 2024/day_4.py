import numpy as np
from typing import Any

all_directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
word = ['X', 'M', 'A', 'S']


def check_word(lines: np.ndarray[Any, Any], pos: tuple[int, int], dir: tuple[int, int]):
    valid = [lines[pos[0] + i * dir[0], pos[1] + i * dir[1]] == word[i] for i in range(1, len(word))]
    return all(valid)


def part1(testcase: str):
    lines = np.array([[*x] for x in testcase.splitlines()])
    # Stack 3 columns on each side
    lines = np.hstack([
        np.empty((lines.shape[0], 3), dtype=str),
        lines,
        np.empty((lines.shape[0], 3), dtype=str)
    ])
    # Stack 3 rows on each side
    lines = np.vstack([
        np.empty((3, lines.shape[1]), dtype=str),
        lines,
        np.empty((3, lines.shape[1]), dtype=str)
    ])

    start_positions = np.argwhere(lines == word[0])
    xmas = [(pos, dir) for pos in start_positions for dir in all_directions if check_word(lines, pos, dir)]
    return len(xmas)
