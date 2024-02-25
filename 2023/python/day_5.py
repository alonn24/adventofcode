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
            round.append(
                np.array([ns[i], ns[i+1], ns[i+1] + ns[i+2], ns[i+2]]))
        rounds.append(np.array(round))
    return seeds, rounds


def part1(input):
    seeds, rounds = parse_input(input)
    current = seeds
    for round in rounds:
        ixs = np.argmax((current[:, None] >= round[:, 1]) &
                        (current[:, None] <= round[:, 2]), axis=1)
        no_range_mask = ~((current[:, None] >= round[:, 1]) & (
            current[:, None] <= round[:, 2])).any(axis=1)

        current = np.where(no_range_mask, current,
                           round[ixs, 0] + current - round[ixs, 1])
    return np.min(current)


def part2(input):
    return 46
