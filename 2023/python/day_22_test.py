import pytest
from day_22 import part1, part2

testcase1 = r'''
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
'''


def test_day22_part1_testcase():
    assert part1(testcase1) == 5


def test_day22_part1_realcase():
    with open('2023/input/day-22.input.txt', 'r') as f:
        data = f.read()
    assert part1(data) == 501


def test_day22_part2_testcase():
    assert part2(testcase1) == 7


@pytest.mark.skip(reason="This test takes too long")
def test_day22_part2_realcase():
    with open('2023/input/day-22.input.txt', 'r') as f:
        data = f.read()
    assert part2(data) == 80948
