from itertools import count, product


def read_input_file():
    return [list(line.strip()) for line in open("input.txt")]


def tilt_reflector(mirrors_state):
    num_rows = len(mirrors_state)
    num_cols = len(mirrors_state[0])
    for _ in range(num_rows):
        for col, row in list(product(range(1, num_rows), range(num_cols))):
            if mirrors_state[col][row] == "O" and mirrors_state[col-1][row] == ".":
                mirrors_state[col-1][row], mirrors_state[col][row] = "O", "."
    return mirrors_state


def compute_load(state):
    return sum([line.count('O') * (len(state) - i) for i, line in enumerate(state)])


def part_one(initial_state):
    return compute_load(tilt_reflector(initial_state))


def cycle_state(state):
    new_state = state
    # tilt surface and rotate left : repeat 4 times (N, W, S, E)
    for _ in range(4):
        new_state = [list(reversed(l)) for l in list(zip(*tilt_reflector(new_state)))]
    return new_state


def stringify_state(state):
    return "".join(sum(state, []))


def find_cycle(initial_state):
    cycle_cache = {stringify_state(initial_state): 0}
    state = initial_state
    for iteration in count(1):
        state = cycle_state(state)
        state_string = stringify_state(state)
        if state_string in cycle_cache:
            first_occurrence = cycle_cache[state_string]
            # return the first occurrence in cycle, cycle period length and cycle cache
            return first_occurrence, iteration - first_occurrence, cycle_cache
        cycle_cache[state_string] = iteration


def part_two(initial_state, cycles):
    # find the period of the rotation cycle
    first, period, cache = find_cycle(initial_state)
    # swap keys and values of cache to create a lookup
    lookup = {first_occurrence: state_string for state_string, first_occurrence in cache.items()}
    # use the cycle period to find the state
    state_string = lookup[(first + (cycles - first) % period)]
    # return the state to a usable format
    state = list(zip(*[iter(state_string)] * len(initial_state[0])))
    return compute_load(state)


if __name__ == "__main__":
    from time import time

    reflector_state = read_input_file()

    p1 = part_one(reflector_state)
    print(f"part_one: {p1}")
    st = time()
    p2 = part_two(reflector_state, cycles=1_000_000_000)
    print(f"part_two: {p2}")
    print(f"Execution Time: {time() - st} seconds.")
