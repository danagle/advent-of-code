"""
Advent of Code 2016
Day 24: Air Duct Spelunking
https://adventofcode.com/2016/day/24
"""
from collections import defaultdict, deque
from itertools import combinations, permutations


def read_input_data():
    return open("input.txt", "r").read().splitlines()


def find_numbers_in_map(tiles):
    return {int(tiles[i][j]): (i, j) for i in range(len(tiles)) for j in range(len(tiles[i])) if tiles[i][j].isdigit()}


def navigate_hvac_system(map_tiles):
    cardinal_moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
    way_points = find_numbers_in_map(map_tiles)
    shortest_paths = defaultdict(int)

    def bfs_from_a_to_b(start, end):
        nonlocal cardinal_moves, map_tiles
        q = deque([(0, start)])
        visited = set([start])
        while q:
            distance, current = q.pop()
            if current == end:
                return distance
            y, x = current
            for cardinal_y, cardinal_x in cardinal_moves:
                next_y, next_x = y + cardinal_y, x + cardinal_x
                if map_tiles[next_y][next_x] != "#" and (next_y, next_x) not in visited:
                    q.appendleft((distance + 1, (next_y, next_x)))
                    visited.add((next_y, next_x))
        return -1

    for a, b in combinations(sorted(way_points), 2):
        visited_nodes = bfs_from_a_to_b(way_points[a], way_points[b])
        shortest_paths[(a, b)] = visited_nodes
        shortest_paths[(b, a)] = visited_nodes

    path_distances = []
    for permutation in permutations(way_points):
        points = [(permutation[i], permutation[i + 1]) for i in range(len(permutation) - 1)]
        path_distance = sum([shortest_paths[p] for p in points])
        path_distances.append((path_distance, path_distance + shortest_paths[(permutation[-1], permutation[0])]))
    part_one, _ = min(path_distances, key=lambda x: x[0])
    _, part_two = min(path_distances, key=lambda x: x[1])
    print(f"{part_one=}, {part_two=}")


if __name__ == "__main__":
    tiles = read_input_data()
    navigate_hvac_system(tiles)
