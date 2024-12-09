import numpy as np
import re


def is_possible_equation(res: int, items: list[int], accumulator: int = 0) -> bool:
    if len(items) == 0:
        return res == accumulator
    [item, *rest_of_items] = items
    return (
        is_possible_equation(res, rest_of_items, accumulator + item) or
        is_possible_equation(res, rest_of_items, accumulator * item))


def part1(testcase: str):
    lines = [np.array(re.findall(r'(\d+)', row), dtype=int) for row in testcase.splitlines()]
    results = [res for res, *items in lines if is_possible_equation(res, items)]
    return sum(results)
