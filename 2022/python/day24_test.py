from day24 import has_blizzard_after, part_1, part_2

input = [
    '#.######',
    '#.>..v.#',
    '#.<...^#',
    '###.####',
]


def test_has_blizzard_after():
    # now
    assert not has_blizzard_after(input, 1, 1, 0)
    assert has_blizzard_after(input, 1, 2, 0)

    # after wrapping a wall
    assert has_blizzard_after(input, 1, 3, 1)  # >
    assert has_blizzard_after(input, 1, 6, 4)  # > wrap a wall
    assert has_blizzard_after(input, 1, 1, 5)  # >
    assert has_blizzard_after(input, 1, 2, 6)  # >
    assert has_blizzard_after(input, 1, 3, 7)  # >
    assert has_blizzard_after(input, 1, 3, 7)  # >
    assert has_blizzard_after(input, 1, 1, 5+6*3)  # > several wraps

    assert has_blizzard_after(input, 2, 1, 1)  # <
    assert has_blizzard_after(input, 2, 6, 2)  # < wrap a wall
    assert has_blizzard_after(input, 2, 5, 3)  # <
    assert has_blizzard_after(input, 2, 6, 2+6*3)  # < several wraps

    assert has_blizzard_after(input, 2, 5, 1)  # v
    assert has_blizzard_after(input, 1, 5, 2)  # v wrap a wall
    assert has_blizzard_after(input, 2, 5, 3)  # v
    assert has_blizzard_after(input, 1, 5, 2+2*3)  # v several wraps

    assert has_blizzard_after(input, 1, 6, 1)  # ^
    assert has_blizzard_after(input, 2, 6, 2)  # ^
    assert has_blizzard_after(input, 1, 6, 3)  # ^ wrap a wall
    assert has_blizzard_after(input, 1, 6, 1+2*3)  # ^ several wraps


def test_part_1():
    assert part_1() == 305


def test_part_2():
    assert part_2() == 905
