import numpy as np
from functools import lru_cache


PLACEHOLDER = '?'
SPRING = '#'
FREE = '.'


def prepare_row(row: str, copies: int = 1):
    [pattern, groups] = row.strip().split(" ")
    pattern = '?'.join([pattern] * copies)
    groups = [*map(int, groups.split(',')*copies)]
    return pattern, groups


def get_row_combinations(pattern: str, groups: list[int]) -> int:
    """
    Recursive with cache return the number of combinations of the pattern
    """

    @lru_cache(maxsize=None)
    def recursive_combinations(pi: int, gi: int, acc: int) -> int:
        result = 0
        # Got to the end
        if pi == len(pattern):
            # If we ended the groups as well
            is_end_group = (gi == len(groups) and acc == 0) or (
                gi == len(groups) - 1 and acc == groups[gi])
            return 1 if is_end_group else 0

        # Skip a group
        if pattern[pi] == '.' or pattern[pi] == '?':
            if acc == 0:
                result += recursive_combinations(pi + 1, gi, 0)
            elif gi < len(groups) and acc == groups[gi]:
                result += recursive_combinations(pi + 1, gi+1, 0)
        # Continue a group
        if pattern[pi] == '#' or pattern[pi] == '?':
            result += recursive_combinations(pi + 1, gi, acc+1)
        return result

    return recursive_combinations(0, 0, 0)


def part1(case: str) -> int:
    """
    Day 12: Hot Springs
    Part 1 - calculate the number of combinations of the pattern
    """
    return np.sum([get_row_combinations(*prepare_row(row)) for row in case.splitlines()])


def part2(case: str) -> int:
    """
    Part 2 - calculate the number of combinations when multiply the stripe by 5
    """
    return np.sum([get_row_combinations(*prepare_row(row, 5)) for row in case.splitlines()])
