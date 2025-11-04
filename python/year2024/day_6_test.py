from python.year2024.day_6 import part1, part2
from pathlib import Path


def test_day6_part1_test_case():
    testcase = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    assert part1(testcase) == 41


def test_day6_part1_real_case():
    with open(Path('inputs/2024/day_6.input.txt'), 'r') as f:
        data = f.read()
    assert part1(data) == 4883


def test_day6_part2_test_case():
    testcase = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    assert part2(testcase) == 6

# 1829 too high
# Not 1777


def test_day6_part2_real_case():
    with open(Path('inputs/2024/day_6.input.txt'), 'r') as f:
        data = f.read()
    assert part2(data) == 1655
