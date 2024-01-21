
import functools
import re
input = [[*map(int, re.findall('\d+', v))]
         for v in open("2022/input/day-18.input.txt")]

# add the
check_dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def get_surfaces(cube, cubes_set):
    (x, y, z) = cube
    # Get all free surfaces around the cube
    return [(x+dx, y+dy, z+dz) for (dx, dy, dz) in check_dir if (x+dx, y+dy, z+dz) not in cubes_set]


def part_1(input):
    # a set for all cubes to check if a cube exists in O(1)
    cubes_set = set([(r[0], r[1], r[2]) for r in input])
    # Get all the number of free surfaces
    surfaces = [len(get_surfaces(cube, cubes_set)) for cube in input]
    # Return the total amount
    return sum(surfaces)


# 3586
print(f'part 1 - {part_1(input)}')
