import re
from typing import Literal
from math import lcm

FLIP_FLOP = r'%'
CONJUNCTION = r'&'
BROADCASTER = 'broadcaster'

HIGH = 'high'
LOW = 'low'

# Type of FLIP_FLOP
Type = Literal['%'] | Literal['&']
Signal = Literal['low'] | Literal['high']
Modules = dict[str, tuple[Type, list[str]]]
Conjunctions = dict[str, list[str]]


def get_connected_to(module: str, modules: Modules) -> list[str]:
    return [k for k, v in modules.items() if module in v[1]]


def get_type(type: str) -> Type:
    if type == FLIP_FLOP:
        return FLIP_FLOP
    elif type == CONJUNCTION:
        return CONJUNCTION
    else:
        raise ValueError(f'Invalid type: {type}')


def parse_case(case: str) -> tuple[str, Modules]:
    [broadcaster, *modules] = case.split('\n')
    initial = re.findall(r'broadcaster -> (\w+.*)', broadcaster)[0].split(', ')

    # Get all modules and their connections
    modules_grouped: list[list[str]] = [list(re.findall(r'([%|&])(\w*) -> (.*)', x)[0]) for x in modules]
    modules_dict: Modules = {x[1]: (get_type(x[0]), x[2].split(', ')) for x in modules_grouped}

    return initial, modules_dict


def flip(signal: Signal) -> Signal:
    return HIGH if signal == LOW else LOW


Item = tuple[str, str, Signal]
State = dict[str, Signal]
ConjunctionState = dict[str, list[Signal]]
ModulesConnectedTo = dict[str, list[str]]


def run_module(modules: Modules,
               item: Item,
               state: State,
               conjunction_state: ConjunctionState,
               modules_connected_to: ModulesConnectedTo) -> list[Item]:
    from_module, current, sig = item
    if current not in modules:
        return []

    type, nodes = modules[current]

    # Flip-flop
    if type == FLIP_FLOP and sig == 'low':
        # Flip the signal
        state[current] = flip(state[current])
        # Propagate the signal
        return [(current, x, state[current]) for x in nodes]

    # Conjunction
    elif type == CONJUNCTION:
        # Update memory
        connects_to_current = modules_connected_to[current]
        idx = connects_to_current.index(from_module)
        conjunction_state[current][idx] = sig

        # If all signals are high, propagate the signal
        all_high = all(x == HIGH for x in conjunction_state[current])
        current_sig = LOW if all_high else HIGH
        state[current] = current_sig
        return [(current, x, current_sig) for x in nodes]
    return []


def part1(case: str):
    """
    Day 20: Pulse Propagation
    Push the button 1000 times, count the number of pulse in each round multiplied together.
    """
    initial, modules = parse_case(case)
    modules_connected_to: ModulesConnectedTo = {k: get_connected_to(k, modules) for k in modules}

    # Conjunctions has internal memory of the signals
    # This is important because we handle signals by order
    conjunction_state: ConjunctionState = {k: [LOW for _ in v]
                                           for k, v in modules_connected_to.items()
                                           if modules[k][0] == CONJUNCTION}
    # Modules state
    state: State = {k: LOW for k in modules}

    # Starts with 1 for the broadcaster push
    high_count = 0
    low_count = 0

    for _ in range(1000):
        # Q with items (from, to, signal)
        q: list[Item] = [(BROADCASTER, x, LOW) for x in initial]
        aggregator: list[Item] = []

        # Click the button
        low_count += 1

        while q:
            item = q.pop(0)
            _, _, sig = item

            # Handle a signal here so increasing teh count
            low_count += 1 if sig == LOW else 0
            high_count += 1 if sig == HIGH else 0

            aggregator.extend(run_module(modules, item,
                                         state, conjunction_state, modules_connected_to))

            # Aggregate
            if not q:
                q = aggregator
                aggregator = []
    return high_count * low_count


def part2(case: str):
    """
    Find out how many button presses are needed for rx to turn
    """
    initial, modules = parse_case(case)
    modules_connected_to = {k: get_connected_to(k, modules) for k in modules}

    # Conjunctions has internal memory of the signals
    # This is important because we handle signals by order
    conjunction_state: dict[str, list[Signal]] = {k: [LOW for _ in v]
                                                  for k, v in modules_connected_to.items()
                                                  if modules[k][0] == CONJUNCTION}
    # Modules state
    state: dict[str, Signal] = {k: LOW for k in modules}

    con_write_to_rx = get_connected_to('rx', modules)[0]
    # Search for all writes_to_con to read HIGHto it will send LOW to rx
    writes_to_con = get_connected_to(con_write_to_rx, modules)
    cycles = [0 for _ in writes_to_con]

    count = 0
    while True:
        count += 1
        # Q with items (from, to, signal)
        q: list[tuple[str, str, Signal]] = [(BROADCASTER, x, LOW) for x in initial]
        aggregator: list[tuple[str, str, Signal]] = []

        while q:
            # Find cycles
            for i, con in enumerate(writes_to_con):
                if state[con] == HIGH:
                    cycles[i] = count
            if all(x != 0 for x in cycles):
                return lcm(*cycles)

            item = q.pop(0)
            aggregator.extend(run_module(modules, item,
                                         state, conjunction_state, modules_connected_to))

            # Aggregate
            if not q:
                q = aggregator
                aggregator = []
