from day_13 import part1


def test_day13_part1_test_case():
    with open('2023/input/day-13.test.txt', 'r') as f:
        data = f.read()
        assert part1(data) == 405


def test_day13_part1_real_case():
    with open('2023/input/day-13.input.txt', 'r') as f:
        data = f.read()
        assert part1(data) == 30705
