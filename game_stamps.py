from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    last = len_stamps = len(game_stamps)
    while not isinstance(game_stamps, dict) and len_stamps != 1:
        first = 0
        len_stamps = len(game_stamps)
        mid = len_stamps//2
        first, last = (mid, last) if offset > game_stamps[mid]['offset'] else (first, mid)
        game_stamps = game_stamps[mid] if game_stamps[mid]['offset'] == offset else game_stamps[first:last]
    home, away = (game_stamps['score']['home'], game_stamps['score']['away']) if isinstance(game_stamps, dict) \
        else ("Момент отсутствует в таблице", "")
    return home, away


offset = int(input("На какой момент вернуть счет?: "))
get_scores = get_score(game_stamps=game_stamps, offset=offset)
pprint(get_scores)
