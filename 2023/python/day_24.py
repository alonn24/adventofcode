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


def part2(case: str):
    hailstones = np.array(re.findall(r'-?\d+', case), dtype=np.int64).reshape(-1, 6)
    n = len(hailstones)

    pts = hailstones[:, :3].tolist()
    vels = hailstones[:, 3:].tolist()
    p1, v1 = pts[0], vels[0]
    for i in range(1, n):
        if indep(v1, vels[i]):
            p2, v2 = pts[i], vels[i]
            break
    for j in range(i+1, n):
        if indep(v1, vels[j]) and indep(v2, vels[j]):
            p3, v3 = pts[j], vels[j]
            break

    rock, S = find_rock(p1, v1, p2, v2, p3, v3)
    return sum(rock) / S


def find_rock(p1: list[int], v1: list[int], p2: list[int], v2: list[int], p3: list[int], v3: list[int]):
    a, A = find_plane(p1, v1, p2, v2)
    b, B = find_plane(p1, v1, p3, v3)
    c, C = find_plane(p2, v2, p3, v3)

    w = lin(A, cross(b, c), B, cross(c, a), C, cross(a, b))
    wx, wy, wz = w
    t = dot(a, cross(b, c))
    # given that w is integer, so force it here to avoid carrying through
    # imprecision
    # rest of the computation is integer except the final division
    w = [round(wx / t), round(wy / t), round(wz / t)]

    w1 = sub(v1, w)
    w2 = sub(v2, w)
    ww = cross(w1, w2)

    E = dot(ww, cross(p2, w2))
    F = dot(ww, cross(p1, w1))
    G = dot(p1, ww)
    S = dot(ww, ww)

    rock = lin(E, w1, -F, w2, G, ww)
    return (rock, S)


def find_plane(p1: list[int], v1: list[int], p2: list[int], v2: list[int]):
    p12 = sub(p1, p2)
    v12 = sub(v1, v2)
    vv = cross(v1, v2)
    return (cross(p12, v12), dot(p12, vv))


def cross(a: list[int], b: list[int]):
    ax, ay, az = a
    ba, by, bz = b
    return [ay*bz - az*by, az*ba - ax*bz, ax*by - ay*ba]


def dot(a: list[int], b: list[int]):
    ax, ay, az = a
    ba, by, bz = b
    return ax*ba + ay*by + az*bz


def sub(a: list[int], b: list[int]):
    ax, ay, az = a
    ba, by, bz = b
    return [ax-ba, ay-by, az-bz]


def lin(r: int, a: list[int], s: int, b: list[int], t: int, c: list[int]):
    ax, ay, az = a
    bx, by, bz = b
    cx, cy, cz = c
    return [
        r*ax + s*bx + t*cx,
        r*ay + s*by + t*cy,
        r*az + s*bz + t*cz
    ]


def indep(a: list[int], b: list[int]):
    return any(v != 0 for v in cross(a, b))
