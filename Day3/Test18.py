weight = int(input("Enter te weight in KG:"))
height = int(input("Enter the height in meters:"))
bmi = weight / (height * height)
if(bmi <15):
    print("Very severely underweight")
elif(bmi >= 15 and bmi <16):
    print("Severely underweight")
elif(bmi >= 16 and bmi <18.5):
    print("Underweight")
elif(bmi >= 18.5 and bmi <25):
    print("Normal(healthy weight)")
elif(bmi >= 25 and bmi <30):
    print("Overweight")
elif(bmi >= 30 and bmi <35):
    print("Moderately obese")
elif(bmi >= 35 and bmi <40):
    print("Severely obese")
else:
    print("Very severely obese")