n=int(input("Enter the number of elements in the array: "))
arr=[]
summ=0
for i in range(n):
    arr.append(int(input("Enter the element: ")))
    summ+=arr[i]
print("The sum of the elements in the array is: ",summ)