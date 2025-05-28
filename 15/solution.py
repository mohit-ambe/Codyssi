file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

artifacts = list(map(int, [line.split()[2] for line in data if line]))
codes = {int(line.split()[2]):line.split()[0] for line in data[:-3] if line}


def build_bst(nodes):
    tree = {'':nodes[0]}
    layers = 0

    for n in nodes[1:]:
        path = ''
        while path in tree:
            if n > tree[path]:
                path += 'R'
            else:
                path += 'L'
        tree[path] = n
        layers = max(layers, len(path) + 1)

    return layers, sorted(tree.items(), key=lambda n:(len(n[0]), n[0]))


def part1():
    global artifacts

    layers, tree = build_bst(artifacts[:-2].copy())

    layer_max = 0
    for i in range(0, layers):
        layer_max = max(layer_max, sum([v for k, v in tree if len(k) == i]))

    print(layer_max * layers)


def part2():
    global artifacts, codes

    layers, tree = build_bst(artifacts[:-2].copy())

    tree = {k:v for k, v in tree}

    path = ''
    sequence = []
    while path in tree:
        sequence.append(codes[tree[path]])
        if 500_000 > tree[path]:
            path += 'R'
        else:
            path += 'L'

    print('-'.join(sequence))


def part3():
    global artifacts, codes
    layers, tree = build_bst(artifacts[:-2].copy())
    tree = {v:k for k, v in tree}

    # get the tree position for the two artifacts
    a1, a2 = [tree[int(d.split()[2])] for d in data[-2:]]
    # find the largest common path
    i = min(len(a1), len(a2))
    while a1[:i] != a2[:i]:
        i -= 1

    # get the code of the id of the path
    tree = {k:v for v, k in tree.items()}
    print(codes[tree[a1[:i]]])


part1()
part2()
part3()
