"""
Advent of Code 2017
Day 8: I Heard You Like Registers
https://adventofcode.com/2017/day/8
"""
import operator as op
from collections import defaultdict


def read_input_file():
    return [tuple(line.split()) for line in open("input.txt", "r").read().splitlines()]


def both_parts(instructions):
    comparisons = {">": op.gt, "<": op.lt, ">=": op.ge, "<=": op.le, "!=": op.ne, "==": op.eq}
    operations = {"inc": 1, "dec": -1}
    registers = defaultdict(int)
    max_value = float("-inf")
    for r1, operation, v1, _, r2, c, v2 in instructions:
        registers[r1] += operations[operation] * int(v1) if comparisons[c](registers[r2], int(v2)) else 0
        max_value = max(max_value, registers[r1])
    return max(registers.values()), max_value


if __name__ == "__main__":
    instructions = read_input_file()
    part_one, part_two = both_parts(instructions)
    print(f"{part_one=}, {part_two=}")
