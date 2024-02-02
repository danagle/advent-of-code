"""
Advent of Code 2017
Day 23: Coprocessor Conflagration
https://adventofcode.com/2017/day/23
"""
from collections import defaultdict, deque


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(instructions):
    registers = defaultdict(int)
    mul_called = pointer = 0

    def get(value):
        nonlocal registers
        try:
            return int(value)
        except ValueError:
            return registers[value]

    while 0 <= pointer < len(instructions):
        tokens = instructions[pointer].split()
        pointer += 1
        match tokens[0]:
            case "set":
                registers[tokens[1]] = get(tokens[2])
            case "sub":
                registers[tokens[1]] -= get(tokens[2])
            case "mul":
                mul_called += 1
                registers[tokens[1]] *= get(tokens[2])
            case "jnz":
                if get(tokens[1]) != 0:
                    pointer += get(tokens[2]) - 1

    print(mul_called)


def part_two(instructions):
    registers = defaultdict(int)
    registers["a"] = 1
    pointer = 0

    def get(value):
        nonlocal registers
        try:
            return int(value)
        except ValueError:
            return registers[value]

    while pointer < 11:
        tokens = instructions[pointer].split()
        pointer += 1
        match tokens[0]:
            case "set":
                registers[tokens[1]] = get(tokens[2])
            case "sub":
                registers[tokens[1]] -= get(tokens[2])
            case "mul":
                registers[tokens[1]] *= get(tokens[2])
            case "jnz":
                if get(tokens[1]) != 0:
                    pointer += get(tokens[2]) - 1

    non_primes = 0
    for b in range(registers["b"], registers["c"] + 1, 17):
        if any(b % d == 0 for d in range(2, int(b ** 0.5))):
            non_primes += 1
    print(non_primes)


if __name__ == "__main__":
    code = read_input_file()
    part_one(code)
    part_two(code)
