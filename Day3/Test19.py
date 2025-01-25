n = int(input("Enter the number of elements"))
lis = []
for i in range(n):
    ele = int(input())
    lis.append(ele)
lis.sort()
print("Second largest element is:", lis[-2])
