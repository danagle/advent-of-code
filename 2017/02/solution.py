"""
Advent of Code 2017
Day 2: Corruption Checksum
https://adventofcode.com/2017/day/2
"""
from re import findall


def read_input_file():
    lines = open("input.txt", "r").read().splitlines()
    return [list(map(int, findall("(\d+)", line))) for line in lines]


def part_one(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)


def part_two(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        sorted_values = sorted(row, reverse=True)
        for i, value in enumerate(sorted_values):
            for j in range(i + 1, len(sorted_values)):
                if 0 == value % sorted_values[j]:
                    checksum += value // sorted_values[j]
    return checksum


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
