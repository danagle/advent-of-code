"""
Advent of Code 2017
Day 17: Spinlock
https://adventofcode.com/2017/day/17
"""


def read_input_file():
    return int(open("input.txt", "r").read().strip())


def part_one(steps):
    buffer, position = [0], 0
    for number in range(1, 2018):
        position = (position + steps) % len(buffer) + 1
        buffer.insert(position, number)
    print(buffer[buffer.index(2017) + 1])


def part_two(steps):
    buffer_1, position, buffer_size = None, 0, 1
    for number in range(1, 50_000_001):
        position = (position + steps) % buffer_size + 1
        buffer_size += 1
        if position == 1:
            buffer_1 = number
    print(buffer_1)


if __name__ == "__main__":
    value = read_input_file()
    part_one(value)
    part_two(value)
