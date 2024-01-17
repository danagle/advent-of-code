"""
Advent of Code 2015
Day 4: The Ideal Stocking Stuffer
https://adventofcode.com/2015/day/4
"""
from hashlib import md5


def read_input_file():
    return open("input.txt", "r").read().strip()


def find_leading_zeroes_hash(data, num_zeroes=5):
    positive = 0
    zeroes = "0" * num_zeroes
    while True:
        data_string = data + str(positive)
        if zeroes == (md5(data_string.encode("utf-8")).hexdigest())[:num_zeroes]:
            break
        positive += 1
    return positive


def part_one(data):
    return find_leading_zeroes_hash(data, 5)


def part_two(data):
    return find_leading_zeroes_hash(data, 6)


if __name__ == "__main__":
    input_string = read_input_file()
    print(part_one(input_string))
    print(part_two(input_string))
