
from math_series.series import fibonacci

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected