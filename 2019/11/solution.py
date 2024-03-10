"""
Advent of Code 2019
Day 11: Space Police
https://adventofcode.com/2019/day/11
"""
from collections import defaultdict
from copy import deepcopy


def read_input_file():
    computer_memory = defaultdict(int)
    for index, value in enumerate(list(map(int, open("input.txt", "r").read().strip().split(",")))):
        computer_memory[index] = value
    return computer_memory


def decode_instruction(instruction_code):
    decoded = str(instruction_code).zfill(5)
    return decoded[0], decoded[1], decoded[2], int(decoded[3:])


def intcode_eleven(memory):
    global hull_panels, position
    pointer = relative_base = operation = 0

    def get_param(mode, p):
        nonlocal relative_base, memory
        mode_param = {
            "0": memory[p],
            "1": p,
            "2": memory[relative_base + p]
        }
        return mode_param[mode]

    def get_store(mode, p):
        nonlocal relative_base
        return p if "0" == mode else relative_base + p

    while operation != 99:
        offset = 0
        mode_c, mode_b, mode_a, operation = decode_instruction(memory[pointer])
        match operation:
            case 1:  # add
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                memory[get_store(mode_c, c)] = get_param(mode_b, b) + get_param(mode_a, a)
            case 2:  # multiply
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                memory[get_store(mode_c, c)] = get_param(mode_b, b) * get_param(mode_a, a)
            case 3:  # input
                offset = 2
                memory[get_store(mode_a, memory[pointer + 1])] = hull_panels[position]
            case 4:  # output
                offset = 2
                yield get_param(mode_a, memory[pointer + 1])
            case 5:  # jump-if-true
                a, b = memory[pointer + 1], memory[pointer + 2]
                if get_param(mode_a, a):
                    pointer = get_param(mode_b, b)
                else:
                    offset = 3
            case 6:  # jump-if-false
                a, b = memory[pointer + 1], memory[pointer + 2]
                if not get_param(mode_a, a):
                    pointer = get_param(mode_b, b)
                else:
                    offset = 3
            case 7:  # less-than
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                if get_param(mode_a, a) < get_param(mode_b, b):
                    memory[get_store(mode_c, c)] = 1
                else:
                    memory[get_store(mode_c, c)] = 0
            case 8:  # equals
                offset = 4
                a, b, c = memory[pointer + 1], memory[pointer + 2], memory[pointer + 3]
                if get_param(mode_a, a) == get_param(mode_b, b):
                    memory[get_store(mode_c, c)] = 1
                else:
                    memory[get_store(mode_c, c)] = 0
            case 9:  # relative base
                offset = 2
                relative_base += get_param(mode_a, memory[pointer + 1])

        pointer += offset
    yield None


def activate_painting_robot(program, start_colour=0):
    global hull_panels, position
    hull_panels, position, vector = defaultdict(int), 0, -1j
    hull_panels[position] = start_colour
    output_gen = intcode_eleven(program)
    while True:
        # First, it will output a value indicating the color to paint the panel
        if (panel_color := next(output_gen)) is None:
            break
        hull_panels[position] = panel_color
        # Second, it will output a value indicating the direction the robot should turn
        if next(output_gen):
            vector *= 1j   # 1 means it should turn right 90 degrees
        else:
            vector *= -1j  # 0 means it should turn left 90 degrees
        position += vector
    return hull_panels


def part_one(operations):
    panels = activate_painting_robot(operations)
    print(f"part_one: {len(panels)}")


def print_text(container):
    min_x, min_y = int(min([p.real for p in container])), int(min([p.imag for p in container]))
    max_x, max_y = int(max([p.real for p in container])), int(max([p.imag for p in container]))
    for y in range(min_y, max_y+1):
        print("".join(["*" if x+1j*y in container else " " for x in range(min_x, max_x+1)]))


def part_two(operations):
    panels = activate_painting_robot(operations, 1)  # Robot to start on a white panel
    # Display the registration code
    print_text(set([k for k, v in panels.items() if v > 0]))


if __name__ == "__main__":
    hull_panels = defaultdict(int)
    position = 0
    memory_operations = read_input_file()
    part_one(deepcopy(memory_operations))
    part_two(deepcopy(memory_operations))
