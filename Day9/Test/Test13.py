class shape:
    def area(self):
        pass

class circle(shape):
    def area(self,radius):
        print("Area of circle is "+str(3.14*radius*radius))

class square(shape):
    def area(self,side):
        print("Area of square is "+str(side*side))

class rectangle(shape):
    def area(self,length,breadth):
        print("Area of rectangle is "+str(length*breadth))

circleObj = circle()
circleObj.area(5)
squareObj = square()
squareObj.area(4)
rectangleObj = rectangle()
rectangleObj.area(4,5)
