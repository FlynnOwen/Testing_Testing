class Calculator():
    @classmethod
    def __init__(cls,brand):
        cls.brand = brand
        cls.battery = 100

    @staticmethod
    def add(x,y):
        return(x + y)

    @staticmethod
    def subtract(x,y):
        return(x - y)

    @classmethod
    def multiply(cls,x,y):
        cls.battery -= 10
        return(x * y)

    @classmethod
    def divide(cls,x,y):
        cls.battery -= 10
        return(x/y)

    @classmethod
    def print_brand(cls):
        cls.battery -= 10
        return(cls.brand)

    @classmethod
    def battery_level(cls):
        cls.battery -= 10
        return(cls.battery)
