import pytest
from series.series import fibonacci, lucas, sum_series


def test_fibonacci_zero():
    actual=fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual=fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual=fibonacci(2)
    expected = 1
    assert actual == expected    

def test_fibonacci_three():
    actual=fibonacci(3)
    expected = 2
    assert actual == expected    

def test_fibonacci_four():
    actual=fibonacci(4)
    expected = 3
    assert actual == expected    

def test_fibonacci_five():
    actual=fibonacci(5)
    expected = 5
    assert actual == expected    

def test_fibonacci_six():
    actual=fibonacci(6)
    expected = 8
    assert actual == expected    

def test_fibonacci_saven():
    actual=fibonacci(7)
    expected = 13
    assert actual == expected    

def test_fibonacci_eghit():
    actual=fibonacci(8)
    expected = 21
    assert actual == expected    

def test_fibonacci_nine():
    actual=fibonacci(9)
    expected = 34
    assert actual == expected   

#/.....................lucas test......................#/

def test_lucas_zero():
    actual=lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual=lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual=lucas(2)
    expected = 3
    assert actual == expected    

def test_lucas_three():
    actual=lucas(3)
    expected = 4
    assert actual == expected    

def test_lucas_four():
    actual=lucas(4)
    expected = 7
    assert actual == expected    

def test_lucas_five():
    actual=lucas(5)
    expected = 11
    assert actual == expected    

def test_lucas_six():
    actual=lucas(6)
    expected = 18
    assert actual == expected    

def test_lucas_saven():
    actual=lucas(7)
    expected = 29
    assert actual == expected    

def test_lucas_eghit():
    actual=lucas(8)
    expected = 47
    assert actual == expected    

def test_lucas_nine():
    actual=lucas(9)
    expected = 76
    assert actual == expected

#.........................................

# sum_series Tests

def test_zero_sum_series():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_one_sum_series():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_two_sum_series():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_three_sum_series():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_four_sum_series():
    actual = sum_series(4)
    expected = 3
    assert actual == expected


def test_five_sum_series():
    actual = sum_series(5)
    expected = 5
    assert actual == expected
def test_six_sum_series():
    actual = sum_series(6)
    expected = 8
    assert actual == expected


def test_seven_sum_series():
    actual = sum_series(7)
    expected = 13
    assert actual == expected


def test_eight_sum_series():
    actual = sum_series(8)
    expected = 21
    assert actual == expected


def test_nine_sum_series():
    actual = sum_series(9)
    expected = 34
    assert actual == expected



