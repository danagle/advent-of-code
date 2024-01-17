"""
Advent of Code 2015
Day 1: Not Quite Lisp
https://adventofcode.com/2015/day/1
"""


def read_input_file():
    return open("input.txt", "r").read().strip()


def part_one(data):
    level = 0
    for char in data:
        match char:
            case "(":
                level += 1
            case ")":
                level -= 1
    return level


def part_two(data):
    level = 0
    for position, char in enumerate(data, start=1):
        match char:
            case "(":
                level += 1
            case ")":
                level -= 1
        if level == -1:
            break
    return position


if __name__ == "__main__":
    text = read_input_file()
    print(part_one(text))
    print(part_two(text))
