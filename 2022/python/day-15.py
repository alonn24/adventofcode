import re

input = open("2022/input/day-15.input.txt", "r").read().strip().split("\n")
# Map each line to a list of integers
sensors = list(
    map(lambda x: list(map(lambda r: int(r), re.findall('[-0-9]+', x))), input))


def get_row_range_for_sensor(target_y, sensor, from_limit=None, to_limit=None):
    x, y, bx, by, *_ = sensor
    dis_x = abs(x - bx)
    dis_y = abs(y - by)
    dis_Y_to_target = abs(y - target_y)

    # We first get the current row distance and move it to the target
    # Current row start and end are the distance to the beacon + adding each y distance twice, to the left and to the right
    # The target row distance is decreasing the start and end for each y travel
    # If the target y is out of range, the start and end will exchange sides and wont be counted in the later loop
    start_x = x - dis_x - dis_y + dis_Y_to_target
    end_x = x + dis_x + dis_y - dis_Y_to_target

    # If the start is bigger than the end, the row is out of range
    if start_x > end_x:
        return None
    if from_limit is not None and to_limit is not None:
        return [between(start_x, from_limit, to_limit), between(end_x, from_limit, to_limit)]
    return [start_x, end_x]


def get_no_beacon_at_part_1(target_y):
    free_in_row = set()
    for x, y, bx, by, *_ in sensors:
        row_range = get_row_range_for_sensor(target_y, [x, y, bx, by])
        if row_range is None:
            continue
        # adding all the points to the set to ignore duplications
        for i in range(row_range[0], row_range[1] + 1):
            free_in_row.add(i)

# removing the beacons from the free spots
    for sensor in sensors:
        _, _, bx, by, *_ = sensor
        # If the sensor is in the target row, remove it
        if by == target_y and bx in free_in_row:
            free_in_row.remove(bx)
    # return the list of the free spots on target_y
    return list(free_in_row)


# answer - 4861076
print('part 1 - ', len(get_no_beacon_at_part_1(2000000)))


def between(x, start, end):
    return min(max(x, start), end)


# In order to run faster we skip taken ranges iteratively and not going one by one
def get_free_spot_in_row(target_y, search_area):
    row_range_for_sensor = [*filter(lambda x: x is not None, map(
        lambda sensor: get_row_range_for_sensor(target_y, sensor, 0, search_area), sensors))]
    # start walking the row from 0 skipping with ranges
    i = 0
    while (i <= search_area):
        # find the next range that can jump i forward
        range = next(
            (x for x in row_range_for_sensor if x[0] <= i and x[1] >= i), None)
        if range is None:
            # We have found a place without it being taken by a sensor, this is for sure our free spot
            return [i, target_y]
        elif i <= range[1]:
            # Skip this range and keep skipping the next one
            i = range[1]+1


def get_no_beacon_at_part_2(search_area):
    # We go over all the lines and search for a free spot
    for target_y in range(search_area):
        print('target_y', target_y, end='\r')
        free_spot = get_free_spot_in_row(target_y, search_area)
        if free_spot is not None:
            return free_spot

# part 2 -  [2662275, 3160102]
free_spot = get_no_beacon_at_part_2(4000000)
print('part 2 - ', free_spot[0]*4000000+free_spot[1]) # 10649103160102
