from day_19 import part1, part2


def test_day19_part1_testcase():
    with open('2023/input/day-19.test.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 19114


def test_day19_part1_realcase():
    with open('2023/input/day-19.input.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 391132


def test_day19_part2_testcase():
    with open('2023/input/day-19.test.txt', 'r') as file:
        case = file.read()
        assert part2(case) == 167409079868000


def test_day19_part2_realcase():
    with open('2023/input/day-19.input.txt', 'r') as file:
        case = file.read()
        assert part2(case) == 128163929109524
