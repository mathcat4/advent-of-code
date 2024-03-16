from ...utils.helper import *


class Module:
    def __init__(self, name, typ, outs):
        self.name = name
        self.typ = typ
        self.outs = outs
        if typ == "%":
            self.mem = 0
        elif typ == "&":
            self.mem = {}

    def __repr__(self):
        return (
            self.name
            + "{"
            + f"type={self.typ},outputs={self.outs},memory={self.mem}"
            + "}"
        )


def main():
    modules = {}
    broadcast_targets = []
    for line in open(0).read().splitlines():
        left, right = line.split(" -> ")
        outs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = outs
        else:
            typ = left[0]
            name = left[1:]
            modules[name] = Module(name, typ, outs)
    for name, module in modules.items():
        for out in module.outs:
            if out in modules and modules[out].typ == "&":
                modules[out].mem[name] = 0
    lo = hi = 0
    for _ in range(1000):
        lo += 1
        q = deque([("broadcaster", x, 0) for x in broadcast_targets])

        while q:
            inp, out, pulse = q.popleft()
            if pulse == 0:
                lo += 1
            else:
                hi += 1
            if out not in modules:
                continue
            module = modules[out]
            if module.typ == "%" and pulse == 0:
                module.mem ^= 1
                for out in module.outs:
                    q.append((module.name, out, module.mem))
            if module.typ == "&":
                modules[out].mem[inp] = pulse
                if all(modules[out].mem.values()):
                    for out in module.outs:
                        q.append((module.name, out, 0))
                else:
                    for out in module.outs:
                        q.append((module.name, out, 1))
    return lo * hi


if __name__ == "__main__":
    print(main())
