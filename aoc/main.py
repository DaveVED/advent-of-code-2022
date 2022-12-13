#!/usr/bin/env python3
import day1.calorie_counting as day1
import day2.rock_paper_scissors as day2

CALORIE_COUNTING_ANSWER_PART1 = 70613
CALORIE_COUNTING_ANSWER_PART2 = 205805
ROCK_PAPER_SCISSORS_ANSWER_PART1 = 14163
ROCK_PAPER_SCISSORS_ANSWER_PART2 = 12091


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


if __name__ == "__main__":
    main()
