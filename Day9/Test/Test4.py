#student class
class Student:
    def __init__(self):
        self.name=input("Enter the name:")
        self.id=int(input("Enter the id:"))
        self.department=input("Enter the department:")

    def display(self):
        return "Name: "+self.name+"\nId: "+str(self.id)+"\nDepartment: "+self.department
    
stud1=Student()
print(stud1.display())
