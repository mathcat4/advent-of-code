"""Day 2, 2023, Part 2"""

from aoc.utils import *


def main(inp):
    s = 0
    for i, ln in enumerate(inp.split("\n")):
        r = max([ints(a)[-1] for a in ln.split("red")[:-1]])
        g = max([ints(a)[-1] for a in ln.split("green")[:-1]])
        b = max([ints(a)[-1] for a in ln.split("blue")[:-1]])
        s += r * g * b
    return s
