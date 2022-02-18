"""Exaxmple of a function that searches through a lists."""

def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))
# Define a function named contains
# Two parametersL
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #   For each item in the haystack
    #       Test if it is equal to the needle
    #           If so, return True
    for item in haystack:
        if item == needle:
            return True
    return False
    # Returns true if needle in haystack, false otherwise


if __name__ == "__main__":
    main()