from day_8 import part1, part2


def test_part_1_test_case_1():
    _input = \
        '''
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''
    assert part1(_input) == 2


def test_part_1_test_case_2():
    _input = \
        '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''
    assert part1(_input) == 6


def test_part_1_real_case():
    assert part1(open('2023/input/day-8.input.txt').read()) == 11911


def test_part_2_test_case_1():
    _input = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
    assert part2(_input) == 6


def test_part_2_real_case():
    # 1095800616108638720 too high
    assert part2(open('2023/input/day-8.input.txt').read()) == 10151663816849
