import numpy as np
import itertools as it
import re


def part1(case: str, min: int, max: int):
    """
                Day 24: Never Tell Me The Odds
    Part 1 - count intersections within a tested area
    """
    hailstones = np.array(re.findall(r'-?\d+', case), dtype=np.int64).reshape(-1, 6)

    count = 0
    # For every two stones combination
    for a, b in it.combinations(hailstones, 2):
        apx, apy, _, avx, avy, _ = a
        bpx, bpy, _, bvx, bvy, _ = b

        # slopes
        ma = (avy/avx)
        mb = (bvy/bvx)

        # assume the lines intersect
        if ma == mb:
            continue

        # calc c -> y = mx + c
        ca = apy - (ma*apx)
        cb = bpy - (mb*bpx)

        # intersection point when apx = bpx and apy = bpy
        xpos = (cb-ca)/(ma-mb)
        ypos = ma*xpos + ca

        # Check if the stones were in this position in the past
        a_passed = (xpos < apx and avx > 0) or (xpos > apx and avx < 0)
        b_passed = (xpos < bpx and bvx > 0) or (xpos > bpx and bvx < 0)
        if a_passed or b_passed:
            continue
        if min <= xpos <= max and min <= ypos <= max:
            count += 1
    return count
