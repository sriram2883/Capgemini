#calculator
from abc import ABC, abstractmethod

class Icalculator:
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def mul(self):
        pass

    @abstractmethod
    def div(self):
        pass

class BaseCalci(Icalculator):
    def add(self,a,b):
        print("Addition is "+str(a+b))

    def sub(self,a,b):
        print("Subtraction is "+str(a-b))

    def mul(self,a,b):
        print("Multiplication is "+str(a*b))

    def div(self,a,b):
        print("Division is "+str(a/b))

calciObj = BaseCalci()
calciObj.add(10,20)
calciObj.sub(20,10)
calciObj.mul(10,20)
calciObj.div(20,10)
