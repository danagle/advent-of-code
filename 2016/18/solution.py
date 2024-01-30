"""
Advent of Code 2016
Day 18: Like a Rogue
https://adventofcode.com/2016/day/18
"""


def read_input_file():
    """Returns the puzzle input as a string."""
    return open("input.txt", "r").read().strip()


def part_one(tiles, num_rows=40):
    """Returns the number of safe tiles in the first 'num_rows' lines."""
    trap_patterns = {(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)}
    row = [1 if t == "." else 0 for t in tiles]
    rows_visited = 1
    safe_count = sum(row)
    while rows_visited < num_rows:
        new_row = []
        for position in range(len(row)):
            if 0 == position:
                t = (1, row[0], row[1])
            elif 0 < position < len(row) - 1:
                t = (row[position-1], row[position], row[position+1])
            else:
                t = (row[position-1], row[position], 1)
            new_row.append(0 if t in trap_patterns else 1)
        safe_count += sum(new_row)
        rows_visited += 1
        row = new_row
    return safe_count


def part_two(tiles):
    """Returns the number of safe tiles in the first 400,000 rows."""
    return part_one(tiles, num_rows=400_000)


if __name__ == "__main__":
    first_row = read_input_file()
    print(part_one(first_row))
    print(part_two(first_row))
