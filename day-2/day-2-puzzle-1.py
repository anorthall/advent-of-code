#!/usr/bin/env python
"""
Advent of Code 2023
Day 2, Puzzle 1

Andrew Northall <andrew@northall.me.uk>
"""
import re

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

PATTERN = re.compile(r"((\d+) (red|blue|green))")


def is_possible(game_id: int, line: str) -> bool:
    matches = PATTERN.findall(line)
    for game, num, colour in matches:
        if int(num) > LIMITS[colour]:
            return False
    return True


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    possible_game_ids = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        game_id = int(line.split(":")[0][5:])
        line = line.split(":")[1].strip()

        if is_possible(game_id, line):
            possible_game_ids.append(game_id)

    print(sum(possible_game_ids))


if __name__ == "__main__":
    main()
