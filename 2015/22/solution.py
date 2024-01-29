"""
Advent of Code 2015
Day 22: Wizard Simulator 20XX
https://adventofcode.com/2015/day/22
"""
from re import findall
from heapq import heappop, heappush


def read_input_file():
    return tuple(map(int, findall(r"-?[0-9]+", open("input.txt", "r").read())))


def get_minimum_mana_spend(boss_stats, hard_difficulty=False):
    boss_hp, boss_damage = boss_stats
    damage_with_shield = max(1, boss_damage - 7)
    simulator_states = [(0, boss_hp, 50 if not hard_difficulty else 49, 500, 0, 0, 0)]
    seen_states = set(simulator_states)
    while simulator_states:
        mana_spent, boss_hp, player_hp, player_mana, shield, poison, recharge = heappop(simulator_states)
        # Handle active poison and recharge effects
        if poison > 0:
            boss_hp -= 3
            poison -= 1
        if recharge > 0:
            player_mana += 101
            recharge -= 1
        # Create new states for possible spell casts
        new_states = []
        # Magic Missile: costs 53 mana. It instantly does 4 damage.
        if 53 <= player_mana:
            new_states.append((mana_spent + 53, boss_hp - 4, player_hp, player_mana - 53, shield, poison, recharge))
        # Drain costs 73 mana. It instantly does 2 damage and heals 2 hit points.
        if 73 <= player_mana:
            new_states.append((mana_spent + 73, boss_hp - 2, player_hp + 2, player_mana - 73, shield, poison, recharge))
        # Shield costs 113 mana. It starts an effect that lasts for 6 turns.
        if 113 <= player_mana and shield <= 1:
            new_states.append((mana_spent + 113, boss_hp, player_hp, player_mana - 113, 3, poison, recharge))
        # Poison costs 173 mana. It starts an effect that lasts for 6 turns.
        if 173 <= player_mana and poison == 0:
            new_states.append((mana_spent + 173, boss_hp, player_hp, player_mana - 173, shield, 6, recharge))
        # Recharge costs 229 mana. It starts an effect that lasts for 5 turns.
        if 229 <= player_mana and recharge <= 1:
            new_states.append((mana_spent + 229, boss_hp, player_hp, player_mana - 229, shield, poison, 5))
        # Update states
        for mana_spent, boss_hp, player_hp, player_mana, shield, poison, recharge in new_states:
            if poison > 0:
                boss_hp -= 3
                poison -= 1
            if boss_hp <= 0:
                return mana_spent
            player_hp -= boss_damage if shield == 0 else damage_with_shield
            # On hard difficulty level lose 1 hit point
            if hard_difficulty:
                player_hp -= 1
            if player_hp <= 0 or (player_mana < 53 and recharge == 0):
                continue
            if recharge > 0:
                recharge -= 1
                player_mana += 101
            if shield > 0:
                shield -= 1
            next_state = (mana_spent, boss_hp, player_hp, player_mana, shield, poison, recharge)
            if next_state not in seen_states:
                heappush(simulator_states, next_state)
                seen_states.add(next_state)


if __name__ == "__main__":
    boss_initial = read_input_file()
    part_one = get_minimum_mana_spend(boss_initial)
    part_two = get_minimum_mana_spend(boss_initial, True)
    print(f"{part_one=}, {part_two=}")
