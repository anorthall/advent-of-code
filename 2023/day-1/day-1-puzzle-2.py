#!/usr/bin/env python
"""
Advent of Code 2023
Day 1, Puzzle 2

Andrew Northall <andrew@northall.me.uk>
"""

import re


NUMBERS = {
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


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    pattern = "(" + "|".join(NUMBERS.keys()) + r"|\d)"
    pattern = f"(?={pattern})"
    pattern = re.compile(pattern)

    total = 0
    for num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        matches = pattern.finditer(line)
        matches = [str(match.group(1)) for match in matches]

        if not matches:
            print(f"Line {num}: `{line}` => No match found")
            exit(1)

        first, last = matches[0], matches[-1]
        if first in NUMBERS:
            first = NUMBERS[first]
        if last in NUMBERS:
            last = NUMBERS[last]

        result = int(first + last)
        total += result
        print(f"Line {num}: `{line}` => {first} + {last} = {result} ({total})")

    print(total)


if __name__ == "__main__":
    main()
