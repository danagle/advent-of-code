from queue import PriorityQueue


class CrucibleState:
    def __init__(self, cost, position, direction, streak):
        self.cost = cost
        self.position = position
        self.direction = direction
        self.streak = streak
        self.key = (position, direction, streak)

    def __lt__(self, another):
        return (self.cost, self.streak) < (another.cost, another.streak)

    def as_tuple(self):
        return self.cost, self.position, self.direction, self.streak


def read_input_file():
    return {x + y * 1j: int(loss)
            for y, row in enumerate(open('input.txt').read().splitlines())
            for x, loss in enumerate(row)}


def part_one(grid, length, max_streak):
    end_point = (length - 1) + (length - 1) * 1j
    visited = set()  # (position, direction, streak)
    pq = PriorityQueue()  # (cost, position, direction, streak)
    pq.put(CrucibleState(grid[0 + 1j], 1j, 1j, 1))
    pq.put(CrucibleState(grid[1 + 0j], 1, 1, 1))
    while not pq.empty():
        crucible = pq.get()
        if crucible.key in visited:
            continue
        visited.add(crucible.key)
        cost, position, direction, streak = crucible.as_tuple()
        if position == end_point and streak <= max_streak:
            return crucible.cost
        if streak < max_streak and (new_position := position + direction) in grid:
            pq.put(CrucibleState(cost + grid[new_position], new_position, direction, streak + 1))
        for change in (1j, -1):
            direction *= change
            if (new_position := position + direction) in grid:
                pq.put(CrucibleState(cost + grid[new_position], new_position, direction, 1))


def part_two(grid, length, min_streak, max_streak):
    end_point = (length - 1) + (length - 1) * 1j
    visited = set()  # (position, direction, streak)
    pq = PriorityQueue()  # (cost, position, direction, streak)
    pq.put(CrucibleState(grid[0 + 1j], 1j, 1j, 1))
    pq.put(CrucibleState(grid[1 + 0j], 1, 1, 1))
    while not pq.empty():
        crucible = pq.get()
        if crucible.key in visited:
            continue
        visited.add(crucible.key)
        cost, position, direction, streak = crucible.as_tuple()
        if position == end_point and streak <= max_streak:
            return crucible.cost
        if streak < max_streak and (new_position := position + direction) in grid:
            pq.put(CrucibleState(cost + grid[new_position], new_position, direction, streak + 1))
        for change in (1j, -1):
            direction *= change
            if min_streak <= streak and (new_position := position + direction) in grid:
                pq.put(CrucibleState(cost + grid[new_position], new_position, direction, 1))


if __name__ in "__main__":
    from time import time
    from math import sqrt

    heat_loss_grid = read_input_file()
    grid_length = int(sqrt(len(heat_loss_grid)))

    st = time()
    p1 = part_one(heat_loss_grid, grid_length, 3)
    p2 = part_two(heat_loss_grid, grid_length, 4, 10)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    print(f"Execution Time: {time() - st} seconds.")
