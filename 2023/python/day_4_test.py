from day_4 import part1, part2


def test_part1_test_case():
    assert part1(open('2023/input/day-4.test.txt').read().splitlines()) == 13


def test_part1_real_case():
    assert part1(
        open('2023/input/day-4.input.txt').read().splitlines()) == 21088


def test_part2_test_case():
    assert part2(open('2023/input/day-4.test.txt').read().splitlines()) == 30


def test_part2_real_case():
    assert part2(
        open('2023/input/day-4.input.txt').read().splitlines()) == 6874754
