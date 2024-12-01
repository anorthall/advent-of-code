#!/usr/bin/env python3
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class NumberLists:
    left_list: list[int]
    right_list: list[int]


def read_input(filename: str = "input-1.txt") -> NumberLists:
    """Return sorted input data."""
    with open(filename) as f:
        data = f.read()

    left_list: list[int] = []
    right_list: list[int] = []

    for line in data.splitlines():
        left, right = line.split("  ")
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    return NumberLists(left_list, right_list)


def calculate_difference(lists: NumberLists) -> int:
    difference = 0
    for left, right in zip(lists.left_list, lists.right_list, strict=True):
        difference += abs(left - right)
    return difference


def calculate_similarity(lists: NumberLists) -> int:
    right_list_appearances = defaultdict(int)
    for num in lists.right_list:
        right_list_appearances[num] += 1

    similarity = 0
    for num in lists.left_list:
        similarity += num * right_list_appearances[num]

    return similarity


if __name__ == "__main__":
    number_lists = read_input()
    print(calculate_difference(number_lists))
    print(calculate_similarity(number_lists))
