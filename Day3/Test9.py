#string analyzer
string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special_characters = 0
for i in string:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowels += 1
        else:
            consonants += 1
    elif i.isdigit():
        digits += 1
    else:
        special_characters += 1
print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("Special Characters: ", special_characters)
print("Reverse", string[::-1])