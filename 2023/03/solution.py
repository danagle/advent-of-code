from re import compile, finditer
from itertools import chain
from math import prod


def adjacent_to_part_number(row, start, end):
    return set(sorted(chain(*[[(row-1, col) for col in range(start-1, end+1)],
                              [(row+1, col) for col in range(start-1, end+1)],
                              [(row, start-1), (row, end)]])))


def read_input_file():
    with open("input.txt", "r") as input_file:
        schematic = input_file.read().splitlines()
        # Create a set of all symbol positions
        symbol_positions = set(chain(*[[(row, symbol.start())
                                        for symbol in finditer(compile("[\#\$\%\&\*\+\-\/\=\@]"), line)]
                                       for row, line in enumerate(schematic)]))
        # Create a list of part numbers and their adjacent positions
        number_adjacent = list(chain(*[[(int(p.group()), adjacent_to_part_number(row, p.start(), p.end()), row)
                                        for p in finditer("(\d+)", line)]
                                       for row, line in enumerate(schematic)]))
        # Filter list of symbol positions to get list of gear positions
        gear_positions = [(row, col) for row, col in symbol_positions if schematic[row][col] == "*"]
        return symbol_positions, number_adjacent, gear_positions


def part_one(symbols, numbers):
    return sum([n for n, adjacent, _ in numbers if len(adjacent.intersection(symbols))])


def part_two(gears, numbers):
    parts_list = []
    for gear in sorted(gears):
        # Filter list of parts for rows adjacent to gear
        filtered_parts = list(filter(lambda t: (gear[0]-1) <= t[2] <= (gear[0]+1), numbers))
        parts_list.append([n for n, adjacent, _ in filtered_parts if len(adjacent.intersection({gear}))])
    return sum(prod(parts) for parts in parts_list if len(parts) > 1)


if __name__ == "__main__":
    symbol_set, number_tuples, gears_list = read_input_file()
    parts_sum = part_one(symbol_set, number_tuples)
    parts_prod = part_two(gears_list, number_tuples)
    print(f"Part numbers sum : {parts_sum}")
    print(f"Part numbers prod : {parts_prod}")
