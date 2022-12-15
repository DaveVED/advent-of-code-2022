from typing import List


def build_elfs(file_path: str) -> List[List[int]]:
    """Builds a list of lists of integers representing the elves and their calorie counts from the specified input file.

    Args:
        file_path: The path to the input file.

    Returns:
        A list of lists of integers representing the elves and their calorie counts.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

        elfs = []
        elf_calories = []
        for index, line in enumerate(lines):
            line_strip = line.strip()
            if line_strip == "":
                elfs.append(elf_calories)
                elf_calories = []
            else:
                elf_calories.append(int(line))
                if index == len(lines) - 1:
                    elfs.append(elf_calories)
                    elf_calories = []

    return elfs


def find_richest_elf(elfs: List[List[int]]) -> int:
    """Finds the elf with the highest total number of calories.

    Args:
        elfs: A list of lists of integers representing the elves and their calorie counts.

    Returns:
        An integer representing the total number of calories consumed by the richest elf.
    """
    richest_elf = -1
    for elf in elfs:
        elf_total_calories = sum(elf)
        if elf_total_calories > richest_elf:
            richest_elf = elf_total_calories
    return richest_elf


def find_top_3_elfs(elfs: List[List[int]]) -> int:
    """Finds the elves with the top 3 highest total numbers of calories.

    Args:
        elfs: A list of lists of integers representing the elves and their calorie counts.

    Returns:
        An integer representing the total number of calories consumed by the top 3 richest elves.
    """
    riches_elfs = []
    for elf in elfs:
        elf_total_calories = sum(elf)
        if len(riches_elfs) <= 2:
            riches_elfs.append(elf_total_calories)
            if len(riches_elfs) == 2:
                riches_elfs.sort(reverse=True)
        else:
            if any(elf_total_calories > calorie for calorie in riches_elfs):
                riches_elfs.append(elf_total_calories)
                riches_elfs.sort(reverse=True)
                riches_elfs.pop()
    return sum(riches_elfs)
