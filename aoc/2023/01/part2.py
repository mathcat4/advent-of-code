"""Day 1, 2023, Part 2"""

from aoc.utils import *

n = "one, two, three, four, five, six, seven, eight, nine".split(", ")
d = {a: i + 1 for i, a in enumerate(n)}
d.update({str(i): i for i in range(1, 11)})


def main(inp):
    s = 0
    for ln in inp.split("\n"):
        digits = [d[a] for a in re.findall(f"(?=({'|'.join(d.keys())}))", ln)]
        s += int(str(digits[0]) + str(digits[-1]))
    return s
