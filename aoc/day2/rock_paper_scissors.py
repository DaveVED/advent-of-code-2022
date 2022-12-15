from typing import List


def match_outcome_score(opponent_move: str, outcome: str) -> int:
    """
    Calculate the score for a match outcome.

    Args:
        opponent_move: The move made by the opponent, as a string ("A", "B", or "C").
        outcome: The outcome of the match, as a string ("X", "Y", or "Z").

    Returns:
        The score for the match outcome, as an integer.
    """
    match_outcome_map = {"X": 0, "Y": 3, "Z": 6}
    move_value_map = {"X": 1, "Y": 2, "Z": 3}
    matchups_map = {
        "Y": {"A": "X", "B": "Y", "C": "Z"},
        "X": {"A": "Z", "B": "X", "C": "Y"},
        "Z": {"A": "Y", "B": "Z", "C": "X"},
    }

    return move_value_map[matchups_map[outcome][opponent_move]] + match_outcome_map[outcome]


def guess_outcome_score(opponent_move: str, our_move: str) -> int:
    """
    Calculate the score for a guessed match outcome.

    Args:
        opponent_move: The move made by the opponent, as a string ("A", "B", or "C").
        our_move: The move made by us, as a string ("X", "Y", or "Z").

    Returns:
        The score for the guessed match outcome, as an integer.
    """
    win_map = {"X": "C", "Y": "A", "Z": "B"}
    tie_map = {"X": "A", "Y": "B", "Z": "C"}
    choice_map = {"X": 1, "Y": 2, "Z": 3}
    round_outcome_score = 0
    if win_map[our_move] == opponent_move:
        round_outcome_score = 6
    elif tie_map[our_move] == opponent_move:
        round_outcome_score = 3
    return round_outcome_score + choice_map[our_move]


def calculate_rock_paper_scissors_score(file_path: str, part: str) -> int:
    """
    Calculate the total score for a game of Rock-Paper-Scissors.

    Args:
        file_path: The path to the file containing the game moves, as a string.
        part: The part of the game to calculate the score for, as a string ("one" or "two").

    Returns:
        The total score for the game, as an integer.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

        scores = []
        for line in lines:
            opponent_move, outcome = tuple(line.strip().split(" "))
            if part == "two":
                match_score = match_outcome_score(opponent_move, outcome)
            elif part == "one":
                match_score = guess_outcome_score(opponent_move, outcome)
            scores.append(match_score)

    return sum(scores)
