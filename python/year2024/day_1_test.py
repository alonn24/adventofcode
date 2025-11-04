from python.year2024.day_1 import part1, part2
from pathlib import Path


def test_day1_part1_test_case():
    testcase = '''3   4
4   3
2   5
1   3
3   9
3   3'''
    assert part1(testcase) == 11


def test_day1_part1_real_case():
    with open(Path("inputs/2024/day_1.input.txt"), "r") as file:
        testcase = file.read()
        assert part1(testcase) == 936063


def test_day1_part2_test_case():
    testcase = '''3   4
4   3
2   5
1   3
3   9
3   3'''
    assert part2(testcase) == 31


def test_day1_part2_real_case():
    with open(Path("inputs/2024/day_1.input.txt"), "r") as file:
        testcase = file.read()
        assert part2(testcase) == 23150395
