from typing import List


def calculate_rucksack_priority_sum(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()

        priority = 0
        for line in lines:
            rucksack = line.strip()
            compartment_one = rucksack[: len(rucksack) // 2]
            compartment_two = rucksack[len(rucksack) // 2:]
            for item in compartment_one:
                if item in compartment_two:
                    priority = priority + get_priority(item)
                    break
    return priority


def calculate_badge_sum(file_path: str) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()

        rucksacks = []
        badges = []
        for index, line in enumerate(lines):
            rucksack = line.strip()
            if (index + 1) % 3 == 0:
                rucksacks.append(rucksack)
                common_badge = find_common_badge(rucksacks)
                badges.append(common_badge)
                rucksacks = []
                continue

            rucksacks.append(rucksack)

    return sum(get_priority(badge[0]) for badge in badges)


def find_common_badge(rucksacks: List[str]) -> List[str]:
    badges = set(rucksacks[0])
    for rucksack in rucksacks[1:]:
        badges &= set(rucksack)
    return list(badges)


def get_priority(item: str) -> int:
    priority = 0
    for char in item:
        ascii_val = ord(char)

        if "a" <= char <= "z":
            priority += ascii_val - 96
        elif "A" <= char <= "Z":
            priority += ascii_val - 38

    return priority
