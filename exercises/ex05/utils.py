"""EX05 - Utility Functions."""

__author__ = "730394746"


def only_evens(input: list[int]) -> list[int]:
    """Returns even values given a list of integers."""
    evens: list[int] = list()
    for number in input:
        if number % 2 == 0:
            evens.append(number)
    return evens


def sub(given_list: list[int], start_i: int, end_i: int) -> list[int]:
    """Generates a list of subset integers given a list."""
    subset: list[int] = list()
    i = 0
    if start_i >= 0:
        i = start_i
    if len(given_list) > 0 and len(given_list) > start_i and end_i > 0:
        while i < end_i:
            subset.append(given_list[i])
            i += 1
    return subset


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists, returns a list that includes components of first lists followed by componenets of second list."""
    concat_list: list[int] = list()
    for number in list_one:
        concat_list.append(number)
    for number in list_two:
        concat_list.append(number)
    return concat_list