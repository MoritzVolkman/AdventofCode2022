def part1(instruction):
    h_x = 0
    h_y = 0
    t_x = 0
    t_y = 0
    visited = []
    for line in instruction:
        direction = line.split()[0]
        distance = int(line.split()[1])
        for i in range(distance):
            if direction == "R":
                h_x += 1
            elif direction == "L":
                h_x -= 1
            elif direction == "U":
                h_y += 1
            elif direction == "D":
                h_y -= 1
            if abs(h_x - t_x) > 1:
                if direction == "R":
                    t_x = h_x - 1
                elif direction == "L":
                    t_x = h_x + 1
                if h_y != t_y:
                    t_y = h_y
            if abs(h_y - t_y) > 1:
                if direction == "U":
                    t_y = h_y - 1
                elif direction == "D":
                    t_y = h_y + 1
                if h_x != t_x:
                    t_x = h_x
            visited.append(f"[{t_x}, {t_y}]")
    print("Different Spots visited by Tail Part 1: ", len(set(visited)))


def part2(instruction):
    h_x = 0
    h_y = 0
    t_x = [0 for i in range(9)]
    t_y = [0 for i in range(9)]
    last_x = [0 for i in range(9)]
    last_y = [0 for i in range(9)]
    visited_p2 = []
    for line in instruction:
        direction = line.split()[0]
        distance = int(line.split()[1])
        for x in range(distance):
            if direction == "R":
                h_x += 1
            elif direction == "L":
                h_x -= 1
            elif direction == "U":
                h_y += 1
            elif direction == "D":
                h_y -= 1
            for i in range(9):
                last_x[i] = t_x[i]
                last_y[i] = t_y[i]
                if i == 0:
                    if abs(h_x - t_x[i]) > 1:
                        if direction == "R":
                            t_x[i] = h_x - 1
                        elif direction == "L":
                            t_x[i] = h_x + 1
                        if h_y != t_y[i]:
                            t_y[i] = h_y
                    if abs(h_y - t_y[i]) > 1:
                        if direction == "U":
                            t_y[i] = h_y - 1
                        elif direction == "D":
                            t_y[i] = h_y + 1
                        if h_x != t_x[i]:
                            t_x[i] = h_x
                else:
                    if abs(t_x[i-1] - t_x[i]) > 1 or abs(t_y[i-1] - t_y[i]) > 1:
                        t_x[i] = last_x[i-1]
                        t_y[i] = last_y[i-1]
                    if i == 8:
                        visited_p2.append(f"[{t_x[i]}, {t_y[i]}]")
                        print(f"[{t_x[i]}, {t_y[i]}]")
                    print(f"Positions: HEAD: {h_x},{h_y} TAIL: {t_x}, {t_y}")
    print("Different Spots visited by Tail Part 2: ", len(set(visited_p2)))


if __name__ == "__main__":
    instruction = open("input.txt").read().split("\n")
    part1(instruction)
    part2(instruction)
