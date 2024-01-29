"""
Advent of Code 2015
Day 25:
https://adventofcode.com/2015/day/25
"""
from re import findall


def read_input_file():
    return tuple(map(int, findall(r"-?\d+", open("input.txt", "r").read())))


def part_one(row_column):
    """
       | 1   2   3   4   5   6
    ---+---+---+---+---+---+---+
     1 |  1   3   6  10  15  21
     2 |  2   5   9  14  20
     3 |  4   8  13  19
     4 |  7  12  18
     5 | 11  17
     6 | 16

    The sequence makes up an isoceles triangle, the first row and column are the sides
    of equal length. Given the coordinates of a position on the third side the length
    of the top edge of the triangle can be obtained by: X + Y - 1

    The step size for the top row is an increasing series: 2, 3, 4, 5, 6 ... etc.

    This pattern can be used to determine how many codes in the triangle need to be calculated.

    The final value in the top row of the triangle is row - 1 positions after the value
    we are looking for (row, column). This is the number of codes to generate.
    """
    row, column = row_column
    step, value, code = 1, 0, 20151125
    top_row_length = row + column - 1
    for _ in range(top_row_length - 1):
        step += 1
        value += step
    number_of_codes = value - (row - 1)
    for _ in range(number_of_codes):
        code = (code * 252533) % 33554393
    return code


if __name__ == "__main__":
    location = read_input_file()
    print(f"Part 1: {part_one(location)}")
