from day_7 import part1, part2


def test_part_1_test_case():
    assert part1(open('2023/input/day-7.test.txt').read().splitlines()) == 6440


def test_part_1_real_case():
    assert part1(
        open('2023/input/day-7.input.txt').read().splitlines()) == 250347426


def test_part_2_test_case():
    assert part2(open('2023/input/day-7.test.txt').read().splitlines()) == 5905

# 251598109 too high


def test_part_2_real_case():
    assert part2(
        open('2023/input/day-7.input.txt').read().splitlines()) == 251598109
