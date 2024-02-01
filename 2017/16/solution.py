"""
Advent of Code 2017
Day 16: Permutation Promenade
https://adventofcode.com/2017/day/16
"""


def read_input_file():
    return open("input.txt", "r").read().strip().split(",")


def perform_dance(programs, dance_steps):
    for step in dance_steps:
        match step[0]:
            case "s":
                size = int(step[1:])
                programs = programs[-size:] + programs[:-size]
            case "x":
                sep = step.index("/")
                a, b = int(step[1:sep]), int(step[sep+1:])
                programs[a], programs[b] = programs[b], programs[a]
            case "p":
                a, b = programs.index(step[1]), programs.index(step[-1])
                programs[a], programs[b] = programs[b], programs[a]
    return programs


def part_one(dance_steps):
    return "".join(perform_dance([p for p in "abcdefghijklmnop"], dance_steps))


def part_two(dance_steps):
    programs, previous = [p for p in "abcdefghijklmnop"], []
    while (state := tuple(programs)) not in previous:
        previous.append(state)
        programs = perform_dance(programs, dance_steps)
    return "".join(previous[1_000_000_000 % len(previous)])


if __name__ == '__main__':
    steps = read_input_file()
    print(part_one(steps))
    print(part_two(steps))
