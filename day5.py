import re


def part1():
    crate = [["D", "H", "N", "Q", "T", "W", "V", "B"],
             ["D", "W", "B"],
             ["T", "S", "Q", "W", "J", "C"],
             ["F", "J", "R", "N", "Z", "T", "P"],
             ["G", "P", "V", "J", "M", "S", "T"],
             ["B", "W", "F", "T", "N"],
             ["B", "L", "D", "Q", "F", "H", "V", "N"],
             ["H", "P", "F", "R"],
             ["Z", "S", "M", "B", "L", "N", "P", "H"]]
    instructions = open("input.txt").read().split("\n")
    for line in instructions:
        instruction = re.findall(r'\d+', line)
        amount = int(instruction[0])
        start = int(instruction[1])
        end = int(instruction[2])
        for i in range(amount):
            transfer = crate[start-1].pop()
            crate[end-1].append(transfer)
    print(crate)


def part2():
    crate = [["D", "H", "N", "Q", "T", "W", "V", "B"],
             ["D", "W", "B"],
             ["T", "S", "Q", "W", "J", "C"],
             ["F", "J", "R", "N", "Z", "T", "P"],
             ["G", "P", "V", "J", "M", "S", "T"],
             ["B", "W", "F", "T", "N"],
             ["B", "L", "D", "Q", "F", "H", "V", "N"],
             ["H", "P", "F", "R"],
             ["Z", "S", "M", "B", "L", "N", "P", "H"]]
    instructions = open("input.txt").read().split("\n")
    for line in instructions:
        instruction = re.findall(r'\d+', line)
        amount = int(instruction[0])
        start = int(instruction[1])
        end = int(instruction[2])
        transfer = []
        for i in range(amount):
            transfer.append(crate[start-1].pop())
        for i in range(amount):
            crate[end-1].append(transfer.pop())
    print(crate)


if __name__ == "__main__":
    part1()
    part2()
