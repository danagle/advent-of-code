"""
Advent of Code 2017
Day 22: Sporifica Virus
https://adventofcode.com/2017/day/22
"""
from collections import defaultdict


def read_input_file():
    infected_text = open("input.txt", "r").read().splitlines()
    middle = len(infected_text) // 2
    infected = [(row - middle, column - middle) for row, line in enumerate(infected_text)
                for column, char in enumerate(line) if char == "#"]
    return set(infected)


def part_one(infected_nodes):
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
    direction = infections = 0
    carrier = (0, 0)
    for _ in range(10_000):
        if carrier in infected_nodes:
            direction = (direction - 1) % 4
            infected_nodes.remove(carrier)
        else:
            direction = (direction + 1) % 4
            infected_nodes.add(carrier)
            infections += 1
        carrier = (carrier[0] + directions[direction][0], carrier[1] + directions[direction][1])
    return infections


def part_two(initial_infected):
    directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
    direction = infections = 0
    carrier = (0, 0)
    nodes_state = defaultdict(int) | {offset: 2 for offset in initial_infected}
    for _ in range(10_000_000):
        current_state = nodes_state[carrier]
        match current_state:
            case 0:  # Clean
                direction = (direction + 1) % 4  # Turn left
            case 1:  # Weakened
                infections += 1
            case 2:  # Infected
                direction = (direction - 1) % 4  # Turn right
            case 3:  # Flagged
                direction = (direction + 2) % 4  # Reverse direction
        nodes_state[carrier] = (current_state + 1) % 4  # Cycle state
        carrier = (carrier[0] + directions[direction][0], carrier[1] + directions[direction][1])
    return infections


if __name__ == "__main__":
    initial = read_input_file()
    print(part_one(initial.copy()))
    print(part_two(initial))
