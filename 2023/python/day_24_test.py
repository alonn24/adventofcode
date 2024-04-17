from day_24 import part1, part2
testcase = '''
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
'''


def test_day24_part1_testcase():
    assert part1(testcase, 7, 27) == 2


def test_day24_part1_realcase():
    with open('2023/input/day-24.input.txt') as f:
        assert part1(f.read(), 200000000000000, 400000000000000) == 13892


def test_day24_part2_testcase():
    assert part2(testcase) == 47


def test_day24_part2_realcase():
    with open('2023/input/day-24.input.txt') as f:
        assert part2(f.read()) == 843888100572888
