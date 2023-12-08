
def parse_input_text():
    with open("input.txt", "r") as input_file:
        blocks = [parts.splitlines() for parts in input_file.read().split("\n\n")]
        seeds = [int(i) for i in blocks[0][0].split()[1:]]
        maps = [[[int(i) for i in line.split()]
                 for line in block[1:]]
                for block in blocks[1:]]
    return seeds, maps


def apply_maps_to_tuples(tuples_list, maps_list):
    for category_map in maps_list:
        next_list = []
        for destination, source, category_length in category_map:
            for index, current_tuple in enumerate(tuples_list):
                tuple_start, tuple_length = current_tuple
                # Calculate id values to make if block more readable
                final_source_id = source + category_length
                final_tuple_id = tuple_start + tuple_length
                next_start_id = tuple_start - source + destination
                if source <= tuple_start < final_tuple_id <= final_source_id:
                    # tuple range is inside category range
                    next_list.append((next_start_id, tuple_length))
                    tuples_list[index] = tuples_list[-1]
                    del tuples_list[-1]
                elif source <= tuple_start < final_source_id <= final_tuple_id:
                    # tuple range begins inside source category and extends beyond
                    next_list.append((next_start_id, final_source_id - tuple_start))
                    tuples_list[index] = (final_source_id, final_tuple_id - final_source_id)
                elif tuple_start <= source < final_tuple_id <= final_source_id:
                    # tuple range begins before source category range and ends within
                    next_list.append((destination, final_tuple_id - source))
                    tuples_list[index] = (tuple_start, source - tuple_start)
                elif tuple_start <= source < final_source_id <= final_tuple_id:
                    # tuple range begins before category range and extends beyond
                    next_list.append((destination, category_length))
                    tuples_list[index] = (tuple_start, source - tuple_start)
                    tuples_list.append((final_source_id, final_tuple_id - final_source_id))
        tuples_list += next_list
    return min(start for start, _ in tuples_list)


if __name__ == "__main__":
    import time
    overall_st = time.time()
    seeds_list, maps = parse_input_text()
    st_1 = time.time()
    seeds = [(n, 1) for n in seeds_list]
    location_1 = apply_maps_to_tuples(seeds, maps)
    et_1 = time.time()
    st_2 = time.time()
    seeds = list(zip(*(iter(seeds_list),) * 2))
    location_2 = apply_maps_to_tuples(seeds, maps)
    et_2 = time.time()
    overall_et = time.time()
    print('part_one Execution time:', et_1 - st_1, 'seconds')
    print(f"Location #1: {location_1}")  # 322500873
    print('part_two Execution time:', et_2 - st_2, 'seconds')
    print(f"Location #2 : {location_2}")  # 108956227
    print('Overall Execution time:', overall_et - overall_st, 'seconds')
