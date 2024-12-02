from day_2 import part1, part2


def test_day2_part1_test_case():
    testcase = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    assert part1(testcase) == 2


def test_day2_part1_real_case():
    with open('day_2.input.txt', 'r') as f:
        testcase = f.read()
        assert part1(testcase) == 686


def test_day2_part2_test_case():
    testcase = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    assert part2(testcase) == 4

def test_day2_part2_real_case():
		with open('day_2.input.txt', 'r') as f:
				testcase = f.read()
				assert part2(testcase) == 717
