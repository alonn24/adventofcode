import numpy as np
import re


def is_possible_equation(
        res: int,
        items: list[int],
        accumulator: int = 0) -> bool:
    if len(items) == 0:
        return res == accumulator
    [item, *rest_of_items] = items
    return (
        is_possible_equation(res, rest_of_items, accumulator + item) or
        is_possible_equation(res, rest_of_items, accumulator * item))


def part1(testcase: str):
    lines = [np.array(re.findall(r'(\d+)', row), dtype=int)
             for row in testcase.splitlines()]
    results = [
        res for res,
        *
        items in lines if is_possible_equation(
            res,
            items)]
    return sum(results)


MKey = tuple[int, tuple[int, ...], int]
MType = dict[MKey, bool]


def is_possible_equation_with_split(
        res: int,
        items: list[int],
        accumulator: int = 0,
        memo: MType = {}
) -> bool:
    # Memo
    key: MKey = (res, tuple(items), accumulator)
    if key in memo:
        return memo[key]
    if len(items) == 0:
        result = res == accumulator
        memo[key] = result
        return result
    elif res < accumulator:
        memo[key] = False
        return False
    [item, *rest_of_items] = items
    result = (is_possible_equation_with_split(res,
                                              rest_of_items,
                                              accumulator + item,
                                              memo) or is_possible_equation_with_split(res,
                                                                                       rest_of_items,
                                                                                       accumulator * item,
                                                                                       memo) or is_possible_equation_with_split(res,
                                                                                                                                rest_of_items,
                                                                                                                                int(str(accumulator) + str(item)),
                                                                                                                                memo))
    memo[key] = result
    return result


def part2(testcase: str):
    lines = [np.array(re.findall(r'(\d+)', row), dtype=int)
             for row in testcase.splitlines()]
    results = [
        res for res,
        *
        items in lines if is_possible_equation_with_split(
            res,
            items)]
    return sum(results)
