from day_6 import part1


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
    with open('day_6.input.txt', 'r') as f:
        data = f.read()
    assert part1(data) == 4883
