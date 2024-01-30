"""
Advent of Code 2016
Day 23: Safe Cracking
https://adventofcode.com/2016/day/23
"""
from math import factorial


def read_input_file():
    code = [line.split() for line in open("input.txt", "r").read().splitlines()]
    for instruction in code:
        for index, token in enumerate(instruction):
            if index > 0 and token[-1].isnumeric():
                instruction[index] = int(token)
    return code


def execute_assembunny_code(assembunny_code, registers):

    def load_register_or_arg(arg):
        nonlocal registers
        return registers[arg] if arg in registers else arg

    pointer = 0
    instruction_toggles = {"cpy": "jnz", "dec": "inc", "inc": "dec", "jnz": "cpy"}
    while 0 <= pointer < len(assembunny_code):
        cmd, *rest = assembunny_code[pointer]
        pointer += 1
        match cmd:
            case "cpy":
                arg1, arg2 = rest
                registers[arg2] = load_register_or_arg(arg1)
            case "inc":
                arg1 = rest[0]
                registers[arg1] += 1
            case "dec":
                arg1 = rest[0]
                registers[arg1] -= 1
            case "jnz":
                arg1, arg2 = rest
                value = load_register_or_arg(arg1)
                offset = load_register_or_arg(arg2)
                if value != 0:
                    pointer += offset - 1
            case "tgl":
                toggle_address = pointer - 1 + load_register_or_arg(rest[0])
                if 0 <= toggle_address < len(assembunny_code):
                    instruction = assembunny_code[toggle_address]
                    if instruction[0] in instruction_toggles:
                        instruction[0] = instruction_toggles[instruction[0]]
    return registers


def part_one(instructions):
    registers = {"a": 7, "b": 0, "c": 0, "d": 0}
    registers = execute_assembunny_code(instructions, registers)
    return registers["a"]


def part_two():
    print(87 * 74 + factorial(12))


if __name__ == '__main__':
    assembunny_code = read_input_file()
    print(part_one(assembunny_code))
    part_two()
