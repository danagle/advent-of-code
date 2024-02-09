"""
Advent of Code 2018
Day 25: Four-Dimensional Adventure
https://adventofcode.com/2018/day/25
"""
from networkx import Graph, number_connected_components


def read_input_file():
    return [tuple(map(int, line.split(","))) for line in open("input.txt", "r").read().splitlines()]


def manhattan_distance(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def part_one(points):
    c = Graph()
    for a in points:
        for b in points:
            if manhattan_distance(a, b) <= 3:
                c.add_edge(a, b)

    return number_connected_components(c)


if __name__ == "__main__":
    fixed_points = read_input_file()
    print(part_one(fixed_points))
