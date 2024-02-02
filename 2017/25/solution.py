"""
Advent of Code 2017
Day 25: The Halting Problem
https://adventofcode.com/2017/day/25
"""
from collections import defaultdict
from re import findall


def read_input_file():
    checksum_steps = int(findall(r"\d+", open("input.txt", "r").read().splitlines()[1])[0])

    program_states = {
        "A": (
            (1, 1, "B"),
            (0, -1, "C")
        ),
        "B": (
            (1, -1, "A"),
            (1, -1, "D")
        ),
        "C": (
            (1, 1, "D"),
            (0, 1, "C")
        ),
        "D": (
            (0, -1, "B"),
            (0, 1, "E")
        ),
        "E": (
            (1, 1, "C"),
            (1, -1, "F")
        ),
        "F": (
            (1, -1, "E"),
            (1, 1, "A")
        )
    }

    return checksum_steps, program_states


def part_one(checksum_steps, program_states):
    state, position = "A", 0
    memory = defaultdict(int)
    for i in range(checksum_steps):
        value, offset, new_state = program_states[state][memory[position]]
        memory[position] = value
        position += offset
        state = new_state
    print(sum(memory.values()))


if __name__ == "__main__":
    steps, program = read_input_file()
    part_one(steps, program)
