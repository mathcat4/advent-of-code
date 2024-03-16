from ...utils.helper import *


def solve(spos, steps, full=False):
    q = deque([(spos, steps)])
    seen = set()
    ans = set()
    while q:
        pos, steps = q.popleft()
        if steps % 2 == 0:
            ans.add(pos)
        if steps == 0 and not full:
            continue
        for dr in [UP, LEFT, DOWN, RIGHT]:
            npos = pos + dr
            if not npos.inbound(op) or op[npos.r][npos.c] == "#" or npos in seen:
                continue
            # if npos.inbound(op) and op[npos.r][npos.c] != "#" and npos not in seen:
            seen.add(npos)
            q.append((npos, steps - 1))
    return len(ans)


op = open(0).read().splitlines()
steps = 26501365

sind = next(
    V(r, c) for r, row in enumerate(op) for c, ch in enumerate(row) if ch == "S"
)
print(sind)
assert len(op) == len(op[0])  # Square grid
size = len(op)
hsize = size // 2
grids = steps // size
print(grids)
assert sind.r == sind.c == hsize  # Starting pos in middle
start = sind.r
assert size % 2 == 1  # Odd side length
assert steps % size == hsize
ans = 0

odd_grids = ((grids - 1) // 2 * 2 + 1) ** 2
odd_steps = solve(sind, 1, full=True)

even_grids = (grids // 2 * 2) ** 2
even_steps = solve(sind, 0, full=True)

ans += odd_grids * odd_steps + even_grids * even_steps

top = solve(V(size - 1, hsize), size - 1)
bottom = solve(V(0, hsize), size - 1)
left = solve(V(hsize, size - 1), size - 1)
right = solve(V(hsize, 0), size - 1)
print((top, bottom, left, right))
ans += (top + bottom + left + right) * (grids - 1)

small_seg_steps = size - 1 - (hsize + 1)

stopleft = solve(V(size - 1, 0), small_seg_steps)
sbottomleft = solve(V(size - 1, size - 1), small_seg_steps)
stopright = solve(V(0, 0), small_seg_steps)
sbottomright = solve(V(0, size - 1), small_seg_steps)
ans += (stopleft + sbottomleft + stopright + sbottomright) * grids

large_seg_steps = 2 * size - 1 - (hsize + 1)
print(large_seg_steps)

ltopleft = solve(V(size - 1, 0), large_seg_steps)
lbottomleft = solve(V(size - 1, size - 1), large_seg_steps)
ltopright = solve(V(0, 0), large_seg_steps)
lbottomright = solve(V(0, size - 1), large_seg_steps)
print((ltopleft, lbottomleft, ltopright, lbottomright))
ans += (stopleft + sbottomleft + stopright + sbottomright) * (grids - 1)

print(ans)


def main():
    for r, row in enumerate(op):
        if "S" in row:
            sind = V(r, row.index("S"))
    assert len(op) == len(op[0])  # Square grid

    steps = 26501365
    size = len(op)

    assert size % 2 == 1  # Odd side length
    assert sind == V(len(op) // 2, len(op) // 2)  # S is in the middle
    assert (
        steps % size == size // 2
    )  # After steps the furthest point will be at the edgee
    grid_width = steps // size - 1
    # print(grid_width)

    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = solve(sind, size * 2 + 1)
    even_points = solve(sind, size * 2)
    print(odd, even, odd_points, even_points)

    # # print(grid_width, steps, size, odd, even, odd_points, even_points)
    # corner_t = sub(V(size - 1, sind.c), size - 1)
    # corner_r = sub(V(sind.r, 0), size - 1)
    # corner_b = sub(V(0, sind.c), size - 1)
    # corner_l = sub(V(sind.r, size - 1), size - 1)

    small_tr = solve(V(size - 1, 0), size // 2 - 1)
    small_tl = solve(V(size - 1, size - 1), size // 2 - 1)
    small_br = solve(V(0, 0), size // 2 - 1)
    small_bl = solve(V(0, size - 1), size // 2 - 1)

    large_tr = solve(V(size - 1, 0), (size * 3) // 2 - 1)
    large_tl = solve(V(size - 1, size - 1), (size * 3) // 2 - 1)
    large_br = solve(V(0, 0), (size * 3) // 2 - 1)
    large_bl = solve(V(0, size - 1), (size * 3) // 2 - 1)
    print(large_bl, large_br, large_tl, large_tr, (size * 3) // 2 - 1)

    # print(corner_b)
    # # return sub(sind, 64)
    # return (
    #     odd * odd_points
    #     + even * even_points
    #     + corner_b
    #     + corner_r
    #     + corner_t
    #     + corner_l
    #     + (grid_width + 1) * (small_bl + small_tl + small_br + small_tr)
    #     + grid_width * (large_bl + large_tl + large_br + large_tr)
    # )


main()
