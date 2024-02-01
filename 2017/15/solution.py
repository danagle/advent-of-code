"""
Advent of Code 2017
Day 15: Dueling Generators
https://adventofcode.com/2017/day/15
"""
from re import findall
from itertools import islice


def read_input_file():
    return tuple(map(int, findall(r"-?\d+", open("input.txt", "r").read())))


def gen(val, mult, check=1):
    while True:
        val = (val * mult) % 2147483647
        if val % check == 0:
            yield val


def part_one(values):
    initial_a, initial_b = values
    generator_a, generator_b = gen(initial_a, 16807), gen(initial_b, 48271)
    judges_count = 0
    for a, b in islice(zip(generator_a, generator_b), 40_000_000):
        if a % 65536 == b % 65536:
            judges_count += 1
    return judges_count


def part_two(values):
    initial_a, initial_b = values
    generator_a, generator_b = gen(initial_a, 16807, 4), gen(initial_b, 48271, 8)
    judges_count = 0
    for a, b in islice(zip(generator_a, generator_b), 5_000_000):
        if a % 65536 == b % 65536:
            judges_count += 1
    return judges_count


if __name__ == "__main__":
    initial_values = read_input_file()
    print(part_one(initial_values))
    print(part_two(initial_values))
