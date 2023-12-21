from collections import defaultdict, deque
from math import sqrt


def read_input_data():
    garden_tiles = dict()
    start_point = None
    for y, row in enumerate(open('input.txt').read().splitlines()):
        for x, tile in enumerate(row):
            garden_tiles[x + y * 1j] = tile
            if "S" == tile:
                start_point = x + y * 1j
                garden_tiles[start_point] = "."
    return garden_tiles, start_point


def original_get_number_visited_tiles(tiles, start, steps):
    adjacent_offsets = [1+0j, 0+1j, 0-1j, -1+0j]
    visited_positions = defaultdict(set)
    visited_positions[0].add(start)
    for step_number in range(steps):
        for position in visited_positions[step_number]:
            for offset in adjacent_offsets:
                next_position = position + offset
                if tiles.get(next_position, None) == ".":
                    visited_positions[step_number + 1].add(next_position)
    return len(visited_positions.get(steps))


def get_number_visited_tiles(garden, start, steps):
    adjacent_offsets = (1+0j, 0+1j, 0-1j, -1+0j)
    result = []
    visited = {start}
    queue = deque([(start, steps)])
    while queue:
        position, steps = queue.popleft()
        if steps % 2 == 0:
            result.append(position)
        if steps == 0:
            continue
        for next_position in [position + offset for offset in adjacent_offsets]:
            if next_position in visited or next_position not in garden or garden[next_position] == "#":
                continue
            visited.add(next_position)
            queue.append((next_position, steps - 1))
    return len(result)


def part_one(tiles, start):
    return get_number_visited_tiles(tiles, start, steps=64)


def part_two(garden_tiles, start):
    steps = 26501365
    garden_size = int(sqrt(len(garden_tiles)))
    grid_size = steps // garden_size  # 202300
    # There are two types of garden to traverse in the infinite grid
    # Odd gardens
    odd_gardens = ((grid_size - 1) // 2 * 2 + 1) ** 2  # 40924885401
    odd_positions = get_number_visited_tiles(garden_tiles, start, (garden_size * 2 + 1))  # 7719
    odd_total = odd_gardens * odd_positions
    # Even gardens
    even_gardens = (grid_size // 2 * 2) ** 2  # 40925290000
    even_positions = get_number_visited_tiles(garden_tiles, start, (garden_size * 2))  # 7734
    even_total = even_gardens * even_positions
    # Outside the filled gardens there are partially filled gardens that make up the edges of the diamond
    # Gardens at tips of the diamond
    tip_fill_steps = garden_size - 1
    top_tip = get_number_visited_tiles(garden_tiles, tip_fill_steps + start.imag * 1j, tip_fill_steps)
    bottom_tip = get_number_visited_tiles(garden_tiles, 0 + start.imag * 1j, tip_fill_steps)
    left_tip = get_number_visited_tiles(garden_tiles, start.real + tip_fill_steps * 1j, tip_fill_steps)
    right_tip = get_number_visited_tiles(garden_tiles, start.real + 0j, tip_fill_steps)
    tips_fill_total = top_tip + bottom_tip + left_tip + right_tip
    # Diagonal start points
    tl, tr, bl, br = (garden_size - 1) + (garden_size - 1) * 1j, (garden_size - 1) + 0j, 0 + (garden_size - 1) * 1j, 0+0j
    # Diagonal edges with small fill gardens
    small_fill_steps = garden_size // 2 - 1
    top_left_small = get_number_visited_tiles(garden_tiles, tl, small_fill_steps)
    top_right_small = get_number_visited_tiles(garden_tiles, tr, small_fill_steps)
    bottom_left_small = get_number_visited_tiles(garden_tiles, bl, small_fill_steps)
    bottom_right_small = get_number_visited_tiles(garden_tiles, br, small_fill_steps)
    small_fills_total = grid_size * (top_left_small + top_right_small + bottom_left_small + bottom_right_small)
    # Diagonal edges with large fill gardens
    large_fill_steps = (garden_size * 3) // 2 - 1
    top_left_large = get_number_visited_tiles(garden_tiles, tl, large_fill_steps)
    top_right_large = get_number_visited_tiles(garden_tiles, tr, large_fill_steps)
    bottom_left_large = get_number_visited_tiles(garden_tiles, bl, large_fill_steps)
    bottom_right_large = get_number_visited_tiles(garden_tiles, br, large_fill_steps)
    large_fills_total = (grid_size - 1) * (top_left_large + top_right_large + bottom_left_large + bottom_right_large)
    # Calculate total
    return odd_total + even_total + tips_fill_total + small_fills_total + large_fills_total


if __name__ == '__main__':
    from time import time
    garden_map, start_position = read_input_data()
    st = time()
    p1 = part_one(garden_map, start_position)
    p2 = part_two(garden_map, start_position)
    print(f"Executuion time: {(time() - st) * 1000} milliseconds")
    print(f"Part 1: {p1} locations")
    print(f"Part 2: {p2} locations")
