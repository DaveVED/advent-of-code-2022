#!/usr/bin/env python3
import day1.calorie_counting as day1
import day2.rock_paper_scissors as day2
import day3.rucksack as day3
import day4.camp_cleanup as day4

CALORIE_COUNTING_ANSWER_PART1 = 70613
CALORIE_COUNTING_ANSWER_PART2 = 205805
ROCK_PAPER_SCISSORS_ANSWER_PART1 = 14163
ROCK_PAPER_SCISSORS_ANSWER_PART2 = 12091
RUCKSACK_ANSWER_PART1 = 8515
RUCKSACK_ANSWER_PART2 = 2434
CAMP_CLEAN_UP_ANSWER_PART1 = 500
CAMP_CLEAN_UP_ANSWER_PART2 = 815


def main():
    # Day 1: Calorie Counting
    print("--- Day 1: Calorie Counting ---")
    elfs = day1.build_elfs("test/files/day1/input.txt")
    single_most_calories = day1.find_richest_elf(elfs)
    assert single_most_calories == CALORIE_COUNTING_ANSWER_PART1
    print(f"--- PASS. Day 1. Part 1 Answer: {single_most_calories} ---")
    top_3_elfs = day1.find_top_3_elfs(elfs)
    print(f"--- PASS. Day 1. Part 2 Answer: {top_3_elfs} ---")
    assert top_3_elfs == CALORIE_COUNTING_ANSWER_PART2

    # Day 2: Rock Paper Scissors
    print("\n--- Day 2: Rock Paper Scissors ---")
    rock_paper_scissors_score = day2.calculate_rock_paper_scissors_score(
        "test/files/day2/input.txt", False)
    assert rock_paper_scissors_score == ROCK_PAPER_SCISSORS_ANSWER_PART1
    print(f"--- PASS. Day 2. Part 1 Answer: {rock_paper_scissors_score} ---")
    rock_paper_scissors_score = day2.calculate_rock_paper_scissors_score(
        "test/files/day2/input.txt", True)
    assert rock_paper_scissors_score == ROCK_PAPER_SCISSORS_ANSWER_PART2
    print(f"--- PASS. Day 2. Part 2 Answer: {rock_paper_scissors_score} ---")

    # Day 3: Day 3: Rucksack Reorganization
    print("\n--- Day 3: Rucksack Reorganization ---")
    priority_rucksack_sum = day3.calculate_rucksack_priority_sum(
        "test/files/day3/input.txt")
    assert priority_rucksack_sum == RUCKSACK_ANSWER_PART1
    print(f"--- PASS. Day 3. Part 1 Answer: {priority_rucksack_sum} ---")
    badge_sum = day3.calculate_badge_sum("test/files/day3/input.txt")
    assert badge_sum == RUCKSACK_ANSWER_PART2
    print(f"--- PASS. Day 3. Part 2 Answer: {badge_sum} ---")

    print(f"\n--- Day 4: Camp Cleanup ---")
    fully_contain_count = day4.find_overlap_count(
        "test/files/day4/input.txt", False)
    assert fully_contain_count == CAMP_CLEAN_UP_ANSWER_PART1
    print(f"--- PASS. Day 4. Part 1 Answer: {fully_contain_count} ---")
    full_overlap_count = day4.find_overlap_count(
        "test/files/day4/input.txt", True)
    assert full_overlap_count == CAMP_CLEAN_UP_ANSWER_PART2
    print(f"--- PASS. Day 4. Part 2 Answer: {full_overlap_count} ---")


if __name__ == "__main__":
    main()
