class employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    def display(self):
        print("Name:",self.__name)
        print("Salary:",self.__salary)
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        self.__salary = salary
    def __del__(self):
        print("Goodbye",self.__name)
        del self.__name
        del self.__salary
emp = employee("Sriram", int(input("Enter salary: ")))
emp.display()
print(emp.get_salary())
emp.set_salary(2000)
emp.display()
del emp