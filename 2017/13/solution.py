"""
Advent of Code 2017
Day 13: Packet Scanners
https://adventofcode.com/2017/day/13
"""
from itertools import count
from re import findall


def read_input_file():
    layers = [tuple(map(int, findall(r"-?[0-9]+", line))) for line in open("input.txt", "r").read().splitlines()]
    return {depth: range_ for depth, range_ in layers}


def scanner(height, time):
    offset = time % ((height - 1) * 2)
    return 2 * (height - 1) - offset if offset > height - 1 else offset


def both_parts(layers):
    part_one = sum(position * layers[position] for position in layers
                   if scanner(layers[position], position) == 0)
    part_two = next(delay for delay in count()
                    if not any(scanner(layers[position], delay + position) == 0
                               for position in layers))

    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    firewall_layers = read_input_file()
    both_parts(firewall_layers)
