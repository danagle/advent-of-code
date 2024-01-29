"""
Advent of Code 2016
Day 13: A Maze of Twisty Little Cubicles
https://adventofcode.com/2016/day/13
"""


def read_input_file():
    favorite_number = int(open("input.txt", "r").read().strip())

    def get_maze_path(location):
        nonlocal favorite_number
        x, y = location
        number = x*x + 3*x + 2*x*y + y + y*y + favorite_number
        return bin(number).count("1") % 2 == 0 and x >= 0 and y >= 0

    def get_next_location(location, steps):
        cardinal_moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
        candidate_locations = [tuple(sum(t) for t in zip(location, move)) for move in cardinal_moves]
        return [(candidate, steps+1) for candidate in candidate_locations if get_maze_path(candidate)]

    return get_next_location


def wander_the_maze(next_location):
    start, target = (1, 1), (31, 39)
    visited = dict()
    queue = [(start, 0)]
    while queue:
        location, steps = queue.pop()
        visited[location] = steps
        queue += [t for t in next_location(location, steps) if not t[0] in visited or visited[t[0]] > t[1]]
    return visited[target], len([visited[location] for location in visited.keys() if visited[location] <= 50])


if __name__ == "__main__":
    data_generator = read_input_file()
    part_one, part_two = wander_the_maze(data_generator)
    print(f"{part_one=}, {part_two=}")
