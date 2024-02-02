"""
Advent of Code 2018
Day 9: Marble Mania
https://adventofcode.com/2018/day/9
"""
from collections import defaultdict, deque
from re import findall


def read_input_file():
    return tuple(map(int, findall(r"\d+", open("input.txt", "r").read())))


def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


if __name__ == "__main__":
    players, last_value = read_input_file()
    print(play_game(players, last_value))
    print(play_game(players, last_value * 100))
