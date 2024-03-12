import numpy as np
from typing import Any


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


def part2(case: str):
    """
    Part 2 - organize the lens in boxes
    """
    parts = np.array(case.split(','))
    lens = np.unique(np.array([part.split('=')[0] for part in parts if '=' in part]))
    index_map = {item: index for index, item in enumerate(lens)}

    # Box index are the rows and the lens are the columns
    # The column index is the parts index
    # We save the round count so we can sort later on
    # boxes = (box, lens, focal length)
    boxes = np.zeros((256, len(lens), 2), dtype=np.int64)
    for i, part in enumerate(parts):
        if '-' in part:
            # Turn off the lens
            lens = part.split('-')[0]
            if not lens in index_map:
                continue
            box = decode_part(lens)
            boxes[box, index_map[lens], 0] = 0
        if '=' in part:
            # Turn on the lens with the round number
            lens, focal = part.split('=')
            if not lens in index_map:
                continue
            box = decode_part(lens)
            # Set order only if not exists
            if boxes[box, index_map[lens], 0] == 0:
                boxes[box, index_map[lens], 0] = i + 1
            boxes[box, index_map[lens], 1] = focal

    # Calculate the score for each box
    scores = np.array([get_box_score(box, i) for i, box in enumerate(boxes)])
    return np.sum(scores)


def get_box_score(box: np.ndarray[int, Any], box_idx: int):
    # remove zeros
    box = box[box[:, 0] != 0]
    # sort by first column - order value
    box = box[np.argsort(box[:, 0])]

    # Each lens score is (box index * lens index * focal length)
    box_scores = [(box_idx+1) * (i + 1) * box[i, 1] for i in range(len(box))]
    return sum(box_scores)
