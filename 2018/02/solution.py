"""
Advent of Code 2018
Day 2: Inventory Management System
https://adventofcode.com/2018/day/2
"""
from collections import Counter
from itertools import permutations


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(box_ids):
    two_count = three_count = 0
    for box_id in box_ids:
        counts = Counter(box_id).most_common()
        has_two_count = has_three_count = 0
        for (_, value) in counts:
            match value:
                case 3:
                    has_three_count = 1
                case 2:
                    has_two_count = 1
                case 1:
                    break
        two_count += has_two_count
        three_count += has_three_count
    return two_count * three_count


def part_two(box_ids):
    for id_a, id_b in list(permutations(box_ids, 2)):
        differences = 0
        string = ""
        for a_char, b_char in zip(id_a, id_b):
            if a_char != b_char:
                differences += 1
            else:
                string += a_char
        if differences == 1:
            return string


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
