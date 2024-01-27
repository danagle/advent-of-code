"""
Advent of Code 2015
Day 8: Matchsticks
https://adventofcode.com/2015/day/8
"""


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def both_parts(santa_list):
    code_length = 0
    literal_length = 0
    encoded_length = 0
    for line in santa_list:
        code_length += len(line)
        literal_length += len(eval(line))

        encoded_string = ""
        for char in line:
            if char == "\\":
                encoded_string += "\\\\"
            elif char == "\"":
                encoded_string += "\\\""
            else:
                encoded_string += char

        encoded_length += len(encoded_string) + 2

    part_one = code_length - literal_length
    part_two = encoded_length - code_length
    print(f"{part_one=}, {part_two=}")


if __name__ == '__main__':
    digital_list = read_input_file()
    both_parts(digital_list)
