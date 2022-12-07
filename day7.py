from collections import defaultdict


def part1():
    cli_input = open("input.txt").read().split("\n")
    sizes = defaultdict(int)
    path = []
    sum = 0
    big_directories = []
    for line in cli_input:
        if "$ cd" in line:
            new_path = line[5:]
            if new_path == "/":
                path.append("/")
            elif new_path == "..":
                path.pop()
            else:
                if path[-1] != "/":
                    path.append(f"{path[-1]}/{new_path}")
                else:
                    path.append(f"{path[-1]}{new_path}")
        if line[0].isnumeric():
            for p in path:
                sizes[p] += int(line.split()[0])
    for entry in sizes:
        if sizes[entry] <= 100000:
            sum += sizes[entry]
        if sizes[entry] >= 8381165:
            big_directories.append(sizes[entry])
    print("Sum Part 1: ", sum)
    print("Directory Size Part 2: ", sorted(set(big_directories))[0])


if __name__ == "__main__":
    part1()
