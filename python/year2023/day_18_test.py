from python.year2023.day_18 import part1, part2
from pathlib import Path


def test_day18_part1_testcase():
    with open(Path('inputs/2023/day-18.test.txt')) as file:
        case = file.read()
        assert part1(case) == 62


def test_day18_part1_realcase():
    with open(Path('inputs/2023/day-18.input.txt')) as file:
        case = file.read()
        assert part1(case) == 33491


def test_day18_part2_testcase():
    with open(Path('inputs/2023/day-18.test.txt')) as file:
        case = file.read()
        assert part2(case) == 952408144115


def test_day18_part2_realcase():
    with open(Path('inputs/2023/day-18.input.txt')) as file:
        case = file.read()
        assert part2(case) == 87716969654406
