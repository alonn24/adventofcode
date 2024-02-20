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


def run_for_seed(seed, rounds):
    current = seed
    for r in rounds:
        # search range [0] - is start range,  [1] - is end range
        entry = np.where(np.logical_and(
            r[:, 1] <= current, r[:, 2] >= current))
        # if we dont find one, the value stays the same
        if entry[0].size >= 1:
            # extract the target by the diff found
            rows = r[entry[0]]
            current = rows[0, 0] + (current - rows[0, 1])
    return current


def part1(input):
    seeds, rounds = parse_input(input)
    values_for_seeds = [run_for_seed(s, rounds) for s in seeds]
    return np.min(values_for_seeds)


def run_ranged_round(seeds, round):
    v_seeds = seeds[:, None]
    ixs = np.argmax((v_seeds >= round[:, 1]) &
                    (v_seeds <= round[:, 2]), axis=1)
    no_range_mask = ~((v_seeds >= round[:, 1]) & (
        v_seeds <= round[:, 2])).any(axis=1)

    result = np.where(no_range_mask, seeds,
                      round[ixs, 0] + seeds - round[ixs, 1])
    return result


def part2(input):
    seeds, rounds = parse_input(input)
    seeds_ranges = [[*range(seeds[x], seeds[x] + seeds[x+1])]
                    for x in range(0, len(seeds), 2)]
    all_seeds = np.array([x for row in seeds_ranges for x in row])
    current = all_seeds
    for r in rounds:
        current = run_ranged_round(current, r)
    return np.min(current)
