import aoc.day4.camp_cleanup as camp_cleanup


def test_find_overlap_count():
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input_easy.txt", overlap=False) == 2
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input_easy.txt", overlap=True) == 4

    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input.txt", overlap=False) == 500
    assert camp_cleanup.find_overlap_count(
        "test/files/day4/input.txt", overlap=True) == 815
