import pytest
from day_16 import part1, part2


def test_day16_part1_test_case():
    with open('2023/input/day-16.test.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 46


def test_day16_part1_real_case():
    with open('2023/input/day-16.input.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 7728


def test_day16_part2_test_case():
    with open('2023/input/day-16.test.txt', 'r') as file:
        case = file.read()
        assert part2(case) == 51


@pytest.mark.skip(reason="This test takes too long")
def test_day16_part2_real_case():
    with open('2023/input/day-16.input.txt', 'r') as file:
        case = file.read()
        assert part2(case) == 8061
