"""
Advent of Code 2015
Day 3: Perfectly Spherical Houses in a Vacuum
https://adventofcode.com/2015/day/3
"""
from collections import defaultdict


def read_input_file():
    return open("input.txt", "r").read().strip()


def change_location(location, direction):
    new_location = location
    match direction:
        case ">":
            new_location += 1
        case "<":
            new_location -= 1
        case "^":
            new_location += 0 + 1j
        case "v":
            new_location += 0 - 1j
    return new_location


def part_one(data):
    houses = defaultdict(int)
    location = 0 + 0j
    houses[location] = 1
    for direction in data:
        location = change_location(location, direction)
        if location in houses:
            houses[location] += 1
        else:
            houses[location] = 1
    return len(houses)


def part_two(data):
    routes = [[0 + 0j], [0 + 0j]]
    for position, direction in enumerate(data):
        index = position % 2
        location = change_location(routes[index][-1], direction)
        routes[index].append(location)
    return len(set(routes[0]).union(set(routes[1])))


if __name__ == "__main__":
    text = read_input_file()
    print(part_one(text))
    print(part_two(text))
