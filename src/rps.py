from typing import List


def match_outcome_score(opponenet_move: str, outcome: str) -> int:
    match_outcome_score = {"X": 0, "Y": 3, "Z": 6}
    move_value = {"X": 1, "Y": 2, "Z": 3}
    matchups = {
        "Y": {"A": "X", "B": "Y", "C": "Z"},
        "X": {"A": "Z", "B": "X", "C": "Y"},
        "Z": {"A": "Y", "B": "Z", "C": "X"},
    }

    return move_value[matchups[outcome][opponenet_move]] + match_outcome_score[outcome]


def calculate_rock_paper_scissors_score(games: List[str]) -> int:
    scores = []
    for game in games:
        opponenet_move, outcome = tuple(game.strip().split(" "))
        match_score = match_outcome_score(opponenet_move, outcome)
        scores.append(match_score)
    return sum(scores)
