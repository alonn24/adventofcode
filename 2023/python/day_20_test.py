from day_20 import part1, part2
test_input1 = r'''broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a'''


def test_day20_part1_testcase1():
    assert part1(test_input1) == 32000000


test_input2 = r'''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''


def test_day20_part1_testcase2():
    assert part1(test_input2) == 11687500


def test_day20_part1_realcase():
    with open('2023/input/day-20.input.txt', 'r') as f:
        assert part1(f.read()) == 763500168


def test_day20_part2_realcase():
    with open('2023/input/day-20.input.txt', 'r') as f:
        assert part2(f.read()) == 207652583562007
