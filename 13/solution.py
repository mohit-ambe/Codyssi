file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

G = {}
weight = {}

for line in data:
    source, _, dest, _, cost = line.split()
    if source not in G:
        G[source] = []
    G[source].append(dest)
    weight[(source, dest)] = int(cost)


def pathfind(step=None):
    Q = [(0, 'STT')]
    visited = set()
    paths = []

    while Q:
        d, u = Q.pop(0)
        if u in visited:
            continue
        visited.add(u)
        paths.append(d)
        if u in G:
            for v in G[u]:
                Q.append((d + (weight[(u, v)] if not step else step), v))
        Q.sort()

    paths.sort()
    return paths[-1] * paths[-2] * paths[-3]


def part1():
    print(pathfind(1))


def part2():
    print(pathfind())


def part3():
    cycle = 0
    for start in G:
        curr = 0
        Q = [(0, start)]

        while Q:
            d, u = Q.pop(0)
            if d > sum(weight.values()):
                break
            if u == start and d:
                curr = d
                break
            if u in G:
                for v in G[u]:
                    Q.append((d + weight[(u, v)], v))
            Q = list(set(Q))
            Q.sort()
        cycle = max(cycle, curr)
    print(cycle)


part1()
part2()
part3()
