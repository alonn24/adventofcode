from sympy import symbols, solve
from enum import Enum
from functools import reduce


# Parse each row with id and indication for the type of monkey - fixed or expression


def parse_row(row):
    [id, expression] = row.split(': ')
    return id, expression.split(' ')


input = [*map(parse_row, open('2022/input/day-21.input.txt').read().splitlines())]


def part_1(monkeys):
    monkeys_map = reduce(lambda acc, monkey: {
        **acc, monkey[0]: monkey}, monkeys, {})

    def get_monkey_result(monkey):
        parts = []
        for part in monkey[1]:
            if part.isdigit() or len(part) == 1:
                # number or operation
                parts.append(part)
            else:
                # monkey id
                parts.append(str(get_monkey_result(monkeys_map[part])))
        exr = ' '.join(parts)
        return eval(exr)  # evil thing

    root = monkeys_map['root']
    return int(get_monkey_result(root))


# 331319379445180
print(f'Part 1: {part_1(input)}')

ME = 'humn'


def part_2(monkeys):
    monkeys_map = reduce(lambda acc, monkey: {
        **acc, monkey[0]: monkey}, monkeys, {})

    def get_monkey_final_expression(monkey):
        parts = []
        for part in monkey[1]:
            if part.isdigit() or len(part) == 1 or part == ME:
                # number or operation
                parts.append(part)
            elif part == ME:
                # symbol to solve the equation afterward
                parts.append(symbols(ME))
            else:
                # spread the statement in parenthesis to keep execution order
                parts = parts + \
                    ['('] + get_monkey_final_expression(monkeys_map[part]) + [')']
        return parts
    root = monkeys_map['root']

    left_expression = get_monkey_final_expression(monkeys_map[root[1][0]])
    right_expression = get_monkey_final_expression(monkeys_map[root[1][2]])

    equal_to_zero = left_expression + ['-'] + right_expression
    [sol] = solve(''.join(equal_to_zero))
    return sol


# 3715799488132
print(f'Part 2: {part_2(input)}')
