"""
Advent of Code 2018
Day 22: Mode Maze
https://adventofcode.com/2018/day/22
"""
from itertools import product
from networkx import Graph, dijkstra_path_length
from re import findall


def read_input_file():
    lines = open("input.txt", "r").read().splitlines()
    depth = int("".join(filter(str.isdigit, lines[0])))
    target = tuple(map(int, findall(r"\d+", lines[1])))
    return depth, target


def generate_cave(depth, target, bottom_right=None):
    if bottom_right is None:
        bottom_right = target
    cave = {}
    for y, x in product(range(0, bottom_right[1]+1), range(0, bottom_right[0]+1)):
        if (x, y) in ((0, 0), target):
            geologic_index = 0
        elif y == 0:
            geologic_index = x * 16807
        elif x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = cave[(x-1, y)][1] * cave[(x, y-1)][1]
        erosion_level = (geologic_index + depth) % 20183
        risk_level = erosion_level % 3
        cave[(x, y)] = (geologic_index, erosion_level, risk_level)

    return cave


def part_one(depth, target):
    cave_map = generate_cave(depth, target)
    return sum([t[2] for t in cave_map.values()])


def part_two(depth, target):
    torch, climbing_gear, neither = 0, 1, 2
    rocky, wet, narrow = 0, 1, 2
    available_tools = {rocky: (torch, climbing_gear), wet: (climbing_gear, neither), neither: (torch, neither)}
    expansion_size = 28  # Required expansion to find the shortest path
    expanded_bottom_right = (target[0] + expansion_size, target[1] + expansion_size)
    cave = generate_cave(depth, target, expanded_bottom_right)
    graph = Graph()

    for y, x in product(range(0, expanded_bottom_right[1]+1), range(0, expanded_bottom_right[0]+1)):
        tools = available_tools[cave[(x, y)][2]]
        graph.add_edge((x, y, tools[0]), (x, y, tools[1]), weight=7)
        for new_x, new_y in [tuple(sum(t) for t in zip((x, y), d)) for d in ((0, 1), (1, 0), (0, -1), (-1, 0))]:
            if 0 <= new_x <= expanded_bottom_right[0] and 0 <= new_y <= expanded_bottom_right[1]:
                new_tools = available_tools[cave[(new_x, new_y)][2]]
                for tool in set(tools).intersection(set(new_tools)):
                    graph.add_edge((x, y, tool), (new_x, new_y, tool), weight=1)

    return dijkstra_path_length(graph, (0, 0, torch), (target[0], target[1], torch))


if __name__ == "__main__":
    cave_depth, target_coordinates = read_input_file()
    print(f"part_one: {part_one(cave_depth, target_coordinates)}")
    print(f"part_two: {part_two(cave_depth, target_coordinates)}")
