import numpy as np
import re


def part1(testcase: str):
    # get only numbers from splitlines
    lines = np.array([list(map(int, re.findall(r'\d+', x))) for x in testcase.splitlines()])
    # Sort each column separately
    lines[:, 0] = np.sort(lines[:, 0])
    lines[:, 1] = np.sort(lines[:, 1])
    # Get the difference between the first and second column
    lines = np.diff(lines, axis=1)

    # sum distances
    return np.sum(np.abs(lines))


def part2(testcase: str):
    # get only numbers from splitlines
    lines = np.array([list(map(int, re.findall(r'\d+', x))) for x in testcase.splitlines()])
    # For every cell in the first column, get the number of occurences in the second column
    lines = [np.multiply(np.sum(lines[:, 1] == x), x) for x in lines[:, 0]]
    return np.sum(lines)
