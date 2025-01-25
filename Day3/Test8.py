#multiplication table
n = int(input("Enter the number: "))
range1 = int(input("Enter the range: "))
for i in range(1, range1+1):
    print(f"{n} x {i} = {n*i}")
