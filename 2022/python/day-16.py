from functools import reduce
import re

input = open("2022/input/day-16.input.txt", "r")


def extract_values_from_row(row):
    part1, part2, *_ = row.split(";")
    result = {}
    result[part1[6:8]] = {'rate': int(part1[23:]),
                          'related_valves': re.findall(r"([A-Z]{2})", part2)}
    return result


def traverse_valves(valve, all_valves, opened_valves, minutes_left):

    if (minutes_left <= 0):
        return 0
    # count the current valve by opened
    # current_round_sum = sum(
    #     map(lambda x: all_valves[x]['rate'] * minutes_left, opened_valves))
    related_valves = all_valves[valve]['related_valves']

    # decide to opened the valve - we decrease 2 minutes, 1 extra for opening the valve
    open_valve_sums = [0]
    current_round_sum = 0 # if we open the valve, sum up the valve pressure
    if all_valves[valve]['rate'] > 0 and valve not in opened_valves:
        current_round_sum = all_valves[valve]['rate'] * minutes_left
        open_valve_sums = [*map(lambda x: traverse_valves(x, all_valves,
                                                          opened_valves + [valve], minutes_left - 2), related_valves)]

    # decide not to opened the valve
    not_open_valve_sums = [*map(lambda x: traverse_valves(
        x, all_valves, opened_valves, minutes_left - 1), related_valves)]

    # return the better result
    return current_round_sum + max(*[0], *open_valve_sums, *not_open_valve_sums)


def part1():
    # build a map from the valves to the rate and related valves
    valves = reduce(lambda result, row: result | extract_values_from_row(row),
                    open("2022/input/day-16.input.txt"),
                    {})
    sum = traverse_valves('AA', valves, [], 30)
    return sum


print(part1())
