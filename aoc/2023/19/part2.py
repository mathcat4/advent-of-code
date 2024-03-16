from ...utils.helper import *
from .part1 import *


def count(ranges, name="in"):
    t = 0
    if name == "R":
        return 0
    if name == "A":
        return math.prod([b - a + 1 for a, b in ranges.values()])

    rules, end = wfs[name]

    for key, op, n, target in rules:
        lo, hi = ranges[key]
        if op == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)

        if T[0] <= T[1]:
            nranges = ranges.copy()
            nranges[key] = T
            t += count(nranges, target)
            # break
        if F[0] <= F[1]:
            ranges = ranges.copy()
            ranges[key] = F
        else:
            break
    else:
        t += count(ranges, end)
    return t


def main():
    global wfs
    b1, _ = open(0).read().split("\n\n")
    wfs = get_wfs(b1)
    return count({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})


if __name__ == "__main__":
    print(main())
