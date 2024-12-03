"""Day 2, 2024, Part 1"""

from aoc.utils import *


def main(inp):
    c = 0
    for ln in inp.split("\n"):
        l = ln.split()
        d = [int(a) - int(b) for a, b in windows(l, 2)]
        ab = [abs(a) for a in d]
        if (
            max(ab) <= 3
            and min(ab) >= 1
            and (all([a < 0 for a in d]) or all([a > 0 for a in d]))
        ):
            c += 1

    return c
