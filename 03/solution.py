file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

ranges = [list(map(int, x.replace(" ", "-").split("-"))) for x in data]


def part1():
    print(sum(r - l + 1 for l, r in [list(map(int, x.split("-"))) for x in " ".join(data).split()]))


def part2():
    boxes = 0
    for l1, r1, l2, r2 in ranges:
        boxes += len(set(range(l1, r1 + 1)) | set(range(l2, r2 + 1)))
    print(boxes)


def part3():
    boxes = 0
    for i in range(len(ranges) - 1):
        labelled = set()
        for j in range(i, i + 2):
            l1, r1, l2, r2 = ranges[j]
            labelled |= set(range(l1, r1 + 1)) | set(range(l2, r2 + 1))
        boxes = max(boxes, len(labelled))
    print(boxes)


part1()
part2()
part3()
