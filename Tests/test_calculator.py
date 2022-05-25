import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator('Casio')


@pytest.mark.parametrize(
    "test_input, expected",
    [((1,2), 3),
     ((3,4), 7),
     ((10, 15), 25)]
)
def test_add(calculator, test_input, expected):
    assert calculator.add(*test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [((6, 4), 2),
     ((12, 4), 8),
     ((10, 15), -5)]
)
def test_subtract(calculator, test_input, expected):
    assert calculator.subtract(*test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [((6, 4), 24),
     ((12, 4), 48),
     ((-5, 5), -25)]
)
def test_multiply(calculator, test_input, expected):

    assert calculator.multiply(*test_input) == expected
    assert calculator.battery == 90


@pytest.mark.parametrize(
    "test_input, expected",
    [((6, 4), 1.5),
     ((12, 4), 3),
     ((-5, 5), -1)]
)
def test_divide(calculator, test_input, expected):
    assert calculator.divide(*test_input) == expected
    assert calculator.battery == 90


@pytest.mark.parametrize("test_input", [(0, 0)])
def test_divide_by_zero_error(calculator, test_input):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(*test_input)

