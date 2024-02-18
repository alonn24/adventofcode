import pytest
from day_5 import part1

def test_part_1_test_case():
	input = open('2023/input/day-5.test.txt').read()
	assert part1(input) == 35

def test_part_1_real_case():
	input = open('2023/input/day-5.input.txt').read()
	assert part1(input) == 662197086