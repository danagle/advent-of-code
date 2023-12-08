import re
from math import ceil, floor, prod, sqrt
from scipy.optimize import fsolve


def parse_input_part_one():
    with open("input.txt", "r") as input_file:
        return list(zip(*[[int(n) for n in re.findall(r'\d+', line)]
                          for line in input_file.read().splitlines()]))


def parse_input_part_two():
    with open("input.txt", "r") as input_file:
        return tuple([int(''.join([n for n in re.findall(r'\d+', line)]))
                      for line in input_file.read().splitlines()])


def part_one_brute(data):
    results = [len([charging for charging in range(race_time, 1, -1)
                    if (charging * (race_time-charging)) > record])
               for (race_time, record) in data]
    print(f"part_one_brute: {prod(results)}")


def part_two_brute(race_time, distance):
    results = [charging for charging in range(race_time)
               if (charging * (race_time-charging)) > distance]
    print(f"part_two_brute: {len(results)}")


def solve_quadratic_equation(a, b, c):
    # distance = (race_time - charging_time) * charging_time
    # 0 = -1*(charging_time**2) + (race_time * charging_time) - distance
    # solve equation to get charging_time solutions
    d = (b ** 2) - (4 * a * c)
    root_1 = (-b - sqrt(d)) / (2 * a)
    root_2 = (-b + sqrt(d)) / (2 * a)
    solutions = sorted([root_1, root_2])
    return ceil(solutions[0]), floor(solutions[1])


def part_one_quadratic(data):
    result = prod([len(range(a, b+1))
                   for a, b in [solve_quadratic_equation(-1, race_time, -distance)
                                for race_time, distance in data]])
    print(f"part_one_quadratic: {result}")


def part_two_quadratic(race_time, distance):
    a, b = solve_quadratic_equation(-1, race_time, -distance)
    print(f"part_two_quadratic: {b+1 - a}")


def part_two_descriminant(race_time, distance):
    print(f"part_two_descriminant: {floor(sqrt(race_time ** 2 - 4 * distance))}")


def part_two_scipy(race_time, distance):
    roots = fsolve(lambda x: x * race_time - x ** 2 - distance, x0=[0, distance])
    print(f"part_two_scipy: {floor(roots[1]) - ceil(roots[0]) + 1}")


if __name__ == "__main__":
    import time
    functions_one = (part_one_brute, part_one_quadratic)
    functions_two = (part_two_brute, part_two_quadratic, part_two_descriminant, part_two_scipy)
    data = parse_input_part_one()
    race_time, distance = parse_input_part_two()
    print(race_time, distance)
    timings = []
    for fn in functions_one:
        st_1 = time.time()
        fn(data)
        et_1 = time.time()
        timings.append((fn.__name__, et_1-st_1))
    for fn in functions_two:
        st_2 = time.time()
        fn(race_time, distance)
        et_2 = time.time()
        timings.append((fn.__name__, et_2 - st_2))
    results = sorted(timings, key=lambda x: x[1])

    print("\nTiming Data:\n")
    for name, timing in results:
        print(f"{name} Execution time: {timing} seconds")
