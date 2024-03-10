"""
Advent of Code 2019
Day 12: The N-Body Problem
https://adventofcode.com/2019/day/12
"""
from math import gcd
from re import match as re_match
from sys import maxsize


def read_input_file():

    def parse_point(s):
        match = re_match("<x=(-?[0-9]+), y=(-?[0-9]+), z=(-?[0-9]+)>", s)
        return int(match[1]), int(match[2]), int(match[3])

    return list(map(parse_point, open("input.txt", "r").read().splitlines()))


def run_simulation(positions, velocities, steps=maxsize):
    original_positions, original_velocities = positions[:], velocities[:]
    step_number = 0
    while step_number < steps and (not step_number or positions != original_positions or velocities != original_velocities):
        for i in range(len(positions)):
            velocities[i] += sum(1 if positions[i] < position else -1 for position in positions if position != positions[i])
        for i in range(len(positions)):
            positions[i] += velocities[i]
        step_number += 1
    return step_number


def part_one(positions):
    px, vx = [x for x, _, _ in positions], [0] * len(positions)
    py, vy = [y for _, y, _ in positions], [0] * len(positions)
    pz, vz = [z for _, _, z in positions], [0] * len(positions)
    for p, v in zip((px, py, pz), (vx, vy, vz)):
        run_simulation(p, v, 1000)
    return sum((abs(px[i]) + abs(py[i]) + abs(pz[i])) * (abs(vx[i]) + abs(vy[i]) + abs(vz[i])) for i in range(len(positions)))


def part_two(positions):

    def _lcm(a, b):
        return a * b // gcd(a, b)

    steps_x = run_simulation([x for x, _, _ in positions], [0] * len(positions))
    steps_y = run_simulation([y for _, y, _ in positions], [0] * len(positions))
    steps_z = run_simulation([z for _, _, z in positions], [0] * len(positions))

    return _lcm(_lcm(steps_x, steps_y), steps_z)


if __name__ == "__main__":
    moon_positions = read_input_file()
    print(f"part_one: {part_one(moon_positions)}")
    print(f"part_two: {part_two(moon_positions)}")
