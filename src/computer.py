from src.calculator import Calculator

class Computer(Calculator):
    def __init__(self, brand):
        super().__init__(brand)
    
    @classmethod
    def run_code(cls):
        cls.battery -= 10
        return('boop code running...')