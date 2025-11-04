import pytest
from python.year2023.day_16 import part1, part2
from pathlib import Path


def test_day16_part1_test_case():
    with open(Path('inputs/2023/day-16.test.txt'), 'r') as file:
        case = file.read()
        assert part1(case) == 46


def test_day16_part1_real_case():
    with open(Path('inputs/2023/day-16.input.txt'), 'r') as file:
        case = file.read()
        assert part1(case) == 7728


def test_day16_part2_test_case():
    with open(Path('inputs/2023/day-16.test.txt'), 'r') as file:
        case = file.read()
        assert part2(case) == 51


@pytest.mark.skip(reason="This test takes too long")
def test_day16_part2_real_case():
    with open(Path('inputs/2023/day-16.input.txt'), 'r') as file:
        case = file.read()
        assert part2(case) == 8061
