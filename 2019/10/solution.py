"""
Advent of Code 2019
Day 10: Monitoring Station
https://adventofcode.com/2019/day/10
"""
from math import atan2, gcd, pi
from sys import maxsize


def read_input_file():
    return [(x, y) for y, row in enumerate(open("input.txt", "r").read().split())
            for x, value in enumerate(row) if value == '#']


def get_angle(a, b):
    angle = atan2(b[0] - a[0], a[1] - b[1]) * 180 / pi
    return angle + (360 if angle < 0 else 0)


def part_one(asteroids_list):
    visible_asteroids = [(origin, len({get_angle(origin, target) for target in asteroids_list if origin != target}))
                         for origin in asteroids_list]
    visible_asteroids.sort(key=lambda x: x[1], reverse=True)
    return visible_asteroids[0]


def part_two(asteroids_list, monitoring_station):
    mx, my = monitoring_station
    vaporized = [monitoring_station]
    while len(vaporized) != len(asteroids_list):
        closest_points = {}
        for x, y in asteroids_list:
            if (x, y) not in vaporized:
                dx, dy = x - mx, y - my
                dx, dy = dx // gcd(dx, dy), dy // gcd(dx, dy)
                closest_x, closest_y = closest_points.get((dx, dy), (maxsize, maxsize))
                if abs(x - mx) + abs(y - my) < abs(closest_x - mx) + abs(closest_y - my):
                    closest_points[(dx, dy)] = (x, y)
        vaporized += sorted(closest_points.values(), key=lambda a: -atan2(a[0] - mx, a[1] - my))
    return vaporized[200][0] * 100 + vaporized[200][1]


if __name__ == "__main__":
    asteroids_locations = read_input_file()
    station_location, visible = part_one(asteroids_locations)
    print(f"part_one: {visible}")
    result = part_two(asteroids_locations, station_location)
    print(f"part_two: {result}")
