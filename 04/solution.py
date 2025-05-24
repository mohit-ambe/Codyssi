file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()


def memory(line):
    return sum(ord(s) - ord('A') + 1 if s.isalpha() else int(s) for s in line)


def part1():
    print(memory(''.join(data)))


def part2():
    units = 0
    for line in data:
        chars = len(line) // 10
        units += memory(line[:chars] + str(len(line) - 2 * chars) + line[-chars:])
    print(units)


def part3():
    units = 0
    for line in data:
        count = 0
        char = ''
        encoded = ""
        for c in line:
            if c != char:
                encoded += char + str(count)
                char = c
                count = 1
            else:
                count += 1
        encoded += char + str(count)
        units += memory(encoded)
    print(units)


part1()
part2()
part3()
