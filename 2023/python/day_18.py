import re
import numpy as np
from typing import Any
import matplotlib.pyplot as plt

Instructions = tuple[str, str]
Pos = tuple[int, int]


def polygon_area(points: np.ndarray[int, Any]):
    # Add the first point to the end to close the polygon
    points = points + [points[0]]

    # Calculate the area using the Shoelace formula
    area = 0
    for i in range(len(points) - 1):
        area += points[i][0] * points[i+1][1] - points[i+1][0] * points[i][1]
    area /= 2

    return abs(area)


def move(start: Pos, inst: Instructions) -> Pos:
    direction, steps = inst
    steps = int(steps)
    if direction == 'U':
        return (start[0], start[1] + steps)
    elif direction == 'D':
        return (start[0], start[1] - steps)
    elif direction == 'L':
        return (start[0] - steps, start[1])
    elif direction == 'R':
        return (start[0] + steps, start[1])
    raise ValueError(f'Invalid direction: {direction}')


re_expression = r'^(U|D|L|R) (\d*) \((.*)\)$'


def calculate_area(instructions: list[Instructions]):
    perimeter = 0
    path: list[Pos] = [(0, 0)]
    for inst in instructions:
        perimeter += int(inst[1])
        path.append(move(path[-1], inst))
    # Get boundary points
    points = np.array(path)
    return polygon_area(points) + perimeter // 2+1


def part1(case: str):
    """
    Day 18: Lavaduct Lagoon
    Part 1 - digging a lagoon
    """
    instructions: list[Instructions] = [re.findall(re_expression, row)[0][:2] for row in case.splitlines()]
    return calculate_area(instructions)


def parse_hex(hex_value: str) -> Instructions:
    a = hex_value[1:6]
    b = hex_value[-1]
    direction = 'R' if b == '0' else 'D' if b == '1' else 'L' if b == '2' else 'U'
    return direction, f"{int(a, 16)}"


def part2(case: str):
    """
    Part 2 - digging a lagoon after converting hex to instructions
    """
    hex_values = [re.findall(re_expression, row)[0][-1] for row in case.splitlines()]
    instructions = [parse_hex(hex_value) for hex_value in hex_values]
    return calculate_area(instructions)


def main():
    case = open('2023/input/day-18.input.txt').read()
    instructions: list[Instructions] = [re.findall(re_expression, row)[0] for row in case.splitlines()]
    path: list[Pos] = [(0, 0)]
    for inst in instructions:
        path.append(move(path[-1], inst))
    points = np.array(path)

    # Extract x and y coordinates of the polygon
    x, y = points.T

    # Plot the polygon
    plt.plot(x, y, 'b-')  # Connect points with lines
    plt.fill(x, y, alpha=0.5)  # Fill the polygon

    # Plot vertices
    plt.plot(x, y, 'ro')

    # Set axis equal to maintain aspect ratio
    plt.axis('equal')

    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
