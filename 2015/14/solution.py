"""
Advent of Code 2015
Day 14: Reindeer Olympics
https://adventofcode.com/2015/day/14
"""
from collections import defaultdict


def read_input_file():
    reindeer = defaultdict(dict)
    lines = open("input.txt", "r").read().splitlines()
    for line in lines:
        tokens = line.split(" ")
        name = tokens[0]
        reindeer[name]["speed"] = int(tokens[3])
        reindeer[name]["fly_time"] = int(tokens[6])
        reindeer[name]["rest_time"] = int(tokens[-2])
    return reindeer


def part_one(reindeer):
    race_time = 2503
    for name in reindeer:
        cycle_time = reindeer[name]["fly_time"] + reindeer[name]["rest_time"]
        cycles = race_time // cycle_time
        remaining_time = race_time % cycle_time
        additional_fly_time = 0
        if remaining_time > 0:
            if remaining_time <= reindeer[name]["fly_time"]:
                additional_fly_time = remaining_time
            else:
                additional_fly_time = reindeer[name]["fly_time"]
        reindeer[name]["distance"] = ((cycles * reindeer[name]["fly_time"]) + additional_fly_time) * reindeer[name]["speed"]
    return max(reindeer[r]["distance"] for r in reindeer)


def part_two(reindeer):
    race_time = 2503
    # Add additional state tracking
    for name in reindeer:
        reindeer[name]["distance"] = 0
        reindeer[name]["points"] = 0
        reindeer[name]["flying"] = True
        reindeer[name]["timer"] = reindeer[name]["fly_time"]
    # Simulate the race
    for t in range(race_time):
        for name in reindeer:
            # Toggle the flying state when timer reaches 0 and re-initialise the timer
            if 0 == reindeer[name]["timer"]:
                reindeer[name]["flying"] = not reindeer[name]["flying"]
                if reindeer[name]["flying"]:
                    reindeer[name]["timer"] = reindeer[name]["fly_time"]
                else:
                    reindeer[name]["timer"] = reindeer[name]["rest_time"]
            # Advance the flying reindeer
            if reindeer[name]["flying"]:
                reindeer[name]["distance"] += reindeer[name]["speed"]
            # Decrement the timer
            reindeer[name]["timer"] -= 1
        # Identify the current leader
        leader_distance = 0
        leader_name = None
        for name in reindeer:
            if leader_distance < reindeer[name]["distance"]:
                leader_name = name
                leader_distance = reindeer[leader_name]["distance"]
        reindeer[leader_name]["points"] += 1
    return max(reindeer[name]["points"] for name in reindeer)


if __name__ == "__main__":
    reindeer_performance = read_input_file()
    print(part_one(reindeer_performance))
    print(part_two(reindeer_performance))
