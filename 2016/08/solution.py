"""
Advent of Code 2016
Day 8: Two-Factor Authentication
https://adventofcode.com/2016/day/8
"""
from re import findall


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def swipe_the_card(instructions):
    display_grid = [[0 for _ in range(50)] for _ in range(6)]
    for instruction in instructions:
        if instruction.startswith("rect"):
            width, height = tuple(map(int, findall(r"(\d+)", instruction)))
            for i in range(height):
                for j in range(width):
                    display_grid[i][j] = 1
        elif "row" in instruction:
            row, pixels = tuple(map(int, findall(r"(\d+)", instruction)))
            for i in range(pixels):
                display_grid[row].insert(0, display_grid[row].pop(-1))
        elif "column" in instruction:
            column, pixels = tuple(map(int, findall(r"(\d+)", instruction)))
            column_state = []
            for row in display_grid:
                column_state.append(row[column])
            for i in range(pixels):
                column_state.insert(0, column_state.pop(-1))
            for index, pixel_value in enumerate(column_state):
                display_grid[index][column] = pixel_value
    # Part 1
    print(f"Part 1: {sum(sum(display_grid, []))}")
    # Part 2
    print("Part 2:")
    for row in display_grid:
        print("".join(["#" if (p == 1) else " " for p in row]))


if __name__ == "__main__":
    data = read_input_file()
    swipe_the_card(data)
