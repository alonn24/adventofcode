from day_3 import part1, part2


def test_day3_part1_test_case():
    testcase = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    assert part1(testcase) == (2*4 + 5*5 + 11*8 + 8*5)


def test_day3_part1_real_case():
    with open("day_3.input.txt", "r") as f:
        data = f.read()
        assert part1(data) == 7


def test_day3_part2_test_case():
    testcase = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
    assert part2(testcase) == (2*4 + 8*5)


def test_day3_part2_real_case():
    with open("day_3.input.txt", "r") as f:
        data = f.read()
        assert part2(data) == 62098619
