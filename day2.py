def part1():
    strategy = open("input.txt").read().split("\n")
    points = 0
    my_points = 0
    points_enemy = 0
    for duel in strategy:
        if "A" in duel:
            points_enemy = 1
        elif "B" in duel:
            points_enemy = 2
        elif "C" in duel:
            points_enemy = 3
        if "X" in duel:
            my_points = 1
        elif "Y" in duel:
            my_points = 2
        elif "Z" in duel:
            my_points = 3

        if my_points == points_enemy:
            points += 3
        elif (my_points == 1 and points_enemy == 3) or (my_points == 2 and points_enemy == 1) or (
                my_points == 3 and points_enemy == 2):
            points += 6
        points += my_points
    print("points part 1: ", points)


def part2():
    strategy = open("input.txt").read().split("\n")
    points = 0
    my_points = 0
    for duel in strategy:
        if "X" in duel:
            if "A" in duel:
                my_points = 3
            elif "B" in duel:
                my_points = 1
            elif "C" in duel:
                my_points = 2
            points += my_points
        elif "Y" in duel:
            if "A" in duel:
                my_points = 1
            elif "B" in duel:
                my_points = 2
            elif "C" in duel:
                my_points = 3
            points += 3
            points += my_points
        elif "Z" in duel:
            if "A" in duel:
                my_points = 2
            elif "B" in duel:
                my_points = 3
            elif "C" in duel:
                my_points = 1
            points += 6
            points += my_points
    print("points part 2: ", points)


if __name__ == "__main__":
    part1()
    part2()
