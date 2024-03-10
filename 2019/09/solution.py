"""
Advent of Code 2019
Day 9: Sensor Boost
https://adventofcode.com/2019/day/9
"""
from collections import defaultdict
from copy import deepcopy


def read_input_file():
    computer_memory = defaultdict(int)
    codes = list(map(int, open("input.txt", "r").read().strip().split(",")))
    for index, value in enumerate(codes):
        computer_memory[index] = value
    return computer_memory


def decode_instruction(instruction_code):
    decoded = str(instruction_code).zfill(5)
    return decoded[0], decoded[1], decoded[2], int(decoded[3:])


def intcode_nine(memory, inputs_list):
    pointer = relative_base = operation = 0

    def get_param(mode, p):
        nonlocal relative_base, memory
        mode_param = {
            "0": memory[p],
            "1": p,
            "2": memory[relative_base + p]
        }
        return mode_param[mode]

    def get_store(mode, p):
        nonlocal relative_base
        return p if "0" == mode else relative_base + p

    while operation != 99:
        offset = 0
        mode_c, mode_b, mode_a, operation = decode_instruction(memory[pointer])
        match operation:
            case 1:  # add
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                memory[get_store(mode_c, c)] = get_param(mode_b, b) + get_param(mode_a, a)
            case 2:  # multiply
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                memory[get_store(mode_c, c)] = get_param(mode_b, b) * get_param(mode_a, a)
            case 3:  # input
                offset = 2
                memory[get_store(mode_a, memory[pointer + 1])] = inputs_list[0]
                inputs_list = inputs_list[1:]
            case 4:  # output
                offset = 2
                yield get_param(mode_a, memory[pointer + 1])
            case 5:  # jump-if-true
                a, b = memory[pointer + 1], memory[pointer + 2]
                if get_param(mode_a, a):
                    pointer = get_param(mode_b, b)
                else:
                    offset = 3
            case 6:  # jump-if-false
                a, b = memory[pointer + 1], memory[pointer + 2]
                if not get_param(mode_a, a):
                    pointer = get_param(mode_b, b)
                else:
                    offset = 3
            case 7:  # less-than
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                if get_param(mode_a, a) < get_param(mode_b, b):
                    memory[get_store(mode_c, c)] = 1
                else:
                    memory[get_store(mode_c, c)] = 0
            case 8:  # equals
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                if get_param(mode_a, a) == get_param(mode_b, b):
                    memory[get_store(mode_c, c)] = 1
                else:
                    memory[get_store(mode_c, c)] = 0
            case 9:  # relative base
                offset = 2
                relative_base += get_param(mode_a, memory[pointer + 1])

        pointer += offset


def part_one(operations):
    for output in intcode_nine(operations, [1]):
        print(f"part_one: {output}")


def part_two(operations):
    for output in intcode_nine(operations, [2]):
        print(f"part_two: {output}")


if __name__ == "__main__":
    memory_operations = read_input_file()
    part_one(deepcopy(memory_operations))
    part_two(deepcopy(memory_operations))
