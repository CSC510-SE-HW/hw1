import pytest
from myfile_Melika import hello, age, count, sqaure

@pytest.mark.parametrize("x, expected", [
    ('Melika', 'Hello Dear Melika')])
def test_hello(x, expected):
    result = hello(x)
    assert result == expected

@pytest.mark.parametrize("x, y, expected", [
    (2000, 2024, 24)])
def test_age(x, y, expected):
    result = age(x, y)
    assert result == expected

#@pytest.mark.xfail(reason="Intentional fail for demonstration")
@pytest.mark.parametrize("x, expected", [
    (6, 21)])
def test_count_fail(x, expected):
    result = count(x)
    assert result == expected

#@pytest.mark.xfail(reason="Intentional fail for demonstration")
@pytest.mark.parametrize("x, expected", [
    (10, 81)])
def test_square_fail(x,expected):
    result = sqaure(x)
    assert result == expected