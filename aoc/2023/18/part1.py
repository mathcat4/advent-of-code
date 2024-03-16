from ...utils.helper import *


def main():
    ins = [row.split(" ") for row in open(0).read().splitlines()]
    maps = {"R": RIGHT, "D": DOWN, "L": LEFT, "U": UP}

    pos = V(0, 0)
    points = []
    boundary = 0
    for dr, dist, _ in ins:
        dist = int(dist)
        vr = maps[dr]
        pos = pos + V(vr.r * dist, vr.c * dist)
        points.append(pos)
        boundary += dist
    return shoelace_pick(points, boundary)


def shoelace_pick(points, boundary):
    area = 0
    for i in range(len(points)):
        area += (points[i].r) * ((points[i - 1].c) - (points[(i + 1) % len(points)].c))

    area = abs(area / 2)
    return area + 1 - boundary // 2 + boundary


if __name__ == "__main__":
    print(main())
