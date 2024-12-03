"""Day 3, 2023, Part 1"""

from aoc.utils import *


def main(inp):
    grid = Grid(inp.split("\n"))
    ninds = set()
    for r, row in enumerate(grid.grid):
        for c, ch in enumerate(row):
            if ch.isdigit() or ch == ".":
                continue
            for nb in nbrs(V(r, c)):
                if not grid.legal(nb) or not grid[V(nb.r, nb.c)].isdigit():
                    continue

                dc = nb.c
                while dc > 0 and grid[V(nb.r, dc - 1)].isdigit():
                    dc -= 1
                ninds.add(V(nb.r, dc))

    s = 0
    for ind in ninds:
        dg = grid[ind]
        c = ind.c
        while c + 1 < grid.w and grid[V(ind.r, c + 1)].isdigit():
            dg += grid[V(ind.r, c + 1)]
            c += 1

        s += int(dg)

    return s
