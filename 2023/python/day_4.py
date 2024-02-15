import re
import numpy as np


def parse_row(row):

    [part1, part2] = row.split(':')[1].split('|')
    return [np.array(re.findall(r'(\d+)', x)) for x in [part1, part2]]


def part1(input):
    print('')
    cards = [parse_row(row) for row in input]
    res = 0
    for [a, b] in cards:
        intersected = np.intersect1d(a, b)
        if (intersected.size > 0):
            res += 2**(intersected.size-1)

    return res
