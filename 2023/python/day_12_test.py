import pytest
from day_12 import cal_for_row, part1


@pytest.mark.parametrize("row, expected", [
    ("#.#.### 1,1,3", 1),
    ("???.### 1,1,3", 1),
    ("???.### 1,1,3", 1),
    (".??..??...?##. 1,1,3", 4),
    ("?#?#?#?#?#?#?#? 1,3,1,6", 1),
    ("????.#...#... 4,1,1", 1),
    ("????.######..#####. 1,6,5", 4),
    ("?###???????? 3,2,1", 10)
])
def test_cal_for_row(row: str, expected: int):
    assert cal_for_row(row) == expected


def test_day12_part1_test_case():
    with open("2023/input/day-12.test.txt", "r") as file:
        case = file.read()
        assert part1(case) == 21


def test_day12_part1_real_case():
    with open("2023/input/day-12.input.txt", "r") as file:
        case = file.read()
        assert part1(case) == 7674
