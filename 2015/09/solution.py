"""
Advent of Code 2015
Day 9: All in a Single Night
https://adventofcode.com/2015/day/9
"""
from collections import defaultdict
from sys import maxsize


def read_input_file():
    distances = defaultdict(list)
    for line in open("input.txt", "r").read().splitlines():
        origin, _, destination, _, distance = line.split(" ")
        distances[origin].append((destination, int(distance)))
        distances[destination].append((origin, int(distance)))
    return distances


def routes_dfs(start, graph):
    longest, shortest, visited = 0, maxsize, set()

    def dfs(place, distance):
        nonlocal longest, shortest, visited
        visited.add(place)
        if len(visited) == len(graph):
            if distance < shortest:
                shortest = distance
            if distance > longest:
                longest = distance
        else:
            for destination, leg_distance in graph[place]:
                if destination not in visited:
                    dfs(destination, distance + leg_distance)
        visited.remove(place)

    dfs(start, 0)
    return shortest, longest


def shortest_and_longest_distances(cities):
    shortest_distance, longest_distance = maxsize, 0
    for city in cities:
        a, b = routes_dfs(city, cities)
        if a < shortest_distance:
            shortest_distance = a
        if b > longest_distance:
            longest_distance = b
    return shortest_distance, longest_distance


if __name__ == "__main__":
    data = read_input_file()
    part_one, part_two = shortest_and_longest_distances(data)
    print(f"{part_one=}, {part_two=}")
