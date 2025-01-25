#program for ATM simulation

Amount = 0
print("Welcome to ATM")
print("1. Withdraw")
print("2. Deposit")
print("3. Check Balance")
print("4. Quit")
while True:
    Option = int(input("Enter your option: "))
    if Option == 1:
        Withdraw = int(input("Enter amount to withdraw: "))
        if Withdraw > Amount:
            print("Insufficient Balance")
        else:
            Amount = Amount - Withdraw
            print("Remaining Balance: ", Amount)
    elif Option == 2:
        Deposit = int(input("Enter amount to deposit: "))
        Amount = Amount + Deposit
        print("Total Balance: ", Amount)
    elif Option == 3:
        print("Balance: ", Amount)
    elif Option == 4:
        break
    else:
        print("Invalid Option")
print("Thank you for using ATM")