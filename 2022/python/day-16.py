from functools import reduce
import re
from functools import wraps

input = open("2022/input/day-16.input.txt", "r")


def extract_values_from_row(row):
    part1, part2, *_ = row.split(";")
    result = {}
    result[part1[6:8]] = {'rate': int(part1[23:]),
                          'related_valves': re.findall(r"([A-Z]{2})", part2)}
    return result


all_valves = reduce(lambda result, row: result | extract_values_from_row(row),
                    open("2022/input/day-16.input.txt"),
                    {})


def traverse_valves(valve, opened_valves, minutes_left):
    if (minutes_left <= 0):
        return 0
    # count the current valve by opened
    related_valves = all_valves[valve]['related_valves']

    # decide to opened the valve - we decrease 2 minutes, 1 extra for opening the valve
    open_valve_sums = [0]
    if all_valves[valve]['rate'] > 0 and valve not in opened_valves:
        # If we open the valve, sum the current rate as well
        current_round_sum = all_valves[valve]['rate'] * minutes_left
        open_valve_sums = [*map(lambda x: current_round_sum + traverse_valves(
            x, opened_valves + [valve], minutes_left - 2), related_valves)]

    # decide not to opened the valve
    not_open_valve_sums = [*map(lambda x: traverse_valves(
        x, opened_valves, minutes_left - 1), related_valves)]

    # return the better result
    result = max(*open_valve_sums, *not_open_valve_sums)
    return result


def part1():
    # build a map from the valves to the rate and related valves
    sum = traverse_valves('AA', [], 30)
    return sum


print(part1())
