def part1():
    input = open("input.txt").read()
    last_chars = []
    position = 0
    for char in input:
        position += 1
        last_chars.append(char)
        if position > 4:
            last_chars.pop(0)
            if len(set(last_chars)) >= 4:
                print("Start of Package Marker Detected, Position = ", position)
                break


def part2():
    input = open("input.txt").read()
    last_chars = []
    position = 0
    for char in input:
        position += 1
        last_chars.append(char)
        if position > 14:
            last_chars.pop(0)
            if len(set(last_chars)) >= 14:
                print("Start of Message Marker Detected, Position = ", position)
                break


if __name__ == "__main__":
    part1()
    part2()
