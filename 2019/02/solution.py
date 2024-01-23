"""
Advent of Code 2019
Day 2: 1202 Program Alarm
https://adventofcode.com/2019/day/2
"""
from itertools import product


def read_input_file():
    return list(map(int, open("input.txt", "r").read().strip().split(",")))


def exec_intcode(memory, noun, verb):
    pointer = 0
    memory[1] = noun
    memory[2] = verb
    while True:
        opcode = memory[pointer]
        if 99 == opcode:
            return memory[0]

        param_1 = memory[pointer + 1]
        param_2 = memory[pointer + 2]
        destination = memory[pointer + 3]

        if opcode == 1:
            memory[destination] = memory[param_1] + memory[param_2]
        elif opcode == 2:
            memory[destination] = memory[param_1] * memory[param_2]

        pointer += 4


def part_one(codes):
    return exec_intcode(codes[:], 12, 2)


def part_two(codes):
    for noun, verb in product(range(100), range(100)):
        if 19690720 == exec_intcode(codes[:], noun, verb):
            break
    return 100 * noun + verb


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
