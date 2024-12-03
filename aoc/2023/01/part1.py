"""Day 1, 2023, Part 1"""

from aoc.utils import *


def main(inp):
    d = [[a for a in l if a.isdigit()] for l in inp.split("\n")]
    return sum([int(a[0] + a[-1]) for a in d])
