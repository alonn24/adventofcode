from functools import cmp_to_key
import numpy as np
import collections
from typing import Any


def parse_input(testcase: str):
    rules, lines = testcase.split('\n\n')
    rules = np.array([x.split('|') for x in rules.splitlines()], dtype=int)
    lines = [np.array(x.split(','), dtype=int) for x in lines.splitlines()]
    return rules, lines


def is_in_order(line: np.ndarray[int, Any],
                rules: np.ndarray[int, Any]) -> np.ndarray[int, Any]:
    # Get the indices of the rules
    index_map = collections.defaultdict(
        lambda: -1, {x: i for i, x in enumerate(line)})
    rules_indices = np.vectorize(lambda x: index_map[x])(rules)
    # Filter relevant rules
    rules_indices = rules_indices[np.all(rules_indices > -1, axis=1)]
    # Filter rows where [0] < [1]
    invalid = rules_indices[:, 0] >= rules_indices[:, 1]
    return np.sum(invalid) == 0


def part1(testcase: str):
    rules, lines = parse_input(testcase)
    # Filter lines that are in order
    valid_lines = [line for line in lines if is_in_order(line, rules)]
    # Return the sum of the middle elements
    return sum([line[int(len(line) / 2)] for line in valid_lines])


def compare(a: int, b: int, rules: np.ndarray[int, Any]) -> int:
    if np.any(np.logical_and(rules[:, 0] == a, rules[:, 1] == b)):
        # Smaller
        return -1
    elif np.any(np.logical_and(rules[:, 0] == b, rules[:, 1] == a)):
        # Greater
        return 1
    # Equal
    return 0


def part2(testcase: str):
    rules, lines = parse_input(testcase)
    # Filter lines that are not in order
    not_in_order_lines = [
        line for line in lines if not is_in_order(
            line, rules)]
    ordered_lines = [
        sorted(
            (line),
            key=cmp_to_key(
                lambda x,
                y: compare(
                    x,
                    y,
                    rules))) for line in not_in_order_lines]
    # Return the sum of the middle elements
    return sum([line[int(len(line) / 2)] for line in ordered_lines])
