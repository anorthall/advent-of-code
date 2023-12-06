#!/usr/bin/env python
"""
Advent of Code 2023
Day 2, Puzzle 2

Andrew Northall <andrew@northall.me.uk>
"""
import re


PATTERN = re.compile(r"((\d+) (red|blue|green))")


def get_power(line: str) -> int:
    cubes = PATTERN.findall(line)
    max = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for _, num, colour in cubes:
        num = int(num)
        if num > max[colour]:
            max[colour] = num

    return max["red"] * max["blue"] * max["green"]


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue

        line = line.split(":")[1].strip()
        total += get_power(line)

    print(total)


if __name__ == "__main__":
    main()
