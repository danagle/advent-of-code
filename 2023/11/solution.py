from itertools import combinations


def read_input_file():
    return [(row, col) for row, line in enumerate(open('input.txt'))
            for col, ch in enumerate(line) if ch == '#']


def expand_dimension(dimension_index, expansion_size):
    expanded_list = []
    limit = max(dimension_index) + 1
    expansion_distance = 0
    for i in range(limit):
        if i not in dimension_index:
            expansion_distance += expansion_size - 1
        expanded_list.append(i + expansion_distance)
    return expanded_list


def sum_of_distances(galaxies_list, expansion_size):
    expanded_rows = expand_dimension(set([row for row, _ in galaxies_list]),
                                     expansion_size)
    expanded_cols = expand_dimension(set([col for _, col in galaxies_list]),
                                     expansion_size)
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1])
               for a, b in combinations([(expanded_rows[row], expanded_cols[col])
                                         for row, col in galaxies_list], 2))


if __name__ == "__main__":
    galaxies = read_input_file()
    for expansion in (2, 1_000_000):
        print(f"Expansion size: {expansion}. Sum of distances: {sum_of_distances(galaxies, expansion)}")
