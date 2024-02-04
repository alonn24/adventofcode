input = open('2022/input/day-23.input.txt').read().splitlines()

noop = lambda *args, **kwargs: None

ELVES = '#'
EMPTY = '.'

N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)
NE = (N[0], E[1])
NW = (N[0], W[1])
SE = (S[0], E[1])
SW = (S[0], W[1])
directions = [N, S, W, E, NE, NW, SE, SW]
propositions = [
    (N, [N, NE, NW]),
    (S, [S, SE, SW]),
    (W, [W, NW, SW]),
    (E, [E, NE, SE]),
]


def get_free_space(elves, pos, directions):
    (x, y) = pos
    return [(x+dx, y+dy) for dx, dy in directions if (x+dx, y+dy) not in elves or elves[(x+dx, y+dy)] == False]


def propose_move(elves, propose_i, position):
    for i in range(4):
        prop = propositions[(propose_i + i) % 4]
        if len(get_free_space(elves, position, prop[1])) == len(prop[1]):
            return (position[0]+prop[0][0], position[1]+prop[0][1])
    return position


def get_result(elves, print_result=False):
    _print = print if print_result else noop
    min_x = min(elves, key=lambda x: x[0])[0]
    max_x = max(elves, key=lambda x: x[0])[0]
    min_y = min(elves, key=lambda x: x[1])[1]
    max_y = max(elves, key=lambda x: x[1])[1]
    free_count = 0
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) not in elves:
                free_count += 1
            _print(ELVES if (x, y) in elves else EMPTY, end='')
        _print('')
    return free_count


def part_1():
    elves = {(x, y): True for x, row in enumerate(
        input) for y, cell in enumerate(row) if cell == ELVES}
    proposition_i = 0
    for _ in range(10):
        elves_places = [(e, get_free_space(elves, e, directions))
                        for e in elves]
        elves_to_move = [e for e, free in elves_places if len(free) < 8]
        moves = [propose_move(elves, proposition_i, e) for e in elves_to_move]
        moves_map = {m: moves.count(m) for m in moves}
        for i, e in enumerate(elves_to_move):
            if moves_map[moves[i]] == 1:
                del elves[e]
                elves[moves[i]] = True
        proposition_i += 1
    return get_result(elves, print_result=True)

# 3684
print(f'Part 1 - {part_1()}')
