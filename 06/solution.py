file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()


def part1():
    print(len([x for x in data[0] if x.isalpha()]))


def part2():
    lower = sum([ord(x) - ord('a') + 1 for x in data[0] if x.isalpha() and x.islower()])
    upper = sum([ord(x) - ord('A') + 1 + 26 for x in data[0] if x.isalpha() and x.isupper()])
    print(lower + upper)


def part3():
    value = 0
    total = 0
    for char in data[0]:
        if char.isalpha():
            if char.islower():
                v = ord(char) - ord('a') + 1
            else:
                v = ord(char) - ord('A') + 1 + 26
        else:
            v = (value * 2 - 5) % 52
        value = v
        total += v
    print(total)


part1()
part2()
part3()
