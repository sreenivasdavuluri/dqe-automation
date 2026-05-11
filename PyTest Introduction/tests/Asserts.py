def test_example1():
    assert 2 + 2 == 4


def test_example2():
    assert 2 + 2 == 5

def test_boolean():
    assert True  # Passes
    assert False  # Fails

def test_membership():
    assert 'a' in 'apple'  # Passes
    assert 'z' in 'apple'  # Fails

def test_comparison():
    assert 5 > 3  # Passes
    assert 3 > 5  # Fails

def test_custom_message():
    assert 2 + 2 == 5, "Math is broken!"  # Fails with custom message

def test_list():
    my_list = [1, 2, 3, 4]
    assert 3 in my_list  # Passes
    assert 5 in my_list  # Fails

def test_dict():
    my_dict = {'a': 1, 'b': 2}
    assert 'a' in my_dict  # Passes
    assert 'c' in my_dict  # Fails


import pytest
def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0  # This will raise ZeroDivisionError

def test_multiple_conditions():
    assert 2 + 2 == 4  # Passes
    assert 3 + 4 == 6  # Fails
    assert 3 + 3 == 6  # Will not run because the previous assert fails.


def test_single_condition1():
    assert 2 + 2 == 4  # Passes


def test_single_condition2():
    assert 3 + 4 == 6  # Fails


def test_single_condition3():
    assert 3 + 3 == 6  # Passes

def test_complex():
    result = [1, 2, 3]
    assert len(result) == 3
    assert result[0] == 1


result = [1, 2, 3]


def test_len():
    assert len(result) == 3


def test_first_value():
    assert len(result) == 3

import pytest

def test_exception():
    with pytest.raises(ValueError) as info:
        int('invalid')  # This will raise a ValueError
    assert str(info.value) == "This is a custom error message"

def test_not_in_list():
    my_list = [1, 2, 3, 4]
    assert 5 not in my_list  # Passes
    assert 3 not in my_list  # Fails


def test_not_in_dict():
    my_dict = {"a": 1, "b": 2}
    assert "c" not in my_dict  # Passes
    assert "a" not in my_dict  # Fails

import pytest

def test_no_exception():
    try:
        result = 10 / 2  # No exception raised
    except ZeroDivisionError:
        pytest.fail("ZeroDivisionError was raised unexpectedly")

import re


def test_no_match():
    pattern = re.compile(r"hello")
    assert not pattern.match("world")  # Passes
    assert not pattern.match("hello")  # Fails


def test_not_subclass():
    class Parent:
        pass
    class Child(Parent):
        pass
    class Unrelated:
        pass
    assert not issubclass(Unrelated, Parent)  # Passes
    assert not issubclass(Child, Parent)  # Fails