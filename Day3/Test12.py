#pattern generator
def pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print("* " * i)
    else:
        for i in range(1, n+1):
            print("* " * i)
n = int(input("Enter the number of lines: ")) 
reverse = input("Do you want to print in reverse order? (y/n): ")
if reverse == 'y':
    pattern(n, True)
else:
    pattern(n)