from ...utils.helper import *


def main():
    op = open(0).read().splitlines()
    for r, row in enumerate(op):
        if "S" in row:
            sind = V(r, row.index("S"))
    ps = {sind}
    for _ in range(64):
        nps = set()
        for a in ps.copy():
            for dr in [UP, LEFT, DOWN, RIGHT]:
                na = a + dr
                if na.inbound(op) and op[na.r % len(op)][na.c % len(op[0])] != "#":
                    nps.add(na)
        ps = nps

    return len(ps)


if __name__ == "__main__":
    print(main())
