import numpy as np
import re


def parse_input(_input):
    parts = _input.split('\n\n')
    instructions = re.findall('R|L', parts[0])
    nodes = np.array(re.findall('[1-9|A-Z]+', parts[1])).reshape(-1, 3)
    return instructions, nodes


def part1(_input):
    """
    --- Day 8 Part 1: Haunted Wasteland ---
    Run over the nodes by instructions and return the number of steps to reach the target
    """
    instructions, nodes = parse_input(_input)
    current = nodes[np.where(nodes[:, 0] == 'AAA')][0]
    target = nodes[np.where(nodes[:, 0] == 'ZZZ')][0]

    count = 0
    while not np.array_equal(current, target):
        # Loop over the instructions in a circular way
        instruction = instructions[count % len(instructions)]
        d = 2 if instruction == 'R' else 1
        # Get the next node
        current = nodes[np.where(nodes[:, 0] == current[d])][0]
        # Next
        count += 1

    return count


def part2(_input):
    """
    --- Day 8 Part 2 ---
    Start from any node that ends with an A until all got to a node that ends with a Z
    """
    instructions, nodes = parse_input(_input)
    current = nodes[np.char.endswith(nodes[:, 0], 'A')]

    count = 0
    # results will store the first and second occurrences of the Z nodes
    results = np.zeros(len(current), dtype=np.int64)
    while np.any(results == 0):
        # Loop over the instructions in a circular way
        instruction = instructions[count % len(instructions)]
        d = 2 if instruction == 'R' else 1
        # get next nodes
        # current = nodes[np.isin(nodes[:, 0], current[:, d])]
        current = np.array([nodes[np.where(nodes[:, 0] == c)][0]
                           for c in current[:, d]])
        count += 1
        # If we got to a Z, mark it
        z_indices = np.where(np.char.endswith(current[:, 0], 'Z'))[0]
        zero_indices = np.where(results == 0)[0]
        results[np.intersect1d(z_indices, zero_indices)] = count

    # We detect cycles and return the lcm
    return np.lcm.reduce(results)
