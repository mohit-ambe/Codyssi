import re

file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

funcs = list(map(int, re.findall("\d+", ' '.join(data[:3]))))
nums = sorted(list(map(int, data[4:])))


def apply_functions(x):
    return x ** funcs[2] * funcs[1] + funcs[0]


def part1():
    print(apply_functions(nums[len(nums) // 2]))


def part2():
    print(apply_functions(sum(x for x in nums if x % 2 == 0)))


def part3():
    prev = 0

    for num in nums:
        if apply_functions(num) > 15_000_000_000_000:
            break
        prev = num

    print(prev)


part1()
part2()
part3()
