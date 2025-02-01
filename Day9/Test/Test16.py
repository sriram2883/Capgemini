#interfaces
from abc import ABC, abstractmethod

class Ishape(ABC):
    @abstractmethod
    def caluculate_area(self):
        pass

class circle(Ishape):
    def caluculate_area(self,radius):
        print("Area of circle is "+str(3.14*radius*radius))

class rectangle(Ishape):
    def caluculate_area(self,length,breadth):
        print("Area of rectangle is "+str(length*breadth))

circleObj = circle()
circleObj.caluculate_area(5)
rectangleObj = rectangle()
rectangleObj.caluculate_area(4,5)
