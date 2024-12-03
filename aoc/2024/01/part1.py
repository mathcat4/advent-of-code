"""Day 1, 2024, Part 1"""

from aoc.utils import *


def main(inp):
    r = transpose([ints(a) for a in inp.split("\n")])
    return sum([abs(a - b) for a, b in zip(sorted(r[0]), sorted(r[1]))])
