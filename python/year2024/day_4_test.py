from python.year2024.day_4 import part1, part2
from pathlib import Path


def test_day4_part1_test_case():
    testcase = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    assert part1(testcase) == 18


def test_day4_part1_real_case():
    with open(Path('inputs/2024/day_4.input.txt'), 'r') as f:
        testcase = f.read()
    assert part1(testcase) == 2562


def test_day4_part2_test_case():
    testcase = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    assert part2(testcase) == 9


def test_day4_part2_real_case():
    with open(Path('inputs/2024/day_4.input.txt'), 'r') as f:
        testcase = f.read()
    assert part2(testcase) == 1902
