import pytest
import aoc.day1.calorie_counting as calorie_counting

from typing import List
from answers.calorie_counting_answers import CalorieCountingAnswers


@pytest.fixture
def easy_elfs() -> List[List[int]]:
    """Returns a list of lists of integers, representing the elves and their calorie counts in the "easy" test case."""
    return calorie_counting.build_elfs("test/files/day1/input_easy.txt")


@pytest.fixture
def hard_efls() -> List[List[int]]:
    """Returns a list of lists of integers, representing the elves and their calorie counts in the "hard" test case."""
    return calorie_counting.build_elfs("test/files/day1/input.txt")


def test_build_elfs(easy_elfs: List[List[int]], hard_efls: List[List[int]]) -> None:
    """Tests the `build_elfs` function by comparing its output to the expected values in the `CalorieCountingAnswers` class."""
    assert easy_elfs == CalorieCountingAnswers.BUILD_ELF_EASY
    assert hard_efls == CalorieCountingAnswers.BUILD_ELF_HARD


def test_find_top_3_elfs(easy_elfs: List[List[int]], hard_efls: List[List[int]]) -> None:
    """Tests the `find_top_3_elfs` function by comparing its output to the expected values in the `CalorieCountingAnswers` class."""
    assert calorie_counting.find_top_3_elfs(
        easy_elfs) == CalorieCountingAnswers.TOP_3_ELF_HARD
    assert calorie_counting.find_top_3_elfs(
        hard_efls) == CalorieCountingAnswers.TOP_3_ELF_EASY
