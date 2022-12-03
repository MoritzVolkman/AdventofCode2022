def part1():
    rucksacks = open("input.txt").read().split("\n")
    priority = 0
    for rucksack in rucksacks:
        compartment1 = ""
        compartment2 = ""
        i = 0
        for item in rucksack:
            if i < (len(rucksack)/2):
                compartment1 += item
            if (len(rucksack)/2) <= i < len(rucksack):
                compartment2 += item
            i += 1
            if item in compartment1 and item in compartment2:
                priority += get_priority(item)
                print(f"Item: {item} Priority: {get_priority(item)}")
                break
        print(f"Rucksack Compartment1: {compartment1}, Compartment2: {compartment2}")
        print(f"Sum of Priority: {priority}")


def part2():
    rucksacks = open("input.txt").read().split("\n")
    priority = 0
    i = 0
    rucksack1 = ""
    rucksack2 = ""
    rucksack3 = ""
    for rucksack in rucksacks:
        if i == 0:
            rucksack1 = rucksack
        elif i == 1:
            rucksack3 = rucksack
        else:
            rucksack2 = rucksack
        i += 1
        if i > 2:
            i = 0
            for item in rucksack:
                if item in rucksack1 and item in rucksack2 and item in rucksack3:
                    print(f"item: {item}")
                    priority += get_priority(item)
                    break
            rucksack1 = ""
            rucksack2 = ""
            rucksack3 = ""
    print(priority)


def get_priority(char):
    if 97 <= ord(char) <= 122:
        return ord(char) - 96
    elif 65 <= ord(char) <= 90:
        return ord(char) - 38


if __name__ == "__main__":
    part1()
    part2()
