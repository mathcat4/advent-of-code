import itertools as itr
import functools as fts
from pprint import pprint
from collections import deque
from copy import deepcopy
import re
import math


# Vectors
class V(tuple):
    def __new__(cls, row, col):
        obj = super().__new__(cls, (row, col))
        obj.r = row
        obj.c = col
        return obj

    def __add__(self, other):
        return V(self.r + other.r, self.c + other.c)

    def __sub__(self, other):
        return V(self.r - other.r, self.c - other.c)

    def __neg__(self):
        return V(-self.r, -self.c)

    def inbound(self, grid):
        return 0 <= self.r < len(grid) and 0 <= self.c < len(grid[0])

    def __invert__(self):
        return V(self.c, self.r)


UP = NORTH = V(-1, 0)
DOWN = SOUTH = V(1, 0)
LEFT = WEST = V(0, -1)
RIGHT = EAST = V(0, 1)
UPRIGHT = NORTHEAST = V(-1, 1)
UPLEFT = NORTHWEST = V(-1, -1)
DOWNRIGHT = SOUTHEAST = V(1, 1)
DOWNLEFT = SOUTHWEST = V(1, -1)
NULL = START = V(0, 0)


# Grid
class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])

    def __getitem__(self, v):
        return self.grid[v.r][v.c]

    def __str__(self):
        return "\n".join([" ".join(r) for r in self.grid])

    def find(self, item):
        if not isinstance(item, list):
            item = [item]
        inds = []
        for i, r in enumerate(self.grid):
            for j, c in enumerate(r):
                if c in item:
                    inds.append(V(i, j))
        return inds

    def legal(self, ind):
        return True if 0 <= ind.r < self.h and 0 <= ind.c < self.w else False

    def filter_legal(self, inds):
        return [ind for ind in inds if self.legal(ind)]


def adjs(v):
    return [v + UP, v + DOWN, v + LEFT, v + RIGHT]


def nbrs(v):
    return [
        v + UP,
        v + UPRIGHT,
        v + RIGHT,
        v + DOWNRIGHT,
        v + DOWN,
        v + DOWNLEFT,
        v + LEFT,
        v + UPLEFT,
    ]


# Structures


def bidict(d):
    ret = {k: set() for k in itr.chain(d.keys(), d.values())}
    for k, v in d.items():
        ret[k].add(v)
        ret[v].add(k)
    return ret


def transdict(d):
    ret = {k: set() for k in d.values()}
    for k, v in d.items():
        ret[v].add(k)
    return ret


def windows(l, n):
    return [l[i : i + n] for i in range(len(l) - n + 1)]


def rotate(l, n=1):
    for _ in range(n):
        l = list(zip(*l))[::-1]
    return l


def transpose(m):
    return [list(i) for i in zip(*m)]


# Math functions


def extended_euclidean(a, b):
    if b == 0:
        gcd, s, t = a, 1, 0
        return (gcd, s, t)
    else:
        s2, t2, s1, t1 = 1, 0, 0, 1
        while b > 0:
            q = a // b
            r, s, t = (a - b * q), (s2 - q * s1), (t2 - q * t1)
            a, b, s2, t2, s1, t1 = b, r, s1, t1, s, t
        gcd, s, t = a, s2, t2
        return (gcd, s, t)


def chinese_remainder_2(constraints):
    constraints = sorted(constraints, reverse=True)
    moduli = []
    remainders = []

    for constraint in constraints:
        moduli.append(constraint[0])
        remainders.append(constraint[1])

    total = 0
    steps = math.prod(moduli)
    for i, modulo in enumerate(moduli):
        moduli_N = moduli.copy()
        moduli_N.remove(modulo)
        prod_N = math.prod(moduli_N)
        _, moduli_M, _ = extended_euclidean(prod_N, modulo)
        total += remainders[i] * moduli_M * prod_N

    if total < 0:
        total = total + steps * abs(total // steps)
    return total, steps


def chinese_remainder_1(div):
    div = sorted(div)[::-1]
    nums = []
    rems = []
    for d in div:
        nums.append(d[0])
        rems.append(d[1])
    current_ind = 0
    add = nums[current_ind]
    current = rems[current_ind]

    while True:
        next_ind = current_ind + 1

        if current % nums[next_ind] == rems[next_ind]:
            current_ind += 1
            add *= nums[next_ind]
            if current_ind >= len(nums) - 1:
                return (current, add)

        current += add


# Regex


def signed_ints(s):
    return [int(a) for a in re.findall(r"-?\d+", s)]


def ints(s):
    return [int(a) for a in re.findall(r"\d+", s)]


def repl_var(pattern, sub_patterns, string):
    stringl = list(string)
    for i, m in enumerate(re.finditer(pattern, string)):
        stringl[m.start() : m.end()] = sub_patterns[i % len(sub_patterns)]
    return "".join(stringl)
