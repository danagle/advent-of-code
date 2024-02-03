"""
Advent of Code 2018
Day 13: Mine Cart Madness
https://adventofcode.com/2018/day/13
"""
from itertools import cycle


def read_input_file():
    track_turns, carts = {}, {}
    directions = {"<": -1, ">": 1, "^": 1j, "v": -1j}
    for i, line in enumerate(open("input.txt", "r").read().splitlines()):
        for j, tile in enumerate(line):
            position = j - i * 1j
            if tile in r"/\+":
                track_turns[position] = tile
            elif tile in directions:
                carts[position] = directions[tile], cycle([1j, 1, -1j])
    return track_turns, carts


def both_parts(track_turns, carts):
    first_crash, part_one = False, ""
    while len(carts) > 1:
        for position in sorted(carts, key=lambda x: (-x.imag, x.real)):
            if position not in carts:
                continue  # Removed due to crash
            direction, turn = carts.pop(position)  # Take cart
            position += direction  # Update position

            if position in carts:  # Handle crash
                if not first_crash:
                    part_one = f"{int(position.real)},{int(-position.imag)}"
                    first_crash = True
                del carts[position]
                continue

            track_tile = track_turns.get(position)  # Update direction
            if "+" == track_tile:
                direction = direction * next(turn)
            elif track_tile is not None:  # / or \
                direction *= 1j * (2 * ((track_tile == "/") ^ (direction.real == 0)) - 1)

            carts[position] = direction, turn  # Return updated cart

    final_cart_position = tuple(carts.keys())[0]
    part_two = f"{int(final_cart_position.real)},{int(-final_cart_position.imag)}"
    print(f"{part_one=},{part_two=}")


if __name__ == "__main__":
    turns, initial_carts = read_input_file()
    both_parts(turns, initial_carts)
