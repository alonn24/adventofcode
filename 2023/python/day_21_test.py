import pytest
from day_21 import part1, part2

testcase1 = r'''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
'''


def test_day21_part1_testcase():
    assert part1(testcase1, 6) == 16


def test_day21_part1_realcase():
    with open('2023/input/day-21.input.txt', 'r') as f:
        assert part1(f.read(), 64) == 3666


@pytest.mark.skip(reason="This test takes too long")
def test_day21_part2_realcase():
    with open('2023/input/day-21.input.txt', 'r') as f:
        assert part2(f.read(), 26501365) == 609298746763952
