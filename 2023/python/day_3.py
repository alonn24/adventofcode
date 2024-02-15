import numpy as np
from functools import reduce


def collection_numbers(data, ixs):
    ns = {}
    for i, j in ixs:
        row = data[i]
        start = j
        end = j
        while start > 0 and row[start - 1].isdigit():
            start -= 1
        while end < len(row) - 1 and row[end + 1].isdigit():
            end += 1
        ns[f'{i}:{start}:{end+1}'] = int(''.join(row[start:end+1]))
    return ns


def part1(input):
    data = np.array([[*row] for row in input])

    # digits mask
    digits = np.char.isdigit(data)
    # symbol mask
    symbols = (data != '.')
    symbols[digits] = False

    # mask all neighbors of symbols
    intersections = digits & np.pad(symbols[1:], [(0, 1), (0, 0)]) | \
        digits & np.pad(symbols[:-1], [(1, 0), (0, 0)]) | \
        digits & np.pad(symbols[:, 1:], [(0, 0), (0, 1)]) | \
        digits & np.pad(symbols[:, :-1], [(0, 0), (1, 0)]) | \
        digits & np.pad(symbols[1:, 1:], [(0, 1), (0, 1)]) | \
        digits & np.pad(symbols[:-1, :-1], [(1, 0), (1, 0)]) | \
        digits & np.pad(symbols[1:, :-1], [(0, 1), (1, 0)]) | \
        digits & np.pad(symbols[:-1, 1:], [(1, 0), (0, 1)])

    ixs = [*zip(*intersections.nonzero())]
    ns = collection_numbers(data, ixs)
    return sum(n for n in ns.values())


GEAR = '*'

d = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]


def is_in_bounds(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[0])


def part2(input):
    data = np.array([[*row] for row in input])
    ixs = [*zip(*(data == '*').nonzero())]
    res = 0
    for i, j in ixs:
        ixs = [[i + d[0], j + d[1]]
               for d in d if is_in_bounds(data, i + d[0], j + d[1]) and data[i + d[0], j + d[1]].isdigit()]
        ns = collection_numbers(data, ixs)
        if (len(ns) > 1):
            res += reduce(lambda acc, n: acc * n, ns.values(), 1)
    return res
