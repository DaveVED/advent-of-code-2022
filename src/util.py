from typing import List, Tuple


def parse_input(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()
