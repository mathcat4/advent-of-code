"""Day 3, 2024, Part 2"""

from aoc.utils import *


def main(inp):
    sm = 0

    don = [g.end() for g in re.finditer(r"don't\(\)", inp)]
    do = [g.end() for g in re.finditer(r"do\(\)", inp)]

    for m in re.finditer(r"(?=(mul\((.+?),(.+?)\)))", inp):
        di = m.start()

        while (di not in don) and (di not in do) and (di > 0):
            di -= 1
        if di in don:
            continue

        s = m.groups()[1:]
        if all([c.isdigit() for c in s[0]]) and all([c.isdigit() for c in s[1]]):
            sm += int(s[0]) * int(s[1])
    return sm
