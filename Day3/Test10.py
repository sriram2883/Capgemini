#bill splitting
def split_bill(total, num_people):
    return total / num_people
total = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
amountperperson = split_bill(total, num_people)
persons=[]
amount=[]
for i in range(num_people):
    persons.append(input(f"Enter name of person {i+1}: "))
    amount.append(amountperperson)
for i in range(num_people):
    tip = int(input(f"Enter tip amount for {persons[i]}: "))
    amount[i] += tip
for i in range(num_people):
    print(f"{persons[i]} has to pay {amount[i]}")
