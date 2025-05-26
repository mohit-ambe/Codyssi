file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

grid = [list(map(int, line.split())) for line in data]


def pathfind(start, end):
    global grid
    dist = 1_000_000
    Q = [(grid[start[0]][start[1]], *start)]
    visited = set()

    while Q:
        d, x, y = Q.pop(0)

        if (x, y) == end:
            dist = min(dist, d)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(x + 1, y), (x, y + 1)]:
            if not (0 <= dx < len(grid) and 0 <= dy < len(grid)):
                continue
            Q.append((d + grid[dx][dy], dx, dy))

        Q.sort(key=lambda r:r[0])

    return dist


def part1():
    print(min(min(sum(x) for x in grid), min(sum(x) for x in list(zip(*grid)))))


def part2():
    start = (0, 0)
    end = (14, 14)
    print(pathfind(start, end))


def part3():
    start = (0, 0)
    end = (len(grid) - 1, len(grid) - 1)
    print(pathfind(start, end))


part1()
part2()
part3()
