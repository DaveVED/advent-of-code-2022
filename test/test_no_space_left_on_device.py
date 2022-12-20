import pytest
import aoc.day7.no_space_left_on_device as no_space_left_on_device

from aoc.day7.no_space_left_on_device import Directory

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


def test_directory_initialization():
    """Test that a directory is initialized with the correct attributes.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the directory is not initialized with the correct attributes.
    """
    directory = Directory()
    assert directory.name == ''
    assert directory.files == []
    assert directory.children == []
    assert directory.parent is None
    assert directory.size == 0


def test_directory_add_file():
    """Test that a file can be added to a directory.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the file is not added to the directory.
    """
    directory = Directory()
    directory.files.append('test.txt')
    assert 'test.txt' in directory.files


def test_directory_add_child_directory():
    """Test that a child directory can be added to a directory.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the child directory is not added to the directory.
    """
    parent_directory = Directory()
    child_directory = Directory()
    parent_directory.children.append(child_directory)
    assert child_directory in parent_directory.children


def test_directory_set_parent():
    """Test that the parent directory of a directory can be set.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the parent directory is not set correctly.
    """
    parent_directory = Directory()
    child_directory = Directory()
    child_directory.parent = parent_directory
    assert child_directory.parent == parent_directory


def test_directory_update_size():
    """Test that the size of a directory is updated correctly when a file is added.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the size of the directory is not updated correctly.
    """
    directory = Directory()
    directory.files.append('test.txt')
    directory.size = 10
    assert directory.size == 10


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
