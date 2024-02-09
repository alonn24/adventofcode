import pytest
from day24 import has_blizzard_after, part_1

input = [
    '#.######',
    '#.>..v.#',
    '#.<...^#',
    '###.####',
]


def test_has_blizzard_after():
    # now
    assert has_blizzard_after(input, 1, 1, 0) == False
    assert has_blizzard_after(input, 1, 2, 0) == True

    # after wrapping a wall
    assert has_blizzard_after(input, 1, 3, 1) == True  # >
    assert has_blizzard_after(input, 1, 6, 4) == True  # > wrap a wall
    assert has_blizzard_after(input, 1, 1, 5) == True  # >
    assert has_blizzard_after(input, 1, 2, 6) == True  # >
    assert has_blizzard_after(input, 1, 3, 7) == True  # >
    assert has_blizzard_after(input, 1, 3, 7) == True  # >
    assert has_blizzard_after(input, 1, 1, 5+6*3) == True  # > several wraps

    assert has_blizzard_after(input, 2, 1, 1) == True  # <
    assert has_blizzard_after(input, 2, 6, 2) == True  # < wrap a wall
    assert has_blizzard_after(input, 2, 5, 3) == True  # <
    assert has_blizzard_after(input, 2, 6, 2+6*3) == True  # < several wraps

    assert has_blizzard_after(input, 2, 5, 1) == True  # v
    assert has_blizzard_after(input, 1, 5, 2) == True  # v wrap a wall
    assert has_blizzard_after(input, 2, 5, 3) == True  # v
    assert has_blizzard_after(input, 1, 5, 2+2*3) == True  # v several wraps

    assert has_blizzard_after(input, 1, 6, 1) == True  # ^
    assert has_blizzard_after(input, 2, 6, 2) == True  # ^
    assert has_blizzard_after(input, 1, 6, 3) == True  # ^ wrap a wall
    assert has_blizzard_after(input, 1, 6, 1+2*3) == True  # ^ several wraps


# @pytest.mark.skip(reason="not implemented yet")
def test_part_1():
    assert part_1() == 305
