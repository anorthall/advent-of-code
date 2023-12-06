#!/usr/bin/env python
"""
Advent of Code 2023
Day 1, Puzzle 1

Andrew Northall <andrew@northall.me.uk>
"""

import re


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    pattern = re.compile(r"(\d)")

    total = 0
    for num, line in enumerate(lines, 1):
        line = line.strip()
        if not line:
            continue

        match = pattern.findall(line)
        if not match:
            print(f"Line {num}: `{line}` => No match found")
            exit(1)

        first, last = match[0], match[-1]
        result = int(str(first) + str(last))
        print(f"Line {num}: `{line}` => {first} + {last} = {result}")
        total += result

    print(total)


if __name__ == "__main__":
    main()
