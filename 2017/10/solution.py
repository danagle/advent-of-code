"""
Advent of Code 2017
Day 10: Knot Hash
https://adventofcode.com/2017/day/10
"""
from functools import reduce
from operator import xor


def read_input_file():
    return open("input.txt", "r").read().strip()


def twist(numbers, skip, position, sequence):
    for l in sequence:
        to_reverse = []
        for x in range(l):
            n = (position + x) % 256
            to_reverse.append(numbers[n])
        to_reverse.reverse()
        for x in range(l):
            n = (position + x) % 256
            numbers[n] = to_reverse[x]
        position += l + skip
        position = position % 256
        skip += 1
    return numbers, skip, position


def part_one(lengths):
    position = skip_size = 0
    numbers_list = [_ for _ in range(256)]
    lengths_list = list(map(int, lengths.split(",")))
    numbers_list, _, _ = twist(numbers_list, skip_size, position, lengths_list)
    return numbers_list[0] * numbers_list[1]


def part_two(lengths):
    position = skip_size = 0
    numbers_list = [_ for _ in range(256)]
    sequence_list = list(map(ord, lengths)) + [17, 31, 73, 47, 23]
    for _ in range(64):
        numbers_list, skip_size, position = twist(numbers_list, skip_size, position, sequence_list)
    dense = []
    for n in range(16):
        sub_slice = numbers_list[16 * n:16 * n + 16]
        dense.append("%02x" % reduce(xor, sub_slice))
    return "".join(dense)


if __name__ == "__main__":
    sequence_str = read_input_file()
    print("Part 1:", part_one(sequence_str))
    print("Part 2:", part_two(sequence_str))
