"""
Advent of Code 2016
Day 11: Radioisotope Thermoelectric Generators
https://adventofcode.com/2016/day/11
"""

print(sum(2 * sum([4, 2, 4, 0][:x]) - 3 for x in range(1, 4)))

print(sum(2 * sum([8, 2, 4, 0][:x]) - 3 for x in range(1, 4)))