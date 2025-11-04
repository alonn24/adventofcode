from python.year2024.day_7 import part1, part2
from pathlib import Path


def test_day7_part1_test_case():
    testcase = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
    assert part1(testcase) == 3749

# 532539761362 too low


def test_day7_part1_real_case():
    with open(Path('inputs/2024/day_7.input.txt'), 'r') as f:
        testcase = f.read()
    assert part1(testcase) == 538191549061


def test_day7_part2_test_case():
    testcase = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
    assert part2(testcase) == 11387


def test_day7_part2_real_case():
    with open(Path('inputs/2024/day_7.input.txt'), 'r') as f:
        testcase = f.read()
    assert part2(testcase) == 34612812972206
