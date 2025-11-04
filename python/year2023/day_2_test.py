from python.year2023.day_2 import part1, part2
from pathlib import Path


def test_day2_part1_test_case():
    with open(Path("inputs/2023/day-2.input.txt"), "r") as file:
        assert part1(file.read()) == 2348


def test_day2_part2_test_case():
    with open(Path("inputs/2023/day-2.input.txt"), "r") as file:
        assert part2(file.read()) == 76008
