"""
Advent of Code 2017
Day 3: Spiral Memory
https://adventofcode.com/2017/day/3
"""
from collections import defaultdict
from itertools import product
from math import ceil, sqrt


def read_input_file():
    return int(open("input.txt", "r").read().strip())


def part_one(square_value):
    row = ceil(sqrt(square_value))
    one_coord = row // 2 + 1
    size = 1
    while (size * size) < square_value:
        size += 2
    size_squared = size * size
    row = column = size
    if (size_squared - ((size-1) * 4)) < square_value <= (size_squared - ((size-1) * 3)):
        row = size_squared - ((size-1) * 3) - square_value + 1
    elif (size_squared - ((size-1) * 3)) < square_value <= (size_squared - ((size-1) * 2)):
        row = 1
        column = square_value - (size_squared - ((size-1) * 2)) + 1
    elif (size_squared - ((size-1) * 2)) < square_value <= (size_squared - ((size-1) * 1)):
        row = square_value - (size_squared - ((size-1) * 2)) + 1
        column = 1
    elif size_squared - size < square_value < size_squared:
        column = square_value - (size_squared - size)
    return abs(row - one_coord) + abs(column - one_coord)


def get_next_square(coords):
    x, y = coords
    if x > y > -x:
        square = (x, y+1)
    elif y >= x and y > -x:
        square = (x-1, y)
    elif y <= -x and x >= y:
        square = (x+1, y)
    elif -x >= y > x:
        square = (x, y-1)
    return square


def part_two(square_value):
    values = defaultdict(int)
    neighbor_offsets = tuple(t for t in product((-1, 0, 1), repeat=2) if t != (0, 0))
    square = (0, 0)
    values[square] = 1
    while values[square] <= square_value:
        square = get_next_square(square)
        neighbors = [tuple(sum(t) for t in zip(square, offset)) for offset in neighbor_offsets]
        values[square] = (sum(values.get(neighbor, 0) for neighbor in neighbors))
    return values[square]


if __name__ == "__main__":
    value = read_input_file()
    print(part_one(value))
    print(part_two(value))
