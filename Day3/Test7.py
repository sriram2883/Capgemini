# loan eligibility check
def check_eligibility(salary, age, creditscore, loanamount):
    if salary >= 50000 and age >= 25 and creditscore >= 750:
        if loanamount <= 1000000:
            print("Loan Approved")
            return True
        else:
            print("Loan amount exceeds the limit")
    elif salary >= 40000 and age >= 23 and creditscore >= 725:
        if loanamount <= 750000:
            print("Loan Approved")
            return True
        else:
            print("Loan amount exceeds the limit")
    elif salary >= 30000 and age >= 21 and creditscore >= 700:
        if loanamount <= 500000:
            print("Loan Approved")
            return True
        else:
            print("Loan amount exceeds the limit")
            return False
    else:
        print("Loan Denied")
        return False

salary = int(input("Enter your salary: "))
age = int(input("Enter your age: "))
creditscore = int(input("Enter your credit score: "))
loanamount = int(input("Enter the loan amount: "))
check_eligibility(salary, age, creditscore, loanamount)