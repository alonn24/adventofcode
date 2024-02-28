import pytest
import numpy as np
from day_7 import part1, get_sorted_hands


@pytest.mark.parametrize('hands, expected', [
    ([['AAAA2', 2], ['AAA23', 1]], [['AAA23', 1], ['AAAA2', 2]]),
    ([['AAAA3', 2], ['AAAA2', 1]], [['AAAA2', 1], ['AAAA3', 2]])
])
def test_get_sorted_hands(hands, expected):
    data = np.array(hands)
    result = get_sorted_hands(data)
    assert np.array_equal(result, expected)


def test_part_1_test_case():
    assert part1(open('2023/input/day-7.test.txt').read().splitlines()) == 6440


def test_part_1_real_case():
    assert part1(
        open('2023/input/day-7.input.txt').read().splitlines()) == 250347426
