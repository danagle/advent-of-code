"""
Advent of Code 2018
Day 19: Go With The Flow
https://adventofcode.com/2018/day/19
"""
from re import findall
from collections import defaultdict


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def wrap_operation(fn):

    def wrapped_func(state, params_list):
        new_state = list(state)
        new_state[params_list[3]] = fn(state, params_list[1], params_list[2])
        return new_state

    return wrapped_func


def get_operations():
    operations = {
        "addr": wrap_operation(lambda state, a, b: state[a] + state[b]),
        "addi": wrap_operation(lambda state, a, b: state[a] + b),
        "mulr": wrap_operation(lambda state, a, b: state[a] * state[b]),
        "muli": wrap_operation(lambda state, a, b: state[a] * b),
        "banr": wrap_operation(lambda state, a, b: state[a] & state[b]),
        "bani": wrap_operation(lambda state, a, b: state[a] & b),
        "borr": wrap_operation(lambda state, a, b: state[a] | state[b]),
        "bori": wrap_operation(lambda state, a, b: state[a] | b),
        "setr": wrap_operation(lambda state, a, b: state[a]),
        "seti": wrap_operation(lambda state, a, b: a),
        "gtir": wrap_operation(lambda state, a, b: 1 if a > state[b] else 0),
        "gtri": wrap_operation(lambda state, a, b: 1 if state[a] > b else 0),
        "gtrr": wrap_operation(lambda state, a, b: 1 if state[a] > state[b] else 0),
        "eqir": wrap_operation(lambda state, a, b: 1 if a == state[b] else 0),
        "eqri": wrap_operation(lambda state, a, b: 1 if state[a] == b else 0),
        "eqrr": wrap_operation(lambda state, a, b: 1 if state[a] == state[b] else 0)
    }
    return operations


def part_one(lines):
    registers = [0, 0, 0, 0, 0, 0]
    pointer, *program = lines
    pointer = tuple(map(int, findall(r"-?\d+", pointer)))[0]
    operations = get_operations()

    while True:
        if registers[pointer] < 0 or registers[pointer] >= len(program):
            break
        instruction, a, b, c = program[registers[pointer]].split()
        registers = operations[instruction](registers, [0, int(a), int(b), int(c)])
        registers[pointer] += 1

    return registers[0]


def part_two_loop(lines):
    registers = [1, 0, 0, 0, 0, 0]
    pointer, *program = lines
    pointer = tuple(map(int, findall(r"-?\d+", pointer)))[0]
    operations = get_operations()
    t = 0
    while True:
        if registers[pointer] < 0 or registers[pointer] >= len(program):
            break
        instruction, a, b, c = program[registers[pointer]].split()
        registers = operations[instruction](registers, [0, int(a), int(b), int(c)])
        registers[pointer] += 1
        t += 1
        print(f"{t}: {registers}")
        if t == 50:
            break
    print(registers)


def part_two(lines):
    a, b = map(int, [findall(r"\d+", lines[i])[1] for i in [22, 24]])
    number_to_factorize = 10551236 + a * 22 + b

    factors = defaultdict(int)
    possible_prime_divisor = 2
    while possible_prime_divisor ** 2 <= number_to_factorize:
        while number_to_factorize % possible_prime_divisor == 0:
            number_to_factorize /= possible_prime_divisor
            factors[possible_prime_divisor] += 1
        possible_prime_divisor += 1
    if number_to_factorize > 1:
        factors[number_to_factorize] += 1

    sum_of_divisors = 1
    for prime_factor in factors:
        sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (prime_factor - 1)

    return int(sum_of_divisors)


if __name__ == "__main__":
    input_lines = read_input_file()
    print("Part 1:", part_one(input_lines))
    print("Part 2:", part_two(input_lines))
