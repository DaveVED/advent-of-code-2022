import pytest
from aoc.day8.treetop_tree_house import TreetopTreeHouse

TREETOP_TREE_HOUSE_PART1_EASY = 21
TREETOP_TREE_HOUSE_PART1_HARD = 1854
TREETOP_TREE_HOUSE_PART2_EASY = 8
TREETOP_TREE_HOUSE_PART2_HARD = 527340
treetop_tree_house = TreetopTreeHouse()


@pytest.fixture
def easy_file():
    """Get the easy test file."""
    with open("test/files/day8/input_easy.txt", 'r', encoding='utf-8') as file:
        lines = file.read()

    lines = lines.split('\n')
    return lines


@pytest.fixture
def hard_file():
    """Get the hard test file."""
    with open("test/files/day8/input.txt", 'r', encoding='utf-8') as file:
        lines = file.read()

    lines = lines.split('\n')
    return lines


def test_find_visible_trees(easy_file, hard_file):
    """Test finding the number of visible trees and the maximum number of tree blockers."""
    nodes = treetop_tree_house.build_nodes(easy_file)
    visible_trees, blocker_count = treetop_tree_house.find_visible_trees(
        nodes)
    assert visible_trees == TREETOP_TREE_HOUSE_PART1_EASY
    assert blocker_count == TREETOP_TREE_HOUSE_PART2_EASY

    nodes = treetop_tree_house.build_nodes(hard_file)
    visible_trees, blocker_count = treetop_tree_house.find_visible_trees(nodes)
    assert visible_trees == TREETOP_TREE_HOUSE_PART1_HARD
    assert blocker_count == TREETOP_TREE_HOUSE_PART2_HARD
