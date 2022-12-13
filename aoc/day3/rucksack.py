from typing import Set


def filterd_rucksacks_sum(rucksacks: str) -> Set:
    sum = 0
    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        compartment_one = rucksack[: len(rucksack) // 2]
        compartment_two = rucksack[len(rucksack) // 2 :]
        for item in compartment_one:
            if item in compartment_two:
                priority = get_priority(item)
                print(
                    "Item Priority - ",
                    item,
                    "-->",
                    priority,
                    " Previous Sum - ",
                    sum,
                    " New Sum - ",
                    sum + priority,
                )
                sum = sum + priority
                break

    return sum


def get_priority(s: str) -> int:
    priority = 0
    for ch in s:
        ascii_val = ord(ch)

        if "a" <= ch <= "z":
            priority += ascii_val - 96
        elif "A" <= ch <= "Z":
            priority += ascii_val - 38

    return priority
