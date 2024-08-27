import pytest
from myfileSravya import add, subtract, multiplication, divide

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
], ids=["2 + 3 = 5"])
def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected, f"Expected {x} + {y} to be {expected}, but got {result}"

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
], ids=["5 - 3 = 2"])
def test_subtract(x, y, expected):
    result = subtract(x, y)
    assert result == expected, f"Expected {x} - {y} to be {expected}, but got {result}"

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 7),
], ids=["2 * 3 != 7"])
def test_multiplication_fail(x, y, expected):
    result = multiplication(x, y)
    assert result == expected, f"Expected {x} * {y} to be {expected}, but got {result}"

@pytest.mark.parametrize("x, y, expected", [
    (10, 2, 4),
], ids=["10 / 2 != 4"])
def test_divide_fail(x, y, expected):
    result = divide(x, y)
    assert result == expected, f"Expected {x} / {y} to be {expected}, but got {result}"
