import re
import numpy as np
from typing import Any

ACCEPT = 'A'
REJECT = 'R'
START_NODE = 'in'
rating_indices = ['x', 'm', 'a', 's']


def parse_case(case: str):
    part1, part2 = case.split('\n\n')

    def parse_workflow(workflow: str):
        # Extract the name , rules as string and the result if the rules are not met
        name, rules, result = re.findall(r'(\w+){(.*),(\w+)}', workflow)[0]
        # Each rule is a tuple of (name, operator, value, result)
        parsed_rules = np.array(re.findall(r'(\w+)([<>])(\d+):(\w+)', rules)).reshape(-1, 4)
        return name, parsed_rules, result

    workflows = [parse_workflow(w) for w in part1.splitlines()]
    workflows_map: Workflows = {w[0]: (w[1], w[2]) for w in workflows}

    ratings = np.array(re.findall(r'\d+', part2), dtype=np.int64).reshape(-1, 4)
    return workflows_map, ratings


# ['a', '<', '3', 'b']
Rule = tuple[str, str, str, str]
# {'in': ([['a', '<', '3', 'b']...], 'out')}
Workflows = dict[str, tuple[np.ndarray[str, Any], str]]


def check_rule(rating: np.ndarray[int, Any], rule: Rule) -> bool:
    idx = rating_indices.index(rule[0])
    val = rating[idx]
    compare_val = int(rule[2])
    return val < compare_val if rule[1] == '<' else val > compare_val


def check_rating(rating: np.ndarray[int, Any], workflows: Workflows, node: str = START_NODE) -> bool:
    if node == ACCEPT:
        return True
    elif node == REJECT:
        return False
    workflow = workflows[node]
    maybe_next_node = next((x for x in workflow[0] if check_rule(rating, x)), None)
    next_node = maybe_next_node[3] if maybe_next_node is not None else workflow[1]
    return check_rating(rating, workflows, next_node)


def part1(case: str):
    """
    Day 19: Aplenty
    part 1 - Run all ratings in front of the workflows and return the sum of ratings that pass
    """
    workflows, ratings = parse_case(case)
    accepted_ratings = [r for r in ratings if check_rating(r, workflows)]
    return np.sum(accepted_ratings)


MIN = 1
MAX = 4000

not_convert = {
    '>': '<=',
    '<': '>=',
}


def negate_rules(rule: list[Rule]) -> list[Rule]:
    return [(r[0], not_convert[r[1]], r[2], r[3]) for r in rule]


def get_combinations(path: list[Rule]) -> int:
    # Inclusive ranges
    ranges: list[tuple[str, int, int]] = [(x, MIN, MAX) for x in rating_indices]
    for node in path:
        idx = rating_indices.index(node[0])
        equal_addition = 0 if node[1] == '<=' or node[1] == '>=' else 1
        if node[1] == '<' or node[1] == '<=':
            # Less than - reduce the max value
            new_top = min(int(node[2]) - equal_addition, ranges[idx][2])
            ranges[idx] = (ranges[idx][0], ranges[idx][1], new_top)
        else:
            # greater than - increase the min value
            new_bottom = max(int(node[2]) + equal_addition, ranges[idx][1])
            ranges[idx] = (ranges[idx][0], new_bottom, ranges[idx][2])
    # Get the range length - inclusive
    result = [r[2] - r[1] + 1 for r in ranges]
    # Return the product of all ranges which is the number of combinations
    return result[0]*result[1]*result[2]*result[3]


def part2(case: str):
    """
    Part 2 - Calculate the number of combinations that will pass the workflows
    """
    workflows, _ = parse_case(case)
    win_paths: list[list[Any]] = []
    q: list[tuple[list[Any], str]] = [([], START_NODE)]
    while q:
        path, node = q.pop()
        # End a path
        if node == ACCEPT:
            win_paths.append(path)
            continue
        # Reject a path
        if node == REJECT:
            continue

        # Continue a path
        workflow = workflows[node]
        rules = workflow[0]
        for i, rule in enumerate(rules):
            # Negate previous rules
            previous_rules = rules[0:i]
            negated_previous_rules = [x[0:3] for x in negate_rules(list(previous_rules))]
            # Append the rule and continue with the accept node
            q.append((path + negated_previous_rules + [tuple(rule[0:3])], rule[3]))
        # Continue with the else node
        q.append((path + [x[0:3] for x in negate_rules(list(rules))], workflow[1]))
    return sum([get_combinations(path) for path in win_paths])
