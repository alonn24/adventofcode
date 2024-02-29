from typing import List
import numpy as np


def calc_for_row(row: List[int]):
    """
    input: row: List[int]
    Calculate for one row
    """
    arr = np.array(row, dtype=np.int64)
    # Generate the stack of differences until we get 0s
    stack = [arr]
    while not np.all(arr == 0):
        arr = np.diff(arr)
        stack.append(arr)

    # Build the next item in the sequence for each row back to the top
    last = 0
    first = 0
    for i in range(len(stack) - 2, -1, -1):
        last = stack[i][-1] + last
        first = stack[i][0] - first
    # Return the next item for the given row
    return first, last


def part1(input: List[str]):
    """
    --- Day 9 Part 1: Mirage Maintenance ---
    Calculate the next value in a sequence of numbers
    """
    data = [[*map(int, x.split(' '))] for x in input]
    return sum([calc_for_row(x)[1] for x in data])


def part2(input: List[str]):
    """
    --- Day 9 Part 2 ---
    Calculate the previous value in a sequence of numbers
    """
    data = [[*map(int, x.split(' '))] for x in input]
    return sum([calc_for_row(x)[0] for x in data]) % 1000000007
