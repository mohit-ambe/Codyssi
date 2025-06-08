file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

instructions = data[:-2]
twists = [*data[-1] + " "]
G_SIZE = 80

orientations = {'L':{'L':['F', 0], 'F':['R', 0], 'R':['B', 0], 'B':['L', 0], 'U':['U', 3], 'D':['D', 1]},
                'U':{'B':['D', 2], 'D':['F', 0], 'F':['U', 2], 'U':['B', 0], 'L':['L', 3], 'R':['R', 1]},
                'R':{'L':['B', 0], 'B':['R', 0], 'R':['F', 0], 'F':['L', 0], 'U':['U', 1], 'D':['D', 3]},
                'D':{'B':['U', 0], 'U':['F', 2], 'F':['D', 0], 'D':['B', 2], 'L':['L', 1], 'R':['R', 3]}}


def twist(faces, direction):
    if direction == " ":
        return faces
    return {x:rotate(faces[y], r) for x, (y, r) in orientations[direction].items()}


def rotate(face, n):
    if type(face) is not list:
        return face
    # clockwise rotation = transpose + reverse of rows
    for _ in range(n):
        face = [list(f)[::-1] for f in list(zip(*face))]
    return face


def dom_sum_prod(faces):
    total = 1
    for f in faces:
        max_row = max([sum(r) for r in faces[f]])
        max_col = max([sum(c) for c in list(zip(*faces[f]))])
        total *= max(max_row, max_col)
    return total


def part1():
    faces = {_:0 for _ in "FBLRDU"}
    for i, r in zip(instructions, twists):
        v = int(i.split()[-1])
        if "FACE" in i:
            faces['F'] += v * G_SIZE * G_SIZE
        else:
            faces['F'] += v * G_SIZE
        faces = twist(faces, r)
    absorptions = sorted(faces.values())
    print(absorptions[-1] * absorptions[-2])


def part2():
    faces = {_:[[1 for _ in range(G_SIZE)] for _ in range(G_SIZE)] for _ in "FBLRDU"}
    for i, r in zip(instructions, twists):
        v = int(i.split()[-1])
        index = i.split()[1]
        index = index if not index.isdigit() else int(index) - 1
        if "FACE" in i:
            faces['F'] = [[(faces['F'][x][y] + v - 1) % 100 + 1 for y in range(G_SIZE)] for x in range(G_SIZE)]
        elif "ROW" in i:
            faces["F"][index] = [(faces["F"][index][y] + v - 1) % 100 + 1 for y in range(G_SIZE)]
        elif "COL" in i:
            [row.__setitem__(index, (row[index] + v - 1) % 100 + 1) for row in faces['F']]
        faces = twist(faces, r)
    print(dom_sum_prod(faces))


def part3():
    faces = {_:[[1 for _ in range(G_SIZE)] for _ in range(G_SIZE)] for _ in "FBLRDU"}
    for i, r in zip(instructions, twists):
        v = int(i.split()[-1])
        index = i.split()[1]
        index = index if not index.isdigit() else int(index) - 1
        if "FACE" in i:
            faces['F'] = [[(faces['F'][x][y] + v - 1) % 100 + 1 for y in range(G_SIZE)] for x in range(G_SIZE)]
        elif "ROW" in i:
            for f in "LRFB":
                faces[f][index] = [(faces[f][index][y] + v - 1) % 100 + 1 for y in range(G_SIZE)]
        elif "COL" in i:
            [row.__setitem__(index, (row[index] + v - 1) % 100 + 1) for row in faces['F']]
            [row.__setitem__(index, (row[index] + v - 1) % 100 + 1) for row in faces['D']]
            index = G_SIZE - 1 - index
            [row.__setitem__(index, (row[index] + v - 1) % 100 + 1) for row in faces['B']]
            [row.__setitem__(index, (row[index] + v - 1) % 100 + 1) for row in faces['U']]
        faces = twist(faces, r)
    print(dom_sum_prod(faces))


part1()
part2()
part3()
