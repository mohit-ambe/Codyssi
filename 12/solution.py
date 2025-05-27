file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

blank_one = data.index("")
blank_two = data.index("", blank_one + 1)

grid = [list(map(int, line.split())) for line in data[:blank_one]]
instructions = data[blank_one + 1:blank_two].copy()
actions = data[blank_two + 1:].copy()


def shift(grid, axis, index, amount):
    if axis == "COL":
        grid = list(zip(*grid))

    grid[index] = grid[index][-amount:] + grid[index][:-amount]

    if axis == "COL":
        grid = list(zip(*grid))
    return [list(g) for g in grid]


def math(grid, op, amount, axis, index):
    if axis == "COL":
        grid = list(zip(*grid))

    lines = [*range(len(grid))] if axis == "ALL" else [index]

    for i in lines:
        if op == 'ADD':
            grid[i] = [g + amount for g in grid[i]]
        elif op == 'SUB':
            grid[i] = [g - amount for g in grid[i]]
        elif op == 'MULTIPLY':
            grid[i] = [g * amount for g in grid[i]]
        grid[i] = [g % 1073741824 for g in grid[i]]

    if axis == "COL":
        grid = list(zip(*grid))

    return [list(g) for g in grid]


def process_instructions(grid, instr):
    for line in instr:
        if 'SHIFT' in line:
            _, ax, i, _, amt = line.split()
            i, amt = list(map(int, [i, amt]))
            grid = shift(grid, ax, i - 1, amt)
        else:
            if 'ALL' in line:
                op, amt, _ = line.split()
                amt = int(amt)
                grid = math(grid, op, amt, 'ALL', -1)
            else:
                op, amt, ax, i = line.split()
                i, amt = list(map(int, [i, amt]))
                grid = math(grid, op, amt, ax, i - 1)
    return grid


def part1():
    global grid, instructions

    p1grid = grid.copy()
    p1grid = process_instructions(p1grid, instructions)

    print(max(max([sum(g) for g in p1grid]), max([sum(g) for g in list(zip(*p1grid))])))


def part2():
    global grid, instructions

    p2grid = grid.copy()
    fc_instr = instructions.copy()
    take = ''

    for line in actions:
        if line == 'TAKE':
            take = fc_instr.pop(0)
        elif line == 'CYCLE':
            fc_instr.append(take)
        elif line == 'ACT':
            p2grid = process_instructions(p2grid, [take])

    print(max(max([sum(g) for g in p2grid]), max([sum(g) for g in list(zip(*p2grid))])))


def part3():
    global grid, instructions

    p3grid = grid.copy()
    fc_instr = instructions.copy()
    take = ''

    while fc_instr:
        for line in actions:
            if line == 'TAKE':
                if fc_instr:
                    take = fc_instr.pop(0)
                else:
                    break
            elif line == 'CYCLE':
                fc_instr.append(take)
            elif line == 'ACT':
                p3grid = process_instructions(p3grid, [take])

    print(max(max([sum(g) for g in p3grid]), max([sum(g) for g in list(zip(*p3grid))])))


part1()
part2()
part3()
