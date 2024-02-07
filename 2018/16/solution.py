"""
Advent of Code 2018
Day 16: Chronal Classification
https://adventofcode.com/2018/day/16
"""
from re import findall


def read_input_file():
    _lines, _program = open("input.txt", "r").read().strip().split("\n\n\n")
    _lines = _lines.splitlines()
    return _lines, _program.strip()


def wrap_operation(fn):

    def wrapped_func(state, params_list):
        new_state = list(state)
        new_state[params_list[3]] = fn(state, params_list[1], params_list[2])
        return new_state

    return wrapped_func


def get_operation_options():
    addr = wrap_operation(lambda state, a, b: state[a] + state[b])
    addi = wrap_operation(lambda state, a, b: state[a] + b)
    mulr = wrap_operation(lambda state, a, b: state[a] * state[b])
    muli = wrap_operation(lambda state, a, b: state[a] * b)
    banr = wrap_operation(lambda state, a, b: state[a] & state[b])
    bani = wrap_operation(lambda state, a, b: state[a] & b)
    borr = wrap_operation(lambda state, a, b: state[a] | state[b])
    bori = wrap_operation(lambda state, a, b: state[a] | b)
    setr = wrap_operation(lambda state, a, b: state[a])
    seti = wrap_operation(lambda state, a, b: a)
    gtir = wrap_operation(lambda state, a, b: 1 if a > state[b] else 0)
    gtri = wrap_operation(lambda state, a, b: 1 if state[a] > b else 0)
    gtrr = wrap_operation(lambda state, a, b: 1 if state[a] > state[b] else 0)
    eqir = wrap_operation(lambda state, a, b: 1 if a == state[b] else 0)
    eqri = wrap_operation(lambda state, a, b: 1 if state[a] == b else 0)
    eqrr = wrap_operation(lambda state, a, b: 1 if state[a] == state[b] else 0)

    operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    return {index: list(enumerate(operations)) for index in range(len(operations))}


def part_one(samples, candidates):
    total = 0
    for line_number in range(0, len(samples), 4):
        if samples[line_number].startswith("Before:"):
            assert samples[line_number + 2].startswith("After:")
            before = list(map(int, findall(r"-?\d+", samples[line_number])))
            instruction = list(map(int, findall(r"-?\d+", samples[line_number + 1])))
            after = list(map(int, findall(r"-?\d+", samples[line_number + 2])))
            candidates[instruction[0]] = [(index, fn) for (index, fn) in candidates[instruction[0]]
                                          if fn(before, instruction) == after]
            if sum([operation(before, instruction) == after for _, operation in candidates[instruction[0]]]) >= 3:
                total += 1

    return total, candidates


def part_two(program_codes, operations):
    # Loop until there is a single option for each operation
    while any(map(lambda x: len(x) > 1, operations.values())):
        single_operations = set(filter(lambda x: x > -1,
                                       map(lambda k: k if len(operations[k]) == 1 else -1, operations)))
        multiple_options = {_ for _ in range(len(operations)) if _ not in single_operations}
        for a in single_operations:
            # Remove all other references to the identified operation
            identified_index = operations[a][0][0]
            for b in multiple_options:
                operations[b] = [(index, fn) for (index, fn) in operations[b] if index != identified_index]
    # Execute the program
    registers = [0, 0, 0, 0]
    for line in program_codes.splitlines():
        instruction = list(map(int, findall(r"-?\d+", line)))
        registers = operations[instruction[0]][0][1](registers, instruction)

    return registers[0]


if __name__ == "__main__":
    lines, program = read_input_file()
    operation_options = get_operation_options()
    part_1, operation_options = part_one(lines, operation_options)
    print(part_1)
    part_2 = part_two(program, operation_options)
    print(part_2)
