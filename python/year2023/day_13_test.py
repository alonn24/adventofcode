from python.year2023.day_13 import part1, part2
from pathlib import Path


def test_day13_part1_test_case():
    with open(Path('inputs/2023/day-13.test.txt'), 'r') as f:
        data = f.read()
        assert part1(data) == 405


def test_day13_part1_real_case():
    with open(Path('inputs/2023/day-13.input.txt'), 'r') as f:
        data = f.read()
        assert part1(data) == 30705


def test_day13_part2_test_case():
    with open(Path('inputs/2023/day-13.test.txt'), 'r') as f:
        data = f.read()
        assert part2(data) == 400


def test_day13_part2_real_case():
    with open(Path('inputs/2023/day-13.input.txt'), 'r') as f:
        data = f.read()
        assert part2(data) == 44615
