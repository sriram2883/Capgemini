inp = input("Enter a string: ")
lis = list(inp)
if lis == lis[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")