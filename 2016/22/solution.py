"""
Advent of Code 2016
Day 22: Grid Computing
https://adventofcode.com/2016/day/22
Reference: https://en.wikipedia.org/wiki/15_Puzzle
"""
from itertools import product
from re import findall


def read_input_file():
    nodes = [tuple(tuple(map(int, findall(r"(\d+)", line))))
             for line in open("input.txt", "r").read().splitlines()[2:]]
    return {(n[0], n[1]): {"used": n[3], "available": n[4]} for n in nodes}


def part_one(nodes):
    viable_total = 0
    values = list(nodes.values())
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i]["used"] != 0 and values[i]["used"] <= values[j]["available"]:
                viable_total += 1
            if values[j]["used"] != 0 and values[j]["used"] <= values[i]["available"]:
                viable_total += 1
    return viable_total


def find_path_bfs(nodes, start, target, obst=None):
    len_x, len_y = max([_[0] for _ in nodes.keys()]) + 1, max([_[1] for _ in nodes.keys()]) + 1
    cardinal_directions = list(product(range(-1, 2), range(-1, 2)))[1::2]
    for value in nodes.values():
        value["distance"] = float("inf")
        value["previous"] = None
    queue = [start]
    nodes[start]["distance"] = 0
    while len(queue) > 0:
        node = queue.pop(0)
        for x, y in [tuple(sum(x) for x in zip(node, d)) for d in cardinal_directions]:
            if 0 <= x < len_x and 0 <= y < len_y and nodes[(x, y)]["used"] < 100 and (x, y) != obst:
                if nodes[(x, y)]["distance"] > nodes[node]["distance"] + 1:
                    nodes[(x, y)]["distance"] = nodes[node]["distance"] + 1
                    nodes[(x, y)]["previous"] = node
                    queue.append((x, y))
                if target == (x, y):
                    path = [(x, y)]
                    while nodes[path[-1]]["previous"] is not None:
                        path.append(nodes[path[-1]]["previous"])
                    return path[-2::-1]


def part_two(nodes):
    len_x = max([_[0] for _ in nodes.keys()]) + 1
    start, target, empty, count = (0, 0), (len_x - 1, 0), (None, None), 0
    for key in nodes:
        if 0 == nodes[key]["used"]:
            empty = key
            break
    reverse_path = find_path_bfs(nodes, target, start)
    while target != start:
        path_ = find_path_bfs(nodes, empty, reverse_path.pop(0), obst=target)
        count += len(path_) + 1
        empty = target
        target = path_[-1]
    return count


if __name__ == "__main__":
    nodes_data = read_input_file()
    print(part_one(nodes_data))
    print(part_two(nodes_data))
