"""
Advent of Code 2015
Day 18: Like a GIF For Your Yard
https://adventofcode.com/2015/day/18
"""
from collections import defaultdict
from copy import deepcopy
from itertools import product


def read_input_file():
    lines = open("input.txt", "r").read().splitlines()
    return {(x, y): "#" == char for y, line in enumerate(lines) for x, char in enumerate(line)}


def both_parts(initial_grid):
    width, height = max([p[0] for p in initial_grid.keys()]) + 1,  max([p[1] for p in initial_grid.keys()]) + 1
    grid_corners = ((0, 0), (height - 1, 0), (height - 1, width - 1), (0, width - 1))
    neighbor_offsets = list(filter(lambda p: (0, 0) != p, product(range(-1, 2), range(-1, 2))))
    lights_grid_one, lights_grid_two = deepcopy(initial_grid), deepcopy(initial_grid)

    def iterate_grid(grid, corners_static=False):
        nonlocal grid_corners, neighbor_offsets
        new_grid = defaultdict(int)
        for location in grid:
            neighbors = [tuple(sum(t) for t in zip(location, neighbor)) for neighbor in neighbor_offsets]
            on_count = sum([grid[neighbor] for neighbor in filter(lambda t: t in grid, neighbors)])
            if on_count == 3:
                new_grid[location] = 1
            elif on_count != 2:
                new_grid[location] = 0
            else:
                new_grid[location] = grid[location]
        if corners_static:
            for corner_to_reset in grid_corners:
                new_grid[corner_to_reset] = 1
        return new_grid

    for corner in grid_corners:
        lights_grid_two[corner] = 1
    for _ in range(100):
        lights_grid_one = iterate_grid(lights_grid_one)
        lights_grid_two = iterate_grid(lights_grid_two, True)
    return [sum(grid.values()) for grid in (lights_grid_one, lights_grid_two)]


if __name__ == "__main__":
    lights = read_input_file()
    part_one, part_two = both_parts(lights)
    print(f"{part_one=}, {part_two=}")
