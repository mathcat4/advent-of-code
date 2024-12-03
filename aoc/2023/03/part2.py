"""Day 3, 2023, Part 2"""

from aoc.utils import *


def main(inp):
    grid = Grid(inp.split("\n"))
    ninds = set()
    for r, row in enumerate(grid.grid):
        for c, ch in enumerate(row):
            if ch != "*":
                continue
            ginds = set()
            for nb in nbrs(V(r, c)):
                if not grid.legal(nb) or not grid[V(nb.r, nb.c)].isdigit():
                    continue

                dc = nb.c
                while dc > 0 and grid[V(nb.r, dc - 1)].isdigit():
                    dc -= 1
                ginds.add(V(nb.r, dc))
            if len(ginds) == 2:
                ninds.add(tuple(ginds))

    s = 0
    for gs in ninds:
        p = 1
        for g in gs:
            dg = grid[g]
            c = g.c
            while c + 1 < grid.w and grid[V(g.r, c + 1)].isdigit():
                dg += grid[V(g.r, c + 1)]
                c += 1

            p *= int(dg)
        s += p

    return s
