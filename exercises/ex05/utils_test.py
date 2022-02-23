"""Tests for Utility Functions."""


from exercises.ex05.utils import only_evens


def test_only_evens_edge() -> None:
    """Test edge case with no input list."""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_use() -> None:
    """Test use case with sample list."""
    input: list[int] = [1, 2, 3]
    assert only_evens(input) == [2]


def test_only_evens_use_2() -> None:
    """Test use case with second sample list."""
    input: list[int] = [1, 5, 3]
    assert only_evens(input) == []


from exercises.ex05.utils import sub


def test_sub_edge() -> None:
    """Test edge case with no sample list and out of range index."""
    given_list: list[int] = []
    assert sub(given_list, -1, 6) == []


def test_sub_use() -> None:
    """Test use case with a sample list."""
    given_list: list[int] = [10, 20, 30, 40]
    assert sub(given_list, 1, 3) == [20, 30]


def test_sub_use_2() -> None:
    """Test use case with a second sample list."""
    given_list: list[int] = [23, 34, 45, 56, 67, 78, 98]
    assert sub(given_list, 3, 6) == [56, 67, 78, 98]


from exercises.ex05.utils import concat


def test_concat_edge() -> None:
    """Test edge case with a sample list and an empty list."""
    list_one: list[int] = []
    list_two: list[int] = [34, 56]
    assert concat(list_one, list_two) == [34, 56]


def test_concat_use() -> None:
    """Test use case with two sample lists."""
    list_one: list[int] = [22]
    list_two: list[int] = [33]
    assert concat(list_one, list_two) == [22, 33]


def test_concat_use_2() -> None:
    """Test use case with two sample lists again."""
    list_one: list[int] = [1, 2, 3, 4]
    list_two: list[int] = [4, 3, 2, 1]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 4, 3, 2, 1]