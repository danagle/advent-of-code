from itertools import combinations
from operator import methodcaller
from z3 import Int, Ints, Solver


def read_input_file():
    return [tuple(map(int, sum(map(methodcaller("split", ", "),
                                   line.split(" @ ")), [])))
            for line in open("input.txt").read().splitlines()]


def part_one(hail):
    result = 0
    test_area = (200000000000000, 400000000000000)
    for hail_1, hail_2 in combinations(hail, 2):
        px_1, py_1, pz_1, vx_1, vy_1, vz_1 = hail_1
        px_2, py_2, pz_2, vx_2, vy_2, vz_2 = hail_2
        # y = mx + c
        # Slope: m = vy / vx
        m_1 = vy_1 / vx_1
        m_2 = vy_2 / vx_2
        # Intercept: c = y - mx
        c_1 = py_1 - m_1 * px_1
        c_2 = py_2 - m_2 * px_2
        # Find intersections
        # y = ax + b, y = cx + d
        # ax + b = cx + d
        # ax - cx = d - b
        # x(a - c) = d - b
        # x = (d - b) / (a - c)
        # Parallel lines check
        if m_1 == m_2:
            continue
        # Intersection point
        i_x = (c_2 - c_1) / (m_1 - m_2)
        i_y = m_1 * i_x + c_1
        # Ignore if before starting point
        t_1 = (i_x - px_1) / vx_1
        t_2 = (i_x - px_2) / vx_2
        if t_1 < 0 or t_2 < 0:
            continue
        if test_area[0] <= i_x <= test_area[1] and test_area[0] <= i_y <= test_area[1]:
            result += 1
    return result


def part_two(hail):
    f_x, f_y, f_z, f_vx, f_vy, f_vz = Ints("fx fy fz fvx fvy fvz")
    z3_solver = Solver()
    for index, (x, y, z, vx, vy, vz) in enumerate(hail):
        t = Int(f"t{index}")
        z3_solver.add(t >= 0)
        z3_solver.add(x + vx * t == f_x + f_vx * t)
        z3_solver.add(y + vy * t == f_y + f_vy * t)
        z3_solver.add(z + vz * t == f_z + f_vz * t)
    z3_solver.check()
    return z3_solver.model().eval(f_x + f_y + f_z)


if __name__ == "__main__":
    hail_stones = read_input_file()

    p1 = part_one(hail_stones)
    print(f"Part 1: {p1}")
    p2 = part_two(hail_stones)
    print(f"Part 2: {p2}")
