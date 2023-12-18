def read_input_file():
    return [tuple(line.split()) for line in open('input.txt').read().splitlines()]


def shoelace_theorem(tuples_list):
    """
    Apply Shoelace Theorem to list of dig plan instructions.
    Info: https://artofproblemsolving.com/wiki/index.php/Shoelace_Theorem
    """
    position = 0 + 0j
    area_a, area_b, total_distance = 0, 0, 0
    for direction, distance in tuples_list:
        match direction:
            case 0:
                new_position = position + (1j * distance)
            case 1:
                new_position = position + distance
            case 2:
                new_position = position - (1j * distance)
            case 3:
                new_position = position - distance
        area_a += position.real * new_position.imag
        area_b += position.imag * new_position.real
        total_distance += distance
        position = new_position
    return int((abs(area_a - area_b) / 2) + (total_distance / 2) + 1)


def part_one(plan):
    # Parse the plan : (direction, distance)
    instructions = [("RDLU".index(direction), int(distance)) for direction, distance, _ in plan]
    return shoelace_theorem(instructions)


def part_two(plan):
    # Parse the plan : (direction, distance)
    instructions = [(int(hex_string[-2]), int(hex_string[2:-2], base=16)) for _, _, hex_string in plan]
    return shoelace_theorem(instructions)


if __name__ == "__main__":
    from time import time

    dig_plan = read_input_file()

    st = time()
    p1 = part_one(dig_plan)
    p2 = part_two(dig_plan)
    print(f"Execution Time: {time() - st} seconds.")
    print(f"part_one: {p1}")
    print(f"part_two: {p2}")
