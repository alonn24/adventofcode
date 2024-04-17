import pytest
from day_23 import part1, part2

testcase1 = '''
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
'''


def test_day23_part1_testcase():
    assert part1(testcase1) == 94


def test_day23_part1_realcase():
    with open('2023/input/day-23.input.txt', 'r') as f:
        assert part1(f.read()) == 2030


def test_day23_part2_testcase():
    assert part2(testcase1) == 154


@pytest.mark.skip(reason="This test takes too long")
def test_day23_part2_realcase():
    with open('2023/input/day-23.input.txt', 'r') as f:
        assert part2(f.read()) == 6390
