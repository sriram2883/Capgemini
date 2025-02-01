#banking with deposit and withdraw methods and prevent overdraft

class Bank:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("Enter the amount to deposit:"))
        self.balance+=amount
        print("Amount deposited successfully")
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw:"))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            print("Amount withdrawn successfully")
    def display(self):
        print("Balance:",self.balance)
bank=Bank()
bank.deposit()
bank.withdraw()
