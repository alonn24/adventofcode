from day_14 import part1, part2


def test_day14_part1_test_case():
    with open('2023/input/day-14.test.txt', 'r') as file:
        data = file.read()
        assert part1(data) == 136


def test_day14_part1_real_case():
    with open('2023/input/day-14.input.txt', 'r') as file:
        data = file.read()
        assert part1(data) == 103614


def test_day14_part2_test_case():
    with open('2023/input/day-14.test.txt', 'r') as file:
        data = file.read()
        assert part2(data) == 64


def test_day14_part2_real_case():
    with open('2023/input/day-14.input.txt', 'r') as file:
        data = file.read()
        assert part2(data) == 83790
