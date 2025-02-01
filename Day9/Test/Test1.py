#creating employee class and allocate the values to the class dynamically

class Employee:
    def __init__(self):
        self.name=input("Enter the name:")
        self.id=int(input("Enter the id:"))
        self.department=input("Enter the department:")
    def display(self):
        print("Name:",self.name)
        print("Id:",self.id)
        print("Department:",self.department)
emp1=Employee()