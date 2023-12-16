def read_input_data():
    return {x + y * 1j: tile
            for y, row in enumerate(open('input.txt').read().splitlines())
            for x, tile in enumerate(row)}


def count_energized(floor, beam_path):
    energized = set()
    while beam_path:
        position, direction = beam_path.pop()
        while not (position, direction) in energized:
            energized.add((position, direction))
            position += direction
            match floor.get(position):
                case "/":
                    direction = (direction * 1j).conjugate()
                case "\\":
                    direction = (direction * -1j).conjugate()
                case "-":
                    direction = 1; beam_path.add((position, -1))
                case "|":
                    direction = 1j; beam_path.add((position, -1j))
                case None:
                    break
    return len(set(position for position, _ in energized)) - 1


def part_one(floor):
    return count_energized(floor, {(-1, 1)})


def part_two(floor):
    return max([count_energized(floor, {(position - direction, direction)}) for position in floor
                for direction in (1, -1, 1j, -1j) if position - direction not in floor])


if __name__ == "__main__":
    from time import time

    floor_space = read_input_data()

    st = time()
    print(f"Part 1: {part_one(floor_space)}")  # 7111
    print(f"Part 2: {part_two(floor_space)}")  # 7831
    print(f"Execution time: {time() - st} seconds.")
