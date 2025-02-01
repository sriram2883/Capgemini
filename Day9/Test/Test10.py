#multilevel inheritance
class Electronics:
    def __init__(self,type):
        self.type = type

class Mobile(Electronics):
    def __init__(self,type,brand):
        super().__init__(type)
        self.brand = brand
        self.price = int(input("Enter the price of the mobile:"))

class Smartphone(Mobile):
    def __init__(self,type,brand):
        super().__init__(type,brand)
        self.model = input("Enter the model of the smartphone:")
    def display(self):
        print(f"Type: {self.type}, Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

obj = Smartphone("Smartphone","Samsung")
obj.display()