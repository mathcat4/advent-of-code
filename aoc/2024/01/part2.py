"""Day 1, 2024, Part 2"""

from aoc.utils import *


def main(inp):
    r = transpose([ints(a) for a in inp.split("\n")])
    return sum([r[1].count(a) * a for a in r[0]])
