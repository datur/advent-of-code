"""Day 1: Trebuchet?!"""

import re

from inputs import day1

WORD_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def part_one(puzzle_input: list[str]):
    """Find the sum of the first and last digit in each row of the puzzle input."""
    running_total = 0

    for row in puzzle_input:

        results = re.findall(r"\d+", row)

        if len(results) == 0:
            continue

        first_digit = results[0][0]
        last_digit = results[-1][-1]

        running_total += int(f"{first_digit}{last_digit}")

    print(running_total)

def part_two(puzzle_input: list[str]):
    """
    Find the sum of the first and last number in each row of the puzzle input.

    In this case the first and last number in each row can be written as text.
    """
    running_total = 0

    for row in puzzle_input:

        results = re.findall(r"(one|two|three|four|five|six|seven|eight|nine)|(\d+)", row)

        if len(results) == 0:
            continue

        first_digit = results[0][0] or results[0][1]
        last_digit = results[-1][0] or results[-1][-1]

        if first_digit in WORD_DIGIT_MAP:
            first_digit = WORD_DIGIT_MAP[first_digit]
        if last_digit in WORD_DIGIT_MAP:
            last_digit = WORD_DIGIT_MAP[last_digit]

        first_digit = first_digit[0]
        last_digit = last_digit[-1]

        running_total += int(f"{first_digit}{last_digit}")

    print(running_total)


if __name__ == "__main__":
    puzzle_input = day1.split("\n")

    part_one(puzzle_input=puzzle_input)
    part_two(puzzle_input=puzzle_input)
