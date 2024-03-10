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


def map_ranges(start, end, ranges):
    intersected = ranges[(ranges[:, 1] <= end) &
                         (ranges[:, 2] >= start)]
    intersection_map = np.ones((end - start + 1), dtype=bool)
    # Add intersected points
    result = []
    for ied in intersected:
        gap = ied[1] - ied[0]
        result.append([max(start, ied[1]) - gap, min(end, ied[2]) - gap])
        intersection_map[max((ied[1] - start), 0):max((ied[2] - start + 1), 0)] = False
    # Add not intersected points
    indices = np.where(np.diff(np.concatenate(
        ([False], intersection_map, [False]))) != 0)[0]

    not_intersected = indices.reshape(-1, 2)
    not_intersected[:, :] += start
    not_intersected[:, 1] -= 1
    for x in not_intersected:
        result.append(x.tolist())
    return result


def part2(input):
    seeds, rounds = parse_input(input)
    seeds_pairs = seeds.reshape(-1, 2)

    # convert the gap to end range
    seeds_pairs[:, 1] = seeds_pairs[:, 0] + seeds_pairs[:, 1]

    current = seeds_pairs
    for r in rounds:
        new_current = []
        for seed in current:
            new_current.extend(map_ranges(seed[0], seed[1], r))
        current = np.array(new_current)
    return np.min(current[:, 0])
