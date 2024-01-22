import re
from dataclasses import dataclass

input = open("2022/input/day-19.input.txt")


@dataclass
class Resources():
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def has(self, other):
        return self.ore >= other.ore and self.clay >= other.clay and self.obsidian >= other.obsidian and self.geode >= other.geode

    def subtract(self, other):
        return Resources(ore=self.ore - other.ore, clay=self.clay - other.clay, obsidian=self.obsidian - other.obsidian, geode=self.geode - other.geode)

    def add(self, other):
        return Resources(ore=self.ore + other.ore, clay=self.clay + other.clay, obsidian=self.obsidian + other.obsidian, geode=self.geode + other.geode)


@dataclass
class Blueprint():
    id: int
    ore_cost: Resources
    clay_cost: Resources
    obsidian_cost: Resources
    geo_cost: Resources


def extract_values_from_row(row):
    [(id, a, b, c, d, e, f)] = re.findall(
        'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.', row)
    ore_cost = Resources(ore=int(a))
    clay_cost = Resources(ore=int(b))
    obsidian_cost = Resources(ore=int(c), clay=int(d))
    geo_cost = Resources(ore=int(e), obsidian=int(f))
    return Blueprint(id, ore_cost, clay_cost, obsidian_cost, geo_cost)


input = [*map(extract_values_from_row, open("2022/input/day-19.input.txt"))]


def build_robots(available_resources: Resources, robots: Resources, blueprint: Blueprint):
    if available_resources.has(blueprint.geo_cost):
        return (available_resources.subtract(blueprint.geo_cost), robots.add(Resources(geode=1)))
    if available_resources.has(blueprint.obsidian_cost):
        return (available_resources.subtract(blueprint.obsidian_cost), robots.add(Resources(obsidian=1)))
    if available_resources.has(blueprint.clay_cost):
        return (available_resources.subtract(blueprint.clay_cost), robots.add(Resources(clay=1)))
    if available_resources.has(blueprint.ore_cost):
        return (available_resources.subtract(blueprint.ore_cost), robots.add(Resources(ore=1)))
    return (available_resources, robots)


def collect_resources(available_resources: Resources, robots: Resources):
    return Resources(ore=available_resources.ore + robots.ore,
                     clay=available_resources.clay + robots.clay,
                     obsidian=available_resources.obsidian + robots.obsidian,
                     geode=available_resources.geode + robots.geode)


def get_quality_level(blueprint):
    print(blueprint)
    available_resources = Resources()
    robots = Resources(ore=1)
    # 24 minutes
    for _ in range(24):
        (available_resources, new_robots) = build_robots(
            available_resources, robots, blueprint)
        available_resources = collect_resources(available_resources, robots)
        # We later merge the new added robots so they wont collect resource this round
        robots = new_robots
        print(available_resources)
        print('robots', robots, end='\n\n')
    return available_resources.geode


def part_1():
    return [get_quality_level(blueprint) for blueprint in [input[0]]]


print(f'part 1 - {sum(part_1())}')
