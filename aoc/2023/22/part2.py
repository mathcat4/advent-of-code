from ...utils.helper import *

op = [
    [tuple(map(int, tup.split(","))) for tup in line.split("~")]
    for line in open(0).read().splitlines()
]
cubes = []
for start, end in op:
    dif = [p2 - p1 for p1, p2 in zip(start, end)]
    cubes.append(
        list(itr.product(*[range(d1, d1 + d2 + 1) for d1, d2 in zip(start, dif)]))
    )


def fall(cubes):
    cubes_sorted = sorted(cubes, key=lambda c: min([sc[2] for sc in c]))
    for i, cube in enumerate(cubes_sorted):
        all_points = [
            point for ccube in cubes_sorted for point in ccube if ccube != cube
        ]
        ncube = cube
        while True:
            nncube = [(point[0], point[1], point[2] - 1) for point in ncube]
            if any([p2 <= 0 or (p0, p1, p2) in all_points for p0, p1, p2 in nncube]):
                break
            ncube = nncube
        cubes_sorted[i] = ncube
        if i % 100 == 0:
            print(i)
    return cubes_sorted


simulated = fall(cubes)
# letters = {frozenset(cube): "ABCDEFG"[i] for i, cube in enumerate(simulated)}
# print(cubes)

support = {tuple(cube): [] for cube in simulated}
i = 0
for cube1, cube2 in itr.combinations(simulated, 2):
    above = False
    for c1, c2 in itr.product(cube1, cube2):
        if c1[0] == c2[0] and c1[1] == c2[1] and c2[2] - c1[2] == 1:
            above = True
    if above:
        support[tuple(cube1)].append(cube2)
    if i % 1000 == 0:
        print(i)
    i += 1
print(support)


def supported_by(cube):
    return [key for key, value in support.items() if cube in value]


print(supported_by([(0, 0, 3), (0, 1, 3), (0, 2, 3)]))
# exit(0)
t = 0
for i, cube in enumerate(simulated):
    seen = [tuple(cube)]
    nsup = deque([cube])
    while nsup:
        csup = nsup.popleft()
        ccsup = support[tuple(csup)]
        for ncsup in ccsup:
            if tuple(ncsup) in seen:
                continue
            if any([supby not in seen for supby in supported_by(ncsup)]):
                continue
            nsup.append(tuple(ncsup))
            seen.append(tuple(ncsup))
            t += 1
    print(i, t)

print(t)
