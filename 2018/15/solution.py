"""
Advent of Code 2018
Day 15: Beverage Bandits
https://adventofcode.com/2018/day/15
"""
from collections import deque
from dataclasses import dataclass
from itertools import count


def neighbors(position):
    return [tuple(sum(t) for t in zip(position, offset)) for offset in ((0, 1), (1, 0), (0, -1), (-1, 0))]


@dataclass
class Unit:
    position: (int, int)
    isElf: bool
    attack: int
    health: int = 200
    isAlive: bool = True


class ElfHasDied(Exception):
    pass


class Battle(dict):
    def __init__(self, arena_map, elf_attack=3):
        super().__init__()

        self.units = []

        for row, line in enumerate(arena_map):
            for col, ch in enumerate(line):
                # Mark walls of cavern
                self[(row, col)] = ch == "#"
                # Add combat units
                if ch in "EG":
                    self.units.append(Unit((row, col), (ch == "E"), {"E": elf_attack, "G": 3}[ch]))

    def combat(self, no_elf_dies=False):
        for rounds in count(start=0):
            if self.round(no_elf_dies=no_elf_dies):
                # The number of full rounds that were completed multiplied by
                # the sum of the hit points of all remaining units at the moment combat ends
                return rounds * sum(unit.health for unit in self.units if unit.isAlive)

    def round(self, no_elf_dies=False):
        for unit in sorted(self.units, key=lambda u: u.position):
            if unit.isAlive and self.unit_move(unit, no_elf_dies=no_elf_dies):
                return True

    def unit_move(self, unit, no_elf_dies=False):
        # Combat only ends when a unit finds no targets during its turn.
        if not (enemies := [target for target in self.units if unit.isElf != target.isElf and target.isAlive]):
            return True
        # Identify all open squares that are in range of each target
        occupied_positions = set(u.position for u in self.units if u.isAlive and unit != u)
        in_range = set(p for e in enemies
                       for p in neighbors(e.position) if not self[p] and p not in occupied_positions)
        # Unit can only move if not already in range of a target
        if unit.position not in in_range and (new_position := self.move_position(unit.position, in_range)):
            unit.position = new_position
        # Find potential targets to attack
        if targets := [e for e in enemies if e.position in neighbors(unit.position)]:
            # Choose the target with the fewest hit points
            target = min(targets, key=lambda u: (u.health, u.position))
            # Unit deals damage equal to its attack power
            target.health -= unit.attack
            # Check if target survives the attack
            if target.health <= 0:
                target.isAlive = False
                # Part 2: No elf can die so raise an exception in the event that one does
                if no_elf_dies and target.isElf:
                    raise ElfHasDied()

    def move_position(self, position, target_positions):
        occupied_positions = {unit.position for unit in self.units if unit.isAlive}
        visited, queue = set(), deque([(position, 0)])
        explored = {position: (0, None)}
        # Perform Breadth First Search
        while queue:
            current_position, steps = queue.popleft()
            for neighbor in neighbors(current_position):
                # Skip cavern walls and occupied spaces
                if self[neighbor] or neighbor in occupied_positions:
                    continue
                # Record shortest path to neighbor
                if neighbor not in explored or explored[neighbor] > (steps + 1, current_position):
                    explored[neighbor] = (steps + 1, current_position)
                # Check if neighbor has already been visited or is queued to visit
                if neighbor in visited:
                    continue
                if not any(neighbor == visit[0] for visit in queue):
                    queue.append((neighbor, steps + 1))
            visited.add(current_position)
        # Determine which of the squares adjacent to a target that can be reached in the fewest steps
        try:
            _, nearest_position = min((steps, position) for position, (steps, previous_position) in explored.items()
                                      if position in target_positions)
        except ValueError:
            return
        # Find the first step in the chosen path
        while explored[nearest_position][0] > 1:
            nearest_position = explored[nearest_position][1]

        return nearest_position


def read_input_file():
    return open("input.txt", "r").read().splitlines()


def part_one(arena):
    return Battle(arena).combat()


def part_two(arena, result=None):
    for elf_attack_power in count(4):
        try:
            result = Battle(arena, elf_attack_power).combat(no_elf_dies=True)
            break
        except ElfHasDied:
            continue
    return result


if __name__ == "__main__":
    input_lines = read_input_file()
    print(part_one(input_lines))
    print(part_two(input_lines))
