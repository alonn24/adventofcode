import re


def break_input(row):
    game = int(re.findall('Game (\d+):', row)[0])
    blue = [int(x) for x in re.findall('(\d+) blue', row)]
    red = [int(x) for x in re.findall('(\d+) red', row)]
    green = [int(x) for x in re.findall('(\d+) green', row)]
    return {'game': game, 'blue': blue, 'red': red, 'green': green}


games = [break_input(row) for row in open("2023/input/day-2.input.txt", "r")]


def is_game_possible(game, limits):
    return max(game['blue'] + [0]) <= limits['blue'] and \
        max(game['red'] + [0]) <= limits['red'] and \
        max(game['green'] + [0]) <= limits['green']


def part_1(limits):
    return [game['game']
            for game in games if is_game_possible(game, limits)]


possible_games = part_1(limits={'blue': 14, 'red': 12, 'green': 13})
print(f'part 1 - {sum(possible_games)}')  # 2348


def part_2():
    return [max(game['blue']) * max(game['red']) * max(game['green']) for game in games]


# 76008
print(f'part 2 - {sum(part_2())}')
