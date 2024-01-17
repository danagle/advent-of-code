"""
Advent of Code 2015
Day 6: Probably a Fire Hazard
https://adventofcode.com/2015/day/6
"""


def read_input_file():
    lines = [line.replace("turn ", "").replace(" through ", " ").replace(",", " ").split(" ")
             for line in open("input.txt", "r").readlines()]
    return [(l[0], (int(l[1]), int(l[2])), (int(l[3]), int(l[4]))) for l in lines]


def part_one(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    for command, position_a, position_b in instructions:
        for y in range(position_a[1], position_b[1] + 1):
            for x in range(position_a[0], position_b[0] + 1):
                match command:
                    case "off":
                        grid[y][x] = 0
                    case "on":
                        grid[y][x] = 1
                    case "toggle":
                        grid[y][x] = not grid[y][x]
    return sum(map(sum, grid))


def part_two(instructions):
    grid = [[0] * 1000 for _ in range(1000)]
    for command, position_a, position_b in instructions:
        for y in range(position_a[1], position_b[1] + 1):
            for x in range(position_a[0], position_b[0] + 1):
                match command:
                    case "off":
                        grid[y][x] = max(0, grid[y][x] - 1)
                    case "on":
                        grid[y][x] += 1
                    case "toggle":
                        grid[y][x] += 2
    return sum(map(sum, grid))


if __name__ == "__main__":
    lights_instructions = read_input_file()
    print(part_one(lights_instructions))
    print(part_two(lights_instructions))
