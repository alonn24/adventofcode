import re
from enum import Enum
from functools import reduce


# Parse each row with id and indication for the type of monkey - fixed or expression


def parse_row(row):
    [id, expression] = row.split(': ')
    return id, expression.split(' ')


input = [*map(parse_row, open('2022/input/day-21.input.txt').read().splitlines())]


def get_monkey_result(moneys_map, monkey):
    parts = []
    for part in monkey[1]:
        if part.isdigit() or len(part) == 1:
            # number or operation
            parts.append(part)
        else:
            # monkey id
            parts.append(str(get_monkey_result(
                moneys_map, moneys_map[part])))
    exr = ' '.join(parts)
    print(exr)
    return eval(exr)


def part_1(monkeys):
    moneys_map = reduce(lambda acc, monkey: {
                        **acc, monkey[0]: monkey}, monkeys, {})
    root = moneys_map['root']
    return get_monkey_result(moneys_map, root)

# 331319379445180
print(f'Part 1: {part_1(input)}')
