from ...utils.helper import *


def get_wfs(block):
    wfs = {}
    for line in block.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        wfs[name] = ([], rules.pop())
        for rule in rules:
            cond, res = rule.split(":")
            key = cond[0]
            op = cond[1]
            n = int(cond[2:])
            wfs[name][0].append((key, op, n, res))
    return wfs


def main():
    b1, b2 = open(0).read().split("\n\n")
    wfs = get_wfs(b1)
    ops = {"<": int.__lt__, ">": int.__gt__}
    t = 0

    for line in b2.splitlines():
        state = {}
        for rule in line[1:-1].split(","):
            name, val = rule.split("=")
            state[name] = int(val)

        cur = "in"
        while True:
            if cur == "A":
                t += sum(state.values())
                break
            elif cur == "R":
                break

            conds, end = wfs[cur]
            for cond in conds:
                key, op, n, res = cond
                if ops[op](state[key], n):
                    cur = res
                    break
            else:
                cur = end
    return t


if __name__ == "__main__":
    print(main())
