"""
Advent of Code 2017
Day 20: Particle Swarm
https://adventofcode.com/2017/day/20
"""
from re import match as regex_match
from collections import namedtuple

Particle = namedtuple('Particle', ['pos', 'vel', 'acc'])


def read_input_file():
    regex = r"p=<(.*?)>, v=<(.*?)>, a=<(.*?)>"
    lines = [regex_match(regex, line).groups() for line in open("input.txt", "r").read().splitlines()]
    return [Particle(*[tuple(map(int, t.split(","))) for t in line]) for line in lines]


def manhattan_distance(particle):
    return sum(abs(k) for k in particle.pos)


def move_particle(particle):
    new_vel = tuple(map(sum, zip(particle.vel, particle.acc)))
    new_pos = tuple(map(sum, zip(particle.pos, new_vel)))
    return Particle(new_pos, new_vel, particle.acc)


def part_one(particles):
    for _ in range(500):
        particles = [move_particle(particle) for particle in particles]
    return particles.index(min(particles, key=manhattan_distance))


def part_two(particles):
    for _ in range(50):
        positions = [particle.pos for particle in particles]
        if len(set(positions)) < len(positions):
            # Keep only the particles with unique positions
            particles = [particle for particle, position in zip(particles, positions) if positions.count(position) == 1]
        particles = [move_particle(particle) for particle in particles]
    return len(particles)


if __name__ == "__main__":
    particles_list = read_input_file()
    print(part_one(particles_list.copy()))
    print(part_two(particles_list.copy()))
