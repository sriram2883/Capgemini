class employee:
    def __init__(self, name, salary,id,department):
        self.name = name
        self.salary = salary
        self.id = id
        self.department = department

    def display(self):
        print("Name:", self.name, "Id: ",self.id)

n = int(input("Enter the number of employees: "))
emp = []
for i in range(n):
    name = input("Enter the name of the employee: ")
    salary = int(input("Enter the salary of the employee: "))
    id = int(input("Enter the id of the employee: "))
    department = input("Enter the department of the employee: ")
    emp.append(employee(name,salary,id,department))

for i in emp:
    i.display()