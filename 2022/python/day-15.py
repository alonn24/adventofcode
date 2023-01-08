import re

input = open("2022/input/day-15.input.txt", "r").read().strip().split("\n")
# Map each line to a list of integers
sensors = list(
    map(lambda x: list(map(lambda r: int(r), re.findall('[-0-9]+', x))), input))


def get_no_beacon_at_part_1(target_y):
    free_in_row = set()
    for x, y, bx, by, *_ in sensors:
        dis_x = abs(x - bx)
        dis_y = abs(y - by)
        dis_Y_to_target = abs(y - target_y)

        # We first get the current row distance and move it to the target
        # Current row start and end are the distance to the beacon + adding each y distance twice, to the left and to the right
        # The target row distance is decreasing the start and end for each y travel
        # If the target y is out of range, the start and end will exchange sides and wont be counted in the later loop
        start_x = x - dis_x - dis_y + dis_Y_to_target
        end_x = x + dis_x + dis_y - dis_Y_to_target

        # adding all the points to the set to ignore duplications
        for i in range(start_x, end_x + 1):
            free_in_row.add(i)

# removing the beacons from the free spots
    for sensor in sensors:
        _, _, bx, by, *_ = sensor
        # If the sensor is in the target row, remove it
        if by == target_y and bx in free_in_row:
            free_in_row.remove(bx)
    return list(free_in_row)


print('part 1 - ', len(get_no_beacon_at_part_1(2000000)))
