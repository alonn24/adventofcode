from day_8 import get_antinode, part1


def test_get_antinode():
    # . x . a . a . x .
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
    with open('day_8.input.txt', 'r') as f:
        testcase = f.read()
    assert part1(testcase) == 271
