
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


## Fibonacci Tests
# def test_0():
#     actual = fibonacci(0)
#     expected = 0
#     assert actual == expected

def test_fib1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


## Lucas Tests
def test_lucas1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas5():
    actual = lucas(5)
    expected = 7
    assert actual == expected

def test_lucas4():
    actual = lucas(4)
    expected = 4
    assert actual == expected

## Sum_series test ??????
def test_sumFib1():
    actual = sum_series(1,0,1)
    expected = 1
    assert actual == expected

def test_sumFib5():
    actual = sum_series(5,0,1)
    expected = 5
    assert actual == expected

def test_sumFib5x():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sumLucas1():
    actual = sum_series(1,2,1)
    expected = 1
    assert actual == expected

def test_sumLucas5():
    actual = sum_series(5,2,1)
    expected = 7
    assert actual == expected



# def test_sum1():
#     actual = sum_series(1)
#     expected = 1
#     assert actual == expected

# def test_sum2():
#     actual = sum_series(5, 2, 1)
#     expected = 1
#     assert actual == expected