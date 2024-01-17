"""
Advent of Code 2016
Day 3: Squares With Three Sides
https://adventofcode.com/2016/day/3
"""
from re import findall


def read_input_file():
    return [list(map(int, findall(r"-?\d+", line))) for line in open("input.txt", "r").read().splitlines()]


def part_one(data):
    count = 0
    for triangle in data:
        a, b, c = sorted(triangle)
        if a + b > c:
            count += 1
    return count


def part_two(data):
    new_data = []
    for i in range(0, len(data), 3):
        for j in range(3):
            new_data.append(sorted([data[i][j], data[i+1][j], data[i+2][j]]))
    return sum(1 for t in new_data if t[0] + t[1] > t[2])


if __name__ == "__main__":
    triangles = read_input_file()
    print(part_one(triangles))
    print(part_two(triangles))
