"""
Advent of Code 2017
Day 6: Memory Reallocation
https://adventofcode.com/2017/day/6
"""
from re import findall


def read_input_file():
    return list(map(int, findall("(\d+)", open("input.txt", "r").read().strip())))


def debug_loop(banks_state):
    previous_states = set()
    trace = []
    cycle_detected = False
    while not cycle_detected:
        position = banks_state.index(max(banks_state))
        blocks_to_distribute = banks_state[position]
        banks_state[position] = 0
        while blocks_to_distribute:
            if position < 15:
                banks_state[position + 1] += 1
            else:
                banks_state[0] += 1
                position = -1
            blocks_to_distribute -= 1
            position += 1
        current_banks = tuple(banks_state)
        if current_banks in previous_states:
            part_one = len(previous_states) + 1
            part_two = len(trace) - trace.index(current_banks)
            cycle_detected = True
        previous_states.add(current_banks)
        trace.append(current_banks)
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    blocks = read_input_file()
    debug_loop(blocks)
