from python.year2024.day_8 import get_antinode, get_antinode_on_line, part1, part2
from pathlib import Path


def test_get_antinode():
    # x . a . a . x . .
    assert get_antinode((0, 3), (0, 5)) == [(0, 1), (0, 7)]
    assert get_antinode((3, 0), (5, 0)) == [(1, 0), (7, 0)]
    # x . . .
    # . a . .
    # . . a .
    # . . . x
    assert get_antinode((1, 1), (2, 2)) == [(0, 0), (3, 3)]
    # . . . x
    # . . a .
    # . a . .
    # x . . .
    assert get_antinode((1, 2), (2, 1)) == [(0, 3), (3, 0)]
    # . . . . . . . .
    # . x . . . . . .
    # . . . a . . . .
    # . . . . . a . .
    # . . . . . . . x
    # . . . . . . . .
    assert get_antinode((2, 3), (3, 5)) == [(1, 1), (4, 7)]


def test_day8_part1_testcase():
    testcase = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    assert part1(testcase) == 14


def test_day8_part1_real_case():
    with open(Path('inputs/2024/day_8.input.txt'), 'r') as f:
        testcase = f.read()
    assert part1(testcase) == 271


def test_get_antinode_on_line():
    # x . a . a . x . x
    result = get_antinode_on_line((1, 10), (0, 3), (0, 5))
    assert sorted(result) == sorted([(0, 1), (0, 3), (0, 5), (0, 7), (0, 9)])

    result = get_antinode_on_line((10, 1), (3, 0), (5, 0))
    assert sorted(result) == sorted([(1, 0), (3, 0), (5, 0), (7, 0), (9, 0)])


def test_day8_part2_testcase():
    testcase = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    assert part2(testcase) == 34


def test_day8_part2_real_case():
    with open(Path('inputs/2024/day_8.input.txt'), 'r') as f:
        testcase = f.read()
    assert part2(testcase) == 994
