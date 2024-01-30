"""
Advent of Code 2016
Day 21: Scrambled Letters and Hash
https://adventofcode.com/2016/day/21
"""
from itertools import permutations


def read_input_file():
    instructions = []
    for line in open("input.txt", "r").read().splitlines():
        tokens = line.split(" ")
        if tokens[0] in ("move", "swap"):
            a, b = tokens[2], tokens[5]
            if a.isnumeric():
                a, b = int(tokens[2]), int(tokens[5])
            instructions.append((tokens[0], a, b))
        elif "rotate" == tokens[0]:
            if "based" == tokens[1]:
                instructions.append((tokens[0], tokens[2], tokens[6]))
            else:
                instructions.append((tokens[0], tokens[1], int(tokens[2])))
        elif "reverse" == tokens[0]:
            instructions.append((tokens[0], int(tokens[2]), int(tokens[4])))
    return instructions


def move_position(s, a, b):
    char_list = list(s)
    c = char_list.pop(a)
    char_list.insert(b, c)
    return "".join(char_list)


def rotate_position(s, letter):
    index = s.index(letter)
    if 3 < index:
        index += 1
    index += 1
    for i in range(index):
        s = s[-1] + s[:-1]
    return s


def rotate_left(s, rotations):
    for _ in range(int(rotations)):
        s = s[1:] + s[0]
    return s


def rotate_right(s, rotations):
    for _ in range(int(rotations)):
        s = s[-1] + s[:-1]
    return s


def reverse_positions(s, a, b):
    char_list = list(s)
    char_list[a:b + 1] = reversed(char_list[a:b + 1])
    return "".join(char_list)


def swap_letters(s, a, b):
    char_list = list(s)
    if isinstance(a, str):
        a, b = char_list.index(a), char_list.index(b)
    char_list[b], char_list[a] = char_list[a], char_list[b]
    return "".join(char_list)


def part_one(instructions, password):
    for instruction in instructions:
        match instruction[0]:
            case "move":
                password = move_position(password, instruction[1], instruction[2])
            case "reverse":
                password = reverse_positions(password, instruction[1], instruction[2])
            case "rotate":
                if instruction[1] == "left":
                    password = rotate_left(password, instruction[-1])
                elif instruction[1] == "right":
                    password = rotate_right(password, instruction[-1])
                else:
                    password = rotate_position(password, instruction[-1])
            case "swap":
                password = swap_letters(password, instruction[1], instruction[2])

    return password


def part_two(instructions, expected_password):
    for candidate in permutations(expected_password, len(expected_password)):
        password = part_one(instructions, "".join(candidate))
        if expected_password == password:
            return "".join(candidate)


if __name__ == "__main__":
    scramble_instructions = read_input_file()
    print(part_one(scramble_instructions, "abcdefgh"))
    print(part_two(scramble_instructions, "fbgdceah"))
