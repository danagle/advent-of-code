"""
Advent of Code 2016
Day 12: Leonardo's Monorail
https://adventofcode.com/2016/day/12
"""


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def execute_assembunny_code(assembunny_code, registers):
    index = 0
    while index < len(assembunny_code):
        parts = assembunny_code[index].split(" ")
        cmd, arg1, arg2, *rest = parts + [None]
        jump = 1
        if cmd == "cpy":
            registers[arg2] = registers[arg1] if arg1 in registers else int(arg1)
        elif cmd == "inc":
            registers[arg1] += 1
        elif cmd == "dec":
            registers[arg1] -= 1
        else:
            val = registers[arg1] if arg1 in registers else int(arg1)
            if val != 0:
                jump = int(arg2)
        index += jump
    return registers


def part_one(instructions):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers = execute_assembunny_code(instructions, registers)
    print("Part One:", registers["a"])


def part_two(instructions):
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    registers = execute_assembunny_code(instructions, registers)
    print("Part Two:", registers["a"])


if __name__ == "__main__":
    assembunny = read_input_file()
    part_one(assembunny)
    part_two(assembunny)
