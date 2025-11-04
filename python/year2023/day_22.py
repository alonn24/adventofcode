import re
import numpy as np
from typing import Any


def read_input(case: str):
    """
    @param case: str
    @return: np.array of shape (n, 2, 3)
    """
    return np.array(re.findall(r'\d+', case), dtype=np.int64).reshape(-1, 2, 3)


def has_bottom_support(bricks: np.ndarray[int, np.dtype[np.int64]],
                       brick: np.ndarray[int, Any],
                       floor: int = 0) -> bool:
    # Check if the brick is on the ground
    if np.min(brick[:, 2]) <= floor + 1:
        return True

    # Check only bricks under the current one
    z = brick[0, 2] - 1
    bottom_bricks = bricks[(bricks[:, 0, 2] == z) | (bricks[:, 1, 2] == z)]

    # Check if we have bricks directly under the current one
    # X-axis overlap checks
    bb_x0 = bottom_bricks[:, 0, 0]
    bb_x1 = bottom_bricks[:, 1, 0]
    b_x0 = brick[0, 0]
    b_x1 = brick[1, 0]
    x_contains_start = (bb_x0 >= b_x0) & (bb_x0 <= b_x1)
    x_contains_end = (bb_x1 >= b_x0) & (bb_x1 <= b_x1)
    x_spans = (bb_x0 <= b_x0) & (bb_x1 >= b_x1)
    has_support_x = x_contains_start | x_contains_end | x_spans

    # Y-axis overlap checks
    bb_y0 = bottom_bricks[:, 0, 1]
    bb_y1 = bottom_bricks[:, 1, 1]
    b_y0 = brick[0, 1]
    b_y1 = brick[1, 1]
    y_contains_start = (bb_y0 >= b_y0) & (bb_y0 <= b_y1)
    y_contains_end = (bb_y1 >= b_y0) & (bb_y1 <= b_y1)
    y_spans = (bb_y0 <= b_y0) & (bb_y1 >= b_y1)
    has_support_y = y_contains_start | y_contains_end | y_spans
    return bool(np.any(has_support_x & has_support_y))


def push_bricks_down(bricks: np.ndarray[int, Any]) -> np.ndarray[int, Any]:
    """
    @param in_bricks: np.array of shape (n, 2, 3)
    @return: np.array of shape (n, 2, 3)
    Push bricks down until they have support
    """
    updated = True
    while updated:
        updated = False
        for i in range(len(bricks)):
            if not has_bottom_support(bricks, bricks[i]):
                bricks[i, :, 2] -= 1
                updated = True
    return bricks


def get_bricks_without(bricks: np.ndarray[int, Any], i: int):
    top_z = bricks[i, 1, 2]
    # Filter out the current brick
    bricks_without = np.vstack([bricks[:i, :, :], bricks[i + 1:, :, :]])
    # Filter same level and top level bricks
    bricks_without = bricks_without[
        (bricks_without[:, 1, 2] == top_z) |
        (bricks_without[:, 0, 2] == top_z + 1)]
    return bricks_without, top_z


def filter_out_brick(
        bricks: np.ndarray[int, Any], brick: np.ndarray[int, Any]):
    return bricks[np.where(np.any(bricks != brick, axis=(1, 2)))[0]]


def get_falling_bricks_without(
        bricks: np.ndarray[int, Any], brick: np.ndarray[int, Any]) -> np.ndarray[int, Any]:
    # Filter out the current brick
    bricks_without = filter_out_brick(bricks, brick)

    # Filter same level and top level bricks
    top_z = brick[1, 2]
    bricks_without = bricks_without[
        (bricks_without[:, 1, 2] == top_z) |
        (bricks_without[:, 0, 2] == top_z + 1)]
    return np.array([bricks for brick in bricks_without if not has_bottom_support(
        bricks_without, brick, floor=top_z - 1)])


def part1(case: str):
    """
    Day 22: Sand Slabs
    Part 1 - find which bricks are not supporting any other bricks
    """
    bricks = read_input(case)
    bricks = bricks[bricks[:, 0, 2].argsort()]
    bricks = push_bricks_down(bricks)

    free_bricks = [
        brick for brick in bricks if len(
            get_falling_bricks_without(
                bricks, brick)) == 0]
    return len(free_bricks)


def part2(case: str):
    """
    Part 2 - count chains of bricks to fall
    """
    bricks = read_input(case)
    bricks = bricks[bricks[:, 0, 2].argsort()]
    bricks = push_bricks_down(bricks)

    count = 0
    for brick in bricks:
        # Filter the brick out, push the bricks down
        bricks_without = filter_out_brick(bricks, brick)
        after_falling = push_bricks_down(bricks_without.copy())
        # Count all bricks that changed their height.
        changed_z = bricks_without[:, 0, 2] != after_falling[:, 0, 2]
        count += len(np.nonzero(changed_z)[0])
    return count
