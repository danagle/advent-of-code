"""
Advent of Code 2015
Day 17: No Such Thing as Too Much
https://adventofcode.com/2015/day/17
"""
from collections import defaultdict
from itertools import combinations


def read_input_file():
    return list(map(int, open("input.txt", "r").read().splitlines()))


def part_one(containers):
    total = 0
    for num_containers in range(1, len(containers)):
        for arrangement in combinations(containers, num_containers):
            if 150 == sum(arrangement):
                total += 1
    return total


def part_two(containers):
    containers_used = defaultdict(int)
    for num_containers in range(1, len(containers)):
        for arrangement in combinations(containers, num_containers):
            if 150 == sum(arrangement):
                containers_used[num_containers] += 1
    return containers_used[min(containers_used.keys())]


if __name__ == "__main__":
    container_capacities = read_input_file()
    print(part_one(container_capacities))
    print(part_two(container_capacities))
