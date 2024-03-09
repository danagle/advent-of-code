"""
Advent of Code 2019
Day 8: Space Image Format
https://adventofcode.com/2019/day/8
"""
from collections import Counter


def read_input_file():
    return list(map(int, open("input.txt", "r").read().strip()))


def part_one(data):
    layer_size = 25 * 6
    # Count values in each layer
    layers = [Counter(data[i:i+layer_size]) for i in range(0, len(data), layer_size)]
    # Sort layers to find the layer that contains the fewest 0 digits
    layers.sort(key=lambda x: x[0])
    # Print the number of 1 digits multiplied by the number of 2 digits
    print(f"part_one: {layers[0][1] * layers[0][2]}")


def part_two(data):
    layer_size = 25 * 6
    # Initialise image with transparent pixel values
    image = [2 for _ in range(layer_size)]
    # Iterate through layers
    for i in range(0, len(data), layer_size):
        layer = data[i:i+layer_size]
        for j in range(len(layer)):
            # Only replace transparent pixel values in image
            if image[j] == 2:
                image[j] = layer[j]
    # Display decoded image
    for k in range(0, len(image), 25):
        print("".join("#" if _ == 1 else " " for _ in image[k:k+25]))


if __name__ == "__main__":
    space_image_format_data = read_input_file()
    part_one(space_image_format_data)
    part_two(space_image_format_data)
