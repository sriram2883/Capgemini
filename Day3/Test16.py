n = int(input("Enter the number of elements"))
odd =[]
even = []
for i in range(0, n):
    ele = int(input())
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)
print("Even numbers:", even)
print("Odd numbers:", odd)