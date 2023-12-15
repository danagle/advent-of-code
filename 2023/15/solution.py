
def read_input_file():
    return tuple(open("input.txt").read().strip().split(","))


def get_hash_value(step):
    value = 0
    for ch in step:
        value = ((value + ord(ch)) * 17) % 256
    return value


def part_one(sequence):
    return sum(map(get_hash_value, sequence))


def box_lenses(equations_list):
    lens_boxes = [dict() for _ in range(256)]
    for equation in equations_list:
        if "-" == equation[-1]:
            label = equation[:-1]
            lens_boxes[get_hash_value(label)].pop(label, None)
        else:
            label, focal_length = equation.split("=")
            lens_boxes[get_hash_value(label)][label] = int(focal_length)
    return lens_boxes


def part_two(sequence):
    boxes = box_lenses(sequence)
    total = 0
    for box_number, box in enumerate(boxes, start=1):
        slot_number = 1
        for _, focal_length in box.items():
            total += box_number * slot_number * focal_length
            slot_number += 1
    return total


if __name__ == "__main__":
    sequences = read_input_file()
    print(part_one(sequences))  # 506437
    print(part_two(sequences))  # 288521
