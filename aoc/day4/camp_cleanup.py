def find_overlap_count(file_path: str, overlap: bool) -> int:
    """Finds the number of ranges in the file at the given file path that overlap,
    or that are fully contained within each other if overlap is False.

    Args:
        file_path: The path to the file containing the ranges.
        overlap: If True, count the number of ranges that overlap.
                 If False, count the number of ranges that are fully contained within each other.

    Returns:
        The number of ranges that satisfy the specified condition.
    """
    with open(file_path, "r") as file:
        contain_count = 0
        for line in file:
            line = line.strip()
            elf_one_range, elf_two_range = line.split(",")
            elf_one_min, elf_one_max = map(int, elf_one_range.split("-"))
            elf_two_min, elf_two_max = map(int, elf_two_range.split("-"))

            if not overlap:
                if elf_one_min <= elf_two_min and elf_one_max >= elf_two_max:
                    contain_count += 1
                elif elf_two_min <= elf_one_min and elf_two_max >= elf_one_max:
                    contain_count += 1
            else:
                if elf_one_min <= elf_two_max and elf_two_min <= elf_one_max:
                    contain_count += 1

    return contain_count
