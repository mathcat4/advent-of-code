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
    # ins = [row for row in open(0).read().splitlines()]
    # hi = lo = 0
    # rules = {}
    # pulses = {}
    # flipflops = {}
    # # conj_inps = []
    # conj = {}
    # modules = deque([])

    # high_pulses = 0
    # low_pulses = 1
    # for line in ins:
    #     inp, outs = line.split("->")
    #     outs = [line.strip() for line in outs.strip().split(",")]
    #     inp = inp.strip()
    #     if inp == "broadcaster":
    #         for out in outs:
    #             pulses[out] = [0]
    #             low_pulses += 1
    #             modules.append(out)
    #     else:
    #         op = inp[0]
    #         inp = inp[1:]
    #         if inp not in pulses:
    #             pulses[inp] = []
    #         for out in outs:
    #             if out not in pulses:
    #                 pulses[out] = [0]
    #                 # modules.append(out)
    #             if out not in rules:
    #                 rules[out] = ("", outs)
    #         rules[inp] = (op, outs)
    #         if op == "%":
    #             flipflops[inp] = 0
    #         elif op == "&":
    #             conj[inp] = {}

    # for inp, (op, outs) in rules.items():
    #     for out in outs:
    #         if out in conj.keys():
    #             conj[out][inp] = 0
    # init_pulses = deepcopy(pulses)
    # init_modules = modules.copy()
    # init_conj = conj.copy()
    # init_high = high_pulses
    # init_low = low_pulses
    # init_rules = rules.copy()
    # # print("start", pulses, conj, modules, flipflops)
    # for _ in range(1000):
    #     pulses = deepcopy(init_pulses)
    #     modules = init_modules.copy()
    #     conj = init_conj.copy()
    #     high_pulses = init_high
    #     low_pulses = init_low
    #     rules = init_rules.copy()

    #     # print("start", pulses, conj, modules, flipflops)
    #     while modules:
    #         module = modules.popleft()
    #         op, outs = rules[module]
    #         if op == "%":
    #             start = pulses[module][0]
    #             pulses[module] = pulses[module][1:]
    #             # print(flipflops[module])

    #             if start == 0:
    #                 if not flipflops[module]:
    #                     flipflops[module] = 1
    #                     for out in outs:
    #                         pulses[out].append(1)
    #                         high_pulses += 1
    #                         modules.append(out)
    #                         if out in conj.keys():
    #                             conj[out][module] = 1
    #                 else:
    #                     flipflops[module] = 0
    #                     for out in outs:
    #                         pulses[out].append(0)
    #                         low_pulses += 1
    #                         modules.append(out)
    #                         if out in conj.keys():
    #                             conj[out][module] = 0
    #             # print(flipflops[module])
    #         elif op == "&":
    #             start = pulses[module][0]
    #             # print(all/(conj[module].))
    #             pulses[module] = pulses[module][1:]

    #             if all(conj[module].values()):
    #                 for out in outs:
    #                     pulses[out].append(0)
    #                     low_pulses += 1
    #                     modules.append(out)
    #                     if out in conj.keys():
    #                         conj[out][module] = 0
    #             else:
    #                 for out in outs:
    #                     pulses[out].append(1)
    #                     high_pulses += 1
    #                     modules.append(out)
    #                     if out in conj.keys():
    #                         conj[out][module] = 1
    #         # print(module, op, outs, modules, pulses, flipflops, high_pulses, low_pulses)
    #     hi += high_pulses
    #     lo += low_pulses
    # return hi * lo
    # type, mem, out
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
    feed = [name for name, module in modules.items() if "rx" in module.outs]
    assert len(feed) == 1
    feed = feed[0]
    ffeed = {name: 0 for name, module in modules.items() if feed in module.outs}
    n = 1
    while not all(ffeed.values()):
        q = deque([("broadcaster", x, 0) for x in broadcast_targets])

        while q:
            inp, out, pulse = q.popleft()
            if feed == out and pulse:
                if not ffeed[inp]:
                    ffeed[inp] = n
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
        n += 1
    return math.lcm(*ffeed.values())


if __name__ == "__main__":
    print(main())
