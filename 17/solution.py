from functools import cache

file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

start, end = list(map(int, data[0].split(" : ")[1].split(" -> ")))
moves = eval(f"[{data[-1].split(' : ')[1]}]")

graph = dict()
for line in data[:-2]:
    id = int(line.split()[0][1:])
    s, e = list(map(int, line.split(" : ")[1].split(" -> ")))
    graph |= {(id, i):[(id, i + 1)] for i in range(s, e)}
    if "START" in line:
        continue
    sc, ec = [int(i[1:]) for i in line.split(" FROM ")[1].split(" TO ")]
    graph[(sc, s)].append((id, s))
    graph[(id, e)] = [(ec, e)]


@cache
def staircase(pos):
    if pos == 0:
        return 1
    paths = 0
    for m in moves:
        if m <= pos:
            paths += staircase(pos - m)
    return paths


@cache
def adj(node):
    Q = [(node, _) for _ in moves]
    adjacent = set()
    while Q:
        n, m = Q.pop(0)
        if m == 0:
            adjacent.add(n)
            continue
        if n in graph:
            Q.extend([(x, m - 1) for x in graph[n]])
            Q.sort()
    return adjacent


@cache
def find(pos):
    if pos not in graph:
        return 1
    return sum([find(a) for a in adj(pos)])


def part1():
    print(staircase(end - start))


def part2():
    print(find((1, 0)))


def part3():
    target = 100000000000000000000000000000
    path = [(1, 0)]
    while path[-1] != (1, end):
        path.append(tuple())
        for next_step in sorted(adj(path[-2])):
            path[-1] = next_step
            if target - find(next_step) <= 0:
                break
            target -= find(next_step)
    print("-".join(f"S{case}_{step}" for case, step in path))


part1()
part2()
part3()
