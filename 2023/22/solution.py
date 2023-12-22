from operator import methodcaller


def read_input_file():
    ordered_bricks = dict()
    sand_bricks = []
    for line in open("input.txt").read().splitlines():
        brick = tuple(map(int, sum(map(methodcaller("split", ","), line.split("~")), [])))
        sand_bricks.append(brick)
    for index, brick_tuple in enumerate(sorted(sand_bricks, key=lambda b: b[2])):
        ordered_bricks[index] = brick_tuple
    return ordered_bricks


def drop_bricks(bricks):
    bricks_above = {index: [] for index in bricks}
    bricks_below = {index: [] for index in bricks}
    settled_positions = {}
    # Brick must fall until there is support found
    for brick_id in bricks:
        x_1, y_1, z_1, x_2, y_2, z_2 = bricks[brick_id]
        support_positions = []
        while z_1 > 1 and len(support_positions) == 0:
            for x in range(x_1, x_2 + 1):
                for y in range(y_1, y_2 + 1):
                    for z in range(z_1, z_2 + 1):
                        if (x, y, z - 1) in settled_positions:
                            support_positions.append((x, y, z - 1))
            # Keep falling if there is no support below
            if len(support_positions) == 0:
                z_1 -= 1
                z_2 -= 1
        # Record the settled position of the brick
        for x in range(x_1, x_2 + 1):
            for y in range(y_1, y_2 + 1):
                for z in range(z_1, z_2+1):
                    settled_positions[(x, y, z)] = brick_id
        # Update the state
        for support_id in set(settled_positions[position] for position in support_positions):
            bricks_above[support_id].append(brick_id)
            bricks_below[brick_id].append(support_id)

    return bricks_above, bricks_below


def part_one(bricks_above, bricks_below):
    total = 0
    for brick_id in bricks_above:
        can_remove = True
        for above_id in bricks_above[brick_id]:
            # Brick can't be removed if it's the only support for bricks above
            if len(bricks_below[above_id]) == 1:
                can_remove = False
                break
        if can_remove:
            total += 1
    return total


def part_two(bricks_above, bricks_below):
    total = 0
    for brick_id in bricks_above:
        check_list = bricks_above[brick_id].copy()
        falling_bricks = {brick_id}
        while check_list and (check_id := check_list.pop()):
            if all(below_id in falling_bricks for below_id in bricks_below[check_id]):
                falling_bricks.add(check_id)
                check_list += bricks_above[check_id]
        total += len(falling_bricks) - 1
    return total


if __name__ == "__main__":
    from time import time

    bricks_dict = read_input_file()
    above, below = drop_bricks(bricks_dict)

    st = time()
    p1 = part_one(above, below)
    p2 = part_two(above, below)
    print(f"Execution Time: {(time() - st) * 1000} milliseconds.")
    print(f"Part One: {p1} bricks can be removed.")
    print(f"Part Two: {p2} other bricks would fall.")
