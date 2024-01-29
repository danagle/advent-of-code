"""
Advent of Code 2015
Day 23: Opening the Turing Lock
https://adventofcode.com/2015/day/23
"""


def read_input_file():
    return open("input.txt").read().splitlines()


def execute_program(instructions, register_a=0):
    registers, pointer = {"a": register_a, "b": 0}, 0
    while 0 <= pointer < len(instructions):
        instruction, arguments = instructions[pointer].split(maxsplit=1)
        arguments = arguments.split(", ")
        pointer += 1
        match (instruction, *arguments):
            case ("hlf", r):
                registers[r] //= 2
            case ("tpl", r):
                registers[r] *= 3
            case ("inc", r):
                registers[r] += 1
            case ("jmp", offset):
                pointer += int(offset) - 1
            case ("jie", r, offset):
                if registers[r] % 2 == 0:
                    pointer += int(offset) - 1
            case ("jio", r, offset):
                if registers[r] == 1:
                    pointer += int(offset) - 1
    return registers["b"]


if __name__ == "__main__":
    program = read_input_file()
    part_one = execute_program(program, 0)
    part_two = execute_program(program, 1)
    print(f"{part_one=}, {part_two=}")
