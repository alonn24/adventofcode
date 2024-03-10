input = open('2022/input/day-25.input.txt').read().splitlines()


def get_entry_value(entry):
    def get_digit_value(d, i):
        d = -1 if d == '-' else -2 if d == '=' else int(d)
        return d * 5**i
    rev = reversed(entry)  # starting from the end
    return sum([get_digit_value(d, i) for i, d in enumerate(rev)])


def convert_to_snafu(d):
    if d == 0:
        return ''
    current = '=-012'[(d+2) % 5]
    return convert_to_snafu((d+2)//5) + current


def f(s): return f(s[:-1])*5 + '=-012'.find(s[-1])-2 if s else 0
def g(d): return g((d+2)//5) + '=-012'[(d+2) % 5] if d else ''


def part1():
    d = sum([get_entry_value(e) for e in input])
    return convert_to_snafu(d)
