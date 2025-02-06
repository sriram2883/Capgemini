import pandas as pd
file = open("./Day12/csvgen.csv","a+")
print("enter number of employees")
num = int(input())
data = []
for i in range(num):
	name = input("Enter the name of employee: ")
	age = input("Enter the age of employee: ")
	salary = input("Enter the salary of employee: ")
	data.append([name,age,salary])

for i in data:
	file.write(",".join(i) + "\n")

file.close()

df = pd.read_csv("./Day12/csvgen.csv", names=['Name','Age','Salary'])

print(df)
