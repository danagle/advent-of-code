
def read_input_file():
    start_position = None
    lines = [line.strip() for line in open("input.txt", "r")]
    # Add a border to simplify calculations
    empty_border = "." * (len(lines[0]) + 2)
    pipe_tiles = [empty_border]
    for line in lines:
        pipe_tiles.append("." + line + ".")
    pipe_tiles.append(empty_border)
    # Find the start position
    for row, line in enumerate(pipe_tiles):
        if "S" in line:
            start_position = (row, line.index("S"))
            break
    return pipe_tiles, start_position


def both_parts(pipes, start_point):
    direction_move = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }
    direction_change = {
        "N": {"|": "N", "7": "W", "F": "E"},
        "E": {"-": "E", "7": "S", "J": "N"},
        "S": {"|": "S", "L": "E", "J": "W"},
        "W": {"-": "W", "L": "N", "F": "S"}
    }
    moves_count = 1
    area_covered = 0
    current_position = start_point
    # Determine starting direction
    for direction in direction_change:
        cy, cx = current_position
        dy, dx = direction_move[direction]
        if pipes[cy + dy][cx + dx] in direction_change[direction]:
            current_direction = direction
    # Walk the path
    while current_position != start_point or moves_count == 1:
        cy, cx = current_position
        dy, dx = direction_move[current_direction]
        area_covered += cx*dy
        new_x = cx + dx
        new_y = cy + dy
        # Exit when the start point is encountered
        if pipes[new_y][new_x] == "S" and moves_count > 1:
            break
        current_position = (new_y, new_x)
        current_direction = direction_change[current_direction][pipes[new_y][new_x]]
        moves_count += 1
    # Furthest point is half the length of the path : moves_count // 2
    # Area inside the polygon is calculated using Green's Theorem : area_covered - (moves_count // 2) + 1
    return (moves_count // 2), (area_covered - (moves_count // 2) + 1)


if __name__ == "__main__":
    pipes_map, starting_position = read_input_file()
    furthest_point, tiles_enclosed = both_parts(pipes_map, starting_position)
    print(f"part_one: {furthest_point}")
    print(f"part_two: {tiles_enclosed}")
