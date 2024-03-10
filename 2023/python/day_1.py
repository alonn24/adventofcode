from functools import reduce
import re


def get_sum_of_digits(case: list[str]):
    digits = map(lambda x: re.findall(r'\d', x), case)
    numbers = map(lambda x: int(f'{x[0]}{x[-1]}'), digits)
    return reduce(lambda a, b: a + b, numbers)


def part1(case: str):
    return get_sum_of_digits(case.strip().splitlines())


words = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
# adding lookahead to support words like twone (2,1) and eightwo (8,2)
words_regex = fr'(?=(\d|{"|".join(words)}))'


def convert_to_digit(word: str):
    if word.isdigit():
        return int(word)
    return words.index(word)


def get_sum_of_all_digits(case: list[str]):
    digits = map(lambda x: re.findall(words_regex, x), case)
    numbers = map(lambda x: convert_to_digit(
        x[0])*10+convert_to_digit(x[-1]), digits)
    return reduce(lambda a, b: a + b, numbers)


def part2(case: str):
    return get_sum_of_all_digits(case.strip().splitlines())
