from functools import reduce
import re

input = open("2023/input/day-1.input.txt", "r").read().strip().split("\n")


def get_sum_of_digits():
    digits = map(lambda x: re.findall('[0-9]', x), input)
    numbers = map(lambda x: int(f'{x[0]}{x[-1]}'), digits)
    return reduce(lambda a, b: a + b, numbers)


print(f'part 1 - {get_sum_of_digits()}')  # 53334

words = ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine']
words_regex = f'([0-9]|{"|".join(words)})'


def convert_to_digit(word):
    if word.isdigit():
        return int(word)
    return words.index(word)


def get_sum_of_all_digits():
    digits = map(lambda x: re.findall(words_regex, x), input)
    numbers = map(lambda x: convert_to_digit(
        x[0])*10+convert_to_digit(x[-1]), digits)
    return reduce(lambda a, b: a + b, numbers)


print(f'part 2 - {get_sum_of_all_digits()}')  # 52834
