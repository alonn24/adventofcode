from day_3 import part1, part2

def test_part1_test_case():
	assert part1(open('2023/input/day-3.input.txt').read().splitlines()) == 4361

def test_part1_real_case():
	# 326410 too low
	assert part1(open('2023/input/day-3-real.input.txt').read().splitlines()) == 539433

def test_part2_test_case():
	assert part2(open('2023/input/day-3.input.txt').read().splitlines()) == 467835

def test_part2_real_case():
	assert part2(open('2023/input/day-3-real.input.txt').read().splitlines()) == 75847567