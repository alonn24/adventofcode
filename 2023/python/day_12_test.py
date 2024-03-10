from day_12 import part1, part2, get_row_combinations


def test_day12_get_row_combinations():
    assert get_row_combinations("#.#", [1, 1]) == 1
    assert get_row_combinations("???.###", [1, 1, 3]) == 1
    assert get_row_combinations(".??..??...?##.", [1, 1, 3]) == 4
    assert get_row_combinations("?#?#?#?#?#?#?#?", [1, 3, 1, 6]) == 1
    assert get_row_combinations("????.#...#...", [4, 1, 1]) == 1
    assert get_row_combinations("????.######..#####.", [1, 6, 5]) == 4
    assert get_row_combinations("?###????????", [3, 2, 1]) == 10


def test_day12_part1_test_case():
    with open("2023/input/day-12.test.txt", "r") as file:
        assert part1(file.read()) == 21


def test_day12_part1_real_case():
    with open("2023/input/day-12.input.txt", "r") as file:
        assert part1(file.read()) == 7674


def test_day12_part2_test_case():
    with open("2023/input/day-12.test.txt", "r") as file:
        assert part2(file.read()) == 525152


def test_day12_part2_real_case():
    with open("2023/input/day-12.input.txt", "r") as file:
        assert part2(file.read()) == 4443895258186
