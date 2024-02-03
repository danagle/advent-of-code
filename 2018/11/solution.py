"""
Advent of Code 2018
Day 11: Chronal Charge
https://adventofcode.com/2018/day/11
"""
from collections import defaultdict
from itertools import product


def read_input_file():
    return int(open("input.txt", "r").read().strip())


def both_parts(serial):
    grid_sums, partial_sums, part_one = {}, defaultdict(int), ""

    def power_level(x, y):
        nonlocal serial
        return ((((x + 10) * y + serial) * (x + 10)) // 10 ** 2 % 10) - 5

    def get_partial_sum(x, y):
        return power_level(x + 1, y + 1) + partial_sums[x, y - 1] + partial_sums[x - 1, y] - partial_sums[x - 1, y - 1]

    for j, i in product(range(300), range(300)):
        partial_sums[(i, j)] = get_partial_sum(i, j)

    for size in range(2, 300):
        for j in range(size - 1, 300):
            for i in range(size - 1, 300):
                a, b = i - size, j - size
                total_sum = partial_sums[(i, j)] + partial_sums[(a, b)] - partial_sums[(a, j)] - partial_sums[(i, b)]
                grid_sums[total_sum] = (a + 2, b + 2, size)
        if size == 3:
            x_3, y_3, _ = grid_sums[max(grid_sums)]
            part_one = ",".join(map(str, (x_3, y_3)))

    part_two = ",".join(map(str, grid_sums[max(grid_sums)]))
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    grid_serial_number = read_input_file()
    both_parts(grid_serial_number)
