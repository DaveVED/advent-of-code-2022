from collections import defaultdict
from typing import List, Tuple


def find_top_crates(file_path: str, order: bool) -> str:
    """Find the top crates in each stack after moving the crates according to the instructions in the specified file.

    Args:
        file_path (str): The path to the file with instructions for moving the crates.
        order (bool): If True, the crates will be moved in the order specified in the file.
                      If False, the crates will be moved in reverse order.

    Returns:
        str: A string containing the top crates in each stack.
    """
    stacks, moves = create_supply_stacks_and_instructions(file_path)
    for move in moves:
        count, source, destination = move

        crates = list(stacks[source][:count]) if order else list(
            reversed(stacks[source][:count]))
        stacks[source] = stacks[source][count:]
        stacks[destination] = crates + stacks[destination]

    top_crates = ""
    for index in range(1, len(stacks) + 1):
        stack = stacks[index]
        if len(stack) > 0:
            top_crates += stack[0]

    return top_crates


def create_supply_stacks_and_instructions(file_path: str) -> Tuple[defaultdict, List[Tuple[int, int, int]]]:
    """
    Create the supply stacks and instructions from the specified file.

    :param file_path: The path to the file with the supply stacks and instructions.
    :return: A tuple containing the supply stacks and instructions.
    """
    with open(file_path, "r") as file:
        raw = file.read()

    raw_stacks, raw_moves = raw.split("\n\n")

    stacks_list = raw_stacks.split("\n")
    stacks = defaultdict(list)
    for stack in stacks_list[:-1]:
        for index, crate in enumerate(stack[1::4]):
            if crate != " ":
                stacks[index + 1].append(crate)

    moves = []
    for move in raw_moves.strip().split("\n"):
        _, move_count, _, source, _, destination = move.split()
        moves.append(tuple(map(int, (move_count, source, destination))))

    return stacks, moves
