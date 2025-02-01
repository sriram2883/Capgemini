#multilevel inheritance
class vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.max_speed = int(input("Enter the max speed of the vehicle:"))

class car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        self.mileage = int(input("Enter the mileage of the car:"))

class bike(vehicle):
    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model
        self.mileage = int(input("Enter the mileage of the bike:"))
    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model},  Max Speed: {self.max_speed}, Mileage: {self.mileage}")

class ElectricCar(car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Max Speed: {self.max_speed}, Mileage: {self.mileage}")

bikeObj = bike("Yamaha", 2017)
bikeObj.display()
carObj = ElectricCar("Tesla", 2020)
carObj.display()