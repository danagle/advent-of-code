"""
Advent of Code 2018
Day 8: Memory Maneuver
https://adventofcode.com/2018/day/8
"""
from re import findall


def read_input_file():
    return tuple(map(int, findall(r"\d+", open("input.txt", "r").read())))


def parse(data):
    child_nodes, metadata_entries = data[:2]
    data = data[2:]
    sum_total, values = 0, []

    for _ in range(child_nodes):
        total, value, data = parse(data)
        sum_total += total
        values.append(value)

    sum_total += sum(data[:metadata_entries])

    if child_nodes == 0:
        return sum_total, sum(data[:metadata_entries]), data[metadata_entries:]
    else:
        return (
            sum_total,
            sum(values[k - 1] for k in data[:metadata_entries] if 0 < k <= len(values)),
            data[metadata_entries:]
        )


if __name__ == "__main__":
    input_data = read_input_file()
    part_one, part_two, _ = parse(input_data)
    print(f"{part_one=}, {part_two=}")
