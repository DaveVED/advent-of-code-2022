import pytest
import aoc.day3.rucksack as rucksack

RUCKSACK_PART_1_EASY = 157
RUCKSACK_PART_1_HARD = 8515
RUCKSACK_PART_2_EASY = 70
RUCKSACK_PART_2_HARD = 2434


def test_get_priority():
    """Tests the get_priority function.

    This function tests the get_priority function by calling it with a range
    of different input values and verifying that the function returns the
    expected results.
    """
    assert rucksack.get_priority("HELLO") == 182
    assert rucksack.get_priority("hElLo") == 104
    assert rucksack.get_priority("") == 0
    assert rucksack.get_priority("hello123") == 52


def test_find_common_badge():
    """Tests the find_common_badge function.

    This function tests the find_common_badge function by calling it with a
    range of different input values and verifying that the function returns
    the expected results.
    """
    rucksacks = ["abc", "def", "ghi"]
    assert rucksack.find_common_badge(rucksacks) == []

    rucksacks = ["abcdef", "defghi", "abcdhi"]
    assert rucksack.find_common_badge(rucksacks) == ['d']


def test_calculate_rucksack_priority_sum():
    """Tests the calculate_rucksack_priority_sum function.

    This function tests the calculate_rucksack_priority_sum function by calling
    it with a range of different input values and verifying that the function
    returns the expected results.
    """
    # Part 1
    assert rucksack.calculate_rucksack_priority_sum(
        "test/files/day3/input_easy.txt") == RUCKSACK_PART_1_EASY
    assert rucksack.calculate_rucksack_priority_sum(
        "test/files/day3/input.txt") == RUCKSACK_PART_1_HARD


def test_calculate_badge_sum():
    """Tests the calculate_badge_sum function.

    This function tests the calculate_badge_sum function by calling it with a
    range of different input values and verifying that the function returns
    the expected results.
    """
    assert rucksack.calculate_badge_sum(
        "test/files/day3/input_easy.txt") == RUCKSACK_PART_2_EASY
    assert rucksack.calculate_badge_sum(
        "test/files/day3/input.txt") == RUCKSACK_PART_2_HARD
