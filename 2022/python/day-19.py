import concurrent.futures
import re
from dataclasses import dataclass
from collections import namedtuple
from functools import cache
input = open("2022/input/day-19.input.txt")


@dataclass
class Resources():
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __hash__(self):
        return hash((self.ore, self.clay, self.obsidian, self.geode))

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
    return Blueprint(int(id), ore_cost, clay_cost, obsidian_cost, geo_cost)


input = [*map(extract_values_from_row, open("2022/input/day-19.input.txt"))]


def build_robots(available_resources: Resources, robots: Resources, blueprint: Blueprint):
    # with the default one of not building a thing
    states = [(available_resources, robots)]
    max_ore_cost = max(blueprint.ore_cost.ore, blueprint.clay_cost.ore,
                       blueprint.obsidian_cost.ore, blueprint.geo_cost.ore)
    max_clay_cost = max(blueprint.ore_cost.clay, blueprint.clay_cost.clay,
                        blueprint.obsidian_cost.clay, blueprint.geo_cost.clay)
    max_obsidian_cost = max(blueprint.ore_cost.obsidian, blueprint.clay_cost.obsidian,
                            blueprint.obsidian_cost.obsidian, blueprint.geo_cost.obsidian)

    # Add all possible robots build
    # geode - always build
    if available_resources.has(blueprint.geo_cost):
        states.append((available_resources.subtract(
            blueprint.geo_cost), robots.add(Resources(geode=1))))
    # obsidian
    if available_resources.has(blueprint.obsidian_cost) and robots.obsidian < max_obsidian_cost:
        states.append((available_resources.subtract(
            blueprint.obsidian_cost), robots.add(Resources(obsidian=1))))
    # clay
    if available_resources.has(blueprint.clay_cost) and robots.clay < max_clay_cost:
        states.append((available_resources.subtract(
            blueprint.clay_cost), robots.add(Resources(clay=1))))
    # ore
    if available_resources.has(blueprint.ore_cost) and robots.ore < max_ore_cost:
        states.append((available_resources.subtract(
            blueprint.ore_cost), robots.add(Resources(ore=1))))
    return states


def collect_resources(available_resources: Resources, robots: Resources):
    return Resources(ore=available_resources.ore + robots.ore,
                     clay=available_resources.clay + robots.clay,
                     obsidian=available_resources.obsidian + robots.obsidian,
                     geode=available_resources.geode + robots.geode)


state = namedtuple('state', ['available_resources', 'robots', 'minutes'])


def get_quality_level(blueprint):
    print(blueprint)

    @cache
    def calculate_for_state(available_resources, robots, minutes):
        if minutes == 0:
            return available_resources.geode
        next_states = build_robots(available_resources, robots, blueprint)
        return max([calculate_for_state(collect_resources(a, robots), b, minutes-1) for (a, b) in next_states])

    available_resources = Resources()
    robots = Resources(ore=1)
    max_geode = calculate_for_state(available_resources, robots, 24)
    print(f'blueprint {blueprint.id} - {max_geode}')
    return max_geode * blueprint.id


def part_1():
    with concurrent.futures.ProcessPoolExecutor(max_workers=30) as executor:
        all = [result for _, result in zip(
            input, executor.map(get_quality_level, input))]
        print('part 1 - ', sum(all))

    return 0


if __name__ == '__main__':
    part_1()	# 1356
