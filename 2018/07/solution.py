"""
Advent of Code 2018
Day 7: The Sum of Its Parts
https://adventofcode.com/2018/day/7
"""
import networkx as nx


def read_input_file():
    assembly_steps = []
    for line in open("input.txt", "r").read().splitlines():
        tokens = line.split(" ")
        assembly_steps.append((tokens[1], tokens[7]))
    return assembly_steps


def both_parts(graph_data):
    graph = nx.DiGraph()
    task_times, tasks, time_taken = [], [], 0

    for tokens in graph_data:
        graph.add_edge(*tokens)
    order = "".join(nx.lexicographical_topological_sort(graph))

    while task_times or graph:
        available_tasks = [t for t in graph if t not in tasks and graph.in_degree(t) == 0]
        if available_tasks and len(task_times) < 5:
            task = min(available_tasks)  # Get the smallest task alphabetically
            task_times.append(ord(task) - 4)
            tasks.append(task)
        else:
            min_time = min(task_times)
            completed = [tasks[i] for i, v in enumerate(task_times) if v == min_time]
            task_times = [v - min_time for v in task_times if v > min_time]
            tasks = [t for t in tasks if t not in completed]
            time_taken += min_time
            graph.remove_nodes_from(completed)

    return order, time_taken


if __name__ == "__main__":
    steps = read_input_file()
    part_one, part_two = both_parts(steps)
    print(f"{part_one=}, {part_two=}")
