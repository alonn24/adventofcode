import re

input = open("2022/input/day-15.input.txt", "r").read().strip().split("\n")
# Map each line to a list of integers
sensors = list(
    map(lambda x: list(map(lambda r: int(r), re.findall('[-0-9]+', x))), input))


def get_row_range_for_sensor(target_y, sensor):
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


def get_free_spots_in_row(target_y, search_area):
    ranges = map(lambda sensor: list(map(
        lambda x: between(x, 0, search_area), get_row_range_for_sensor(target_y, sensor) or [])), sensors)
    ranges = filter(lambda r: len(r) > 0, ranges)
    for i in range(search_area):
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                return [target_y, i]


def get_no_beacon_at_part_2(search_area):
    for target_y in range(search_area):
        print(f'target_y - {target_y}')
        free_spot = get_free_spots_in_row(target_y, search_area)
        print(f'free_spot - {free_spot}')
        if  free_spot is not None:
            return free_spot


print('part 2 - ', get_no_beacon_at_part_2(4000000))
