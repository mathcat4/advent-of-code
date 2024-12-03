"""Day 2, 2023, Part 1"""

from aoc.utils import *


def main(inp):
    s = 0
    for i, ln in enumerate(inp.split("\n")):
        r = max([ints(a)[-1] for a in ln.split("red")[:-1]])
        g = max([ints(a)[-1] for a in ln.split("green")[:-1]])
        b = max([ints(a)[-1] for a in ln.split("blue")[:-1]])
        if r <= 12 and g <= 13 and b <= 14:
            s += i + 1
    return s
