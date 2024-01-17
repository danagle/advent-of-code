"""
Advent of Code 2016
Day 6: Signals and Noise
https://adventofcode.com/2016/day/6
"""
from collections import Counter


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def get_message(messages):
    rotated_text = zip(*messages)
    part_one = ""
    part_two = ""
    for chars in rotated_text:
        frequencies = Counter(chars).most_common()
        part_one += frequencies[0][0]
        part_two += frequencies[-1][0]
    return part_one, part_two


if __name__ == "__main__":
    data = read_input_file()
    print(get_message(data))
