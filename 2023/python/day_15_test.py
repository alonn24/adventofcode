from day_15 import part1, part2


def test_day15_part1_test_case():
    assert part1('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7') == 1320


def test_day15_part1_real_case():
    with open('2023/input/day-15.input.txt', 'r') as file:
        data = file.read()
        assert part1(data) == 508498


def test_day15_part2_test_case():
    assert part2('rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7') == 145


def test_day15_part2_real_case():
    with open('2023/input/day-15.input.txt', 'r') as file:
        data = file.read()
        assert part2(data) == 279116
