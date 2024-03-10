import re
import numpy as np


def beat_record_ways(time, distance):
    result = np.arange(0, time + 1)
    result = result * (time-result)
    return len(result[result > distance])


def part1(input):
    times = [*map(int, re.findall(r'\d+', input[0]))]
    distances = [*map(int, re.findall(r'\d+', input[1]))]

    result = 1
    for i in range(len(times)):
        result *= beat_record_ways(times[i], distances[i])
    return result


def part2(input):
    time = int(''.join(re.findall(r'\d+', input[0])))
    distance = int(''.join(re.findall(r'\d+', input[1])))
    return beat_record_ways(time, distance)
