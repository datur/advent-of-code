import os


FILE_PATH = os.path.dirname(os.path.abspath(__file__))

scores = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

win_loss_draw_map = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}


def read_input(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def calculate_default_strategy_score(file_path):

    result = 0

    _input = read_input(file_path)

    for game in _input:
        game = game.rstrip()

        result += scores[game]

    return result


def calculate_win_loss_draw_strategy(file_path):
    result = 0

    _input = read_input(file_path)

    for game in _input:
        game = game.rstrip()

        calculated_result = win_loss_draw_map[game]

        result += scores[calculated_result]

    return result


def results():
    file_path = os.path.join(FILE_PATH, "input.txt")

    part_1 = calculate_default_strategy_score(file_path)
    part_2 = calculate_win_loss_draw_strategy(file_path)

    return part_1, part_2
