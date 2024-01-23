"""
Advent of Code 2019
Day 3: Crossed Wires
https://adventofcode.com/2019/day/3
"""
from collections import defaultdict


def read_input_file():
    return [[(token[0], int(token[1:])) for token in line.split(',')] for line in open("input.txt", "r").readlines()]


def manhattan_distance(point_a, point_b):
    return sum(abs(a - b) for a, b in zip(point_a, point_b))


def wire_intersections(crossed_wires):
    moves = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    wire_traces, wire_steps = [], []
    for index, wire_path in enumerate(crossed_wires):
        wire_traces.append(set())
        wire_steps.append(defaultdict(int))
        point, steps = (0, 0), 0
        for direction, distance in wire_path:
            for _ in range(distance):
                # Move in direction to the next point
                point = tuple(sum(t) for t in zip(point, moves[direction]))
                steps += 1
                # Only record the shortest number of steps to a point
                if point not in wire_steps[index]:
                    wire_steps[index][point] = steps
                wire_traces[index].add(point)
    # Points where wires cross
    intersections = wire_traces[0].intersection(wire_traces[1])
    # Shortest manhattan distance to central port
    part_one = min(manhattan_distance((0, 0), point) for point in intersections)
    # Fewest combined steps to an intersection
    part_two = min(sum(t) for t in zip(*list(tuple([p[k] for k in intersections]) for p in wire_steps)))

    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    data = read_input_file()
    wire_intersections(data)
