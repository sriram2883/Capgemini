number_of_subjects = int(input("Enter the number of subjects: "))
marks = []
for i in range(number_of_subjects):
    marks.append(int(input(f"Enter the marks for subject {i+1}: ")))
print("Total Marks: ", sum(marks))
print("Percentage: ", sum(marks)/(number_of_subjects*100)*100)
percentage = sum(marks)/(number_of_subjects*100)*100
if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")