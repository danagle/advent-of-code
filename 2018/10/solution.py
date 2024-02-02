"""
Advent of Code 2018
Day 10: The Stars Align
https://adventofcode.com/2018/day/10
"""
from re import findall


def read_input_file():
    return [list(map(int, findall(r"-?\d+", line))) for line in open("input.txt", "r").read().splitlines()]


def fast_forward_lights(lights_data):
    for time_tick in range(20_000):
        min_x, max_x, min_y, max_y = 10_000, 0, 10_000, 0
        for x, y, vx, vy in lights_data:
            min_x = min(min_x, x + time_tick * vx)
            max_x = max(max_x, x + time_tick * vx)
            min_y = min(min_y, y + time_tick * vy)
            max_y = max(max_y, y + time_tick * vy)
        # Assumption : The message area will be small enough to fit in a terminal window
        if (max_x - min_x) < 80 and (max_y - min_y) < 12:
            break
    # Create a blank canvas
    canvas = [[" "] * (max_x - min_x + 1) for _ in range(min_y, max_y + 1)]
    # Add the light points
    for (x, y, vx, vy) in lights_data:
        canvas[y + (time_tick * vy) - min_y][x + (time_tick * vx) - min_x] = "#"
    # Display the message
    for row in canvas:
        print("".join(row))
    # Part 2
    print("\nPart 2:", time_tick)


if __name__ == "__main__":
    data = read_input_file()
    fast_forward_lights(data)
