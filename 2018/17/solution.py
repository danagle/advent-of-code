"""
Advent of Code 2018
Day 17: Reservoir Research
https://adventofcode.com/2018/day/17
"""
from collections import defaultdict
from re import findall
from sys import setrecursionlimit


def read_input_file():
    clay = defaultdict(bool)
    for line in open("input.txt", "r").read().splitlines():
        values = tuple(map(int, findall(r"-?\d+", line)))
        if "x" == line[0]:
            for y in range(values[1], values[2] + 1):
                clay[(values[0], y)] = True
        else:
            for x in range(values[1], values[2] + 1):
                clay[(x, values[0])] = True
    return clay


def both_parts(clay):
    settled, flowing = set(), set()
    y_min, y_max = min(clay, key=lambda t: t[1])[1], max(clay, key=lambda t: t[1])[1]
    spring_location = (500, 0)

    def fill(location, direction=(0, 1)):
        nonlocal settled, flowing, y_max

        flowing.add(location)
        below, left, right = (location[0], location[1] + 1), (location[0] - 1, location[1]), (location[0] + 1, location[1])

        if not clay[below] and below not in flowing and 1 <= below[1] <= y_max:
            fill(below)

        if not clay[below] and below not in settled:
            return False

        left_filled = clay[left] or left not in flowing and fill(left, direction=(-1, 0))
        right_filled = clay[right] or right not in flowing and fill(right, direction=(1, 0))

        if direction == (0, 1) and left_filled and right_filled:
            settled.add(location)

            while left in flowing:
                settled.add(left)
                left = (left[0] - 1, left[1])

            while right in flowing:
                settled.add(right)
                right = (right[0] + 1, right[1])

        return direction == (-1, 0) and (left_filled or clay[left]) or \
            direction == (1, 0) and (right_filled or clay[right])

    fill(spring_location)
    print('Part 1:', len([location for location in flowing | settled if y_min <= location[1] <= y_max]))
    print('Part 2:', len([location for location in settled if y_min <= location[1] <= y_max]))


if __name__ == "__main__":
    setrecursionlimit(3000)
    clay = read_input_file()
    both_parts(clay)
