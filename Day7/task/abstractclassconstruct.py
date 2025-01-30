from abc import ABC, abstractmethod
class vehicle(ABC):
    def __init__(self,brand):
        self.brand = brand
    @abstractmethod
    def max_speed(self):
        pass
class car(vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    def max_speed(self):
        print(f"Max speed of car {self.brand} is 200 km/h")
class bike(vehicle):
    def __init__(self,brand):
        super().__init__(brand)
    def max_speed(self):
        print(f"Max speed of bike {self.brand} is 120 km/h")

c=car("Toyota")
b=bike("Honda")
c.max_speed()
b.max_speed()