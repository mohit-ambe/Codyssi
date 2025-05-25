file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

blank_one = data.index("")
blank_two = data.index("", blank_one + 1)

tracks = list(map(int, data[:blank_one]))
swaps = [list(map(int, d.split("-"))) for d in data[blank_one + 1:blank_two]]


def backtrack(swap_list, target=int(data[-1])):
    i = len(swap_list) - 1
    while i > -1:
        if target in swap_list[i]:
            target = [s for s in swap_list[i] if s != target][0]
        i -= 1
    return target


def part1():
    global tracks, swaps
    # backtrack through swaps
    print(tracks[backtrack(swaps) - 1])


def part2():
    global tracks, swaps
    # for indices x, y, z in the list
    # an x-y-z swap is equivalent to and x-y and x-z swap

    s2_swaps = []
    for i in range(len(swaps) - 1):
        s2_swaps.append(swaps[i])
        s2_swaps.append([swaps[i][0], swaps[i + 1][0]])

    s2_swaps.append(swaps[-1])
    s2_swaps.append([swaps[-1][0], swaps[0][0]])

    print(tracks[backtrack(s2_swaps) - 1])


def part3():
    global tracks, swaps
    # for indices x, y in the list with size n
    # an x-y block swap is equivalent to k consecutive xi-yi swaps
    # where k = min(y-x, n-y+1) to prevent both overlaps and overflow

    s3_swaps = []
    for x, y in swaps:
        if x > y:
            x, y = y, x
        s3_swaps.append([x, y])
        for d in range(1, min(y - x, len(tracks) - y + 1)):
            s3_swaps.append([x + d, y + d])

    print(tracks[backtrack(s3_swaps) - 1])


part1()
part2()
part3()
