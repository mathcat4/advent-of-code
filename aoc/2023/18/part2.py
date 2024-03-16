from ...utils.helper import *
from .part1 import *


def main():
    ins = [row.split(" ") for row in open(0).read().splitlines()]
    maps = [RIGHT, DOWN, LEFT, UP]

    pos = V(0, 0)
    points = []
    boundary = 0
    for _, _, col in ins:
        dist = int(col[2:-2], 16)
        vr = maps[int(col[-2])]
        pos = pos + V(vr.r * dist, vr.c * dist)
        points.append(pos)
        boundary += dist
    return shoelace_pick(points, boundary)


if __name__ == "__main__":
    print(main())
