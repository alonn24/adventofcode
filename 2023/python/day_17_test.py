from day_17 import find_heat_loss


def test_day17_part1_testcase():
    with open('2023/input/day-17.test.txt', 'r') as file:
        data = file.read()
        assert find_heat_loss(data) == 102


def test_day17_part1_realcase():
    with open('2023/input/day-17.input.txt', 'r') as file:
        data = file.read()
        assert find_heat_loss(data) == 870


def test_day17_part2_testcase():
    with open('2023/input/day-17.test.txt', 'r') as file:
        data = file.read()
        assert find_heat_loss(data, min_same_dir=4, max_same_dir=10) == 94


def test_day17_part2_realcase():
    with open('2023/input/day-17.input.txt', 'r') as file:
        data = file.read()
        assert find_heat_loss(data, min_same_dir=4, max_same_dir=10) == 1063
