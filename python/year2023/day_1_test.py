from python.year2023.day_1 import part1, part2
from pathlib import Path


def test_day1_part1_test_case():
    with open(Path("inputs/2023/day-1.input.txt"), "r") as file:
        assert part1(file.read()) == 53334


def test_day1_part2_test_case():
    with open(Path("inputs/2023/day-1.input.txt"), "r") as file:
        assert part2(file.read()) == 52834
