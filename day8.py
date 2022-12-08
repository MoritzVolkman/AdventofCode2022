def part1(grid):
    position_x = 0
    position_y = 0
    visibility = [[0] * len(forest[0]) for x in range(len(forest))]
    highest_tree_x = 0
    highest_tree_y = [0 for x in range(len(forest[0]))]
    # Visibility from the left and top
    for row in grid:
        for tree in row:
            if int(tree) > highest_tree_y[position_x] or position_y == 0:
                highest_tree_y[position_x] = int(tree)
                visibility[position_y][position_x] = 1
            if int(tree) > highest_tree_x or position_x == 0:
                highest_tree_x = int(tree)
                visibility[position_y][position_x] = 1
            position_x += 1
            if position_x >= len(row):
                position_x = 0
                highest_tree_x = 0
        position_y += 1
        if position_y >= len(forest):
            position_y = 0
            highest_tree_y = [0 for x in range(len(forest[0]))]
    highest_tree_x = 0
    highest_tree_y = [0 for x in range(len(forest[0]))]
    # Visibility from the right and bottom
    for row in reverse_upside_down(grid):
        for tree in row:
            if int(tree) > highest_tree_y[position_x] or position_y == 0:
                highest_tree_y[position_x] = int(tree)
                visibility[(len(grid)-1)-position_y][(len(row)-1)-position_x] = 1
            if int(tree) > highest_tree_x or position_x == 0:
                highest_tree_x = int(tree)
                visibility[(len(grid)-1)-position_y][(len(row)-1)-position_x] = 1
            position_x += 1
            if position_x >= len(row):
                position_x = 0
                highest_tree_x = 0
        position_y += 1
        if position_y >= len(forest):
            position_y = 0
    print("Trees visible from the outside: ", sum(row.count(1) for row in visibility))


def part2(grid):
    grid_left = []
    grid_top = []
    score_left = []
    score_top_ = []
    final_score = [[0] * len(grid[0]) for x in range(len(grid))]
    # Viewing Distance to the Right
    score_right = (check_the_view(grid))
    # Viewing Distance to the Left
    for sublist in grid:
        grid_left.append(list(reversed(sublist)))
    score_left_ = (check_the_view(grid_left))
    for sublist in score_left_:
        score_left.append(list(reversed(sublist)))
    # Viewing Distance to the Bottom
    score_bottom_ = (check_the_view(list(map(list, zip(*grid)))))
    score_bottom = list(map(list, zip(*score_bottom_)))
    # Viewing Distance to the Top
    for sublist in list(map(list, zip(*grid))):
        grid_top.append(list(reversed(sublist)))
    score_top__ = (check_the_view(grid_top))
    for sublist in score_top__:
        score_top_.append(list(reversed(sublist)))
    score_top = list(map(list, zip(*score_top_)))
    position_x = 0
    position_y = 0
    for line in score_right:
        for entry in line:
            final_score[position_y][position_x] = score_right[position_y][position_x] * score_left[position_y][position_x] * score_top[position_y][position_x] * score_bottom[position_y][position_x]
            position_x += 1
            if position_x >= len(line):
                position_x = 0
        position_y += 1
        if position_y >= len(score_right):
            position_y = 0
    print("Best possible View-Score: ", max(max(x) for x in final_score))


def check_the_view(grid):
    score = [[0] * len(grid[0]) for x in range(len(grid))]
    position_x = 0
    position_y = 0
    counter = 0
    for row in grid:
        for tree in row:
            if position_x != len(row) - 1:
                for i in range(1, len(row) - position_x):
                    tree_right = grid[position_y][position_x + i]
                    if tree_right < int(tree):
                        counter += 1
                    else:
                        counter += 1
                        break
                score[position_y][position_x] = counter
                position_x += 1
                counter = 0
            else:
                counter = 0
                position_x = 0
        position_y += 1
        if position_y >= len(grid):
            position_y = 0
    return score


def reverse_upside_down(input_list):
    # Flips 2D-List and reverses it
    input_list = list(map(lambda x: list(reversed(x)), reversed(input_list)))
    return input_list


if __name__ == "__main__":
    forest = open("input.txt").read().split("\n")
    position_x = 0
    position_y = 0
    grid = [[0] * len(forest[0]) for x in range(len(forest))]
    for line in forest:
        for tree in line:
            grid[position_y][position_x] = int(tree)
            position_x += 1
            if position_x >= len(line):
                position_x = 0
        position_y += 1
        if position_y >= len(forest):
            position_y = 0
    part1(grid)
    part2(grid)
