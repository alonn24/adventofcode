input = open('2022/input/day-25.input.txt').read().splitlines()


def get_digit_value(d, i):
    d = -1 if d == '-' else -2 if d == '=' else int(d)
    return d * 5**i


def get_entry_value(entry):
    rev = reversed(entry) # starting from the end
    return sum([get_digit_value(d, i) for i, d in enumerate(rev)])


def part1():
    return True
