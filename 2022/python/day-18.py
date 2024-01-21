import itertools
import re
input = [[*map(int, re.findall('\d+', v))]
         for v in open("2022/input/day-18.input.txt")]


# all directions we can check from a cube without diagonals
check_dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, 1), (0, 0, -1)]


# a set for all cubes to check if a cube exists in O(1)
cubes_set = set([(r[0], r[1], r[2]) for r in input])


def part_1(input):
    # Get all free surfaces for a given cube
    def get_surfaces(cube, cubes_set):
        (x, y, z) = cube
        # Get all free surfaces around the cube
        return [(x+dx, y+dy, z+dz) for (dx, dy, dz) in check_dir if (x+dx, y+dy, z+dz) not in cubes_set]
    # Get all the number of free surfaces
    surfaces = [len(get_surfaces(cube, cubes_set)) for cube in input]
    # Return the total amount
    return sum(surfaces)


# 3586
print(f'part 1 - {part_1(input)}')


# Get the max x,y,z to run to
grid_size = max(itertools.chain(*input)) + 1
grid_start = -1  # we start from -1 to get the 0,0,0 cube


def get_in_bounds_check_dir(point):
    (x, y, z) = point
    return [(x+dx, y+dy, z+dz) for (dx, dy, dz) in check_dir if (x+dx >= grid_start and y+dy >= grid_start and z+dz >= grid_start and x+dx <= grid_size and y+dy <= grid_size and z+dz <= grid_size)]


def get_accessible_points(point):
    next_places = get_in_bounds_check_dir(point)
    return (
        [p for p in next_places if p in cubes_set],
        [p for p in next_places if p not in cubes_set]
    )


def part_2():
    # count any time we got blocked. we get block only by facets
    blocks = 0

    # we assume 0,0,0 is accessible
    queue = [(grid_size, grid_size, grid_size)]
    visited = set(queue)
    while (len(queue) > 0):
        point = queue.pop()
        (blocked_points, free_points) = get_accessible_points(point)

        blocks += len(blocked_points)
        queue += [p for p in free_points if p not in visited]
        visited.update(free_points)
    # Return the total amount
    return blocks


# not 2173 - too high
# not 2069 - too low
print(f'part 2 - {part_2()}')
