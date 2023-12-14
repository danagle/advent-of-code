
def read_input_file():
    return tuple("".join(line) for line in zip(*open("input.txt").read().splitlines()))


def compute_load(state):
    return sum(sum(index * (ch == "O") for index, ch in enumerate(line[::-1], 1)) for line in state)


def tilt_reflector(state):
    return tuple("#".join("O" * s.count("O") + "." * s.count(".") for s in line.split("#")) for line in state)


def part_one(initial_state):
    return compute_load(tilt_reflector(initial_state))


def rotate_reflector(state):
    return tuple("".join(line) for line in zip(*state))[::-1]


def cycle_state(state):
    for _ in range(4):
        state = rotate_reflector(tilt_reflector(state))
    return state


def find_cycle(initial_state):
    cycle_cache, counter = {}, 0
    state = initial_state
    while state not in cycle_cache.keys():
        cycle_cache[state] = counter
        state = cycle_state(state)
        counter += 1
    return cycle_cache[state], counter - cycle_cache[state], cycle_cache


def part_two(initial_state, num_cycles):
    # find the period of the rotation cycle
    first, period, cache = find_cycle(initial_state)
    # swap keys and values of cache to create a lookup
    lookup = {first_occurrence: state_string for state_string, first_occurrence in cache.items()}
    # use the cycle period to find the future state
    return compute_load(lookup[(first + (num_cycles - first) % period)])


if __name__ == "__main__":
    from statistics import median
    from time import time

    reflector_state = read_input_file()

    p1 = part_one(reflector_state)
    print(f"part_one: {p1}")  # 108935
    et = []
    for _ in range(10):
        st = time()
        p2 = part_two(reflector_state, 1_000_000_000)
        et.append(time() - st)
    print(f"part_two: {p2}")  # 100876
    print(f"Median Execution Time: {median(et)} seconds.")
