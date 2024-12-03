"""Day 2, 2024, Part 2"""

from aoc.utils import *


def main(inp):
    c = 0
    for ln in inp.split("\n"):
        al = False
        for i in range(len(ln)):
            l = ln.split()

            l = [a for j, a in enumerate(l) if i != j]

            d = [int(a) - int(b) for a, b in windows(l, 2)]
            ab = [abs(a) for a in d]
            if (
                max(ab) <= 3
                and min(ab) >= 1
                and (all([a < 0 for a in d]) or all([a > 0 for a in d]))
            ):
                al = True
        if al:
            c += 1

    return c
