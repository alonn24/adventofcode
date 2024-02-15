import numpy as np


def collect(data, i, j):
    row = data[i]
    start = j
    while start > 0 and row[start - 1].isdigit():
        start -= 1
    end = j
    while end < len(row) - 1 and row[end + 1].isdigit():
        end += 1
    return f'{i}:{start}:{end+1}', int(''.join(row[start:end+1]))


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
    ns = {}
    for i, j in ixs:
        key, res = collect(data, i,  j)
        ns[key] = res
    return sum(n for n in ns.values())
