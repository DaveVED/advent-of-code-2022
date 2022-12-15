import aoc.day4.camp_cleanup as camp_cleanup

CAMP_CLEANUP_PART_1_EASY = 2
CAMP_CLEANUP_PART_1_HARD = 4
CAMP_CLEANUP_PART_2_EASY = 500
CAMP_CLEANUP_PART_2_HARD = 815


def test_find_overlap_count():
    """Tests the find_overlap_count function.

    This function tests the find_overlap_count function by calling it with a
    range of different input values and verifying that the function returns
    the expected results.
    """
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input_easy.txt", overlap=False) == CAMP_CLEANUP_PART_1_EASY
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input_easy.txt", overlap=True) == CAMP_CLEANUP_PART_1_HARD

    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input.txt", overlap=False) == CAMP_CLEANUP_PART_2_EASY
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input.txt", overlap=True) == CAMP_CLEANUP_PART_2_HARD
