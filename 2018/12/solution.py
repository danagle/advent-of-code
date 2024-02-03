"""
Advent of Code 2018
Day 12: Subterranean Sustainability
https://adventofcode.com/2018/day/12
"""


def read_input_file():
    lines = open("input.txt", "r").read().splitlines()
    initial_state = [1 if _ == "#" else 0 for _ in lines[0].split()[-1]]
    rules = {}
    for line in lines[2:]:
        line = line.split()
        k = tuple([1 if _ == "#" else 0 for _ in line[0]])
        rules[k] = 1 if line[-1] == "#" else 0
    return initial_state, rules


def plant_pots_state(state, rules, generations):
    pad, offset = 10, -10
    state = [0] * pad + list(state) + [0] * pad

    for i in range(1, generations + 1):
        next_state = list(state)
        for j in range(0, len(state) - 5):
            k = tuple(state[j:j+5])
            next_state[j+2] = rules.get(k, 0)
        state = next_state

        # Trim state
        if not any(state[:2*pad]):
            state = state[pad:]
            offset += pad

        if any(state[-pad:]):
            state += [0] * pad

    return state, offset


def part_one(state, rules):
    state, offset = plant_pots_state(state, rules, 20)
    return sum(_[1] for _ in zip(state, range(offset, offset + len(state))) if _[0])


def part_two(state, rules):
    state, offset = plant_pots_state(state, rules, 1000)
    # Pattern begins moving one step to the right per generation
    generations_target = 50_000_000_000
    offset = offset + generations_target - 1000
    return sum(_[1] for _ in zip(state, range(offset, offset + len(state))) if _[0])


if __name__ == "__main__":
    data = read_input_file()
    print(part_one(*data))
    print(part_two(*data))
