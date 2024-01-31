"""
Advent of Code 2017
Day 12: Digital Plumber
https://adventofcode.com/2017/day/12
"""
import networkx as nx


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def both_parts(programs):
    graph = nx.Graph()

    for line in programs:
        program, neighbors = line.split(" <-> ")
        graph.add_edges_from((program, neighbor) for neighbor in neighbors.split(", "))

    print("Part 1:", len(nx.node_connected_component(graph, "0")))
    print("Part 2:", nx.number_connected_components(graph))


if __name__ == "__main__":
    programs_list = read_input_file()
    both_parts(programs_list)
