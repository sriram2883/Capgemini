#allowances:["travel","food","medical","insurance"]
#deductions:["pf","tax","insurance"]

class Employee:
    def __init__(self, empid, empname, empsalary, allowances, deductions):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary
        self.allowances = allowances
        self.deductions = deductions

    def calculate_salary(self):
        total_allowances = sum(self.allowances)
        total_deductions = sum(self.deductions)
        netsalary = self.empsalary + total_allowances - total_deductions
        return netsalary
    
    def display(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.empname)
        print("Employee Salary:", self.empsalary)
        print("Employee Allowances:", self.allowances)
        print("Employee Deductions:", self.deductions)
        print("Employee Net Salary:", self.calculate_salary())

allowances = [1000, 2000, 3000, 4000]
deductions = [500, 1000, 1500]   
emp = Employee(1, "Sriram", 10000, allowances, deductions)
emp.display()