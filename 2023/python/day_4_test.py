import pytest
from day_4 import part1

def test_part1_test_case():
	assert part1(open('2023/input/day-4.test.txt').read().splitlines()) == 13

def test_part1_real_case():
	assert part1(open('2023/input/day-4.input.txt').read().splitlines()) == 21088