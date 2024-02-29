from day_9 import part1, part2


def test_part1_test_case():
    assert part1(open('2023/input/day-9.test.txt').read().splitlines()) == 114


def test_part1_real_case():
    assert part1(
        open('2023/input/day-9.input.txt').read().splitlines()) == 2038472161


def test_part2_test_case():
    assert part2(open('2023/input/day-9.test.txt').read().splitlines()) == 2


def test_part2_real_case():
    assert part2(
        open('2023/input/day-9.input.txt').read().splitlines()) == 1091
