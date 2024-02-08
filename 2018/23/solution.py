"""
Advent of Code 2018
Day 23: Experimental Emergency Teleportation
https://adventofcode.com/2018/day/23
"""
from functools import reduce
from queue import PriorityQueue
from re import findall


def read_input_file():
    return [tuple(map(int, findall(r"-?\d+", line))) for line in open("input.txt", "r").read().splitlines()]


def manhattan_distance(xyz_1, xyz_2):
    return sum(abs(a - b) for a, b in zip(xyz_1, xyz_2))


def part_one(bots):
    *xyz, radius = reduce(lambda res, bot: bot if bot[3] > res[3] else res, bots, (-1, -1, -1, -1))

    return sum([manhattan_distance(xyz, abc) <= radius for *abc, _ in bots])


def part_two(bots):
    count = max_count = max_distance = 0
    queue = PriorityQueue()

    for x, y, z, radius in bots:
        distance = abs(x) + abs(y) + abs(z)
        # Add start of line segment to the queue
        queue.put((max(0, distance - radius), 1))
        # Add end of line segment to the queue
        queue.put((distance + radius + 1, -1))

    while not queue.empty():
        distance, e = queue.get()
        count += e
        if count > max_count:
            max_distance = distance
            max_count = count

    return max_distance


if __name__ == "__main__":
    nanobots = read_input_file()
    print(part_one(nanobots))
    print(part_two(nanobots))
