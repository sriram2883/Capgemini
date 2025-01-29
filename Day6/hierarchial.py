class shape:
    def area(self):
        pass
class circle(shape):
    def area(self,r):
        print(f"Area of circle is {3.14*r*r}")
class square(shape):
    def area(self,l):
        print(f"Area of square is {l*l}")
class rectangle(shape):
    def area(self,l,b):
        print(f"Area of rectangle is {l*b}")

obj1=circle()
obj1.area(5)
obj2=square()
obj2.area(5)
obj3=rectangle()
obj3.area(5,6)