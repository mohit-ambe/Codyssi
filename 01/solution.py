file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

nums = list(map(int, data[:-1]))
corrections = [*data[-1]]


def part1():
    offset = nums[0]
    for i, num in enumerate(nums[1:]):
        offset += num * (-1 if corrections[i] == '-' else 1)
    print(offset)


def part2():
    offset = nums[0]
    for i, num in enumerate(nums[1:]):
        offset += num * (-1 if corrections[::-1][i] == '-' else 1)
    print(offset)


def part3():
    offset = nums[0] * 10 + nums[1]
    for i, _ in list(enumerate(nums))[2::2]:
        offset += (nums[i] * 10 + nums[i + 1]) * (-1 if corrections.pop(-1) == '-' else 1)
    print(offset)


part1()
part2()
part3()
