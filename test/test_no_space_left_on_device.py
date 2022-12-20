import pytest
import aoc.day7.no_space_left_on_device as no_space_left_on_device


NO_SPACE_LET_ON_DEVICE_PART1_EASY = 95437
NO_SPACE_LET_ON_DEVICE_PART1_HARD = 1743217
NO_SPACE_LET_ON_DEVICE_PART2_EASY = 24933642
NO_SPACE_LET_ON_DEVICE_PART2_HARD = 8319096


@pytest.fixture
def easy_file():
    with open("test/files/day7/input_easy.txt", 'r', encoding='utf-8') as file:
        txt = file.read()

    terminal_output = txt.split('\n')
    return terminal_output


@pytest.fixture
def hard_file():
    with open("test/files/day7/input.txt", 'r', encoding='utf-8') as file:
        txt = file.read()

    terminal_output = txt.split('\n')
    return terminal_output


def test_build_file_system(easy_file, hard_file):
    file_system = no_space_left_on_device.build_file_system(easy_file)
    matching_dir = no_space_left_on_device.find_matching_directories(
        file_system)
    assert matching_dir == NO_SPACE_LET_ON_DEVICE_PART1_EASY

    file_system = no_space_left_on_device.build_file_system(hard_file)
    matching_dir = no_space_left_on_device.find_matching_directories(
        file_system)
    assert matching_dir == NO_SPACE_LET_ON_DEVICE_PART1_HARD

    file_system = no_space_left_on_device.build_file_system(easy_file)
    min_dir = no_space_left_on_device.find_min_directory(file_system)
    assert min_dir == NO_SPACE_LET_ON_DEVICE_PART2_EASY

    file_system = no_space_left_on_device.build_file_system(hard_file)
    min_dir = no_space_left_on_device.find_min_directory(file_system)
    assert min_dir == NO_SPACE_LET_ON_DEVICE_PART2_HARD
