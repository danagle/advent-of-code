"""
Advent of Code 2016
Day 25: Clock Signal
https://adventofcode.com/2016/day/25
"""


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

    pointer, output = 0, []
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
            case "out":
                output.append(load_register_or_arg(rest[0]))
        if len(output) == 10:
            break

    return registers, "".join(map(str, output))


def part_one(instructions):
    signal_match_found = False
    register_a = 0
    while not signal_match_found:
        register_a += 1
        registers, signal_text = execute_assembunny_code(instructions, {"a": register_a, "b": 0, "c": 0, "d": 0})
        if "0101010101" == signal_text:
            signal_match_found = True
    return register_a


if __name__ == "__main__":
    code_lines = read_input_file()
    print(f"{part_one(code_lines)=}")
