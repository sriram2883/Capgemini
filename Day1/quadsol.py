import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d=(b**2)-(4*a*c)
sol1=(-b+math.sqrt(d))/(2*a)
sol2=(-b-math.sqrt(d))/(2*a)
print("The solutions are",sol1,"and",sol2)
