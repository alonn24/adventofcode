import functools
import itertools
import collections as c
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
valves_names = all_valves.keys()

# build a connection map with every node to every node with the number of hops to get there
connections = c.defaultdict(lambda: 1000)
# initialize the first hops
for k, item in all_valves.items():
    for rv in item['related_valves']:
        connections[k, rv] = 1

# use floyd-warshall algorithm to build the distances
for k, i, j in itertools.product(valves_names, valves_names, valves_names):
    connections[i, j] = min(
        connections[i, j], connections[i, k] + connections[k, j])


def part1():
    @functools.cache
    def search(time_left, current_valve, available_valves):
        next_valves = [
            v for v in available_valves if connections[current_valve, v] < time_left]
        # init to 0 if there are no next steps
        values = [0]
        for v in next_valves:
            # the time after move and open v
            time_after_open_v = time_left - connections[current_valve, v] - 1
            sum = all_valves[v]['rate']*time_after_open_v + \
                search(time_after_open_v, v, available_valves - {v})
            values.append(sum)
        return max(values)

    # filter out 0 valves so we wont check them
    available_valves = [v for v in all_valves if all_valves[v]['rate'] > 0]
    result = search(30, 'AA', frozenset(available_valves))
    return result


print(part1())  # 1701
