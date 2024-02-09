input = open('2022/input/day-25.input.txt').read().splitlines()


def get_entry_value(entry):
    def get_digit_value(d, i):
        d = -1 if d == '-' else -2 if d == '=' else int(d)
        return d * 5**i
    rev = reversed(entry)  # starting from the end
    return sum([get_digit_value(d, i) for i, d in enumerate(rev)])


def convert_to_decimal(snafu):
    return snafu


def part1():
    snafu = sum([get_entry_value(e) for e in input])
    return convert_to_decimal(snafu)
