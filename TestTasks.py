from unittest.mock import Mock
import pytest

from Tasks import Tasks, Person, Bank


# ![properties](info/properties.png)
# [test](./ie.png)

@pytest.fixture
def person_and_bank():
    person = Person(1000)
    bank = Bank()
    return person, bank


def test_find_average():
    assert Tasks.find_average([10, 20, 30]) == 20
    assert Tasks.find_average([]) == 0
    assert Tasks.find_average([5]) == 5


def test_find_average_with_error():
    assert Tasks.find_average_with_error([10, 20, 30]) == 20
    assert Tasks.find_average_with_error([]) == 0
    with pytest.raises(TypeError):
        Tasks.find_average_with_error("2, 5")


def test_person_bank_interaction(person_and_bank):
    person, bank = person_and_bank
    person.transfer_money(500, bank)
    assert person.balance == 500
    assert bank.balance == 500


def test_person_bank_value_error():
    with pytest.raises(ValueError):
        person = Person(0)
        bank = Bank()
        person.transfer_money(500, bank)


def test_transfer_with_mock():
    person = Person(1000)
    bank_mock = Mock()

    person.transfer_money(500, bank_mock)
    bank_mock.receive_money.assert_called_with(500)


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        Tasks.divide(5, 0)


@pytest.mark.parametrize("a, b, expected", [
    (10, 0, 0),
    (-1, 5, -5),
    (3, 3, 9),
    (-2, -2, 4),
    (0, 0, 0)
])
def test_multiply(a, b, expected):
    assert Tasks.multiply(a, b) == expected


def test_string_length():
    assert len("Hello") == 5


@pytest.mark.parametrize("test_input, expected", [
    (2, True),
    (3, True),
    (4, False),
    (16, False),
    (17, True),
    (18, False)
])
def test_is_prime(test_input, expected):
    assert Tasks.is_prime(test_input) == expected
