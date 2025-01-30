from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        print(f"Area of rectangle is {self.length*self.breadth}")
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"Area of circle is {3.14*self.radius*self.radius}")
r=rectangle(5,10)
c=circle(5)
r.area()
c.area()