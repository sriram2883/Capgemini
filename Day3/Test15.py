#leapyear check
print("Enter break to exit")
while True:
    year = input("Enter the year: ")
    if year == 'break':
        break
    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
