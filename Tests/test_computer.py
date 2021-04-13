import pytest
from src.computer import Computer

class TestComputer():
    def setup(self):
        self.computer = Computer('Casio')

    def test_add(self):
        
        output = self.computer.add(1,2)
        assert output == 3
    
    def test_subtract(self):
        
        output = self.computer.subtract(3,1)
        assert output == 2

    def test_multiply(self):
        
        output = self.computer.multiply(3,4)
        assert output == 12
        assert self.computer.battery == 90
    
    def test_divide(self):
        
        output = self.computer.divide(4,2)
        assert output == 2
        assert self.computer.battery == 90

    def test_run_code(self):

        code_running = self.computer.run_code()
        assert code_running == 'boop code running...'
        assert self.computer.battery == 90