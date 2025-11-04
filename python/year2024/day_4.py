import numpy as np
from typing import Any


word = ['X', 'M', 'A', 'S']
all_directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


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

    # Start from X and search for MAS in all directions
    start_positions = np.argwhere(lines == 'X')

    xmas = [(pos, dir) for pos in start_positions for dir in all_directions if check_word(lines, pos, dir)]
    return len(xmas)


letters = ['M', 'S']


def check_word_x(lines: np.ndarray[Any, Any], pos: tuple[int, int]):
    res = (
        ((
            # top left to bottom right
            (lines[pos[0] - 1, pos[1] - 1] == letters[0] and
             lines[pos[0] + 1, pos[1] + 1] == letters[1]))
            or (lines[pos[0] - 1, pos[1] - 1] == letters[1] and
                lines[pos[0] + 1, pos[1] + 1] == letters[0]))
        and ((
            # top right to bottom left
            (lines[pos[0] - 1, pos[1] + 1] == letters[0] and
             lines[pos[0] + 1, pos[1] - 1] == letters[1]))
             or (lines[pos[0] - 1, pos[1] + 1] == letters[1] and
                 lines[pos[0] + 1, pos[1] - 1] == letters[0]))
    )
    return res


def part2(testcase: str):
    lines = np.array([[*x] for x in testcase.splitlines()])
    # Stack 3 columns on each side
    lines = np.hstack([
        np.empty((lines.shape[0], 1), dtype=str),
        lines,
        np.empty((lines.shape[0], 1), dtype=str)
    ])
    # Stack 3 rows on each side
    lines = np.vstack([
        np.empty((1, lines.shape[1]), dtype=str),
        lines,
        np.empty((1, lines.shape[1]), dtype=str)
    ])

    # Start from A and search for MAS in diagonals
    start_positions = np.argwhere(lines == 'A')
    xmas = [pos for pos in start_positions if check_word_x(lines, pos)]
    return len(xmas)
