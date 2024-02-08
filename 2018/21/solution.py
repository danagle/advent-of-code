"""
Advent of Code 2018
Day 21: Chronal Conversion
https://adventofcode.com/2018/day/21
"""
from re import findall


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


def both_parts_slow(lines):
    registers = [0, 0, 0, 0, 0, 0]
    pointer, *program = lines
    pointer = tuple(map(int, findall(r"-?\d+", pointer)))[0]
    operations = get_operations()
    unique_set, first_value, last_value = set(), -1, -1

    while True:
        if registers[pointer] < 0 or registers[pointer] >= len(program):
            break
        instruction, a, b, c = program[registers[pointer]].split()
        registers = operations[instruction](registers, [0, int(a), int(b), int(c)])
        if "eqrr" == instruction:
            if (value := registers[int(a)]) not in unique_set:
                unique_set.add(value)
                last_value = value
                if 1 == len(unique_set):
                    first_value = value
            else:
                break
        registers[pointer] += 1

    return first_value, last_value, len(unique_set)


def both_parts_optimized(lines):
    magic_number = int(lines[8].split()[1])
    unique_values, first_value, last_value = set(), 0, -1
    c = 0

    while True:
        a = c | 65536
        c = magic_number

        while True:
            # Execute lines[7:15] in a single step
            c = (((c + (a & 255)) & 16777215) * 65899) & 16777215

            if 256 > a:
                if 1 == len(unique_values):
                    first_value = last_value
                if c not in unique_values:
                    unique_values.add(c)
                    last_value = c
                    break
                else:
                    return first_value, last_value, len(unique_values)
            else:
                a //= 256


if __name__ == "__main__":
    input_lines = read_input_file()
    # Optimized solution runtime: 14 ms
    part_one, part_two, cycle_length = both_parts_optimized(input_lines)
    # Slow solution runtimes - PyPy 3.10: 7 minutes; Python 3.11.7: 54 minutes!
    # part_one, part_two, cycle_length = both_parts_slow(input_lines)
    print(f"{part_one=}, {part_two=}, {cycle_length=}")
