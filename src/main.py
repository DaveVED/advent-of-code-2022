#!/usr/bin/env python3
import elf
import rps
import util
import rucksack

from elf import Elf
from typing import List


def main():
    # Build the Elfs.
    input = util.parse_input("test/files/day1/input.txt")
    elfs = elf.build_elfs(input)

    # Find top 3 elfs, with most calories.
    smart_elfs = elf.find_top_3_elfs(elfs)
    smart_elf_calore_count = sum(smart_elfs)
    print(f"--- Day 1: Calorie Counting --- \n {smart_elf_calore_count}")

    # Build Rocker Paper Siscor File.
    input = util.parse_input("test/files/day2/input.txt")
    rock_paper_scissors_score = rps.calculate_rock_paper_scissors_score(input)
    print(f"--- Day 2: Rock Paper Scissors --- \n {rock_paper_scissors_score}")

    # Rucksack Reorganization
    input = util.parse_input("test/files/day3/input.txt")
    filterd_rucksacks = rucksack.filterd_rucksacks_sum(input)
    print(f"--- Day 3: Rucksack Reorganization --- \n{filterd_rucksacks}")


if __name__ == "__main__":
    main()
