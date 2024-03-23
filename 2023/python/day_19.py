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
Workflows = dict[str, tuple[np.ndarray[int, Any], str]]


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
    print('')
    """
    Day 19: Aplenty
    part 1 - Run all ratings in front of the workflows and return the sum of ratings that pass
    """
    workflows, ratings = parse_case(case)
    accepted_ratings = [r for r in ratings if check_rating(r, workflows)]
    return np.sum(accepted_ratings)
