"""
Advent of Code 2016
Day 2: Bathroom Security
https://adventofcode.com/2016/day/2
"""
from itertools import product


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def get_door_code(key_pad, buttons, position, directions):
    moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    door_code = ""
    for line in directions:
        for move in line:
            next_position = tuple(sum(c) for c in (zip(position, moves["URDL".index(move)])))
            if next_position in buttons:
                position = next_position
        door_code += key_pad[position[0]][position[1]]
    return door_code


def part_one(instructions):
    key_pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    button_positions = set(product(range(3), range(3)))
    start_position = (1, 1)  # "5"
    return get_door_code(key_pad, button_positions, start_position, instructions)


def part_two(instructions):
    key_pad = [
        ["", "", "1", "", ""],
        ["", "2", "3", "4", ""],
        ["5", "6", "7", "8", "9"],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""]
    ]
    button_positions = {(0, 2), (1, 1), (1, 2), (1, 3),
                        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                        (3, 1), (3, 2), (3, 3), (4, 2)}
    start_position = (0, 2)  # "5"
    return get_door_code(key_pad, button_positions, start_position, instructions)


if __name__ == "__main__":
    lines = read_input_file()
    print(part_one(lines))
    print(part_two(lines))
