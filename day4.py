def part1():
    assignments = open("input.txt").read().split("\n")
    area1_start = 0
    area1_end = 0
    area2_start = 0
    area2_end = 0
    pairs = 0
    for assignment in assignments:
        area = ""
        which_sector = 1
        position = 0
        for char in assignment:
            if position == len(assignment) - 1:
                area += char
                area2_end = int(area)
                if (area1_start >= area2_start and area1_end <= area2_end) or (
                        area1_start <= area2_start and area1_end >= area2_end):
                    pairs += 1
                which_sector = 0
            elif char.isnumeric() and char != ",":
                area += char
            else:
                if which_sector == 1:
                    area1_start = int(area)
                elif which_sector == 2:
                    area1_end = int(area)
                elif which_sector == 3:
                    area2_start = int(area)
                which_sector += 1
                area = ""
            position += 1
    print(pairs)


def part2():
    assignments = open("input.txt").read().split("\n")
    area = []
    overlap = 0
    for line in assignments:
        position = 0
        placeholder = ""
        for char in line:
            if position == len(line) - 1:
                placeholder += char
                area.append(int(placeholder))
            elif char.isnumeric() and char != ",":
                placeholder += char
            else:
                if placeholder != "":
                    area.append(int(placeholder))
                    placeholder = ""
            position += 1
    for i in range(0, int(len(area) / 4)):
        print(area)
        start1 = area.pop(0)
        end1 = area.pop(0)
        start2 = area.pop(0)
        end2 = area.pop(0)
        range1 = []
        range2 = []
        for j in range(0, (end1 - start1) + 1):
            range1.append(start1+j)
        for k in range(0, (end2 - start2) + 1):
            range2.append(start2+k)
        overlap_list = [value for value in range1 if value in range2]
        if len(overlap_list):
            overlap += 1
        print(overlap_list)
    print(overlap)


if __name__ == "__main__":
    part1()
    part2()
