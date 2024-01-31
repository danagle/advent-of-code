"""
Advent of Code 2017
Day 11: Hex Ed
https://adventofcode.com/2017/day/11
"""
from functools import reduce
from itertools import accumulate


def read_input_file():
    return open("input.txt", "r").read().strip().split(",")


def tuple_add(a, b):
    return tuple(sum(t) for t in zip(a, b))


def hex_distance(u, v):
    return max(abs(u), abs(v)) if u * v > 0 else abs(u) + abs(v)


def both_parts(path_taken):
    directions = {
        "n": (0, 1), "ne": (1, 1), "se": (1, 0),
        "s": (0, -1), "sw": (-1, -1), "nw": (-1, 0)
    }

    path_tuples = [directions[d] for d in path_taken]

    part_one = hex_distance(*reduce(tuple_add, path_tuples))

    part_two = max(hex_distance(*v) for v in accumulate(path_tuples, tuple_add))

    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    child_path = read_input_file()
    both_parts(child_path)
