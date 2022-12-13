from typing import List


class Elf:
    def __init__(self, calories: List[int], calorie_total: int):
        self._calories = calories
        self._calorie_total = calorie_total
        self._rock_paper_scissor_score = None

    @property
    def calories(self) -> List[int]:
        return self._calories

    @property
    def calorie_total(self) -> int:
        return self._calorie_total


def build_elfs(lines: List[str]) -> List[Elf]:
    elfs = []
    elf_calories = []
    for index, line in enumerate(lines):
        line = line.strip()
        if line == "":
            elfs.append(Elf(elf_calories, sum(elf_calories)))
            elf_calories = []
        else:
            elf_calories.append(int(line))
            if index == len(lines) - 1:
                elfs.append(Elf(elf_calories, sum(elf_calories)))
                elf_calories = []
    return elfs


def find_top_3_elfs(elfs: List[Elf]) -> List[int]:
    smart_elfs = []
    for elf in elfs:
        # Add the first 3
        if len(smart_elfs) <= 2:
            smart_elfs.append(elf.calorie_total)
            if len(smart_elfs) == 2:
                smart_elfs.sort(reverse=True)
        else:
            if any(elf.calorie_total > calorie for calorie in smart_elfs):
                smart_elfs.append(elf.calorie_total)
                smart_elfs.sort(reverse=True)
                smart_elfs.pop()

    return smart_elfs
