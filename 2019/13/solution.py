"""
Advent of Code 2019
Day 13: Care Package
https://adventofcode.com/2019/day/13
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


def intcode_thirteen(memory, input_fn=lambda: 0):
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
                memory[get_store(mode_a, memory[pointer + 1])] = input_fn()
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


def part_one(operations):
    screen = defaultdict(int)
    output_gen = intcode_thirteen(operations)
    while True:
        if (x_position := next(output_gen)) is None:
            break
        y_position = next(output_gen)
        tile_id = next(output_gen)
        screen[(x_position, y_position)] = tile_id

    print(f"part_one: {sum([1 for k, v in screen.items() if v == 2])}")


def part_two(memory):
    memory[0] = 2  # Set Memory address 0 to 2 to play for free
    ball_position = paddle_position = -1
    screen = defaultdict(int)

    def joystick_instruction_fn():
        nonlocal ball_position, paddle_position
        return 1 if ball_position > paddle_position else -1 if ball_position < paddle_position else 0

    output_gen = intcode_thirteen(memory, joystick_instruction_fn)

    while True:
        if (x_position := next(output_gen)) is None:
            break
        y_position = next(output_gen)
        tile_id = next(output_gen)
        screen[(x_position, y_position)] = tile_id
        # Update position of ball and paddle
        if tile_id in (3, 4):
            if tile_id == 3:
                paddle_position = x_position
            else:
                ball_position = x_position

    print(f"part_two: {screen[(-1, 0)]}")


if __name__ == "__main__":
    memory_operations = read_input_file()
    part_one(deepcopy(memory_operations))
    part_two(deepcopy(memory_operations))
