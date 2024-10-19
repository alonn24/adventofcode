from collections import defaultdict


def build_graph(input_str: str):
    graph: defaultdict[str, set[str]] = defaultdict(set)
    for line in input_str.strip().split('\n'):
        component, connections = line.split(': ')
        connections = connections.split()
        for conn in connections:
            graph[component].add(conn)
            graph[conn].add(component)
    return graph


def count_cross_edges(G: defaultdict[str, set[str]], S: set[str]):
    cross = map(lambda x: len(G[x] - S), S)
    return sum(cross)


def part1(case: str):
    """
    Day 25: Snowverload
    Part 1: Find the three wires you need to disconnect in order to divide the components into two separate groups.
        What do you get if you multiply the sizes of these two groups together
    """
    G = build_graph(case)
    S = set(G)
    while count_cross_edges(G, S) != 3:
        S.remove(max(S, key=lambda x: len(G[x] - S)))
    return len(S) * len(set(G)-S)
