from typing import List


def calculate_rucksack_priority_sum(file_path: str) -> int:
    """Calculates the total priority of the items in a rucksack.

    This function calculates the total priority of the items in a rucksack by
    reading a file containing the rucksack's items, splitting the items into
    two compartments, and summing the priorities of the items that appear in
    both compartments.

    Args:
        file_path: The path to the file containing the rucksack's items.

    Returns:
        The total priority of the items in the rucksack.
    """
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
    """Calculates the total priority of the badges in a file.

    This function calculates the total priority of the badges in a file by
    reading the file, splitting it into groups of three rucksacks, finding the
    common badges for each group, and summing the priorities of the badges.

    Args:
        file_path: The path to the file containing the rucksacks.

    Returns:
        The total priority of the badges in the file.
    """
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
    """Returns a list of badges that are common to all rucksacks.

    This function takes a list of rucksacks and returns a list of badges that
    are common to all of the rucksacks.

    Args:
        rucksacks: The list of rucksacks to search for common badges.

    Returns:
        A list of badges that are common to all of the rucksacks.
    """
    badges = set(rucksacks[0])
    for rucksack in rucksacks[1:]:
        badges &= set(rucksack)
    return list(badges)


def get_priority(item: str) -> int:
    """Returns the priority of an item.

    The priority of an item is calculated by summing the ASCII values of its
    characters, with lowercase characters having a higher priority than
    uppercase characters.

    Args:
        item: The item to calculate the priority for.

    Returns:
        The calculated priority of the item.
    """
    priority = 0
    for char in item:
        ascii_val = ord(char)

        if "a" <= char <= "z":
            priority += ascii_val - 96
        elif "A" <= char <= "Z":
            priority += ascii_val - 38

    return priority
