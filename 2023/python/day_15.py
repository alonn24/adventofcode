import numpy as np


def decode_part(part: str):
    result = 0
    for x in part:
        ascii_val = ord(x)
        result = ((result + ascii_val)*17) % 256
    return result


def part1(case: str):
    """
    Day 15: Lens Library
    Part 1 - hash a sequence using ASCII values
    """
    parts = np.array(case.split(','))
    decoded = [decode_part(part) for part in parts]
    return sum(decoded)
