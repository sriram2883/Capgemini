#manager multilevel

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        self.department = input(f"Enter the department of {name}: ")

    
class Manager(Employee):
    def __init__(self, name, age, id):
        super().__init__(name, age, id)
    
    def approveleave(self,Employee:Employee):
        if(Employee.department == self.department):
            print(f"Leave approved for {Employee.name}")
        else:
            print("He is of other dept")
empobj = Employee("John", 25, 101)
manobj = Manager("Tom", 30, 102)
manobj.approveleave(empobj)

