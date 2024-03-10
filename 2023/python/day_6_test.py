import pytest
from day_6 import part1, beat_record_ways, part2


@pytest.mark.parametrize('time, distance, expected', [
    (0, 0, 0),
    (7, 9, 4),
    (15, 40, 8),
    (30, 200, 9)
])
def test_beat_record_ways(time, distance, expected):
    assert beat_record_ways(time, distance) == expected


def test_part1_test_case():
    assert part1(open('2023/input/day-6.test.txt').read().splitlines()) == 288


def test_part1_real_case():
    assert part1(
        open('2023/input/day-6.input.txt').read().splitlines()) == 74698


def test_part2_test_case():
    assert part2(
        open('2023/input/day-6.test.txt').read().splitlines()) == 71503


def test_part2_real_case():
    assert part2(
        open('2023/input/day-6.input.txt').read().splitlines()) == 27563421
