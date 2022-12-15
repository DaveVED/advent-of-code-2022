import pytest
import aoc.day6.tuning_trouble as tuning_trouble

from typing import List

TUNING_TROUBLE_PART1_EASY = [7, 5, 6, 10, 11]
TUNING_TROUBLE_PART1_HARD = 1542
TUNING_TROUBLE_PART2_EASY = [19, 23, 23, 29, 26]
TUNING_TROUBLE_PART2_HARD = 3153


@pytest.fixture
def easy_buffer() -> List[str]:
    """Returns a list of strings from the easy test input file."""
    with open("test/files/day6/input_easy.txt", "r") as file:
        lines = file.readlines()
    return lines


@pytest.fixture
def hard_buffer() -> str:
    """Returns a string from the hard test input file."""
    with open("test/files/day6/input.txt", "r") as file:
        lines = file.readlines()
    return lines[0]


def test_find_packet_marker(easy_buffer, hard_buffer):
    """Tests the find_packet_marker() function with easy and hard test inputs."""
    # Test find_packet_marker() with easy test inputs and substring length of 4
    for index, buffer in enumerate(easy_buffer):
        buffer = buffer.strip()
        assert tuning_trouble.find_packet_marker(
            buffer, 4) == TUNING_TROUBLE_PART1_EASY[index]

    assert tuning_trouble.find_packet_marker(
        hard_buffer, 4) == TUNING_TROUBLE_PART1_HARD

    # Test find_packet_marker() with easy test inputs and substring length of 14
    for index, buffer in enumerate(easy_buffer):
        buffer = buffer.strip()
        assert tuning_trouble.find_packet_marker(
            buffer, 14) == TUNING_TROUBLE_PART2_EASY[index]

    assert tuning_trouble.find_packet_marker(
        hard_buffer, 14) == TUNING_TROUBLE_PART2_HARD
