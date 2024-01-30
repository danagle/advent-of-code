"""
Advent of Code 2016
Day 15: Timing is Everything
https://adventofcode.com/2016/day/15
"""
from re import findall


def read_input_file():
    return [tuple(tuple(map(int, findall(r"(\d+)", line)))[1::2])
            for line in open("input.txt", "r").read().splitlines()]


def part_one(discs):
    time = 0
    while True:
        passed = True
        for delay, disc in enumerate(discs, 1):
            if (disc[1] + time + delay) % disc[0] != 0:
                passed = False
                break
        if passed:
            break
        time += 1
    return time


def part_two(discs):
    discs.append((11, 0))
    return part_one(discs)


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(data))
    print(part_two(data))
