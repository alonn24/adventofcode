from functools import reduce
import numpy as np
import re

# Return arrays with ranges, adding a second column with the range end


def parse_input(input):
    parts = input.split('\n\n')
    seeds = np.array(re.findall(r'(\d+)', parts[0]), dtype=np.int64)
    rounds = []
    for r in parts[1:]:
        round = []
        ns = [*map(int, re.findall(r'(\d+)', r))]
        for i in range(0, len(ns), 3):
            # Add an end range column to the round at [2]
            round.append(np.array([ns[i], ns[i+1], ns[i+1] + ns[i+2], ns[i+2]]))
        rounds.append(np.array(round))
    return seeds, rounds


def part1(input):
    seeds, rounds = parse_input(input)
    values_for_seeds = []
    for s in seeds:
        print(f'seed: {s}', end='')
        current = s
        for r in rounds:
            # search range [0] - is start range,  [1] - is end range
            entry = np.where(np.logical_and(
                r[:, 1] <= current, r[:, 2] >= current))
            # if we dont find one, the value stays the same
            if entry[0].size >= 1:
                # extract the target by the diff found
                rows = r[entry[0]]
                current = rows[0, 0] + (current - rows[0, 1])
            print(f'->{current}', end='')
        print('')
        values_for_seeds.append(current)
    return np.min(values_for_seeds)
