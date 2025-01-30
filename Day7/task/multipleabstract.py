from abc import ABC, abstractmethod

class person(ABC):
    @abstractmethod
    def get_name(self):
        pass
class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass

class Manager(person,Employee):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        print(f"Name of the manager is {self.name}")
    def get_salary(self):
        print(f"Salary of the manager is {self.salary}")

m=Manager("John",50000)
m.get_name()
m.get_salary()