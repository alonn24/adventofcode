input = [*map(int, open("2022/input/day-20.input.txt").read().splitlines())]


def update_indices(indices, i, current_num_i, next_num_i):
    indices[i] = next_num_i

    start, end = min(current_num_i, next_num_i), max(current_num_i, next_num_i)
    direction = 1 if current_num_i < next_num_i else -1
    for j, _ in enumerate(indices):
        if indices[j] >= start and indices[j] <= end and j != i:
            indices[j] -= direction


def mix(numbers):
    # Array of indices, we will talk though this array to access the numbers by their original order
    # We need to keep maintain the indices while moving the numbers in the result array
    indices = [i for i in range(len(numbers))]

    # The result array as we will not change the original one
    result = [v for v in numbers]
    for i, current_num_i in enumerate(indices):
        # Get the next index of the number
        n = result[current_num_i] % (len(result) - 1)

        next_num_i = current_num_i + n
        if next_num_i >= len(result):
            next_num_i = next_num_i - len(result) + 1
        elif next_num_i <= 0:
            next_num_i = next_num_i + len(result) - 1

        # rotate numbers - oddly the pop wont change the array so the insert will work
        result.insert(next_num_i, result.pop(current_num_i))
        update_indices(indices, i, current_num_i, next_num_i)
    return result


def part_1():
    mixed = mix(input)
    zero_i = mixed.index(0)
    return mixed[(zero_i+1000) % len(mixed)] + \
        mixed[(zero_i+2000) % len(mixed)] + \
        mixed[(zero_i+3000) % len(mixed)]


# 11073
print(f'part 1- {part_1()}')
