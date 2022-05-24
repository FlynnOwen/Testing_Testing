import pytest
from src.calculator import Calculator


class TestCalculator:
    def setup(self):
        self.calculator = Calculator('Casio')

    @pytest.mark.parametrize(
        "test_input, expected",
        [((1,2), 3),
         ((3,4), 7),
         ((10, 15), 25)]
    )
    def test_add(self, test_input, expected):
        assert self.calculator.add(*test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [((6, 4), 2),
         ((12, 4), 8),
         ((10, 15), -5)]
    )
    def test_subtract(self, test_input, expected):
        assert self.calculator.subtract(*test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [((6, 4), 24),
         ((12, 4), 48),
         ((-5, 5), -25)]
    )
    def test_multiply(self, test_input, expected):
        
        assert self.calculator.multiply(*test_input) == expected
        assert self.calculator.battery == 90

    @pytest.mark.parametrize(
        "test_input, expected",
        [((6, 4), 1.5),
         ((12, 4), 3),
         ((-5, 5), -1)]
    )
    def test_divide(self, test_input, expected):
        assert self.calculator.divide(*test_input) == expected
        assert self.calculator.battery == 90

    @pytest.mark.parametrize("test_input", [(0, 0)])
    def test_divide_by_zero_error(self, test_input):
        with pytest.raises(ZeroDivisionError):
            self.calculator.divide(*test_input)

