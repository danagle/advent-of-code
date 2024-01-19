"""
Advent of Code 2017
Day 1: Inverse Captcha
https://adventofcode.com/2017/day/1
"""


def read_input_file():
    return list(map(int, [c for c in open("input.txt", "r").read().strip()]))


def part_one(numbers):
    total = 0
    for i, value in enumerate(numbers):
        index = (i + 1) % len(numbers)
        if numbers[index] == value:
            total += value
    return total


def part_two(numbers):
    mid_index = len(numbers) // 2
    total = 0
    for i, value in enumerate(numbers[:mid_index]):
        if numbers[i] == numbers[mid_index + i]:
            total += value
    return total * 2


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
