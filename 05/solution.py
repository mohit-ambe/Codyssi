file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

coords = list(map(eval, data))


def part1():
    print(max(abs(x) + abs(y) for x, y in coords) - min(abs(x) + abs(y) for x, y in coords))


def part2():
    closest = sorted(coords, key=lambda r:abs(r[0]) + abs(r[1]))[0]
    other_islands = coords.copy()
    other_islands.remove(closest)
    print(min(abs(x - closest[0]) + abs(y - closest[1]) for x, y in other_islands))


def part3():
    other_islands = coords.copy()
    path = 0
    prev = [(0, 0)]
    while other_islands:
        closest = sorted(other_islands, key=lambda r:abs(r[0] - prev[-1][0]) + abs(r[1] - prev[-1][1]))[0]
        prev.append(closest)
        other_islands.remove(closest)
        path += abs(closest[0] - prev[-2][0]) + abs(closest[1] - prev[-2][1])
    print(path)


part1()
part2()
part3()
