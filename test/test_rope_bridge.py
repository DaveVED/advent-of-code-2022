import pytest
import aoc.day9.rope_bridge as rope_bridge


@pytest.fixture
def easy_file():
    with open("test/files/day8/input_easy.txt", 'r', encoding='utf-8') as file:
        lines = file.read()

    lines = lines.split('\n')
    return lines


@pytest.fixture
def hard_file():
    with open("test/files/day8/input.txt", 'r', encoding='utf-8') as file:
        lines = file.read()

    lines = lines.split('\n')
    return lines


def test_find_positions_tail_visited(easy_file, hard_file):
    visted_count = rope_bridge.find_positions_tail_visited()
