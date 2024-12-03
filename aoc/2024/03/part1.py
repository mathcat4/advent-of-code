"""Day 3, 2024, Part 1"""

from aoc.utils import *


def main(inp):
    sm = 0

    for m in re.finditer(r"(?=(mul\((.+?),(.+?)\)))", inp):
        s = m.groups()[1:]
        if all([c.isdigit() for c in s[0]]) and all([c.isdigit() for c in s[1]]):
            sm += int(s[0]) * int(s[1])
    return sm
