file = open("input.txt", "r")
data = [line.strip() for line in file.readlines()]
file.close()

nums = [line.split() for line in data]
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^'


def to_dec(num, base):
    number = 0
    for i, n in enumerate(num[::-1]):
        number += chars.index(n) * base ** i
    return number


def from_dec(num, base):
    i = len(chars) - 1
    number = ''
    while num:
        if num > base ** i:
            number += chars[num // (base ** i)]
            num %= base ** i
        i -= 1
    return number


converted = [to_dec(num, int(base)) for num, base in nums]


def part1():
    print(max(converted))


def part2():
    print(from_dec(sum(converted), 68))


def part3():
    total = sum(converted)
    i = 2
    while True:
        if total <= i ** 4:
            print(i)
            break
        i += 1


part1()
part2()
part3()
