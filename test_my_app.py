"""
Test module for my_app.py
"""
import pytest
from my_app import MyApp


def test_positive_initialization():
    """
    Test of my_app successful initialization
    """
    list_a = [1, 2, 3]
    list_b = [2, 4, 6]
    test_app = MyApp(list_a, list_b)
    assert test_app.list1 == list_a
    assert test_app.list2 == list_b


def test_negative_initialization_not_a_list():
    """
    Test of my_app negative initialization cause of not list incoming
    """
    list_a = 8
    list_b = [2, 4, 6]
    with pytest.raises(TypeError):
        MyApp(list_a, list_b)


def test_negative_initialization_not_a_number():
    """
    Test of my_app negative initialization cause of not numbers in list
    """
    list_a = [1, 2, 3]
    list_b = ["2", "3", "4"]
    with pytest.raises(TypeError):
        MyApp(list_a, list_b)


@pytest.mark.parametrize("list1, list2, expected1, expected2", [
    ([1, 2, 3], [1, 2, 3], 2.0, 2.0),
    ([1, 2, 3], [3, 4, 5], 2.0, 4.0),
    ([3, 4, 5], [1, 2, 3], 4.0, 2.0),
    ([1, 2], [3, 4, 5], 1.5, 4.0),
    ([3, 4, 5], [2], 4.0, 2.0)
])
def test_mean_computing(list1, list2, expected1, expected2):
    """
    Test of mean computing function
    :param list1: List of numbers
    :param list2: List of numbers
    :param expected1: mean of first list
    :param expected2: mean of second list
    """
    test_app = MyApp(list1, list2)
    assert test_app.mean_compute() == (expected1, expected2)


def test_negative_mean_computing():
    """
    Test of negative mean computing cause of empty list
    """
    list_a = [1, 2, 3]
    list_b = []
    with pytest.raises(ZeroDivisionError):
        test_app = MyApp(list_a, list_b)
        test_app.mean_compute()


@pytest.mark.parametrize("list1, list2, expected", [
    ([1, 2, 3], [1, 2, 3], "Средние значения равны"),
    ([1, 2, 3], [3, 4, 5], "Второй список имеет большее среднее значение"),
    ([3, 4, 5], [1, 2, 3], "Первый список имеет большее среднее значение"),
    ([1, 2], [3, 4, 5], "Второй список имеет большее среднее значение"),
    ([3, 4, 5], [2], "Первый список имеет большее среднее значение")
])
def test_comparing_lists(list1, list2, expected):
    """
    Test of comparing lists
    :param list1: list of numbers
    :param list2: list of numbers
    :param expected: string answer
    """
    test_app = MyApp(list1, list2)
    test_app.mean_compute()
    assert test_app.list_compare() == expected
