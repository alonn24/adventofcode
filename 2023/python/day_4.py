import re
import numpy as np
from functools import reduce


def parse_row(row):

    [part1, part2] = row.split(':')[1].split('|')
    return [np.array(re.findall(r'(\d+)', x)) for x in [part1, part2]]


def part1(input):
    cards = [parse_row(row) for row in input]
    intersected = [np.intersect1d(a, b) for [a, b] in cards]
    positive_intersections = [x.size for x in intersected if x.size > 0]
    return reduce(lambda res, y: res + 2**(y-1), positive_intersections, 0)


def part2(input):
    cards = [parse_row(row) for row in input]
    intersected_sizes = [np.intersect1d(a, b).size for [a, b] in cards]

    res = np.array([1 for _ in range(len(cards))])
    for i, size in enumerate(intersected_sizes):
        if (size > 0):
            number_of_cards = res[i]
            res[i+1:i+1+size] += number_of_cards
    return np.sum(res, dtype=np.int64)
