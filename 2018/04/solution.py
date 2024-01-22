"""
Advent of Code 2018
Day 4: Repose Record
https://adventofcode.com/2018/day/4
"""
from collections import defaultdict
from math import prod


def read_input_file():
    events = []
    for line in sorted(open("input.txt", "r").read().splitlines()):
        for char in "[]#:":
            line = line.replace(char, " ")
        _, _, m, *event = line.split()
        match event[0]:
            case "Guard":
                guard_id = int(event[1])
            case  "falls":
                asleep = int(m)
            case "wakes":
                events.append((guard_id, asleep, int(m)))
    return events


def analyze_guards_sleep(events):
    guards_sleep = defaultdict(int)
    guard_minute_sleep = defaultdict(int)
    for guard, asleep, awake in events:
        guards_sleep[guard] += awake - asleep
        for minute in range(asleep, awake):
            guard_minute_sleep[(guard, minute)] += 1
    best_guard = max(guards_sleep, key=guards_sleep.get)
    best_guard_keys = list(filter(lambda t: best_guard == t[0], guard_minute_sleep.keys()))
    best_minute, _ = max([(k[1], guard_minute_sleep[k]) for k in best_guard_keys], key=lambda t: t[1])
    return best_guard * best_minute, prod(max(guard_minute_sleep, key=guard_minute_sleep.get))


if __name__ == "__main__":
    data = read_input_file()
    part_one, part_two = analyze_guards_sleep(data)
    print(f"{part_one=}, {part_two=}")
