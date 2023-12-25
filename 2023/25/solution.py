from math import prod
from networkx import Graph, connected_components, minimum_edge_cut


def read_input_file():
    components_graph = Graph()
    for line in open("input.txt").read().splitlines():
        source, destinations = line.split(": ")
        for destination in destinations.split():
            components_graph.add_edge(source, destination.strip())
    return components_graph


def part_one(graph):
    to_remove = minimum_edge_cut(graph)
    graph.remove_edges_from(to_remove)
    return prod(len(components) for components in connected_components(graph))


if __name__ == '__main__':
    from time import time

    g = read_input_file()
    st = time()
    p1 = part_one(g)
    print(f"Execution Time: {time()-st} seconds.")
    print(p1)