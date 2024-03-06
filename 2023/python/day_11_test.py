from day_11 import part1, part2


def test_day11_part1_test_case():
    assert part1(open('2023/input/day-11.test.txt').read()) == 374


def test_day11_paty1_real_case():
    assert part1(open('2023/input/day-11.input.txt').read()) == 10154062


def test_day11_part2_test_case():
    assert part2(open('2023/input/day-11.test.txt').read(), 10) == 1030
    assert part2(open('2023/input/day-11.test.txt').read(), 100) == 8410


def test_day11_part2_real_case():
    assert part2(open('2023/input/day-11.input.txt').read(),
                 1000000) == 553083047914
