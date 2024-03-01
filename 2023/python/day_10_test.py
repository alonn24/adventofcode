import pytest
from day_10 import part1, part2


def test_day10_part1_test_case():
    case = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
    assert part1(case) == 8


def test_day10_part1_real_case():
    assert part1(open("2023/input/day-10.input.txt").read()) == 6773


case1 = """
..F7.
SFJ|.
|J.L7
|F--J
LJ...
"""
case2 = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
case3 = """
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""

case4 = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

case5 = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


@pytest.mark.parametrize("case, expected", [
    (case1, 1),
    (case2, 4),
    (case3, 4),
    (case4, 8),
    (case5, 10)
])
def test_day10_part2_test_cases(case: str, expected: int):
    assert part2(case) == expected


def test_day10_part2_real_case():
    assert part2(open("2023/input/day-10.input.txt").read()) == 495
