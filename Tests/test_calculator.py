import pytest
from src.calculator import Calculator

class TestCalculator():
    def setup(self):
        self.calculator = Calculator('Casio')

    def test_add(self):
        
        output = self.calculator.add(1,2)
        assert output == 3
    
    def test_subtract(self):
        
        output = self.calculator.subtract(3,1)
        assert output == 2

    def test_multiply(self):
        
        output = self.calculator.multiply(3,4)
        assert output == 12
    
    def test_divide(self):
        
        output = self.calculator.divide(4,2)
        assert output == 2