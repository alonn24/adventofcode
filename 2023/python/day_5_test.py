import pytest
import numpy as np
from day_5 import part1, part2, map_ranges


def test_part_1_test_case():
    input = open('2023/input/day-5.test.txt').read()
    assert part1(input) == 35


def test_part_1_real_case():
    input = open('2023/input/day-5.input.txt').read()
    assert part1(input) == 662197086


@pytest.mark.parametrize("start, end, ranges, expected", [
    (0, 10, [[0, 0, 10]], [[0, 10]]),
    (0, 10, [[20, 0, 10]], [[20, 30]]),
    (0, 10, [[0, 30, 40]], [[0, 10]]),
    # split with two spaces around
    (0, 10, [[20, 2, 5]], [[0, 1], [20, 23], [6, 10]]),
    # split between to ranges
    (0, 10, [[20, 0, 3], [30, 6, 8]], [[20, 23], [4, 5], [30, 32], [9, 10]]),
    (55, 68, [[50, 98, 100], [52, 50, 98]], [[57, 70]])

])
def test_map_ranges(start, end, ranges, expected):
    result = map_ranges(start, end, np.array(ranges))
    result = np.array(result)
    expected = np.array(expected)
    sorted_result = result[np.argsort(result[:, 0])].tolist()
    sorted_expected = expected[np.argsort(expected[:, 0])].tolist()
    assert sorted_result == sorted_expected


def test_part_2_test_case():
    input = open('2023/input/day-5.test.txt').read()
    assert part2(input) == 46


def test_part_2_real_case():
    input = open('2023/input/day-5.input.txt').read()
    assert part2(input) == 52510809
