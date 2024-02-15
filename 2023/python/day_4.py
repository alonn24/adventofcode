import re
import numpy as np
from functools import reduce


def parse_row(row):

    [part1, part2] = row.split(':')[1].split('|')
    return [np.array(re.findall(r'(\d+)', x)) for x in [part1, part2]]


def part1(input):
    print('')
    cards = [parse_row(row) for row in input]
    intersected = [np.intersect1d(a, b).size for [a, b] in cards]
    positive_intersections = [x for x in intersected if x > 0]
    return reduce(lambda res, y: res + 2**(y-1), positive_intersections, 0)
