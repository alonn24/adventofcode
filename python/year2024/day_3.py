import numpy as np
import re


def part1(testcase: str):
    # Find all occurrences of mul(X,Y) in the input string
    res = np.array(re.findall(r"mul\((\d+),(\d+)\)", testcase), dtype=int)
    # Multiply the first column with the second
    res = np.prod(res, axis=1)
    # Sum the results
    return res.sum()


def part2(testcase: str):
    # Find all occurrences of mul(X,Y), do(), or don't()
    instructions = re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", testcase)
    should_mul = True
    res: list[tuple[int, int]] = []
    for instruction in instructions:
        if instruction[0] == "do()":
            should_mul = True
        elif instruction[0] == "don't()":
            should_mul = False
        elif should_mul:
            # Multiply the first column with the second
            res.append((int(instruction[1]), int(instruction[2])))
    return np.prod(res, axis=1).sum()
