import pytest
from day_5 import part1, part2


def test_part_1_test_case():
    input = open('2023/input/day-5.test.txt').read()
    assert part1(input) == 35


def test_part_1_real_case():
    input = open('2023/input/day-5.input.txt').read()
    assert part1(input) == 662197086


def test_part_2_test_case():
    input = open('2023/input/day-5.test.txt').read()
    assert part2(input) == 46

@pytest.mark.skip(reason="This test is slow")
def test_part_2_real_case():
    input = open('2023/input/day-5.input.txt').read()
    assert part2(input) == 396285104
