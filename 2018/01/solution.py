"""
Advent of Code 2018
Day 1: Chronal Calibration
https://adventofcode.com/2018/day/1
"""
from itertools import cycle


def read_input_file():
    return [int(line) for line in open("input.txt", "r").read().splitlines()]


def part_one(data):
    return sum(data)


def part_two(data):
    frequency = 0
    frequency_cycle = cycle(data)
    frequency_set = set()
    while True:
        if frequency in frequency_set:
            break
        frequency_set.add(frequency)
        frequency += next(frequency_cycle)
    return frequency


if __name__ == "__main__":
    frequencies = read_input_file()
    print(part_one(frequencies))
    print(part_two(frequencies))
