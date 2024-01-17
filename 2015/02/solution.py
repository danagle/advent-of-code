"""
Advent of Code 2015
Day 2: I Was Told There Would Be No Math
https://adventofcode.com/2015/day/2
"""


def read_input_file():
    return [tuple(map(int, line.split("x"))) for line in open("input.txt", "r").read().splitlines()]


def part_one(data):
    total = 0
    for dimensions in data:
        l, w, h = dimensions
        x, y, _ = sorted(dimensions)
        total += (2 * (l*w + w*h + h*l)) + (x*y)
    return total


def part_two(data):
    total = 0
    for dimensions in data:
        x, y, z = sorted(dimensions)
        total += (2 * (x + y)) + (x * y * z)
    return total


if __name__ == "__main__":
    text = read_input_file()
    print(part_one(text))
    print(part_two(text))
