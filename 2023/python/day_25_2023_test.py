from day_25_2023 import part1

testcase = '''
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
'''


def test_day25_part1_testcase():
    assert part1(case=testcase) == 54


def test_day25_part1_realcase():
    with open('2023/input/day-25.input.txt') as f:
        assert part1(f.read()) == 600225
