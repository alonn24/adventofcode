from day_16 import part1


def test_day16_part1_test_case():
    with open('2023/input/day-16.test.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 46


def test_day16_part1_real_case():
    with open('2023/input/day-16.input.txt', 'r') as file:
        case = file.read()
        assert part1(case) == 7728
