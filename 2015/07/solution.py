"""
Advent of Code 2015
Day 7: Some Assembly Required
https://adventofcode.com/2015/day/7
"""


def read_input_file():
    instructions = []
    lines = open("input.txt", "r").read().splitlines()
    for line in lines:
        tokens = [t.strip() for t in line.split(" ")]
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                tokens[i] = int(tokens[i])
        if "NOT" == tokens[0]:
            instructions.append((tokens[0], (tokens[1], tokens[3])))
        elif "->" == tokens[1]:
            instructions.append(("ASSIGN", (tokens[0], tokens[2])))
        else:
            instructions.append((tokens[1], (tokens[0], tokens[2], tokens[4])))
    return instructions


def run_circuit(instructions):
    signals = {}

    def load_param(p):
        if isinstance(p, str):
            p = signals.get(p)
        return p

    while instructions:
        next_instructions = []
        for instruction, parameters in instructions:

            inputs = [load_param(param) for param in parameters[:-1]]
            output = parameters[-1]

            if None in inputs:
                next_instructions.append((instruction, parameters))
                continue

            match instruction:
                case "ASSIGN":
                    signals[output] = inputs[0]
                case "AND":
                    signals[output] = inputs[0] & inputs[1]
                case "OR":
                    signals[output] = inputs[0] | inputs[1]
                case "LSHIFT":
                    signals[output] = (inputs[0] << inputs[1]) & 0xffff
                case "RSHIFT":
                    signals[output] = inputs[0] >> inputs[1]
                case "NOT":
                    signals[output] = ~inputs[0]

        instructions = next_instructions

    return signals["a"]


def both_parts(instructions):
    part_one = run_circuit(instructions)
    for index, instruction in enumerate(instructions):
        if "ASSIGN" == instruction[0] and "b" == instruction[1][-1]:
            instructions[index] = ("ASSIGN", (part_one, "b"))
            break
    part_two = run_circuit(instructions)
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    instructions_booklet = read_input_file()
    both_parts(instructions_booklet)
