file = open("Day9/sample.txt", "r")
for line in file:
    print(file.readline(),end = "")    
# print(file.read())
file.close()