import numpy as np
from day_5 import compare, is_in_order, part1, part2


def test_day5_compare():
    assert compare(1, 2, np.array([[1, 2]])) == -1
    assert compare(1, 2, np.array([[2, 1]])) == 1
    assert compare(1, 3, np.array([[2, 1]])) == 0


def test_day5_is_in_order():
    rules = np.array([[1, 2], [3, 4]])
    assert is_in_order(np.array([1, 2]), rules)
    assert is_in_order(np.array([1, 5, 2]), rules)
    assert not is_in_order(np.array([2, 1]), rules)


def test_day5_part1_test_case():
    testcase = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
    assert part1(testcase) == 143


def test_day5_part1_real_case():
    with open('day_5.input.txt', 'r') as f:
        testcase = f.read()
    assert part1(testcase) == 5329


def test_day5_part2_test_case():
    testcase = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
    assert part2(testcase) == 123


def test_day5_part2_real_case():
    with open('day_5.input.txt', 'r') as f:
        testcase = f.read()
    assert part2(testcase) == 5833
