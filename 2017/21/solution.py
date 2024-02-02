"""
Advent of Code 2017
Day 21: Fractal Art
https://adventofcode.com/2017/day/21
"""
import numpy as np


def read_input_file():
    rules = {}
    for line in open("input.txt", "r").read().splitlines():
        k, v = map(translate_to_np, line.strip().split(" => "))
        for a in (k, np.fliplr(k)):
            for r in range(4):
                rules[np.rot90(a, r).tobytes()] = v
    return rules


def translate_to_np(string):
    return np.array([[ch == "#" for ch in line] for line in string.split("/")])


def count_pixels_in_on_state(rules, iterations=5):
    grid = translate_to_np(".#./..#/###")
    for _ in range(iterations):
        size = len(grid)
        by = 2 if size % 2 == 0 else 3
        by_1 = by + 1
        new_size = size * by_1 // by
        new_grid = np.empty((new_size, new_size), dtype=bool)
        squares = range(0, size, by)
        new_squares = range(0, new_size, by_1)

        for i, new_i in zip(squares, new_squares):
            for j, new_j in zip(squares, new_squares):
                square = grid[i:i + by, j:j + by]
                new_grid[new_i:new_i + by_1, new_j:new_j + by_1] = rules[square.tobytes()]

        grid = new_grid

    return int(grid.sum())


if __name__ == "__main__":
    enhancement_rules = read_input_file()
    print(count_pixels_in_on_state(enhancement_rules, iterations=5))
    print(count_pixels_in_on_state(enhancement_rules, iterations=18))
