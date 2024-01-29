"""
Advent of Code 2016
Day 9: Explosives in Cyberspace
https://adventofcode.com/2016/day/9
"""
from re import search as regex_search


def read_input_file():
    return open("input.txt", "r").read().strip()


def part_one(text):
    position = 0
    while (left_index := text.find("(", position)) > -1:
        right_index = text.find(")", left_index)
        sequence_length, repeats = tuple(map(int, text[left_index+1:right_index].split("x")))
        sequence = text[right_index+1:right_index+1+sequence_length]
        text = text[:left_index] + (sequence * repeats) + text[right_index+1+sequence_length:]
        position = left_index + len(sequence) * repeats
    return len(text)


def part_two(text):
    marker = regex_search(r"\((\d+)x(\d+)\)", text)
    if not marker:
        return len(text)
    position = marker.start(0)
    size = int(marker.group(1))
    repeats = int(marker.group(2))
    index = position + len(marker.group())
    return len(text[:position]) + part_two(text[index:index+size]) * repeats + part_two(text[index+size:])


if __name__ == "__main__":
    compressed_text = read_input_file()
    print("Part 1:", part_one(compressed_text))
    print("Part 2:", part_two(compressed_text))
