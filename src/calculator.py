
class Calculator():
    def __init__(self,brand):
        self.brand = brand
        self.battery = 100

    def add(self,x,y):
        return(x + y)

    def subtract(self,x,y):
        return(x - y)

    def multiply(self,x,y):
        return(x * y)

    def divide(self,x,y):
        return(x/y)