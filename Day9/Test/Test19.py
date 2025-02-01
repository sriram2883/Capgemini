#vehicle interface
from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")

class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine started")
    def stop_engine(self):
        print("Bike engine stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine started")
    def stop_engine(self):
        print("Truck engine stopped")

carObj = Car()
carObj.start_engine()
carObj.stop_engine()
bikeObj = Bike()
bikeObj.start_engine()
bikeObj.stop_engine()
truckObj = Truck()
truckObj.start_engine()