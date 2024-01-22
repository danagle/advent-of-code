"""
Advent of Code 2018
Day 6: Chronal Coordinates
https://adventofcode.com/2018/day/6
"""
from collections import defaultdict
from itertools import product


def read_input_file():
    return [tuple(map(int, line.split(", "))) for line in open("input.txt").read().splitlines()]


def manhattan_distance(point_a, point_b):
    return sum(abs(a - b) for a, b in zip(point_a, point_b))


def both_parts(data):
    distances = {}
    areas = defaultdict(int)
    total_area = 0

    # Determine the bounding box
    min_x = min(p[0] for p in data)
    max_x = max(p[0] for p in data)
    min_y = min(p[1] for p in data)
    max_y = max(p[1] for p in data)
    # Iterate over each location in bounding box
    for point_a in product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        # Initialise each point in bounding box to 'None'
        distances[point_a] = None
        # Sort by manhattan distance to point
        sorted_distances = sorted([(manhattan_distance(point_a, point), point) for point in data])
        # If this location is closer to a single point then assign the point to it
        if sorted_distances[0][0] != sorted_distances[1][0]:
            distances[point_a] = sorted_distances[0][1]
        # Part 2: Area where sum of manhattan distance to all points is less than 10,000
        if sum(p[0] for p in sorted_distances) < 10_000:
            total_area += 1
    # Get the areas by counting locations closet to each point
    for point_a, point_b in distances.items():
        if point_b is not None:
            areas[point_b] += 1

    return max(areas.values()), total_area


if __name__ == "__main__":
    coords = read_input_file()
    part_one, part_two = both_parts(coords)
    print(f"{part_one=}, {part_two=}")
