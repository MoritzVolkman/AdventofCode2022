def part1(individual_chars):
    input = open("input.txt").read()
    last_chars = []
    position = 0
    for char in input:
        position += 1
        last_chars.append(char)
        if position > individual_chars:
            last_chars.pop(0)
            if len(set(last_chars)) >= individual_chars:
                print("Start of Package Marker Detected, Position = ", position)
                break


if __name__ == "__main__":
    part1(4)
    part1(14)
