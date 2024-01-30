"""
Advent of Code 2016
Day 19: An Elephant Named Joseph
https://adventofcode.com/2016/day/19
"""
from collections import deque


def read_input_file():
    return int(open("input.txt", "r").read().strip())


def part_one(num_elves):
    """
    Reference: https://en.wikipedia.org/wiki/Josephus_problem
    Reference: https://youtu.be/uCsD3ZGzMgE
    """
    return int(bin(num_elves)[3:] + "1", 2)


def part_two(num_elves):
    left = deque(i for i in range(1, int(num_elves / 2) + 1))
    right = deque(i for i in range(num_elves + 1, int(num_elves / 2) + 1, -1))

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # Pop elements to rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0]


def part_two_pattern(num_elves):
    i = 1
    while i * 3 < num_elves:
        i *= 3
    print(num_elves - i)


if __name__ == "__main__":
    elves = read_input_file()
    print(part_one(elves))
    print(part_two(elves))
    part_two_pattern(elves)
