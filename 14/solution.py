import re

file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

items = {}
for line in data:
    code = line.split(" | ")[0].split()[1]
    _, q, c, um = list(map(int, re.findall("\d+", line)))
    items[code] = (q, c, um)

codes = sorted(items.keys())

max_q = int()
min_m = int()
seen = dict()


def combo(index, qual, cost, mat):
    global max_q, min_m, seen
    if cost < 0:
        return

    if (index, cost) in seen and seen[(index, cost)] > qual:
        return
    seen[(index, cost)] = qual

    if qual > max_q or (qual == max_q and mat < min_m):
        max_q = qual
        min_m = mat

    if index == len(codes):
        return

    combo(index + 1, qual, cost, mat)
    qq, cc, mm = items[codes[index]]
    combo(index + 1, qual + qq, cost - cc, mat + mm)


def part1():
    ranked = sorted(items.items(), key=lambda i:(i[1][0], i[1][1]), reverse=True)
    print(sum(i[1][2] for i in ranked[:5]))


def part2():
    global max_q, min_m, seen
    max_q = 0
    min_m = 1_000_000
    seen.clear()
    combo(0, 0, 30, 0)
    print(max_q * min_m)


def part3():
    global max_q, min_m, seen
    max_q = 0
    min_m = 1_000_000
    seen.clear()
    combo(0, 0, 300, 0)
    print(max_q * min_m)


part1()
part2()
part3()
