file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()


def part1():
    print(len([x for x in "".join(data) if x.isalpha()]))


def part2():
    lines = data.copy()
    chars = 0
    for line in lines:
        change = True
        while change:
            change = False
            i = 0
            while i < len(line) - 1:
                if line[i].isdigit():
                    if line[i + 1].isalpha() or line[i + 1] == '-':
                        change = True
                        line = line[:i] + line[i + 2:]
                        break
                elif line[i].isalpha() or line[i] == '-':
                    if line[i + 1].isdigit():
                        change = True
                        line = line[:i] + line[i + 2:]
                        break
                i += 1
        chars += len(line)
    print(chars)


def part3():
    lines = data.copy()
    chars = 0
    for line in lines:
        change = True
        while change:
            change = False
            i = 0
            while i < len(line) - 1:
                if line[i].isdigit():
                    if line[i + 1].isalpha():
                        change = True
                        line = line[:i] + line[i + 2:]
                        break
                elif line[i].isalpha():
                    if line[i + 1].isdigit():
                        change = True
                        line = line[:i] + line[i + 2:]
                        break
                i += 1
        chars += len(line)
    print(chars)


part1()
part2()
part3()
