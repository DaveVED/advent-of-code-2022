import pytest
import aoc.day2.rock_paper_scissors as rock_paper_scissors

from typing import List

TOTAL_SCORE_PART_1_EASY = 15
TOTAL_SCORE_PART_1_HARD = 14163
TOTAL_SCORE_PART_2_EASY = 12
TOTAL_SCORE_PART_2_HARD = 12091


def test_match_outcome_score():
    """Test the `match_outcome_score` function with a variety of input values."""
    # Test matching outcome 'X'
    assert rock_paper_scissors.match_outcome_score("A", "X") == 3
    assert rock_paper_scissors.match_outcome_score("B", "X") == 1
    assert rock_paper_scissors.match_outcome_score("C", "X") == 2

    # Test matching outcome 'Y'
    assert rock_paper_scissors.match_outcome_score("A", "Y") == 4
    assert rock_paper_scissors.match_outcome_score("B", "Y") == 5
    assert rock_paper_scissors.match_outcome_score("C", "Y") == 6

    # Test matching outcome 'Z'
    assert rock_paper_scissors.match_outcome_score("A", "Z") == 8
    assert rock_paper_scissors.match_outcome_score("B", "Z") == 9
    assert rock_paper_scissors.match_outcome_score("C", "Z") == 7


def test_guess_outcome_score():
    """Test the `guess_outcome_score` function with a variety of input values."""
    # Test guessing outcome 'X'
    assert rock_paper_scissors.guess_outcome_score("A", "X") == 4
    assert rock_paper_scissors.guess_outcome_score("B", "X") == 1
    assert rock_paper_scissors.guess_outcome_score("C", "X") == 7

    # Test guessing outcome 'Y'
    assert rock_paper_scissors.guess_outcome_score("A", "Y") == 8
    assert rock_paper_scissors.guess_outcome_score("B", "Y") == 5
    assert rock_paper_scissors.guess_outcome_score("C", "Y") == 2

    # Test guessing outcome 'Z'
    assert rock_paper_scissors.guess_outcome_score("A", "Z") == 3
    assert rock_paper_scissors.guess_outcome_score("B", "Z") == 9
    assert rock_paper_scissors.guess_outcome_score("C", "Z") == 6


def test_calculate_rock_paper_scissors_score():
    """Test the `calculate_rock_paper_scissors_score` function with a variety of input values."""
    # Part 1
    assert rock_paper_scissors.calculate_rock_paper_scissors_score(
        "test/files/day2/input_easy.txt", "one") == TOTAL_SCORE_PART_1_EASY
    assert rock_paper_scissors.calculate_rock_paper_scissors_score(
        "test/files/day2/input.txt", "one") == TOTAL_SCORE_PART_1_HARD

    # Part 2
    assert rock_paper_scissors.calculate_rock_paper_scissors_score(
        "test/files/day2/input_easy.txt", "two") == TOTAL_SCORE_PART_2_EASY
    assert rock_paper_scissors.calculate_rock_paper_scissors_score(
        "test/files/day2/input.txt", "two") == TOTAL_SCORE_PART_2_HARD
