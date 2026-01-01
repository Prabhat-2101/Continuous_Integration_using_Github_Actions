import pytest

def square(x):
    return x * x

def cube(x):
    return x * x * x

def fourth_power(x):
    return x * x * x * x

def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_cube():
    assert cube(2) == 8
    assert cube(3) == 27

def test_fourth_power():
    assert fourth_power(2) == 16
    assert fourth_power(3) == 81
