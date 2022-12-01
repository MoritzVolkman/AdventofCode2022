
if __name__ == '__main__':
    calories = []
    elves = open("input.txt").read().split("\n\n")
    for entry in elves:
        calories.append(sum(int(num) for num in entry.split("\n")))
    print(max(calories))
    print(sum(sorted(calories, reverse=True)[:3]))