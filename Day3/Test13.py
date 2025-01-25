while True:
    palindrome = input("Enter a word to check if it is a palindrome: ")
    if palindrome == palindrome[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
    opt=input("Do you want to continue? (y/n): ")
    if opt=='n':
        break
