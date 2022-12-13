from typing import List


def match_outcome_score(opponenet_move: str, outcome: str) -> int:
    match_outcome_map = {"X": 0, "Y": 3, "Z": 6}
    move_value_map = {"X": 1, "Y": 2, "Z": 3}
    matchups_map = {
        "Y": {"A": "X", "B": "Y", "C": "Z"},
        "X": {"A": "Z", "B": "X", "C": "Y"},
        "Z": {"A": "Y", "B": "Z", "C": "X"},
    }

    return move_value_map[matchups_map[outcome][opponenet_move]] + match_outcome_map[outcome]


def guess_outcome_score(opponenet_move: str, our_move: str) -> int:
    win_map = {"X": "C", "Y": "A", "Z": "B"}
    tie_map = {"X": "A", "Y": "B", "Z": "C"}
    choice_map = {"X": 1, "Y": 2, "Z": 3}
    round_outcome_score = 0
    if win_map[our_move] == opponenet_move:
        round_outcome_score = 6
    elif tie_map[our_move] == opponenet_move:
        round_outcome_score = 3
    return round_outcome_score + choice_map[our_move]


def calculate_rock_paper_scissors_score(file_path: str, part: bool) -> int:
    with open(file_path, "r") as file:
        lines = file.readlines()

        scores = []
        for index, line in enumerate(lines):
            if part:
                opponenet_move, outcome = tuple(line.strip().split(" "))
                match_score = match_outcome_score(opponenet_move, outcome)
                scores.append(match_score)
            else:
                opponenet_move, outcome = tuple(line.strip().split(" "))
                match_score = guess_outcome_score(opponenet_move, outcome)
                scores.append(match_score)
    return sum(scores)
