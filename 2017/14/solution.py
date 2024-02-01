"""
Advent of Code 2017
Day 14: Disk Defragmentation
https://adventofcode.com/2017/day/14
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


def knot_hash(lengths):
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


def both_parts(key_string):
    regions, unseen = 0, []
    for i in range(128):
        hash_str = knot_hash(key_string + "-" + str(i))
        bin_hash = bin(int(hash_str, 16))[2:].zfill(128)
        unseen += [(i, j) for j, d in enumerate(bin_hash) if d == "1"]
    part_one = str(len(unseen))
    while unseen:
        queued = [unseen[0]]
        while queued:
            (x, y) = queued.pop()
            if (x, y) in unseen:
                unseen.remove((x, y))
                queued += [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        regions += 1
    part_two = str(regions)
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    key = read_input_file()
    both_parts(key)
