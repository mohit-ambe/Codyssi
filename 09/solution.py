file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

accounts = {}
trades = []
i = 0
while data[i]:
    x, y = data[i].split(" HAS ")
    accounts[x] = int(y)
    i += 1
i += 1
while i < len(data):
    _, start, _, end, _, value = data[i].split()
    trades.append((start, end, int(value)))
    i += 1


def part1():
    acc = accounts.copy()
    for s, e, v in trades:
        acc[s] -= v
        acc[e] += v
    print(sum(sorted(acc.values())[-3:]))


def part2():
    acc = accounts.copy()
    for s, e, v in trades:
        v = min(v, acc[s])
        acc[s] -= v
        acc[e] += v
    print(sum(sorted(acc.values())[-3:]))


def part3():
    acc = accounts.copy()
    debt = []
    for s, e, v in trades:
        if v < acc[s]:
            acc[s] -= v
            acc[e] += v
        else:
            acc[e] += acc[s]
            debt.append((s, e, v - acc[s]))
            acc[s] = 0
        change = True
        while change:
            change = False
            for d, (debtor, creditor, owed) in enumerate(debt):
                if acc[debtor] == 0:
                    continue
                change = True
                if owed < acc[debtor]:
                    acc[debtor] -= owed
                    acc[creditor] += owed
                    debt.pop(d)
                else:
                    acc[creditor] += acc[debtor]
                    debt.pop(d)
                    debt.insert(0, (debtor, creditor, owed - acc[debtor]))
                    acc[debtor] = 0
                break

    print(sum(sorted(acc.values())[-3:]))


part1()
part2()
part3()
