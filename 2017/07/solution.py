"""
Advent of Code 2017
Day 7: Recursive Circus
https://adventofcode.com/2017/day/7
"""
from collections import Counter
import networkx as nx


def read_input_file():
    graph = nx.DiGraph()
        # Build the graph of programs
    for line in open("input.txt", "r").read().splitlines():
        name = line.split()[0]
        graph.add_node(name, weight=int(line.split()[1].strip('()')))
        if '->' in line:
            children = [n.strip() for n in line.split('->')[1].split(',')]
            for child in children:
                graph.add_edge(name, child)
    return graph


def both_parts(graph):
    # Topological sort to find the root of the tree
    ordered = list(nx.topological_sort(graph))
    part_one = ordered[0]

    # Keep track of each node's total weight (itself + its children)
    weights = {}

    # Going backwards (starting from the leaves)
    for node in reversed(ordered):
        # Start with the weight of the node
        total = graph.nodes[node]['weight']

        counts = Counter(weights[child] for child in graph[node])
        unbalanced = None

        for child in graph[node]:
            # If this child's weight is different than others, we've found it
            if len(counts) > 1 and counts[weights[child]] == 1:
                unbalanced = child
                break

            # Otherwise add to the total weight
            value = weights[child]
            total += weights[child]

        if unbalanced:
            # Find the weight adjustment and the new weight of this node
            diff = weights[unbalanced] - value
            part_two = graph.nodes[unbalanced]['weight'] - diff
            break

        # Store the total weight of the node
        weights[node] = total

    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    program_graph = read_input_file()
    both_parts(program_graph)
