import aoc.day5.supply_stacks as supply_stacks


SUPPY_STACKS_PAR1_EASY = "CMZ"
SUPPY_STACKS_PAR1_HARD = "WSFTMRHPP"
SUPPLY_STACKS_PART2_EASY = "MCD"
SUPPLY_STACKS_PART2_HARD = "GSLCMFBRP"


def test_find_top_crates():
    """Tests the find_top_crates function.

    This function tests the find_top_crates function by calling it with a range
    of different input values and verifying that the function returns the
    expected results.
    """
    assert supply_stacks.find_top_crates(
        "test/files/day5/input_easy.txt", False) == "CMZ"
    assert supply_stacks.find_top_crates(
        "test/files/day5/input.txt", False) == "WSFTMRHPP"

    assert supply_stacks.find_top_crates(
        "test/files/day5/input_easy.txt", True) == "MCD"

    assert supply_stacks.find_top_crates(
        "test/files/day5/input.txt", True) == "GSLCMFBRP"


def test_create_supply_stacks():
    """Tests the create_supply_stacks_and_instructions function.

    This function tests the create_supply_stacks_and_instructions function by
    calling it with a range of different input values and verifying that the
    function returns the expected results.
    """
    crates, moves = supply_stacks.create_supply_stacks_and_instructions(
        "test/files/day5/input_easy.txt")

    assert crates[1] == ['N', 'Z']
    assert crates[2] == ['D', 'C', 'M']
    assert crates[3] == ['P']

    assert moves == [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
