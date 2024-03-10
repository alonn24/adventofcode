import re
from typing import NamedTuple


class Game(NamedTuple):
    id: int
    blue: list[int]
    red: list[int]
    green: list[int]


def break_input(row: str):
    id = int(re.findall(r'Game (\d+):', row)[0])
    blue = [int(x) for x in re.findall(r'(\d+) blue', row)]
    red = [int(x) for x in re.findall(r'(\d+) red', row)]
    green = [int(x) for x in re.findall(r'(\d+) green', row)]
    return Game(id, blue, red, green)


def is_game_possible(game: Game, limit_blue: int, limit_red: int, limit_green: int):
    return max(game.blue + [0]) <= limit_blue and \
        max(game.red + [0]) <= limit_red and \
        max(game.green + [0]) <= limit_green


def part1(case: str) -> int:
    LIMIT_BLUE = 14
    LIMIT_RED = 12
    LIMIT_GREEN = 13
    games = [break_input(row) for row in case.splitlines()]
    possible_games = [game.id for game in games if is_game_possible(game, LIMIT_BLUE, LIMIT_RED, LIMIT_GREEN)]
    return sum(possible_games)


def part2(case: str) -> int:
    games = [break_input(row) for row in case.splitlines()]
    return sum([max(game.blue) * max(game.red) * max(game.green) for game in games])
