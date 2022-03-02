from math_series.series import fibonacci, lucas, sum_series

"""
This test file contains a code that tests the actual code (functions) in the file (module) --> series.py

The test functions are going to test what the actual code returns

"""

# Tests for the fibonacci function
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_eighteen():
    actual = fibonacci(18)
    expected = 2584
    assert actual == expected


def test_fibonacci_twenty_eight():
    actual = fibonacci(28)
    expected = 317811
    assert actual == expected



#Tests for the lucas function
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_eighteen():
    actual = lucas(18)
    expected = 5778
    assert actual == expected


def test_lucas_twenty_eight():
    actual = lucas(28)
    expected = 710647
    assert actual == expected




# Tests for the sum_series function
# 1- calling the sum_series function with no optional arguments will print out fibonacci sepuence numbers
def test_sum_series_as_fibonacci_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_as_fibonacci_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_as_fibonacci_four():
    actual = sum_series(4)
    expected = 3
    assert actual == expected



# 2- calling the sum_series function with optional arguments of 2 and 1 will print out lucas sepuence numbers
def test_sum_series_as_lucas_zero():
    actual = sum_series(0, x=2, y=1)
    expected = 2
    assert actual == expected


def test_sum_series_as_lucas_one():
    actual = sum_series(1, x=2, y=1)
    expected = 1
    assert actual == expected


def test_sum_series_as_lucas_four():
    actual = sum_series(4, x=2, y=1)
    expected = 7
    assert actual == expected


# 3- calling the sum_series function with different optional arguments will print out numbers from other sequnces
def test_sum_series_as_first_different_series():
    actual = sum_series(5, x=8, y=2)
    expected = 34
    assert actual == expected

def test_sum_series_as_second_different_series():
    actual = sum_series(4, x=97, y=6)
    expected = 212
    assert actual == expected

def test_sum_series_as_third_different_series():
    actual = sum_series(1, x=11, y=111)
    expected = 111
    assert actual == expected
